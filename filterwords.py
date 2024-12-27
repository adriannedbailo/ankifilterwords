import sys
import os
from aqt import mw
from aqt.qt import QInputDialog, QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QCheckBox, QScrollArea, QWidget, QHBoxLayout
from aqt.utils import showInfo
import string
import datetime

# Додаємо шлях до віртуального середовища spaCy
venv_path = os.path.expanduser("~/Library/Application Support/Anki2/addons21/spacyenv/lib/python3.9/site-packages")
if venv_path not in sys.path:
    sys.path.insert(0, venv_path)

# Імпортуємо spaCy
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    print("spaCy та модель en_core_web_sm завантажені успішно.")
except Exception as e:
    print(f"Помилка завантаження spaCy або моделі: {e}")
    nlp = None

# Налаштування логування
log_file_path = os.path.expanduser("~/Library/Application Support/Anki2/addons21/filterwords/filter_log.txt")

def write_log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

# Завантажуємо відомі слова з файлу
def load_known_words_from_file():
    file_path = os.path.expanduser("~/Library/Application Support/Anki2/addons21/filterwords/known_words.txt")
    if not os.path.exists(file_path):
        return set()
    
    known_words = set()
    ignore_block = False
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().lower()
            if line == "# start":
                ignore_block = True
            elif line == "# end":
                ignore_block = False
            elif line and not ignore_block and not line.startswith("#"):
                known_words.add(line)
    return known_words

# Функція лематизації тексту з виключенням небажаних частин мови та власних назв
def lemmatize_text(text):
    global nlp
    if not nlp:
        raise ValueError("Модель spaCy не ініціалізована.")
    doc = nlp(text)
    unwanted_pos = {"DET", "AUX", "PRON", "PROPN", "NUM"}
    lemmas = [
        token.lemma_.lower()
        for token in doc
        if token.lemma_.isalpha() and token.pos_ not in unwanted_pos
    ]
    write_log(f"Леми для тексту '{text}': {lemmas}")
    return lemmas

# Функція для копіювання нотатки без порожніх полів
def copy_note_without_empty_fields(note):
    new_note = mw.col.newNote(note.model())  # Створюємо нову нотатку з тією ж моделлю

    # Копіюємо тільки непорожні поля
    new_note.fields = [field for field in note.fields if field.strip() != '']

    # Якщо нова нотатка має менше полів, додаємо порожні
    while len(new_note.fields) < len(note.fields):
        new_note.fields.append('')

    # Копіюємо теги
    new_note.tags = list(note.tags)
    
    return new_note

# Функція для видалення дублікатів
def remove_duplicates(deck_name):
    notes_in_deck = mw.col.findNotes(f'deck:"{deck_name}"')
    unique_values = set()
    notes_to_delete = []

    for note_id in notes_in_deck:
        note = mw.col.getNote(note_id)
        value = note.fields[0]  # Використовуємо перше поле для перевірки на унікальність

        if value in unique_values:
            notes_to_delete.append(note_id)
        else:
            unique_values.add(value)

    # Видаляємо дублікатні нотатки
    mw.col.remove_notes(notes_to_delete)
    write_log(f"Видалено {len(notes_to_delete)} дублікатних нотаток у колоді '{deck_name}'")

# Основна функція для фільтрації
def perform_filtering(known_words_notes, known_phrases_notes, notes_to_filter, save_deck_name, ignore_phrases, field_index):
    filtered_words = set()

    known_words = [note.fields[0] for note in known_words_notes if note.fields]
    known_lemmas = set(lemma for word in known_words for lemma in lemmatize_text(word))
    known_lemmas.update(load_known_words_from_file())

    known_phrases = [note.fields[0] for note in known_phrases_notes if note.fields]

    for note in notes_to_filter:
        # Перевірка на порожні поля
        if not note.fields:
            msg = f"Нотатка з ID {note.id} не містить полів, пропускаємо."
            write_log(msg)
            continue

        text = note.fields[field_index]

        unknown_lemmas = [lemma for lemma in lemmatize_text(text) if lemma not in known_lemmas]
        write_log(f"Невідомі леми: {unknown_lemmas}")

        if not ignore_phrases and any(phrase in text for phrase in known_phrases):
            write_log(f"Відома фраза знайдена в нотатці з ID {note.id}, пропускаємо.")
            continue

        if not unknown_lemmas:
            write_log(f"У нотатці з ID {note.id} немає невідомих лем, пропускаємо.")
            continue

        for lemma in unknown_lemmas:
            if lemma in filtered_words:
                write_log(f"Лема '{lemma}' вже була додана, пропускаємо.")
                continue

            filtered_words.add(lemma)

            # Копіюємо нотатку без порожніх полів
            new_note = copy_note_without_empty_fields(note)

            # Додаємо лему в перше поле нової нотатки
            new_note.fields[0] = lemma

            # Додаємо нову нотатку в колекцію
            try:
                mw.col.addNote(new_note)
                mw.col.set_deck([new_note.id], mw.col.decks.id(save_deck_name))
                write_log(f"Додано нову нотатку з ID {new_note.id} з лемою '{lemma}'")
            except Exception as e:
                write_log(f"Помилка додавання нотатки з лемою '{lemma}': {e}")
                continue

    write_log("Фільтрацію завершено.")
    remove_duplicates(save_deck_name)  # Видалити дублікати після фільтрації

# Діалогове вікно з параметрами фільтрації
class FilterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Параметри фільтрації")

        self.layout = QVBoxLayout()

        # Отримуємо всі назви колод
        self.all_decks = mw.col.decks.all_names()

        # Прокручуваний контейнер для чекбоксів
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_area_content)

        # Додавання чекбоксів для вибору колод з відомими словами
        self.layout.addWidget(QLabel("Колоди з відомими словами:"))
        self.known_words_checkboxes = []
        for deck in self.all_decks:
            checkbox = QCheckBox(deck)
            self.known_words_checkboxes.append(checkbox)
            self.scroll_layout.addWidget(checkbox)

        self.scroll_area.setWidget(self.scroll_area_content)
        self.layout.addWidget(self.scroll_area)

        # Вибір колоди для фільтрації
        self.layout.addWidget(QLabel("Колода для фільтрації:"))
        self.filter_deck_combo = QComboBox()
        self.filter_deck_combo.addItems(self.all_decks)
        self.layout.addWidget(self.filter_deck_combo)

        # Вибір колоди для збереження слів
        self.layout.addWidget(QLabel("Колода для збереження слів:"))
        self.save_deck_combo = QComboBox()
        self.save_deck_combo.addItems(self.all_decks)
        self.layout.addWidget(self.save_deck_combo)

        # Вибір для ігнорування перевірки фраз
        self.layout.addWidget(QLabel("Ігнорувати перевірку фраз"))
        self.ignore_phrases_checkbox = QCheckBox("Ігнорувати перевірку фраз")
        self.layout.addWidget(self.ignore_phrases_checkbox)

        # Вибір типу нотаток для фільтрації
        self.layout.addWidget(QLabel("Тип нотаток для фільтрації:"))
        self.note_type_combo = QComboBox()
        self.note_type_combo.addItems(mw.col.models.allNames())
        self.layout.addWidget(self.note_type_combo)

        # Вибір індексу поля для фільтрації
        self.layout.addWidget(QLabel("Індекс поля для фільтрації (починається з 0):"))
        self.field_index_combo = QComboBox()
        self.field_index_combo.addItems([str(i) for i in range(10)])  # Припускаємо, що максимальний індекс поля - 9
        self.layout.addWidget(self.field_index_combo)

        # Кнопка підтвердження
        self.ok_button = QPushButton("Почати фільтрацію")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

        self.setLayout(self.layout)

def start_filtering():
    dialog = FilterDialog()
    if dialog.exec():
        # Отримуємо вибрані опції
        known_words_deck_names = [checkbox.text() for checkbox in dialog.known_words_checkboxes if checkbox.isChecked()]
        filter_deck_name = dialog.filter_deck_combo.currentText()
        save_deck_name = dialog.save_deck_combo.currentText()
        ignore_phrases = dialog.ignore_phrases_checkbox.isChecked()
        note_type = dialog.note_type_combo.currentText()
        field_index = int(dialog.field_index_combo.currentText())

        if not known_words_deck_names:
            showInfo("Будь ласка, виберіть хоча б одну колоду з відомими словами.")
            return

        # Отримуємо нотатки
        known_words_notes = []
        for deck_name in known_words_deck_names:
            known_words_notes += [mw.col.getNote(id) for id in mw.col.findNotes(f'deck:"{deck_name}"')]
        notes_to_filter = [mw.col.getNote(id) for id in mw.col.findNotes(f'deck:"{filter_deck_name}"')]

        if not known_words_notes:
            showInfo("У вибраній колоді з відомими словами немає нотаток.")
            return
        if not notes_to_filter:
            showInfo("У вибраній колоді для фільтрації немає нотаток.")
            return

        # Виконуємо фільтрацію
        perform_filtering(
            known_words_notes,
            [],
            notes_to_filter,
            save_deck_name,
            ignore_phrases,
            field_index
        )

        # Відображаємо повідомлення після завершення
        showInfo("Фільтрацію завершено.")
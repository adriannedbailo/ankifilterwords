# **FilterWords Add-on for Anki**

FilterWords is an add-on for Anki that helps filter out known words from your decks. It considers a list of known words, phrases, and a `known_words.txt` file to personalize your language learning process.

---

## **Key Features**
- 📖 **Filter Unknown Words**: Excludes known words from your decks.
- 🔄 **Multiple Deck Selection**: Allows you to use multiple decks for comparison.
- 📝 **Edit `known_words.txt`**: A simple text file to store and edit your list of known words.
- 🧹 **Remove Duplicates**: Automatically excludes duplicate cards.
- 📋 **Detailed Logging**: Logs all actions during filtering into `filter_log.txt`.

---

## **Installation**

1. **Download the repository files**:
   - Clone the repository or download it as a ZIP file.
   - Extract the files into a folder named `filterwords`.

2. **Create a folder in the Anki extensions directory**:
   - Navigate to the folder for Anki add-ons. The default path is:
     - **Windows**: `%APPDATA%\Anki2\addons21\`
     - **macOS**: `~/Library/Application Support/Anki2/addons21/`
     - **Linux**: `~/.local/share/Anki2/addons21/`
   - Place the `filterwords` folder inside the `addons21` directory.

3. **Install the spaCy library and the English model**:
   - Create a Python virtual environment:
     ```bash
     python3 -m venv spacyenv
     source spacyenv/bin/activate
     ```
   - Install spaCy and the required model:
     ```bash
     pip install spacy
     python -m spacy download en_core_web_sm
     ```

4. **Add the `known_words.txt` file to the `filterwords` folder**:
   Use this file to store your list of known words.

---

## **How to Use**

1. Launch **FilterWords** via the Anki menu:
   Tools → FilterWords Add-on

2. Configure the add-on:
   - **Known Words Decks**: Select one or more decks for comparison.
   - **Deck to Filter**: Specify the deck to filter unknown words from.
   - **Save Results**: A new deck will be created with only the unknown words.

3. Edit `known_words.txt` to add or remove words:
   ```plaintext
   # START Known Words
   the
   be
   and
   have
   it
   I
   you
   # END
   ```

4. Check the filtering results:
   Logs will be saved in the `filter_log.txt` file.

---

## **Example Usage with spaCy**
Here is how the program uses lemmatization to process text:
```python
import spacy

# Load the English spaCy model
nlp = spacy.load("en_core_web_sm")

# Text for analysis
text = "I am learning new words every day."

# Lemmatize the text
doc = nlp(text)
lemmas = [token.lemma_ for token in doc]

print("Lemmas:", lemmas)
# Output: ['I', 'be', 'learn', 'new', 'word', 'every', 'day', '.']
```

---

## **Common Issues**
> ⚠️ **Empty Fields in Notes**:  
> Notes with empty fields will be skipped during filtering.

> ⚠️ **spaCy Model Not Installed**:  
> Ensure you have downloaded the English model (`en_core_web_sm`).

---

## **Recent Updates**
- ✅ Added **multiple deck selection** for known words.
- ✅ Implemented the ability to **ignore known phrases**.
- ✅ Introduced a scrollable window for deck selection.
- ✅ Supported commenting blocks of words in `known_words.txt`.
- ✅ Detailed logging into the `filter_log.txt` file.

---

## **Contact**
For questions or suggestions, please reach out via [GitHub Issues](https://github.com/your-repository/issues).

# **FilterWords Add-on для Anki**

FilterWords – це додаток для Anki, який допомагає фільтрувати невідомі слова з ваших колод. Він враховує список відомих слів, фраз та текстовий файл `known_words.txt`, щоб персоналізувати процес вивчення мов.

---

## **Основні функції**
- 📖 **Фільтрація невідомих слів**: Виключає з ваших колод слова, які ви вже знаєте.
- 🔄 **Множинний вибір колод**: Ви можете використовувати кілька колод для порівняння.
- 📝 **Редагування `known_words.txt`**: Простий текстовий файл для збереження та редагування списку відомих слів.
- 🧹 **Видалення дублікатів**: Автоматично виключає повторювані картки.
- 📋 **Детальне логування**: Дії під час фільтрації зберігаються у файлі `filter_log.txt`.

---

## **Встановлення**

1. **Завантажте файли з репозиторію**:
   - Клонуйте репозиторій або завантажте його у форматі ZIP.
   - Розпакуйте файли у папку з назвою `filterwords`.

2. **Створіть папку в директорії розширень Anki**:
   - Перейдіть у директорію для розширень Anki. Шлях за замовчуванням:
     - **Windows**: `%APPDATA%\Anki2\addons21\`
     - **macOS**: `~/Library/Application Support/Anki2/addons21/`
     - **Linux**: `~/.local/share/Anki2/addons21/`
   - Помістіть папку `filterwords` у директорію `addons21`.

3. **Встановіть бібліотеку spaCy та модель англійської мови**:
   - Створіть віртуальне середовище Python:
     ```bash
     python3 -m venv spacyenv
     source spacyenv/bin/activate
     ```
   - Встановіть spaCy та потрібну модель:
     ```bash
     pip install spacy
     python -m spacy download en_core_web_sm
     ```

4. **Додайте файл `known_words.txt` до папки `filterwords`**:
   У цьому файлі збережіть слова, які ви вже знаєте.

---

## **Як користуватися**

1. Запустіть **FilterWords** через меню Anki:
   Tools → FilterWords Add-on

2. Налаштуйте додаток:
   - **Колоди відомих слів**: Виберіть одну або кілька колод для аналізу.
   - **Колоду для фільтрації**: Вкажіть ту, з якої потрібно виключити відомі слова.
   - **Збережіть результати**: У новій колоді будуть тільки невідомі слова.

3. Редагуйте `known_words.txt`, додаючи або видаляючи слова:
   ```plaintext
   # START Відомі слова
   the
   be
   and
   have
   it
   I
   you
   # END
   ```

4. Перевірте результати фільтрації:
   Логи будуть збережені у файлі `filter_log.txt`.

---

## **Приклад використання spaCy**
Ось як програма працює з лематизацією тексту:
```python
import spacy

# Завантажуємо англійську модель spaCy
nlp = spacy.load("en_core_web_sm")

# Текст для аналізу
text = "I am learning new words every day."

# Лематизація тексту
doc = nlp(text)
lemmas = [token.lemma_ for token in doc]

print("Леми:", lemmas)
# Вивід: ['I', 'be', 'learn', 'new', 'word', 'every', 'day', '.']
```

---

## **Типові помилки**
> ⚠️ **Порожні поля в нотатках**:  
> Якщо в нотатках є порожні поля, вони будуть пропущені під час фільтрації.

> ⚠️ **Невстановлена модель spaCy**:  
> Переконайтеся, що ви завантажили модель англійської мови (`en_core_web_sm`).

---

## **Останні оновлення**
- ✅ Додано **множинний вибір колод** для відомих слів.
- ✅ Реалізовано можливість **ігнорувати відомі фрази**.
- ✅ Створено прокручуване вікно для вибору колод.
- ✅ Підтримка коментування блоку слів у `known_words.txt`.
- ✅ Докладне логування у файл `filter_log.txt`.

---

## **Контакти**
Якщо у вас є питання або пропозиції, звертайтеся через [GitHub Issues](https://github.com/ваш-репозиторій/issues).

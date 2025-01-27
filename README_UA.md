# FilterWords Add-on для Anki
_(Українська версія / Ukrainian Version)_

[English Version](README.md)

FilterWords – це додаток для Anki, який допомагає фільтрувати невідомі слова з ваших колод. Він враховує список відомих слів, фраз та текстовий файл `known_words.txt`, щоб персоналізувати процес вивчення мов.

---

## **Мета створення**

Цей додаток був створений для вирішення проблеми автоматичного фільтрування карток у великих колодах. Наприклад, після створення багатьох нотаток із фільмів за допомогою **mpvacious**, де речення можуть бути такими, як:

```
I love big money
```

Мені потрібно було швидко залишити лише ті картки, у яких є слова, які я ще не знаю. Для цього додаток порівнює нову колоду з уже вивченими колодами або текстовим файлом `known_words.txt`, фільтрує відомі слова та залишає лише ті картки, які містять невідомі слова.

Крім того, я хотів, щоб додаток:
1. **Копіював картку**, якщо речення містить два чи більше невідомих слова.  
   Наприклад, для речення:
   ```
   I love big money
   ```
   Якщо "big" і "money" є невідомими словами, після фільтрації буде створено дві картки:
   - Одна для слова "big".
   - Інша для слова "money".  

   Обидві картки матимуть однакові поля (зображення, звук тощо), за винятком поля "слово для вивчення", яке буде різним.

---

## **Основні функції**
- 📖 **Фільтрація невідомих слів**: Виключає з ваших колод слова, які ви вже знаєте.
- 🔄 **Множинний вибір колод**: Ви можете використовувати кілька колод для порівняння.
- 📝 **Редагування `known_words.txt`**: Простий текстовий файл для збереження та редагування списку відомих слів.
- 🧹 **Видалення дублікатів**: Автоматично виключає повторювані картки.
- 📋 **Детальне логування**: Дії під час фільтрації зберігаються у файлі `filter_log.txt`.
- 🔍 **Копіювання карток з кількома невідомими словами**: Створює окремі картки для кожного невідомого слова в одному реченні.

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
- ✅ **Копіювання карток** для кожного невідомого слова у реченні.

---

## **Контакти**
Якщо у вас є питання або пропозиції, звертайтеся через [GitHub Issues](README.md).

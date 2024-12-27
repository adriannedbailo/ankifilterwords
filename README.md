# FilterWords Add-on for Anki
_(English Version)_

[Українська версія](https://github.com/adriannedbailo/ankifilterwords/blob/main/README_UA.md)

FilterWords is an add-on for Anki that helps filter out known words from your decks. It considers a list of known words, phrases, and a `known_words.txt` file to personalize your language learning process.

---

## **Purpose**

This add-on was created to solve the problem of automatically filtering cards in large decks. For example, after generating many notes from movies using **mpvacious**, with sentences such as:

```
I love big money
```

I needed to quickly keep only those cards that contained words I didn’t know. The add-on compares the new deck with already studied decks or the `known_words.txt` file, filters out known words, and leaves only cards with unknown words.

Additionally, I wanted the add-on to:
1. **Duplicate a card** if the sentence contains two or more unknown words.  
   For example, for the sentence:
   ```
   I love big money
   ```
   If "big" and "money" are unknown, the filtering will create two cards:
   - One for the word "big".
   - Another for the word "money".

   Both cards will have the same fields (image, sound, etc.), except for the "word to study" field, which will differ.

This flexibility makes the add-on especially useful for those who want to focus on individual words while preserving the sentence context.

---

## **Key Features**
- 📖 **Filter Unknown Words**: Excludes known words from your decks.
- 🔄 **Multiple Deck Selection**: Allows you to use multiple decks for comparison.
- 📝 **Edit `known_words.txt`**: A simple text file to store and edit your list of known words.
- 🧹 **Remove Duplicates**: Automatically excludes duplicate cards.
- 📋 **Detailed Logging**: Logs all actions during filtering into `filter_log.txt`.
- 🔍 **Duplicate Cards with Multiple Unknown Words**: Creates separate cards for each unknown word in a single sentence.

---

## **Installation**

1. **Download the repository files**:
   - Clone the repository or download it as a ZIP file.
   - Extract the files into a folder named `filterwords`.

2. **Create a folder in the Anki add-ons directory**:
   - Navigate to the directory for Anki add-ons. The default path is:
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
- ✅ **Duplicated cards** for each unknown word in a sentence.

---

## **Contact**
For questions or suggestions, please reach out via [GitHub Issues](https://github.com/adriannedbailo/ankifilterwords/issues).

# 🔤 Text Normalizer & Case Converter

This Python script allows you to **normalize accented characters** (commonly used in Portuguese) and convert text into either **uppercase** or **lowercase**.  
It is especially useful for cleaning names or words by removing diacritics (accents) and ensuring consistent formatting.

---

## ✨ Features
- Cleans the terminal screen for a fresh start.
- Accepts user input for a name or word.
- Normalizes accented characters:
  - Converts `ã, â, á, à, ä → a`
  - Converts `ê, é, è, ë → e`
  - Converts `ì, î, í, ï → i`
  - Converts `ö, ò, ó, õ, ô → o`
  - Converts `ú, ù, û, ü → u`
  - Converts `ç → c`
- Removes punctuation and non-printable characters.
- Allows the user to choose:
  - `1` → Convert to **uppercase**
  - `2` → Convert to **lowercase**
- Repeats until the user decides to exit.

---

## 🛠️ Requirements
- Python 3.6+
- Standard libraries (`os`, `string`) — no external dependencies.

---

## 🚀 Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/text-normalizer.git
   cd text-normalizer
Run the script:

bash
python text_normalizer.py
Follow the prompts:

Enter a name or word.

Choose whether to convert to uppercase or lowercase.

Decide if you want to process another name.

📂 Example
Input:

```
Digite o nome:
João Çésar
Deseja transformar o texto em:
1 - Letras Maiúsculas
2 - Letras Minúsculas
Output (option 1 - uppercase):
```
```
JOAO CESAR
```
```
Output (option 2 - lowercase):
```
```
joao cesar
```
⚠️ Notes
Only basic Latin letters are preserved; accented characters are replaced with their closest equivalents.

Punctuation and non-printable characters are ignored.

The program runs in a loop until the user chooses to exit.

📜 License
This project is licensed under the MIT License. Feel free to use and modify it.

👨‍💻 Author
Developed by [Your Name]. Contributions are welcome!

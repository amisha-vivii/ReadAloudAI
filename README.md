# ReadAloudAI - PDF & DOCX Text Reader

ReadAloudAI is a Python-based text-to-speech application that can read PDF and Word documents aloud using system voices.

It supports:
- 📄 PDF files
- 📝 DOCX files
- 🎙 Multiple voice selection
- ⚡ Adjustable speech speed
- ⛔ Stop reading anytime with a keypress

---

# ✨ Features

- Select PDF or DOCX files through a file picker
- Extracts and reads text aloud
- Choose from available system voices
- Customize speech rate
- Stop speech instantly by pressing `s`
- Supports multi-language voices (if installed on your OS)

---

# 🛠 Technologies Used

- Python
- pyttsx3
- PyPDF2
- python-docx
- tkinter
- threading
- msvcrt

---

# 📦 Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ReadAloudAI.git
cd ReadAloudAI
```

## 2️⃣ Install dependencies

```bash
pip install pyttsx3 PyPDF2 python-docx
```

---

# ▶️ How to Run

```bash
python main.py
```

1. Select a PDF or DOCX file
2. Choose a voice
3. Set speech rate
4. Listen to your document 🎧

Press `s` anytime to stop reading.

---

# 📂 Supported File Types

- `.pdf`
- `.docx`

---

# ⚠️ Important Note

`pyttsx3` uses voices installed in your operating system.

For better multilingual support:
- Install additional language voices in Windows settings
- The app reads text aloud but does not translate it

---

# 🚀 Future Improvements

- GUI interface
- Pause/Resume feature
- Convert speech to MP3
- OCR support for scanned PDFs
- AI voice integration
- Dark mode UI

---

# 👩‍💻 Author

Made with Python by Amisha 🌸

# 🗣️ PDF To Speech Ultimate Converter

An intelligent desktop application that **reads PDF documents aloud**, supports **OCR for scanned PDFs**, allows **summarization**, and can **export audio files** — with background music and speech rate control. Built using Python and powerful AI tools like HuggingFace Transformers.

---

## 🚀 Features

- 📄 Read text from PDF documents
- 🧠 Automatically perform **OCR** on image-based PDFs
- 🗣️ Convert text to speech using `pyttsx3` (offline TTS)
- 🔊 Export speech to MP3 using `gTTS` (Google Text-to-Speech)
- 🎶 Optional background music support while reading
- 🏁 Choose specific **page ranges** to read
- 🌍 Multilingual support (`en`, `es`, `fr`, `de`)
- 📈 Adjustable **speech rate**
- 🛑 Stop reading anytime
- 🧾 Summarization with HuggingFace Transformers

---

## 📁 Project Structure

PDFToSpeechApp/
├── app.py # Main application code
├── background_music.mp3 # Optional music file
├── output_audio.mp3 # Exported audio output
└── README.md # Project documentation

markdown
Copy
Edit

---

## 🛠️ Technologies Used

- `tkinter` – GUI
- `pyttsx3` – Offline Text-to-Speech
- `gTTS` – Export to MP3 (Google TTS)
- `PyPDF2` – PDF reading
- `pytesseract` – OCR for scanned PDFs
- `pdf2image` – Convert PDF pages to images
- `transformers` – Summarization pipeline
- `pygame` – Play background music

---

## 💻 Installation

### 🐍 Prerequisites

- Python 3.7+
- Tesseract OCR installed on your system  
  - [Install Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

### 📦 Install Required Packages

```bash
pip install pyttsx3 gTTS PyPDF2 pytesseract pdf2image pygame transformers
▶️ How to Run
bash
Copy
Edit
python app.py



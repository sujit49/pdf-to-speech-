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


🧠 How It Works
Select a PDF file

Choose a page range (e.g., 1-5)

Click Read PDF Aloud to listen to the content

If the PDF is scanned, it will automatically use OCR

Use Export Audio to save speech as output_audio.mp3

Optional: Toggle background music while reading

Control speech rate and language via GUI

📸 Screenshots
(You can add screenshots here)

💡 Future Improvements
Add summarization toggle with output preview

Support for EPUB and DOCX

Export as WAV format

GUI-based audio editor

❗ Note
Make sure Tesseract OCR is installed and added to your system path for OCR to work correctly.

The background_music.mp3 file must exist in the project directory to play background music.

📄 License
This project is licensed under the MIT License.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

⭐ Show Your Support
If you like this project, consider starring it on GitHub or sharing it with others!

---

Let me know if you'd like this turned into a downloadable `.md` file or customized further (e.g., author name, demo video, GitHub repo link, etc.).




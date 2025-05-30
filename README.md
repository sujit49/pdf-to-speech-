# 📚🔊 PDF To Speech Ultimate Converter

A powerful desktop application built using **Python and Tkinter** that converts **PDF files into spoken audio** with options to export the audio, adjust speech rate, summarize content, and add background music — all in one simple interface!

---

## 🧩 Features

- 📄 Select any PDF file for reading
- 🔊 Read selected pages aloud using text-to-speech (TTS)
- 💾 Export audio as `.mp3` using Google Text-to-Speech (gTTS)
- 🎼 Toggle background music during reading
- 📝 Page range selection (e.g., "1-3")
- 🌐 Multi-language support (`en`, `es`, `fr`, `de`)
- ⚙️ Adjustable speech rate (100–200 words per minute)
- 🤖 Built-in text summarizer using `transformers`
- 🧠 OCR fallback using Tesseract if no embedded text is found

---

## 🚀 Technologies Used

- Python 3
- Tkinter (GUI)
- PyPDF2 (PDF reading)
- pyttsx3 (offline TTS)
- gTTS (online TTS)
- pdf2image + pytesseract (OCR)
- pygame (background music)
- transformers (summarization)

---

## 📁 File Structure

```
pdf_to_speech_app/
├── main.py                   # Main application script
├── background_music.mp3      # Optional music (add your own file)
├── README.md                 # Project documentation
```

---

## ▶️ How to Run

1. Clone or download this repository.
2. Install the required packages:

```bash
pip install PyPDF2 pytesseract pdf2image pyttsx3 pygame gTTS transformers tkinter
```

3. Ensure `poppler` is installed for `pdf2image` (see instructions: https://github.com/Belval/pdf2image).
4. Run the application:

```bash
python main.py
```

---

## 🎮 How to Use

- Click **Select PDF** to choose a file.
- Optionally, enter a **page range** like `1-3`.
- Click **Read PDF Aloud** to start text-to-speech.
- Click **Export Audio** to save the output as an MP3.
- Use **Toggle Background Music** to play/stop music.
- Use **Stop Reading** to halt ongoing speech.

---

## 📌 Notes

- If no embedded text is found in the PDF, the app will try OCR using Tesseract.
- Summarization is built-in but not triggered directly in the UI (expandable).
- Make sure to add your own `background_music.mp3` for background playback.

---

## 💡 Future Enhancements

- Add a visual summarization feature
- Real-time highlighting during speech
- Drag-and-drop PDF support
- PDF metadata and title display

---

## 📜 License

This project is open-source and for educational use. Modify and improve as you wish!

---

Enjoy converting your PDFs into immersive audio! 🎧📖✨





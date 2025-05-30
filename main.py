import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import pygame
import pytesseract
import pyttsx3
from gtts import gTTS
from transformers import pipeline
import threading


class PDFToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF To Speech Ultimate Converter")
        self.pdf_file = None
        self.text_content = ""
        self.bg_music = False
        self.is_reading = False  # Flag to check if speech is ongoing

        # Text-to-Speech Engine
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty("rate", 150)

        # Summarizer Model
        self.summarizer = pipeline("summarization")

        # GUI Elements
        tk.Button(root, text="Select PDF", command=self.select_pdf, font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Read PDF Aloud", command=self.read_pdf, font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Export Audio", command=self.export_audio, font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Toggle Background Music", command=self.toggle_music, font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Stop Reading", command=self.stop_reading, font=("Arial", 12)).pack(pady=5)  # Stop button
        self.page_entry = tk.Entry(root, font=("Arial", 12))
        self.page_entry.insert(0, "Enter Page Range (e.g., 1-3)")
        self.page_entry.pack(pady=5)
        self.language_var = tk.StringVar(value="en")
        tk.OptionMenu(root, self.language_var, "en", "es", "fr", "de").pack(pady=5)
        tk.Label(root, text="Speech Rate (Words Per Minute):", font=("Arial", 12)).pack()
        self.rate_spinbox = tk.Spinbox(root, from_=100, to=200, font=("Arial", 12))
        self.rate_spinbox.pack(pady=5)

    def select_pdf(self):
        self.pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if not self.pdf_file:
            messagebox.showerror("Error", "No file selected!")
        else:
            messagebox.showinfo("Success", "PDF file selected successfully.")

    def extract_text(self):
        if not self.pdf_file:
            messagebox.showerror("Error", "Please select a PDF first.")
            return ""

        try:
            # Try to extract text from the PDF
            text = ""
            with open(self.pdf_file, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                page_range = self.page_entry.get().strip()
                start, end = (0, len(reader.pages)) if "-" not in page_range else map(int, page_range.split("-"))
                for page in reader.pages[start - 1:end]:
                    text += page.extract_text()

            # If no text, use OCR
            if not text.strip():
                messagebox.showinfo("Info", "No text found. Attempting OCR...")
                images = convert_pdf_to_images(self.pdf_file)
                text = "".join([pytesseract.image_to_string(img) for img in images])

            return text
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract text: {e}")
            return ""

    def read_pdf(self):
        self.text_content = self.extract_text()
        if not self.text_content:
            return

        # Flag to indicate reading is in progress
        self.is_reading = True
        self.tts_engine.setProperty("rate", int(self.rate_spinbox.get()))

        # Start reading the PDF in a separate thread
        threading.Thread(target=self.read_text_aloud).start()

    def read_text_aloud(self):
        """Run the text-to-speech in a separate thread."""
        self.tts_engine.say(self.text_content)
        self.tts_engine.runAndWait()

    def export_audio(self):
        self.text_content = self.extract_text()
        if not self.text_content:
            return

        try:
            tts = gTTS(text=self.text_content, lang=self.language_var.get())
            tts.save("output_audio.mp3")
            messagebox.showinfo("Success", "Audio saved as output_audio.mp3.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save audio: {e}")

    def toggle_music(self):
        if self.bg_music:
            pygame.mixer.music.stop()
            self.bg_music = False
        else:
            pygame.mixer.init()
            pygame.mixer.music.load("background_music.mp3")
            pygame.mixer.music.play(-1)
            self.bg_music = True

    def stop_reading(self):
        """Stop the ongoing text-to-speech reading."""
        if self.is_reading:
            self.tts_engine.stop()  # Stop the current speech
            self.is_reading = False


def convert_pdf_to_images(pdf_path):
    """Convert PDF to image for OCR (placeholder function)."""
    from pdf2image import convert_from_path
    return convert_from_path(pdf_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToSpeechApp(root)
    root.mainloop()

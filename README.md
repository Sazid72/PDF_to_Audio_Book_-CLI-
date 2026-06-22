# 📚 PDF to Audiobook Converter (Python CLI Project)

## 📌 Description

I built a PDF-to-audiobook application using Python to convert digital PDF documents into spoken audio using text-to-speech technology. The project works as a simple interactive tool where the user selects a PDF file through a file dialog, and the program reads its contents page by page aloud. The goal was to automate the process of listening to documents instead of manually reading them, making it useful for studying, multitasking, or improving accessibility for users who prefer audio-based content consumption.

I created this project to explore how real-world automation can be achieved using Python libraries and to understand how text extraction and speech synthesis work together. I also wanted to build something practical that could help transform long reading materials like books, notes, and research papers into an audiobook format. This helped me combine two important concepts—file processing and speech generation—into a single working application.

To build it, I used `tkinter.filedialog` to allow users to select a PDF file from their system. Then I used `PyPDF2.PdfReader` to read the PDF and determine the number of pages. For each page, I extracted text using `extract_text()` and passed it to `pyttsx3`, an offline text-to-speech engine initialized with `pyttsx3.init()`. The program loops through all pages, checks if extracted text exists, and then converts it into speech using `say()` followed by `runAndWait()`. This creates a continuous narration of the PDF content page by page.

During development, I faced challenges mainly related to text extraction quality and performance. Some PDFs did not extract clean text, resulting in missing or broken sentences during speech output. Another issue was that calling `runAndWait()` inside the loop made the playback slower for large files, since each page is processed separately. Additionally, handling empty pages and ensuring the program does not crash required simple checks like verifying if text exists before sending it to the speech engine. Despite these challenges, the project helped me understand how to integrate multiple Python libraries and build a functional automation tool from scratch.

---

## 🎯 Features
- 📄 Load PDF files using a file picker
- 🔊 Convert PDF text into speech using offline TTS
- 📖 Reads content page by page
- 🧠 Skips empty pages automatically
- 💻 Simple and lightweight Python script

---

## 🛠️ Technologies Used
- Python 3
- PyPDF2 (PDF text extraction)
- pyttsx3 (Offline text-to-speech engine)
- tkinter (File selection dialog)

---

## 🚀 How It Works
1. The program opens a file dialog to select a PDF file.
2. It reads the PDF using `PyPDF2`.
3. It extracts text from each page.
4. The extracted text is passed to `pyttsx3`.
5. The engine converts text to speech and plays it sequentially.

---

## 💻 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/pdf-to-audiobook.git
cd pdf-to-audiobook
```
## Install dependencies
pip install PyPDF2 <br>
pip install pyttsx3 <br>

Note: tkinter usually comes pre-installed with Python.
---

## ▶️ Usage

Run the script:

python pdf_to_audio_book.py

Then:

Select a PDF file from the file explorer <br>
The program will automatically start reading it aloud

## 👨‍💻 Author

Built by: Md. Sazid Al Mafi <br>
Purpose: Learning Python automation, file processing, and text-to-speech systems

import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdf_reader = PyPDF2.PdfReader(book)
num_pages = len(pdf_reader.pages)

player = pyttsx3.init()

for num in range(0, num_pages):
    page = pdf_reader.pages[num]
    text = page.extract_text()
    
    if text:
        player.say(text)
        player.runAndWait()
        
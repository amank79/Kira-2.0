import PyPDF2
from tkinter import Tk, filedialog
from chatbot import say_david ,say
def pdf_read(voice):
    root = Tk()
    root.withdraw()
    say("Please select a PDF file.", voice)
    file_path = filedialog.askopenfilename(
        initialdir='/',
        title='Select PDF file',
        filetypes=[('PDF Files', '*.pdf')]
    )

    if not file_path:
        say("No file selected.", voice)
        return

    book = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(book)
    say("Please enter the page number you want to read:", voice)
    page_number = int(input())

    if page_number < 0 or page_number >= len(pdf_reader.pages):
        say("Invalid page number.", voice)
        return

    page = pdf_reader.pages[page_number]
    page_text = page.extract_text()
    say_david(page_text)


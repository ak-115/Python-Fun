import PyPDF4
from gtts import gTTS
import pyfiglet

"""I Don't know why this is full of errors"""

figlet = pyfiglet.figlet_format("PDF to Audio")

RED = '\33[31m'

print(RED + figlet)

print("Enter the path of the pdf file:")

file_path = open(input(), 'rb')

Read_PDF = PyPDF4.PdfFileReader(file_path)

print("Enter the page number:")

page = input()

Page = Read_PDF.getPage()

text = Page.extractText()

audio = gTTS(text)

print("Enter the name of the file you want to create:")

Name_Save = str(input())

audio.save(Name_Save)

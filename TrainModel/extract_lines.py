#given a list of pdf files, this program will extract each line of text from the pdf files and write them to a text file
#then randomly select 20 lines from and write to a txt document
import os
import random
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages[10:]:
            pdf_text += page.extract_text()
    return pdf_text
#function to write text to a file
def write_text_to_file(text, file_name):
    with open(file_name, 'w') as file:
        file.write(text)

#function to extract lines from text
def extract_lines(text):
    lines = text.split('\n')
    return lines

#function to select random lines from a list of lines
def select_random_lines(lines, num_lines):
    random_lines = random.sample(lines, num_lines)
    return random_lines

files_location="/cookingbooks"
#extract text from pdf files
pdf_files = [f for f in os.listdir(files_location) if f.endswith('.pdf')]
for pdf_file in pdf_files:
    pdf_text = extract_text_from_pdf(os.path.join(files_location, pdf_file))
    text_file = pdf_file.replace('.pdf', '.txt')
    write_text_to_file(pdf_text, os.path.join("/extractedtotext", text_file))
    

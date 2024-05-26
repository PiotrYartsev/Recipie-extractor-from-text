#extract pages from pdfs, and write each page to a text file
import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    pdf_text = []
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages[10:]:
            if page.extract_text() is not None:
                pdf_text.append(page.extract_text())
    #remove pages with less than 100 characters
    pdf_text = [page for page in pdf_text if len(page) > 50]
    return pdf_text

files_location="cookingbooks"
txtlocation="extractedtotextpages"
#extract text from pdf files
pdf_files = [f for f in os.listdir(files_location) if f.endswith('.pdf')]

for pdf_file in pdf_files:
    pdf_text = extract_text_from_pdf(os.path.join(files_location, pdf_file))
    n=0
    for page in pdf_text:
        with open(os.path.join(txtlocation, str(n)+".txt"), 'w') as file:
            file.write(page)
        n+=1

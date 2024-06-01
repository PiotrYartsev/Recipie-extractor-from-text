# Import necessary modules
import os
from PyPDF2 import PdfReader
import string

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        list: A list of extracted text from the PDF pages.

    """
    # Initialize an empty list to store the extracted text
    pdf_text = []
    
    # Open the PDF file in binary read mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PdfReader(file)
        
        # Loop through each page in the PDF (starting from the 11th page)
        for page in pdf_reader.pages[10:]:
            # If the page has text, append it to the list
            if page.extract_text() is not None:
                pdf_text.append(page.extract_text())
    
    # Remove pages with less than 50 characters
    pdf_text = [page for page in pdf_text if len(page) > 50]
    
    return pdf_text

# Define the directories for the PDF files and the extracted text files
files_location="cookingbooks"
txtlocation="extractedtotextpages"

# Get a list of all PDF files in the directory
pdf_files = [f for f in os.listdir(files_location) if f.endswith('.pdf')]

# Loop through each PDF file
for pdf_file in pdf_files:
    # Extract the text from the PDF file
    pdf_text = extract_text_from_pdf(os.path.join(files_location, pdf_file))
    
    # Initialize a counter for the text file names
    n=0
    #make a directory named as the pdf_files name
    #remove all wierd characters from the pdf file name, all of them
    pdf_file_2 = pdf_file.translate(str.maketrans('', '', string.punctuation + ' '))

    os.makedirs(os.path.join(txtlocation, pdf_file_2), exist_ok=True)
    # Loop through each page's text
    for page in pdf_text:
        # Write the text to a new text file
        with open(os.path.join(txtlocation+"/"+pdf_file_2, str(n)+".txt"), 'w') as file:
            file.write(page)
        
        # Increment the counter
        n+=1
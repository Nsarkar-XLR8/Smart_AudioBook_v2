# '''
#  Writing Code For Smart Audio Book
# '''

import pyttsx3
import fitz  # PyMuPDF

# Open the PDF file
book = open('Week 12 - Image Restoration in DIP.pdf', 'rb')
pdfReader = fitz.open(book)  # Use PyMuPDF to open the PDF
no_of_pages = pdfReader.page_count  # Get the total number of pages
print(f"The book has {no_of_pages} pages.")

# Initialize the text-to-speech engine
friend = pyttsx3.init()

# Get the starting page number from the user
while True:
    try:
        start_page = int(input(f"Enter the starting page number (1 to {no_of_pages}): "))
        if 1 <= start_page <= no_of_pages:
            break  # Valid input, exit loop
        else:
            print(f"Please enter a valid page number between 1 and {no_of_pages}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Iterate through the pages from the user-specified start page
for page_number in range(start_page - 1, no_of_pages):  # Adjust for 0-index
    page = pdfReader[page_number]  # Get the page
    text = page.get_text()  # Extract text from the page
    
    print(f"Reading Page {page_number + 1}...\n")  # Display page number in console
    friend.say(text)  # Use pyttsx3 to say the text
    friend.runAndWait()  # Ensure it waits for the speech to finish before moving on

# Close the book
book.close()

# Smart_AudioBook_v2

📖 Smart Audio Book
A Python-based audiobook application that reads the contents of a PDF file aloud using text-to-speech (TTS) technology. This project allows users to specify the starting page and reads from that page onwards. The solution leverages the pyttsx3 library for offline TTS and PyMuPDF (fitz) for PDF text extraction.

🚀 Features
* Read any PDF book or document aloud.
* Specify the starting page number from the console.
* Works offline using pyttsx3 (no need for internet-based TTS services).
* Handles multiple pages sequentially with smooth page-to-page reading.
* Customizable voice and speed options for text-to-speech.

🛠️ Requirements
Make sure you have the following installed:

* Python 3.12.5 or higher
Required Python Libraries:
* pyttsx3 for TTS.
* PyMuPDF (also known as fitz) for PDF parsing.

🔧 Installation Guide
* Step 1: Clone the Repository

git clone https://github.com/your-username/smart-audiobook.git
cd smart-audiobook

* Step 2: Install Required Libraries
If pip isn't installed, first install it using:

python -m ensurepip --upgrade

* Then, install the necessary dependencies:
pip install pyttsx3
pip install PyMuPDF

📂 Project Structure
'''bash
SmartAudioBook/
│
├── Week 12 - Image Restoration in DIP.pdf  # Example PDF file
├── smart_audiobook.py                      # Main Python script
└── README.md  
'''

Here’s a detailed GitHub README for your smart audiobook project:

📖 Smart Audio Book
A Python-based audiobook application that reads the contents of a PDF file aloud using text-to-speech (TTS) technology. This project allows users to specify the starting page and reads from that page onwards. The solution leverages the pyttsx3 library for offline TTS and PyMuPDF (fitz) for PDF text extraction.

🚀 Features
Read any PDF book or document aloud.
Specify the starting page number from the console.
Works offline using pyttsx3 (no need for internet-based TTS services).
Handles multiple pages sequentially with smooth page-to-page reading.
Customizable voice and speed options for text-to-speech.
🛠️ Requirements
Make sure you have the following installed:

Python 3.12.5 or higher
Required Python Libraries:
pyttsx3 for TTS.
PyMuPDF (also known as fitz) for PDF parsing.
🔧 Installation Guide
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/your-username/smart-audiobook.git
cd smart-audiobook
Step 2: Install Required Libraries
If pip isn't installed, first install it using:

bash
Copy code
python -m ensurepip --upgrade
Then, install the necessary dependencies:

bash
Copy code
pip install pyttsx3
pip install PyMuPDF
📂 Project Structure
bash
Copy code
SmartAudioBook/
│
├── Week 12 - Image Restoration in DIP.pdf  # Example PDF file
├── smart_audiobook.py                      # Main Python script
└── README.md                               # Project documentation

▶️ How to Run the Project
* Place your PDF file in the project folder.
(You can replace Week 12 - Image Restoration in DIP.pdf with your own book.)

* Run the script using the following command:
python smart_audiobook.py

* Enter the starting page number when prompted:
The book has 12 pages.
* Enter the starting page number (1 to 12): 1
The audiobook will start reading from the specified page.

📝 Code Explanation
Below is a brief breakdown of the smart_audiobook.py code:

* Imports:

pyttsx3 for text-to-speech.
fitz (PyMuPDF) to extract text from the PDF.
* PDF Handling:
book = open('Week 12 - Image Restoration in DIP.pdf', 'rb')
pdfReader = fitz.open(book)
no_of_pages = pdfReader.page_count
User Input for Starting Page:

The user specifies the starting page number.
Input is validated to ensure it falls within the page range.
*Reading the PDF Content:

* The TTS engine reads each page sequentially:
for page_number in range(start_page - 1, no_of_pages):
    page = pdfReader[page_number]
    text = page.get_text()
    friend.say(text)
    friend.runAndWait()
* Closing Resources:
book.close()


🎯 Customization Options
* Change the Voice or Speed: You can modify the TTS engine settings to adjust the voice and reading speed:


friend.setProperty('rate', 150)  # Speed of speech
friend.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id)  # Choose a different voice
Limit the Range of Pages: You can adjust the script to read only a subset of pages by modifying the range() in the for loop.


🛑 Troubleshooting
ModuleNotFoundError: No module named 'pyttsx3'

* Make sure pyttsx3 is installed by running:

pip install pyttsx3
ModuleNotFoundError: No module named 'fitz'

* Install PyMuPDF with:

pip install PyMuPDF
TTS Engine Stops After One Page:

Make sure friend.runAndWait() is inside the loop to ensure the engine finishes reading each page before proceeding.


🤝 Contributing
Feel free to fork the repository, make your changes, and submit a pull request. Contributions are always welcome!

🛡️ License
This project is licensed under the MIT License – see the LICENSE file for details.

📞 Contact
If you have any questions or need help with the project, feel free to reach out!

Email: nsarkar6251gmail.com
GitHub: Nsarkar-XLR8

🌟 Acknowledgements
Pyttsx3: For offline text-to-speech capabilities.
PyMuPDF: For efficient PDF parsing and text extraction.

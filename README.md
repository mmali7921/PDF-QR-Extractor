# PDF-QR-Extractor

A simple Python script to extract QR codes from PDF files and display their decoded data.

## Features
- Converts PDF pages to images.
- Detects and decodes QR codes from each page.
- Displays all extracted QR code data.
- (Optional) Save extracted QR links to a text file.

## Requirements
- Python 3.8+
- [Homebrew](https://brew.sh/) (for macOS users)

### Python Packages
Install via pip:
```bash
pip install -r requirements.txt
```
## System Dependencies (macOS)
This project requires ZBar and Poppler utilities.

Install them using Homebrew:
```bash
brew install zbar
brew install poppler
```
##Example Usage after Installing Requirements
Once the packages are installed, you can run the script:
```bash
python3 main.py path/to/yourfile.pdf
```



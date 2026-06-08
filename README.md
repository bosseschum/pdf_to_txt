# PDF to Text Converter

A Python script that extracts text from scanned or image-based PDFs using OCR (Optical Character Recognition).

## How it works

Each PDF page is rendered as a high-resolution image (300 DPI), then passed through Tesseract OCR to extract the text. The result is saved to a plain text file with clear page markers.

## Requirements

**Python packages:**

```bash
pip install pytesseract pdf2image
```

**System dependencies:**

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) — the OCR engine
- [Poppler](https://poppler.freedesktop.org/) — required by `pdf2image` to render PDF pages

Installation by platform:

| Platform | Command |
|----------|---------|
| Ubuntu/Debian | `sudo apt install tesseract-ocr poppler-utils` |
| macOS | `brew install tesseract poppler` |
| Windows | Install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) manually |

## Configuration

Edit the two constants at the top of `convert.py`:

```python
PDF_PATH = ""   # Path to your input PDF, e.g. "/path/to/document.pdf"
OUTPUT_TXT = "" # Path for the output file,  e.g. "/path/to/output.txt"
```

**Windows only:** Also uncomment and set the Tesseract executable path:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Usage

```bash
python convert.py
```

The script will print progress as it processes each page. Output is a `.txt` file with each page's content separated by markers:

```
--- Page 1 ---
<extracted text>

--- Page Break ---

--- Page 2 ---
...
```

## Notes

- Works best on clearly scanned documents with standard fonts.
- 300 DPI is used for optimal OCR accuracy; lowering it speeds up processing at the cost of quality.
- For PDFs that already contain selectable text, a simpler library like `pdfminer` or `pypdf` will be faster and more accurate than OCR.

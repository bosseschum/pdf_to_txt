import os

import pytesseract
from pdf2image import convert_from_path

# --- CONFIGURATION ---
PDF_PATH = ""  # Path to the PDF file
OUTPUT_TXT = ""  # Path to the output text file

# Windows needs to set the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def convert_pdf_to_txt(pdf_path, output_txt):
    print("Step 1: Converting PDF pages to images...")
    # Convert PDF pages to a list of PIL image objects
    pages = convert_from_path(
        pdf_path, dpi=300
    )  # optimal for optical character recognition
    print(f"Total pages found: {len(pages)}")

    print("Step 2: Extracting text page by page...")
    with open(output_txt, "w", encoding="utf-8") as text_file:
        for i, page in enumerate(pages, start=1):
            print(f"  Processing page {i}/{len(pages)}")

            # Preserve layout attempts to keep paragraphs and columns intact
            custom_config = r"--oem 3 --psm 3"
            page_text = pytesseract.image_to_string(page, config=custom_config)

            # Write page content and visual separator for clarity
            text_file.write(f"--- Page {i} ---\n")
            text_file.write(page_text)
            text_file.write("\n\n--- Page Break ---\n\n")

    print(f"Step 3: Text extraction complete. Output saved to {output_txt}")


if __name__ == "__main__":
    if os.path.exists(PDF_PATH):
        convert_pdf_to_txt(PDF_PATH, OUTPUT_TXT)
    else:
        print(f"Error: PDF file not found at {PDF_PATH}")

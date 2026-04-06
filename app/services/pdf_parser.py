import re
import os
import pdfplumber


def clean_text(text: str) -> str:
    """
    Cleans extracted text by removing extra spaces,
    line breaks, and unwanted formatting.
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file and returns cleaned text.

    Args:
        pdf_path (str): Path to the PDF file

    Returns:
        str: Cleaned extracted text
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    try:
        text_chunks = []

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text_chunks.append(page_text)

        raw_text = "\n".join(text_chunks)
        cleaned_text = clean_text(raw_text)

        if not cleaned_text:
            raise ValueError("No text extracted. PDF may be image-based.")

        return cleaned_text

    except Exception as e:
        raise RuntimeError(f"PDF parsing failed: {str(e)}")
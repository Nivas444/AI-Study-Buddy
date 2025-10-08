import pytesseract
from PIL import Image
import easyocr
import PyPDF2

def pdf_to_text(pdf_path):
    """Extract text from PDF"""
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def image_to_text(image_path, method="tesseract"):
    """Extract text from image using Tesseract or EasyOCR"""
    if method == "tesseract":
        return pytesseract.image_to_string(Image.open(image_path))
    elif method == "easyocr":
        reader = easyocr.Reader(['en'])
        result = reader.readtext(image_path)
        return " ".join([res[1] for res in result])
    else:
        raise ValueError("Invalid OCR method")

# Example usage
if __name__ == "__main__":
    print(pdf_to_text("data/notes/sample.pdf"))
    print(image_to_text("data/notes/sample.jpg"))

import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import io

def ocr_iz_slike(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        try:
            tekst = pytesseract.image_to_string(image, lang='srp')
        except:
            tekst = pytesseract.image_to_string(image, lang='eng')
        return tekst.strip()
    except Exception as e:
        return f"OCR greška (slika): {e}"

def ocr_iz_pdf(pdf_bytes):
    try:
        tekst_ukupno = ""
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        for page in doc:
            pix = page.get_pixmap(dpi=300)
            img_bytes = pix.tobytes("png")
            tekst = ocr_iz_slike(img_bytes)
            tekst_ukupno += tekst + "\n"
        return tekst_ukupno.strip()
    except Exception as e:
        return f"OCR greška (PDF): {e}"

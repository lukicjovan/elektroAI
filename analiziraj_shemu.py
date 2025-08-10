import os
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader

def analiziraj_shemu(projekat):
    shema_folder = os.path.join("projekti", projekat["naziv"], "sheme")
    rezultati = {}

    if not os.path.exists(shema_folder):
        return {"greska": "Nema šema u projektu."}

    for ime_fajla in os.listdir(shema_folder):
        putanja = os.path.join(shema_folder, ime_fajla)
        tekst = ""

        if ime_fajla.lower().endswith(".pdf"):
            try:
                reader = PdfReader(putanja)
                for i, stranica in enumerate(reader.pages):
                    if stranica:
                        tekst += stranica.extract_text() or ""
            except Exception as e:
                tekst += f"[Greška PDF]: {e}"

        elif ime_fajla.lower().endswith((".png", ".jpg", ".jpeg")):
            try:
                slika = Image.open(putanja)
                tekst = pytesseract.image_to_string(slika)
            except Exception as e:
                tekst = f"[Greška OCR]: {e}"

        rezultati[ime_fajla] = tekst.strip() if tekst else "[Nema teksta]"

    return rezultati

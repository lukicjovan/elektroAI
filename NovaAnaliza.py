
import fitz

def analiziraj_pdf(pdf_path, ime_projekta):
    tekst = ""
    try:
        pdf = fitz.open(pdf_path)
        for page in pdf:
            tekst += page.get_text()
        pdf.close()
    except Exception as e:
        tekst = f"[GREŠKA] Ne mogu da pročitam PDF: {e}"

    return {
        "ime_projekta": ime_projekta,
        "tekst": tekst
    }

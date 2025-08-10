
import os
import fitz
from PIL import Image
import io

from klasifikuj_simbolicne_oznake import klasifikuj_simbolicne_oznake
from ml_prioritet_klasifikator import predvidi_prioritet_ml
from huggingface_ocr import izvuci_tekst_iz_slike

def analiziraj_sheme(lista_putanja, ime_projekta):
    objedinjeni_tekst = ""

    for putanja in lista_putanja:
        try:
            if putanja.lower().endswith(".pdf"):
                doc = fitz.open(putanja)
                for page in doc:
                    tekst = page.get_text()
                    objedinjeni_tekst += tekst + "\n"
                doc.close()
            else:
                with open(putanja, "rb") as f:
                    img = Image.open(io.BytesIO(f.read()))
                    tekst = izvuci_tekst_iz_slike(img)
                    objedinjeni_tekst += tekst + "\n"
        except Exception as e:
            print(f"[GREŠKA] Ne mogu da obradim {putanja}: {e}")

    oznake = klasifikuj_simbolicne_oznake(objedinjeni_tekst)
    prioritet = predvidi_prioritet_ml(objedinjeni_tekst)

    return {
        "tekst": objedinjeni_tekst,
        "simboli": oznake,
        "ml_prioritet": prioritet,
        "broj_fajlova": len(lista_putanja)
    }

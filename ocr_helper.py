import os

def ucitaj_ocr_tekstove_aktivnog_projekta(projekat):
    tekst = ""

    ocr_sheme = projekat.get("ocr_sheme", [])
    ocr_dok = projekat.get("ocr_dokumentacija", [])

    if ocr_sheme:
        tekst += "\n\n--- TEKST IZ ŠEMA ---\n"
        for s in ocr_sheme:
            tekst += f"\n• {s}\n"

    if ocr_dok:
        tekst += "\n\n--- TEKST IZ DOKUMENTACIJE ---\n"
        for d in ocr_dok:
            tekst += f"\n• {d}\n"

    return tekst.strip()

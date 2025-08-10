import os
from PIL import Image
import torch
import json
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from klasifikuj_simbolicne_oznake import klasifikuj_simbolicne_oznake

# Učitavanje OCR modela
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

def prepoznaj_tekst_sa_slike(image_path):
    """
    OCR sa slike pomoću TrOCR modela.
    :param image_path: putanja do slike
    :return: string sa tekstom
    """
    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    with torch.no_grad():
        generated_ids = model.generate(pixel_values)
    tekst = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return tekst

def izdvoji_oznake(tekst):
    """
    Ekstraktuje tehničke oznake iz OCR teksta.
    :param tekst: tekst sa slike
    :return: lista oznaka
    """
    kandidati = []
    for linija in tekst.split():
        linija = linija.strip().upper()
        if any(simbol in linija for simbol in ["QF", "K", "S", "M", "PLC", "VFD", "FU", "L", "PE", "R", "X", "G"]):
            kandidati.append(linija)
    return kandidati

def prepoznaj_komponente_na_slikama(projekat_ime="TreningOrman"):
    """
    Pokreće OCR analizu nad slikama iz foldera 'fotografije/' i klasifikuje oznake.
    :param projekat_ime: ime projekta radi čuvanja rezultata
    :return: dict sa nazivom slike i listom komponenti
    """
    folder = "fotografije"
    rezultati = {}
    sve_komponente = []

    for ime_fajla in os.listdir(folder):
        if not ime_fajla.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        putanja = os.path.join(folder, ime_fajla)
        tekst = prepoznaj_tekst_sa_slike(putanja)
        oznake = izdvoji_oznake(tekst)
        klasifikovane = klasifikuj_simbolicne_oznake(oznake)
        rezultati[ime_fajla] = klasifikovane

        for k in klasifikovane:
            sve_komponente.append({
                "oznaka": k["oznaka"],
                "tip": k["tip"],
                "izvor": f"OCR_{ime_fajla}"
            })

    # 💾 Čuvanje rezultata u JSON po projektu
    os.makedirs("prethodni_projekti", exist_ok=True)
    folder_proj = os.path.join("prethodni_projekti", projekat_ime)
    os.makedirs(folder_proj, exist_ok=True)

    with open(os.path.join(folder_proj, "komponente.json"), "w", encoding="utf-8") as f:
        json.dump(sve_komponente, f, indent=2, ensure_ascii=False)

    return rezultati
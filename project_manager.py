import os
import json

BAZA_PROJEKATA = "projekti"

def sacuvaj_novi_projekat(naziv):
    putanja = os.path.join(BAZA_PROJEKATA, naziv)
    os.makedirs(os.path.join(putanja, "sheme"), exist_ok=True)
    os.makedirs(os.path.join(putanja, "dokumentacija"), exist_ok=True)
    meta_path = os.path.join(putanja, "meta.json")
    if not os.path.exists(meta_path):
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump({"naziv": naziv}, f)

def ucitaj_listu_projekata():
    if not os.path.exists(BAZA_PROJEKATA):
        return []
    return [ime for ime in os.listdir(BAZA_PROJEKATA) if os.path.isdir(os.path.join(BAZA_PROJEKATA, ime))]

def ucitaj_aktivni_projekat(naziv):
    path = os.path.join(BAZA_PROJEKATA, naziv, "meta.json")
    if not os.path.exists(path):
        return {"naziv": naziv}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["naziv"] = naziv
    return data

def get_project_path(projekat):
    return os.path.join(BAZA_PROJEKATA, projekat["naziv"])

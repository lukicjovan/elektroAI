import os
import json
import pandas as pd

def ucitaj_sve_komponente(projekti_folder="prethodni_projekti"):
    sve_komponente = []

    for projekat in os.listdir(projekti_folder):
        putanja_json = os.path.join(projekti_folder, projekat, "komponente.json")
        if os.path.exists(putanja_json):
            try:
                with open(putanja_json, "r", encoding="utf-8") as f:
                    komponente = json.load(f)
                    for k in komponente:
                        k["projekat"] = projekat
                        sve_komponente.append(k)
            except Exception as e:
                print(f"⚠️ Greška u projektu {projekat}: {str(e)}")

    df = pd.DataFrame(sve_komponente)
    return df
import os
import json
from analiziraj_dokumentaciju import izvuci_znanje_iz_dokumenta, izvuci_tekst_iz_pdf

def obradi_dokumente_iz_foldera(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    """
    Analizira sve PDF/TXT dokumente iz foldera i vraća uvid-e po dokumentu.
    :param folder_path: folder gde se nalaze dokumenti
    :return: lista dict-ova sa 'fajl' i 'uvidi'
    """
    svi_uvidi = []

    for fajl_ime in os.listdir(folder_path):
        putanja = os.path.join(folder_path, fajl_ime)

        if fajl_ime.lower().endswith(".pdf"):
            tekst = izvuci_tekst_iz_pdf(putanja)
        elif fajl_ime.lower().endswith(".txt"):
            with open(putanja, "r", encoding="utf-8") as f:
                tekst = f.read()
        else:
            print(f"⚠️ Preskačem '{fajl_ime}' — nije PDF/TXT.")
            continue

        uvidi = izvuci_znanje_iz_dokumenta(tekst)
        svi_uvidi.append({
            "fajl": fajl_ime,
            "uvidi": uvidi
        })

    return svi_uvidi

# 🧠 Direktno pokretanje treninga
if __name__ == "__main__":
    folder = "trening_dokumentacija"
    rezultati = obradi_dokumente_iz_foldera(folder)

    with open("uvidi_iz_treninga.json", "w", encoding="utf-8") as f:
        json.dump(rezultati, f, indent=2, ensure_ascii=False)

    print("\n✅ Trening završen. Uvidi sačuvani u 'uvidi_iz_treninga.json'.")
    for rezultat in rezultati:
        print(f"\n📄 {rezultat['fajl']}")
        for u in rezultat["uvidi"]:
            print(f"- {u}")

def obradi_sve(folder_path):
    return obradi_dokumente_iz_foldera(folder_path)

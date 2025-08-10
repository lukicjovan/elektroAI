import os

def obradi_dokumentaciju(projekat):
    """
    Simulacija obrade dodatne tehničke dokumentacije. Prava logika će uključiti OCR ekstrakciju teksta iz PDF-ova/slika.
    """
    ime_projekta = projekat.get("ime", "nepoznato")
    broj_dokumenata = len(projekat.get("dokumentacija", []))

    rezultat = {
        "projekat": ime_projekta,
        "broj_dokumenata": broj_dokumenata,
        "analiza": [
            {
                "dokument": f"dokument_{i+1}.pdf",
                "sadrzaj": "Simulirani tekst iz dokumenta",
                "napomena": "Nema primedbi"
            } for i in range(broj_dokumenata)
        ]
    }

    return rezultat

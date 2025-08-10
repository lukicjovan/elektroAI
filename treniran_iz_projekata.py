from upravljaj_projektima import ucitaj_sve_projekte

def ucitaj_dataset_za_trening():
    """
    Priprema tekstualni skup i label-e iz istorije dijagnoza za treniranje ML modela.
    Svaki unos je spoj simptoma i tipova komponenti, a label je prioritet.
    """
    projekti = ucitaj_sve_projekte()
    tekstovi, labeli = [], []

    for proj in projekti:
        # Svaki projekat može imati više dijagnoza u okviru liste "dijagnoze"
        for d in proj.get("dijagnoze", []):
            opis = d.get("opis", "").strip()
            prio = d.get("prioritet", "").strip()
            if not opis or not prio:
                continue

            # Spoji opis sa svim tipovima komponenti u projektu
            kom_tips = " ".join(
                [k.get("tip", "") for k in proj.get("komponente", [])]
            ).strip()

            ulaz = f"{opis} {kom_tips}".strip()
            tekstovi.append(ulaz)
            labeli.append(prio)

    return tekstovi, labeli

def ucitaj_sve_projekte_info():
    """
    Prosta alias-funkcija za dobavljanje svih projekata (sve njihove podatke).
    Koristi se tamo gde trebamo kompletan JSON svakog projekta.
    """
    return ucitaj_sve_projekte()

def pokreni_trening(projekat_ime):
    return ucitaj_trening_podatke(projekat_ime)

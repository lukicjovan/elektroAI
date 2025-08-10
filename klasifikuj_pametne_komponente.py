def klasifikuj_pametne_komponente(komponente):
    """
    Prolazi kroz listu komponenti i automatski dodeljuje tip 'KNX' ili 'DALI' prema nazivu, oznaci i opisu.
    :param komponente: lista dict objekata sa komponentama
    :return: lista sa ažuriranim komponentama
    """
    pametni_tipovi = []

    for komp in komponente:
        tekstovi = [
            komp.get("oznaka", "").lower(),
            komp.get("naziv", "").lower(),
            komp.get("opis", "").lower()
        ]
        spojeno = " ".join(tekstovi)

        tip = komp.get("tip", "").lower()

        # Detekcija KNX
        if "knx" in spojeno or "group address" in spojeno or "/".join(spojeno.split()):
            komp["tip"] = "KNX"
            pametni_tipovi.append("KNX")
        # Detekcija DALI
        elif "dali" in spojeno or "driver" in spojeno or "lighting" in spojeno or "scene" in spojeno or "ballast" in spojeno:
            komp["tip"] = "DALI"
            pametni_tipovi.append("DALI")
        else:
            # Ako već ima tip, ostavi — inače stavi "standard"
            komp["tip"] = tip if tip else "standard"

    return komponente
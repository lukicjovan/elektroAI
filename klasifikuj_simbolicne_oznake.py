
def klasifikuj_simbolicne_oznake(tekst):
    # Ovo je pojednostavljena verzija klasifikatora
    simboli = []
    linije = tekst.lower().split("\n")
    for linija in linije:
        if "svetlo" in linija or "rasveta" in linija:
            simboli.append("Rasveta")
        elif "utičnica" in linija:
            simboli.append("Utičnica")
        elif "prekidač" in linija:
            simboli.append("Prekidač")
        elif "knx" in linija:
            simboli.append("KNX sistem")
    return list(set(simboli))

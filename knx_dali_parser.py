def klasifikuj_knx_dali_linije(tekst):
    """
    Analizira tekstualnu dokumentaciju i identifikuje KNX i DALI komponente, magistrale i veze.
    :param tekst: sirovi string iz PDF-a ili TXT dokumentacije
    :return: lista uvida (stringova) o pametnim sistemima
    """
    uvidi = []

    linije = tekst.split("\n")
    for linija in linije:
        l = linija.lower()

        # KNX detekcija
        if "knx" in l:
            if "group address" in l or "/" in l:
                uvidi.append("🔗 Otkrivena KNX grupna adresa: " + linija.strip())
            elif "line controller" in l or "lc" in l:
                uvidi.append("🧠 Identifikovan KNX Line Controller: " + linija.strip())
            elif "sensor" in l or "actuator" in l:
                uvidi.append("🎛️ KNX komponenta (senzor/aktuator): " + linija.strip())
            elif "gateway" in l:
                uvidi.append("🌐 KNX gateway detektovan: " + linija.strip())
            else:
                uvidi.append("📘 KNX referenca u dokumentaciji: " + linija.strip())

        # DALI detekcija
        if "dali" in l:
            if "driver" in l or "group" in l or "bus" in l or "ballast" in l:
                uvidi.append("🔌 DALI segment detektovan: " + linija.strip())
            elif "scene" in l or "lighting" in l or "intensity" in l:
                uvidi.append("💡 DALI svetlosni sistem / scenariji: " + linija.strip())
            elif "controller" in l or "interface" in l:
                uvidi.append("🧠 DALI kontrolni modul: " + linija.strip())
            else:
                uvidi.append("📘 DALI referenca u dokumentaciji: " + linija.strip())

    return uvidi
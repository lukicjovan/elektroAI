import re

def analiziraj_ocr_tekst(tekst):
    komponente = []
    linije = tekst.split("\n")
    for linija in linije:
        linija = linija.strip()
        oznake = re.findall(r"\b[A-Z]{1,2}\d{1,3}\b", linija)
        for oznaka in oznake:
            tip = klasifikuj_oznaku(oznaka)
            if not any(k["oznaka"] == oznaka for k in komponente):
                komponente.append({"oznaka": oznaka, "tip": tip, "opis": linija})
    return komponente

def klasifikuj_oznaku(oznaka):
    oznaka = oznaka.upper()
    if oznaka.startswith("F"):
        return "osigurač"
    if oznaka.startswith("S"):
        return "prekidač"
    if oznaka.startswith("L"):
        return "svetlo"
    if oznaka.startswith("K"):
        return "rele/kontaktor"
    if oznaka.startswith("T"):
        return "termička zaštita"
    if oznaka.startswith("A"):
        return "aktuator"
    if "KNX" in oznaka:
        return "KNX pametni uređaj (smart home)"
    if "DALI" in oznaka:
        return "DALI pametni uređaj (smart home)"
    if "ZIGBEE" in oznaka or "ZB" in oznaka:
        return "Zigbee uređaj (smart home)"
    if "IOT" in oznaka:
        return "IoT uređaj (smart home)"
    if oznaka.startswith("M") or oznaka.startswith("Q"):
        return "industrijski motor/oprema"
    if "PLC" in oznaka:
        return "PLC (industrijska automatika)"
    return "nepoznato"

def detektuj_veze(tekst):
    veze = []
    linije = tekst.split("\n")
    for linija in linije:
        match = re.search(r"\b([A-Z]{1,2}\d{1,3})\b\s+upravlja\s+\b([A-Z]{1,2}\d{1,3})\b\s+preko\s+\b([A-Z]{1,2}\d{1,3})\b", linija)
        if match:
            veze.append({"izvor": match.group(1), "meta": match.group(2), "preko": match.group(3)})
            continue
        match2 = re.search(r"\b([A-Z]{1,2}\d{1,3})\b\s+upravlja\s+\b([A-Z]{1,2}\d{1,3})\b", linija)
        if match2:
            veze.append({"izvor": match2.group(1), "meta": match2.group(2)})
    return veze

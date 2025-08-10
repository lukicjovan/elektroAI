import difflib
try:
    from transformers import pipeline
except ImportError:
    pipeline = None
from treniran_iz_projekata import ucitaj_sve_projekte
from ml_prioritet_klasifikator import predvidi_prioritet_ml

# ================ Baza poznatih kvarova (faza 2) ================
BAZA_KVAROVA = [
    {"simptom": "lampica ne svetli", "tip": "svetiljka",
     "akcija": "Proveri prekidač (QF) i relej (R).", "prioritet": "srednji"},
    {"simptom": "pregrevanje", "tip": "motor",
     "akcija": "Proveri ventilacione otvore i relej termičke zaštite.", "prioritet": "visok"},
    {"simptom": "greška e48", "tip": "vfd",
     "akcija": "Proveri komunikaciju između VFD i PLC modula.", "prioritet": "visok"},
    {"simptom": "ne reaguje sistem", "tip": "plc jedinica",
     "akcija": "Proveri napajanje i ulaze na PLC.", "prioritet": "srednji"}
]

# ================ Zero-shot NLP model (faza 5) ================
if pipeline:
    nlp_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
else:
    nlp_model = None

# ================ Pomoćna funkcija: boost iz istorije (faza 8a) ================
def proveri_istoriju_ponavljanja(simptom, akcija):
    svi_projekti = ucitaj_sve_projekte()
    brojac = 0
    for p in svi_projekti:
        dij = p.get("dijagnoze", [])
        for d in dij:
            if d.get("opis", "").lower() == simptom.lower() and d.get("akcija", "") == akcija:
                brojac += 1

    if brojac >= 5:
        return "visok"
    if brojac >= 3:
        return "srednji"
    if brojac >= 1:
        return "nizak"
    return "nepoznat"

# ================ Glavna funkcija analize (faze 5, 8a i 13) ================
def analiziraj_opis_nlp(opis, komponente):
    """
    Ulaz:
      opis: slobodan tekst korisnika
      komponente: lista dictova s poljem "tip"
    Izlaz: dict with keys: "akcija", "prioritet", "skor"
    """

    # 1) Zero-shot klasifikacija simptoma
    labels = [k["simptom"] for k in BAZA_KVAROVA]
    pred = nlp_model(opis, labels, multi_label=True)
    kandidati = sorted(zip(pred["labels"], pred["scores"]),
                       key=lambda x: x[1], reverse=True)

    # 2) Pronađi prvi koji odgovara tipu komponente
    for label, skor in kandidati:
        for kvar in BAZA_KVAROVA:
            if label == kvar["simptom"] and any(
               k["tip"].lower() == kvar["tip"] for k in komponente):
                # 3) Boost iz istorije
                boost_prior = proveri_istoriju_ponavljanja(kvar["simptom"], kvar["akcija"])

                # 4) ML predikcija prioriteta
                ml_pred = predvidi_prioritet_ml(opis, komponente)

                # 5) Usporedi i izaberi viši prioritet
                red = {"nepoznat": 0, "nizak": 1, "srednji": 2, "visok": 3}
                final_prior = boost_prior
                if ml_pred and red.get(ml_pred, 0) > red.get(boost_prior, 0):
                    final_prior = ml_pred

                return {
                    "akcija": kvar["akcija"],
                    "prioritet": final_prior,
                    "skor": round(skor, 2)
                }

    # 6) Ako ništa ne nađemo
    return {
        "akcija": "Nemam dovoljnih podataka za preciznu dijagnozu.",
        "prioritet": "nepoznat",
        "skor": 0.0
    }

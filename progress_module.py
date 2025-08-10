import streamlit as st
import time

def pokreni_napredak(trajanje_sekundi=5, tekstovi=None):
    """
    Pokreće progresni prikaz za zadatu obradu
    :param trajanje_sekundi: ukupno trajanje animacije
    :param tekstovi: lista poruka koje se postepeno prikazuju
    """
    progress_bar = st.progress(0)
    status = st.empty()

    if tekstovi is None:
        tekstovi = [
            "🔍 Pripremam podatke...",
            "📄 Učitavam dokumentaciju...",
            "🧠 Izvlačim znanje...",
            "🛠️ Obradjujem relacije...",
            "✅ Gotovo!"
        ]

    koraci = len(tekstovi)
    pauza = trajanje_sekundi / koraci

    for i, poruka in enumerate(tekstovi):
        status.info(poruka)
        progress_bar.progress(int((i + 1) * 100 / koraci))
        time.sleep(pauza)

    status.success("✅ Obrada završena.")
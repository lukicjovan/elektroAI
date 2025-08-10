import streamlit as st
import pandas as pd
from upravljaj_projektima import ucitaj_sve_projekte

def prikazi_uporedjivanje_projekata(aktivni_projekat):
    st.subheader("📊 Uporedi sa drugim projektima")

    # Učitaj sve projekte i isključi aktivni
    svi = ucitaj_sve_projekte()
    ostali = [p for p in svi if p["naziv"] != aktivni_projekat["naziv"]]
    if not ostali:
        st.info("ℹ️ Nema drugih projekata za poređenje.")
        return

    # Izbor projekta za poređenje
    imena = [p["naziv"] for p in ostali]
    odabrano = st.selectbox("Izaberi projekat za poređenje:", imena)
    drugi = next(p for p in ostali if p["naziv"] == odabrano)

    # 1) Osnovni metrički pregled
    def izracunaj_metričke(p):
        return {
            "Projekat": p["naziv"],
            "Broj dijagnoza": len(p.get("dijagnoze", [])),
            "Servisnih uzoraka": len(p.get("servisni_uzorci", [])),
            "Broj komponenti": len(p.get("komponente", []))
        }

    df_metričke = pd.DataFrame([
        izracunaj_metričke(aktivni_projekat),
        izracunaj_metričke(drugi)
    ]).set_index("Projekat")
    st.markdown("### 🔢 Osnovni metrički pregled")
    st.table(df_metričke)

    # 2) Distribucija prioriteta u dijagnozama
    def broji_prioritete(p):
        prios = [d.get("prioritet", "nepoznat") for d in p.get("dijagnoze", [])]
        return pd.Series(prios).value_counts()

    df_prio = pd.DataFrame({
        aktivni_projekat["naziv"]: broji_prioritete(aktivni_projekat),
        drugi["naziv"]: broji_prioritete(drugi)
    }).fillna(0).astype(int)
    st.markdown("### 📈 Distribucija prioriteta")
    st.bar_chart(df_prio)

    # 3) Poređenje tipova komponenti
    tips1 = {c.get("tip") for c in aktivni_projekat.get("komponente", []) if c.get("tip")}
    tips2 = {c.get("tip") for c in drugi.get("komponente", []) if c.get("tip")}
    zajednički = tips1 & tips2
    unikatni1 = tips1 - tips2
    unikatni2 = tips2 - tips1

    st.markdown("### 🔧 Tipovi komponenti")
    st.write(f"- Zajednički tipovi: {', '.join(sorted(zajednički)) or '–'}")
    st.write(f"- Samo u aktivnom: {', '.join(sorted(unikatni1)) or '–'}")
    st.write(f"- Samo u poređenom: {', '.join(sorted(unikatni2)) or '–'}")

def uporedi(projekat1, projekat2):
    st.warning("⚠️ Funkcija 'uporedi' koristi Streamlit UI za poređenje projekata.")

import os
import streamlit as st
from project_manager import (
    ucitaj_listu_projekata,
    ucitaj_aktivni_projekat,
    sacuvaj_novi_projekat
)
from analiziraj_shemu import analiziraj_shemu
from analiziraj_dokumentaciju import obradi_dokumentaciju
from shema_ui import shema_ui
from dokumentacija_ui import dokumentacija_ui
from ai_ui import ai_ui

st.set_page_config(layout="wide")
st.title("🔌 elektroAI – Dijagnostika elektroinstalacija")

projekti = ucitaj_listu_projekata()

if "projekat_select" not in st.session_state:
    st.session_state["projekat_select"] = projekti[0] if projekti else None

col1, col2 = st.columns([3, 1])

with col2:
    st.markdown("### ➕ Novi projekat")
    novi_projekat_ime = st.text_input("Unesi ime projekta")
    if st.button("Kreiraj projekat"):
        if novi_projekat_ime.strip():
            sacuvaj_novi_projekat(novi_projekat_ime.strip())
            st.session_state["projekat_select"] = novi_projekat_ime.strip()
            st.experimental_rerun()
        else:
            st.warning("Ime projekta ne može biti prazno.")

    st.markdown("### 📁 Odaberi projekat")
    odabrani = st.selectbox("", projekti, key="projekat_select")

if odabrani:
    aktivni_projekat = ucitaj_aktivni_projekat(odabrani)
    st.markdown(f"### 📊 Aktivni projekat: `{odabrani}`")

    shema_ui(aktivni_projekat)
    dokumentacija_ui(aktivni_projekat)

    if st.button("🔍 Analiziraj projekat"):
        with st.spinner("Analiziram..."):
            rezultat = analiziraj_shemu(aktivni_projekat)
            st.success("Analiza završena")
            st.json(rezultat)

    st.markdown("### 🧾 Dijagnostika kvara")
    opis_kvara = st.text_area("Unesi opis kvara")
    if st.button("🛠 Dijagnostikuj kvar"):
        with st.spinner("Pokrećem dijagnostiku..."):
            st.info("(Simulacija) Dijagnostički rezultat: Proveri kabl između F2 i L2.")

    ai_ui(aktivni_projekat)

else:
    st.warning("Nema dostupnih projekata. Kreiraj novi za početak.")

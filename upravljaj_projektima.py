import os
import json
try:
    import streamlit as st
except ImportError:
    st = None
from datetime import datetime

FOLDER_PROJEKATA = "projekti"

def inicijalizuj_folder():
    if not os.path.exists(FOLDER_PROJEKATA):
        os.makedirs(FOLDER_PROJEKATA)

def sacuvaj_projekat(naziv, data):
    """
    Sačuva ceo projekat u JSON fajl pod nazivom <naziv>.json.
    """
    inicijalizuj_folder()
    putanja = os.path.join(FOLDER_PROJEKATA, f"{naziv}.json")
    with open(putanja, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def ucitaj_projekat(naziv):
    """
    Učita projekat iz JSON fajla. Vraća dict ili None.
    """
    inicijalizuj_folder()
    putanja = os.path.join(FOLDER_PROJEKATA, f"{naziv}.json")
    if not os.path.exists(putanja):
        return None
    with open(putanja, "r", encoding="utf-8") as f:
        return json.load(f)

def ucitaj_sve_projekte():
    """
    Učita sve JSON fajlove iz foldera i vraća listu projekata (dict).
    """
    inicijalizuj_folder()
    projekti = []
    for fname in os.listdir(FOLDER_PROJEKATA):
        if fname.endswith(".json"):
            path = os.path.join(FOLDER_PROJEKATA, fname)
            with open(path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    projekti.append(data)
                except:
                    continue
    return projekti

def prikazi_upravljanje_projekte():
    st.subheader("📂 Upravljanje projektima")

    inicijalizuj_folder()
    postojeći = [p["naziv"] for p in ucitaj_sve_projekte()]

    # Kreiranje novog projekta
    novi_naziv = st.text_input("Naziv novog projekta:")
    if st.button("➕ Kreiraj novi projekt"):
        if not novi_naziv.strip():
            st.error("⚠️ Unesite važeći naziv projekta.")
        elif novi_naziv in postojeći:
            st.error("❌ Projekat sa tim imenom već postoji.")
        else:
            novi = {
                "naziv": novi_naziv,
                "komponente": [],
                "sheme": [],
                "dijagnoze": [],
                "servisni_uzorci": [],
                "profil_signala": None,
                "kreirano": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            sacuvaj_projekat(novi_naziv, novi)
            st.success(f"✅ Projekat '{novi_naziv}' je kreiran.")
            postojeći.append(novi_naziv)

    st.markdown("---")

    # Lista i učitavanje postojećeg projekta
    if postojeći:
        izaberi = st.selectbox("Odaberi projekat za učitavanje:", postojeći)
        if st.button("📂 Učitaj projekat"):
            projekat = ucitaj_projekat(izaberi)
            if projekat:
                st.session_state["aktivni_projekat"] = projekat
                st.success(f"✅ Projekat '{izaberi}' je učitan.")
            else:
                st.error("❌ Greška pri učitavanju projekta.")
    else:
        st.info("ℹ️ Još nema sačuvanih projekata.")

    # Brisanje projekta
    if st.session_state.get("aktivni_projekat"):
        aktif = st.session_state["aktivni_projekat"]["naziv"]
        if st.button(f"🗑️ Obriši projekt '{aktif}'"):
            putanja = os.path.join(FOLDER_PROJEKATA, f"{aktif}.json")
            try:
                os.remove(putanja)
                st.session_state.pop("aktivni_projekat")
                st.success(f"✅ Projekat '{aktif}' je obrisan.")
            except:
                st.error("❌ Ne mogu da obrišem projekat.")

    # Prikaz detalja aktivnog projekta
    aktivni = st.session_state.get("aktivni_projekat")
    if aktivni:
        st.markdown("### 📋 Detalji aktivnog projekta")
        st.write(f"- Naziv: {aktivni['naziv']}")
        st.write(f"- Kreirano: {aktivni.get('kreirano','–')}")
        st.write(f"- Broj komponenti: {len(aktivni.get('komponente', []))}")
        st.write(f"- Broj šema: {len(aktivni.get('sheme', []))}")
        st.write(f"- Broj ranijih dijagnoza: {len(aktivni.get('dijagnoze', []))}")
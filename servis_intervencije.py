import os
import json
import streamlit as st
from datetime import datetime

FOLDER_PROJEKATA = "projekti"

def inicijalizuj_folder():
    if not os.path.exists(FOLDER_PROJEKATA):
        os.makedirs(FOLDER_PROJEKATA)

def sacuvaj_servisni_uzorak(naziv_projekta, simptom, resenje):
    inicijalizuj_folder()
    putanja = os.path.join(FOLDER_PROJEKATA, f"{naziv_projekta}.json")
    if not os.path.exists(putanja):
        st.error("❌ Projekat ne postoji, prvo sačuvaj dijagnozu.")
        return

    with open(putanja, "r+", encoding="utf-8") as f:
        data = json.load(f)
        uzorci = data.get("servisni_uzorci", [])
        uzorci.append({
            "simptom": simptom,
            "resenje": resenje,
            "datum": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        data["servisni_uzorci"] = uzorci
        f.seek(0)
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.truncate()
    st.success("✅ Tvoj servisni uzorak je sačuvan.")

def ucitaj_sve_servisne_uzorke():
    inicijalizuj_folder()
    svi = []
    for fajl in os.listdir(FOLDER_PROJEKATA):
        if fajl.endswith(".json"):
            with open(os.path.join(FOLDER_PROJEKATA, fajl), "r", encoding="utf-8") as f:
                data = json.load(f)
                svi.extend(data.get("servisni_uzorci", []))
    return svi

def predlozi_uzorci_po_simptomu(simptom):
    svi = ucitaj_sve_servisne_uzorke()
    return [u["resenje"] for u in svi if u["simptom"].lower() == simptom.lower()]

def prikazi_servisni_uzorak(naziv_projekta, rezultat_dijagnostike):
    st.subheader("🔧 Servisne intervencije – tvoja istorija rešenja")

    simptom = rezultat_dijagnostike.get("opis", "")
    st.markdown(f"**Opis kvara:** {simptom}")

    predlozi = predlozi_uzorci_po_simptomu(simptom)
    if predlozi:
        st.markdown("### 💡 Prethodna rešenja za ovaj simptom:")
        for i, p in enumerate(predlozi, 1):
            st.write(f"{i}. {p}")
    else:
        st.info("ℹ️ Još nema sačuvanih rešenja za ovaj simptom.")

    novo = st.text_area("📝 Opis tvog rešenja:")
    if st.button("💾 Sačuvaj svoje rešenje"):
        if novo.strip():
            sacuvaj_servisni_uzorak(naziv_projekta, simptom, novo.strip())
        else:
            st.error("⚠️ Unesi tekst rešenja pre čuvanja.")
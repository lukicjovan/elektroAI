import streamlit as st
import os

# 🔐 Autentifikacija i inicijalizacija
from auth_manager import login_user, register_user, init_auth_db
from database import init_db
from theme_manager import apply_theme
from gallery import render_sidebar_gallery
from usage_tracker import get_top_features

# 🎯 Osnovne funkcije
from KomponenteDashboard import pokreni_dashboard
from feedback_collector import feedback_form
from izvestaj_generator import generate_report
from report_scheduler import schedule_report
from plugin_manager import get_plugins, run_plugin
from onboarding_guide import launch_guide
from video_player import play_tutorial

# 📂 ElektroAI analize
elektroai_moduli = []
try:
    from NovaAnaliza import analiziraj_pdf
    elektroai_moduli.append("Analiza PDF-a")
except ImportError:
    pass
try:
    from obradi_sve_dokumente import obradi_sve
    elektroai_moduli.append("Batch obrada")
except ImportError:
    pass
try:
    from dijagnostika import pokreni_dijagnostiku
    elektroai_moduli.append("Dijagnostika sistema")
except ImportError:
    pass

# 🧪 Napredne funkcije
napredni_moduli = []
try:
    from treniran_iz_projekata import pokreni_trening
    napredni_moduli.append("Treniraj iz projekata")
except ImportError:
    pass
try:
    from uporedi_projekte import uporedi
    napredni_moduli.append("Uporedi projekte")
except ImportError:
    pass
try:
    from vise_shema_analiza import analiziraj_sheme
    napredni_moduli.append("Analiziraj više šema")
except ImportError:
    pass
try:
    from validacija_signala import validiraj_signale
    napredni_moduli.append("Validiraj signale")
except ImportError:
    pass
try:
    from spoljni_faktori import faktori_okruzenja
    napredni_moduli.append("Spoljni faktori")
except ImportError:
    pass
try:
    from mrezna_dijagnostika import mreza_info
    napredni_moduli.append("Mrežna dijagnostika")
except ImportError:
    pass
try:
    from izvestaj_dijagnostike import generisi_dijagnosticki_izvestaj
    napredni_moduli.append("Izveštaj dijagnostike")
except ImportError:
    pass
try:
    from heatmap_kvarova import prikazi_heatmap
    napredni_moduli.append("Heatmap kvarova")
except ImportError:
    pass
try:
    from graf_dijagnostika import prikazi_dijagnostiku_graf
    napredni_moduli.append("Graf dijagnostike")
except ImportError:
    pass
try:
    from ml_prioritet_klasifikator import klasifikuj_prioritete
    napredni_moduli.append("Prioriteti klasifikator")
except ImportError:
    pass
try:
    from render_shema import prikazi_shemu
    napredni_moduli.append("Render šeme")
except ImportError:
    pass
try:
    from klasifikuj_simbolicne_oznake import prikazi_klasifikaciju
    napredni_moduli.append("Simbolična klasifikacija šeme")
except ImportError:
    pass

# 🛠️ Inicijalizacija
init_db()
init_auth_db()
apply_theme(st.session_state.get("theme_mode", "light"))
render_sidebar_gallery()

# 📋 Sidebar navigacija
dostupne_opcije = [
    "Početna", "Login", "Dashboard", "Izveštaji", "Plugin-i", "Feedback",
    "Vodič", "Video", "Statistika"
]
if elektroai_moduli:
    dostupne_opcije.append("📂 ElektroAI")
if napredni_moduli:
    dostupne_opcije.append("🧪 Napredne funkcije")

menu = st.sidebar.radio("📋 Navigacija", dostupne_opcije)

# 🎯 Osnovne funkcije
if menu == "Početna":
    st.title("⚡ Elektro Analizator & ElektroAI")
    if "user" in st.session_state:
        st.success(f"Prijavljen kao: {st.session_state['user']['username']}")
    else:
        st.warning("🔐 Nisi prijavljen.")

elif menu == "Login":
    st.subheader("🔐 Prijava korisnika")
    username = st.text_input("Korisničko ime")
    password = st.text_input("Lozinka", type="password")
    if st.button("Prijavi se"):
        user = login_user(username, password)
        if user:
            st.session_state["user"] = user
            st.success(f"✅ Dobrodošao, {username}!")
        else:
            st.error("❌ Pogrešno korisničko ime ili lozinka.")

    st.subheader("🆕 Registracija korisnika")
    new_username = st.text_input("Novo korisničko ime", key="reg_user")
    new_password = st.text_input("Nova lozinka", type="password", key="reg_pass")
    if st.button("Registruj se"):
        success = register_user(new_username, new_password)
        if success:
            st.success("✅ Uspešna registracija.")
        else:
            st.error("❌ Korisničko ime već postoji.")

elif menu == "Dashboard":
    if "user" in st.session_state:
        st.subheader("📊 Dashboard komponenti")
        projekti = os.listdir("prethodni_projekti")
        dostupni = [p for p in projekti if os.path.isdir(os.path.join("prethodni_projekti", p))]
        izabrani_projekat = st.selectbox("📁 Izaberi projekat", dostupni)
        if izabrani_projekat:
            pokreni_dashboard(izabrani_projekat)
    else:
        st.warning("🔐 Prijavi se da bi pristupio dashboardu.")

elif menu == "Izveštaji":
    if "user" in st.session_state:
        sample_data = {"broj kvarova": 3, "aktivni senzori": 12}
        generate_report(sample_data)
        schedule_report(60, lambda: generate_report({"status": "OK"}))
    else:
        st.warning("🔐 Prijavi se da bi generisao izveštaj.")

elif menu == "Plugin-i":
    plugins = get_plugins()
    selected = st.selectbox("Izaberi plugin", plugins)
    if st.button("Pokreni plugin"):
        result = run_plugin(selected)
        st.write("📤 Rezultat plugin-a:", result)

elif menu == "Feedback":
    if "user" in st.session_state:
        feedback_form()
    else:
        st.warning("🔐 Prijava neophodna za slanje feedback-a.")

elif menu == "Vodič":
    launch_guide()

elif menu == "Video":
    play_tutorial()

elif menu == "Statistika":
    top = get_top_features()
    st.subheader("📊 Najčešće korišćene funkcije")
    for feature, count in top:
        st.write(f"- **{feature}**: {count} puta")

# 📂 ElektroAI
elif menu == "📂 ElektroAI":
    st.subheader("📁 ElektroAI funkcije")
    if "Analiza PDF-a" in elektroai_moduli:
        st.subheader("Analiza PDF-a")
        pdf_file = st.file_uploader("Otpremi PDF fajl", type=["pdf"])
        if pdf_file:
            rezultati = analiziraj_pdf(pdf_file)
            st.write(rezultati)
    if "Batch obrada" in elektroai_moduli:
        st.subheader("Batch obrada")
        if st.button("Pokreni batch obradu"):
            obradi_sve()
    if "Dijagnostika sistema" in elektroai_moduli:
        st.subheader("Dijagnostika sistema")
        rezultat = pokreni_dijagnostiku()
        st.write(rezultat)

# 🧪 Napredne funkcije
elif menu == "🧪 Napredne funkcije":
    st.subheader("🧠 Eksperimentalni alati i analize")
    if "Treniraj iz projekata" in napredni_moduli:
        if st.button("Treniraj iz projekata"):
            pokreni_trening()
    if "Uporedi projekte" in napredni_moduli:
        if st.button("Uporedi projekte"):
            uporedi()
    if "Analiziraj više šema" in napredni_moduli:
        if st.button("Analiziraj više šema"):
            analiziraj_sheme()
    if "Validiraj signale" in napredni_moduli:
        if st.button("Validiraj signale"):
            validiraj_signale()
    if "Spoljni faktori" in napredni_moduli:
        if st.button("Spoljni faktori"):
            faktori_okruzenja()
    if "Mrežna dijagnostika" in napredni_moduli:
        if st.button("Mrežna dijagnostika"):
            mreza_info()
    if "Izveštaj dijagnostike" in napredni_moduli:
        if st.button("Izveštaj dijagnostike"):
            generisi_dijagnosticki_izvestaj()
    if "Heatmap kvarova" in napredni_moduli:
        if st.button("Heatmap kvarova"):
            prikazi_heatmap()
    if "Graf dijagnostike" in napredni_moduli:
        if st.button("Graf dijagnostike"):
            prikazi_dijagnostiku_graf()
    if "Prioriteti klasifikator" in napredni_moduli:
        if st.button("Prioriteti klasifikator"):
            klasifikuj_prioritete()
    if "Render šeme" in napredni_moduli:
        if st.button("Render šeme"):
            prikazi_shemu()
    if "Simbolična klasifikacija šeme" in napredni_moduli:
        if st.button("Simbolična klasifikacija šeme"):
            prikazi_klasifikaciju()
import streamlit as st

def launch_guide():
    st.title("👋 Dobrodošao u Elektro Analizator")

    st.markdown("""
    Ova aplikacija ti omogućava:
    - 📁 Upravljanje elektro-projektima
    - 🖼️ Vizuelni prikaz šema i kvarova
    - 📡 Live nadzor senzora
    - 📝 Slanje feedback-a i generisanje izveštaja
    """)

    st.info("🔐 Prijavi se da bi pristupio svim funkcijama aplikacije.")

    st.markdown("---")
    st.subheader("🧭 Navigacija")
    st.markdown("""
    - **Početna**: pregled aktivnih projekata  
    - **Galerija**: prikaz šema i preview  
    - **Live Dashboard**: nadzor u realnom vremenu  
    - **Izveštaji**: zakazivanje i pregled izveštaja  
    - **Podešavanja**: tema, jezik, korisnički profil
    """)

    st.success("✅ Spreman si da započneš sa radom!")
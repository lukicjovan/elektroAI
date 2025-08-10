import streamlit as st
import datetime

def generate_report(data=None):
    st.subheader("📄 Generisani izveštaj")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"🕒 Vreme generisanja: {timestamp}")

    if not data:
        st.info("Nema dostupnih podataka za izveštaj.")
        return

    st.write("📊 Sadržaj izveštaja:")
    for key, value in data.items():
        st.write(f"- **{key}**: {value}")

    st.success("✅ Izveštaj uspešno prikazan.")
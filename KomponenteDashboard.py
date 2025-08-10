import streamlit as st
import pandas as pd
import os
import json
import plotly.express as px

def pokreni_dashboard(projekat_ime):
    """
    Prikazuje analizu komponenti za izabrani projekat.
    :param projekat_ime: ime projekta u folderu 'prethodni_projekti'
    """
    folder = os.path.join("prethodni_projekti", projekat_ime)
    json_path = os.path.join(folder, "komponente.json")

    if not os.path.exists(json_path):
        st.warning("⚠️ Nema komponenti za ovaj projekat.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        komponente = json.load(f)

    if not komponente:
        st.info("ℹ️ Komponente nisu definisane.")
        return

    df = pd.DataFrame(komponente)

    st.subheader("📋 Pregled komponenti")
    st.write(df[["oznaka", "tip", "izvor"]].sort_values(by="tip"))

    # === Grupisanje po tipu ===
    st.subheader("📊 Komponente po tipu")
    tipovi = df["tip"].value_counts()
    st.bar_chart(tipovi)

    # === Grupisanje po izvoru ===
    st.subheader("🔎 Izvor informacija")
    izvori = df["izvor"].value_counts()
    fig = px.pie(names=izvori.index, values=izvori.values, title="Distribucija po izvorima")
    st.plotly_chart(fig)

    # === Statistika
    st.markdown("### 🧠 Statistika:")
    st.markdown(f"- **Ukupno komponenti:** `{len(df)}`")
    st.markdown(f"- **Broj različitih tipova:** `{df['tip'].nunique()}`")
    st.markdown(f"- **Izvori:** `{df['izvor'].nunique()}`")

    if st.checkbox("📤 Izvezi CSV"):
        st.download_button(
            label="⬇️ Preuzmi CSV komponenti",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name=f"{projekat_ime}_komponente.csv",
            mime="text/csv"
        )
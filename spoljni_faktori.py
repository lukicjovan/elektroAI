import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

EXTERNAL_CSV = "external_conditions.csv"

def load_external_data():
    """
    Učitaj istorijske podatke o temperaturi, vlažnosti i naponu.
    CSV mora sadržati kolone: timestamp, temperature, humidity, voltage.
    """
    if not os.path.exists(EXTERNAL_CSV):
        st.error(f"⚠️ Ne mogu naći {EXTERNAL_CSV}.")
        return pd.DataFrame()
    df = pd.read_csv(EXTERNAL_CSV, parse_dates=["timestamp"])
    return df

def get_failure_dates(projekat):
    """
    Izvuci datume svih prethodnih kvarova (dijagnoza) iz projekta.
    """
    dates = []
    for d in projekat.get("dijagnoze", []):
        try:
            dates.append(pd.to_datetime(d["datum"]))
        except:
            continue
    return dates

def correlate_with_failures(dates, external):
    """
    Grupisanje po danu i izračun korelacije faktora sa brojem kvarova.
    """
    # priprema DataFrame kvarova
    df_fail = pd.DataFrame({"Date": dates})
    df_fail["Date"] = df_fail["Date"].dt.normalize()
    df_fail = df_fail.groupby("Date").size().reset_index(name="fail_count")

    # priprema eksternih podataka
    df_ext = external.copy()
    df_ext["Date"] = df_ext["timestamp"].dt.normalize()

    # spoj po datumu
    df = pd.merge(df_ext, df_fail, on="Date", how="left").fillna(0)

    # korelacija
    cols = ["temperature", "humidity", "voltage", "fail_count"]
    return df[cols].corr()

def prikazi_spoljne_faktore_i_korelaciju():
    st.subheader("🌍 Korelacija spoljnim faktorima")

    projekat = st.session_state.get("aktivni_projekat")
    if not projekat:
        st.warning("⚠️ Molim prvo izaberi projekat u '📂 Upravljanje projektima'.")
        return

    external = load_external_data()
    if external.empty:
        return

    dates = get_failure_dates(projekat)
    if not dates:
        st.info("ℹ️ Nema zabeleženih kvarova za korelaciju.")
        return

    corr = correlate_with_failures(dates, external)

    st.markdown("### 📈 Korelacijska matrica:")
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.markdown("### 🔎 Korelacija faktora sa brojem kvarova:")
    series = corr["fail_count"].drop("fail_count")
    st.bar_chart(series)

def faktori_okruzenja():
    st.warning("⚠️ Funkcija 'faktori_okruzenja' koristi interaktivni UI prikaz (Streamlit).")

# validacija_signala.py

import streamlit as st
import numpy as np
import pandas as pd

# opcionalno za stvarno očitavanje signala putem VISA/pyvisa
try:
    import pyvisa
except ImportError:
    pyvisa = None

def ucitaj_signal(channel="CH1", num_points=1000, sample_rate=1e3):
    """
    Očitaj signal sa osciloskopa ili simuliraj sinus sa šumom.
    channel: naziv kanala (npr. "CH1")
    num_points: broj uzoraka
    sample_rate: frekvencija uzorkovanja u Hz
    """
    # Ako je pyvisa dostupan, pokušaj stvarno očitavanje
    if pyvisa:
        try:
            rm = pyvisa.ResourceManager()
            inst = rm.open_resource("USB0::0x0699::0x0363::C000000::INSTR")
            inst.write(f":CHANNEL1:DISPLAY ON")
            inst.write(f":ACQUIRE:POINTS {num_points}")
            raw = inst.query_binary_values(":WAV:DATA?", datatype='B', container=np.array)
            t = np.linspace(0, num_points/sample_rate, num_points)
            ymult = float(inst.query(":WAV:YMULT?"))
            v = (raw - 128) * ymult
            return t, v
        except:
            pass

    # Fallback – simulacija osnovnog signala (50 Hz sinus + šum)
    t = np.linspace(0, 1, num_points)
    v = np.sin(2 * np.pi * 50 * t) + 0.05 * np.random.randn(num_points)
    return t, v

def analiza_poređenja(mereno, ocekivano, tolerancija=0.1):
    """
    Uporedi mereni vs. očekivani signal.
    Vraća niz [diferencija, greška_bool] za svaki uzorak.
    """
    if len(ocekivano) != len(mereno):
        # Interpolacija očekivanog signala na dužinu merenog
        ocekivano = np.interp(
            np.linspace(0, 1, len(mereno)),
            np.linspace(0, 1, len(ocekivano)),
            ocekivano
        )
    diff = np.abs(mereno - ocekivano)
    greske = diff > tolerancija
    return np.column_stack([diff, greske])

def prikazi_validaciju_signala(ocekivani_signal=None):
    st.subheader("📡 Real-time validacija toka signala")

    if ocekivani_signal is None:
        st.info("⚠️ Nedefinisan `ocekivani_signal`. Odaberi projekat sa signalnim profilom.")
        return

    kanal   = st.selectbox("Izaberite kanal:", ["CH1", "CH2"])
    num     = st.slider("Broj uzoraka:", min_value=100, max_value=5000, value=1000, step=100)
    rate    = st.number_input("Sample rate (Hz):", value=1000.0)

    if st.button("🔄 Očitaj i validiraj"):
        with st.spinner("⏳ Očitavanje signala..."):
            t, mereno = ucitaj_signal(kanal, num, rate)

        odst = analiza_poređenja(mereno, ocekivani_signal, tolerancija=0.1)

        # Priprema DataFrame za prikaz i graf
        df = pd.DataFrame({
            "Vreme (s)": t,
            "Mereno (V)": mereno,
            "Očekivano (V)": np.interp(
                t,
                np.linspace(0, 1, len(ocekivani_signal)),
                ocekivani_signal
            ),
            "Diferencija": odst[:, 0],
            "Greška?": odst[:, 1]
        })

        st.markdown("### 📈 Graf merenog vs. očekivanog signala")
        st.line_chart(df.set_index("Vreme (s)")[["Mereno (V)", "Očekivano (V)"]])

        st.markdown("### ⚠️ Tačke van tolerancije")
        df_err = df[df["Greška?"]]
        if not df_err.empty:
            st.dataframe(df_err, use_container_width=True)
        else:
            st.success("Sve tačke su unutar tolerancije.")

def validiraj_signale():
    st.warning("⚠️ Funkcija 'validiraj_signale' koristi Streamlit UI i nije direktno pozivna.")

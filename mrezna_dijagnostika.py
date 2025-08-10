# mrezna_dijagnostika.py
import streamlit as st
import pandas as pd

# opcionalni importi za protokole
try:
    from pymodbus.client.sync import ModbusTcpClient
except ImportError:
    ModbusTcpClient = None

try:
    from xknx import XKNX
    from xknx.devices import Light
except ImportError:
    XKNX = None

try:
    from dali.controller.somes import DaliController
except ImportError:
    DaliController = None

# === Skener Modbus uređaja ===
def scan_modbus(komponente):
    rezultati = []
    for comp in komponente:
        cfg = comp.get("config", {})
        if comp.get("protocol") == "modbus" and ModbusTcpClient:
            host = cfg.get("host")
            port = cfg.get("port", 502)
            unit = cfg.get("unit_id", 1)
            reg  = cfg.get("register", 0)
            client = ModbusTcpClient(host, port=port)
            status = None
            if client.connect():
                rr = client.read_coils(reg, 1, unit=unit)
                status = rr.bits[0] if hasattr(rr, "bits") else None
                client.close()
            rezultati.append({
                "Naziv": comp.get("oznaka"),
                "Protokol": "Modbus",
                "Očekivano": cfg.get("expected"),
                "Stvarno": status
            })
    return rezultati

# === Skener DALI uređaja ===
def scan_dali(komponente):
    rezultati = []
    for comp in komponente:
        cfg = comp.get("config", {})
        if comp.get("protocol") == "dali":
            status = None
            if DaliController:
                try:
                    ctrl = DaliController()
                    status = ctrl.get_state(cfg.get("address"))
                except:
                    status = None
            rezultati.append({
                "Naziv": comp.get("oznaka"),
                "Protokol": "DALI",
                "Očekivano": cfg.get("expected"),
                "Stvarno": status
            })
    return rezultati

# === Skener KNX uređaja ===
def scan_knx(komponente):
    rezultati = []
    if not XKNX:
        return rezultati

    xknx = XKNX()
    xknx.start(auto_start=True)
    for comp in komponente:
        cfg = comp.get("config", {})
        if comp.get("protocol") == "knx":
            status = None
            try:
                device = Light(xknx,
                               name=comp.get("oznaka"),
                               group_address=cfg.get("group_address"))
                status = device.state.value
            except:
                status = None
            rezultati.append({
                "Naziv": comp.get("oznaka"),
                "Protokol": "KNX",
                "Očekivano": cfg.get("expected"),
                "Stvarno": status
            })
    xknx.stop()
    return rezultati

# === Streamlit UI funkcija ===
def prikazi_mreznu_dijagnostiku(komponente):
    st.subheader("🌐 Mrežna dijagnostika (Modbus / DALI / KNX)")

    with st.spinner("🔍 Očitavam stanje uređaja..."):
        mb   = scan_modbus(komponente)
        dal  = scan_dali(komponente)
        knx  = scan_knx(komponente)
        svi  = mb + dal + knx

    if not svi:
        st.warning("⚠️ Nije pronađen nijedan mrežni uređaj za skeniranje.")
        return

    df = pd.DataFrame(svi)
    st.markdown("### 🔎 Rezultati očitavanja:")
    st.dataframe(df, use_container_width=True)

    # Automatsko označavanje problema
    df["Problem"] = df.apply(
        lambda r: r["Očekivano"] is not None and r["Stvarno"] != r["Očekivano"],
        axis=1
    )
    st.markdown("### ⚠️ Mismatches (Problem = True):")
    st.dataframe(df[df["Problem"]], use_container_width=True)

def mreza_info():
    st.warning("⚠️ Funkcija 'mreza_info' koristi Streamlit UI i nije direktno pozivna.")

import streamlit as st
from ui_helpers import expander_section
from lang_helper import t
from ml_prioritet_klasifikator import klasifikuj_kvar
from notifikator import notify_kvar
from usage_tracker import track_event

def analiziraj_shemu(shema_id):
    def content():
        st.write(t("analizator_starting"))

        # Simulirani ulazni podaci (placeholder)
        senzori = {
            "napon": 235,
            "temperatura": 68,
            "vlaznost": 58,
        }

        # Poziv modela
        rezultat = klasifikuj_kvar(senzori)
        st.metric(label=t("prioritet_kvara"), value=rezultat["prioritet"])

        if rezultat["prioritet"] == "Visok":
            notify_kvar(shema_id, rezultat["opis"])
            st.error(t("kvar_alert") + ": " + rezultat["opis"])
        else:
            st.success(t("kvar_status_normalan"))

        track_event("analiza_izvrsena", {"shema_id": shema_id, "prioritet": rezultat["prioritet"]})

    expander_section(t("analizator_section"), t("analizator_description"), content)
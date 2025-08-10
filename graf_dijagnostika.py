import streamlit as st
import plotly.graph_objects as go
from lang_helper import t
from ui_helpers import expander_section
from usage_tracker import track_event
from notifikator import notify_threshold_exceeded

def prikazi_dijagnostiku(shema_id):
    def content():
        track_event("dijagnostika_pokrenuta", {"shema_id": shema_id})

        # Simulirani senzorski podaci
        podaci = {
            "temperatura": 74,
            "napon": 236,
            "vlaznost": 61,
        }

        # Prikaz grafika
        fig = go.Figure()
        fig.add_trace(go.Bar(x=list(podaci.keys()), y=list(podaci.values())))
        st.plotly_chart(fig, use_container_width=True)

        # Alarmna provera
        if podaci["temperatura"] > 70:
            notify_threshold_exceeded("temperatura", podaci["temperatura"], 70)
            st.warning(t("sensor_limit_exceeded"))

    expander_section(t("diagnostics_section"), t("diagnostics_description"), content)

def prikazi_dijagnostiku_graf():
    st.warning("⚠️ Funkcija 'prikazi_dijagnostiku_graf' koristi Streamlit UI i nije direktno pozivna.")

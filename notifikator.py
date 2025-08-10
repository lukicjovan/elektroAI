import streamlit as st

def notify_threshold_exceeded(sensor_name, value, limit):
    st.toast(f"⚠️ {sensor_name.capitalize()} ({value}) > limit ({limit})", icon="⚠️")

def notify_kvar(shema_id, opis):
    st.error(f"🚨 Detektovan kvar u šemi {shema_id}: {opis}")
    st.toast("📢 Kvar prijavljen notifikatoru", icon="📣")

def notify_connection_loss(device_id):
    st.warning(f"🔌 Izgubljena veza sa uređajem {device_id}")
    st.toast("⛔ Nema komunikacije", icon="⛔")

def notify_feedback_received():
    st.success("✅ Hvala na povratnoj informaciji!")

def notify_bug_reported():
    st.warning("🐞 Izveštaj o grešci je sačuvan i prosleđen timu.")
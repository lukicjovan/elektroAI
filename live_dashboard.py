import streamlit as st
import random
import time

def render_live_dashboard():
    st.subheader("📡 Live Nadzor Sistema")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Aktivni senzori", random.randint(5, 15))
    with col2:
        st.metric("Upozorenja", random.randint(0, 5))
    with col3:
        st.metric("Kvarovi", random.randint(0, 2))

    st.info("🔄 Podaci se osvežavaju svakih 10 sekundi")

    placeholder = st.empty()
    for _ in range(5):
        with placeholder.container():
            st.write("📈 Simulacija podataka:")
            st.line_chart([random.randint(20, 80) for _ in range(10)])
        time.sleep(10)
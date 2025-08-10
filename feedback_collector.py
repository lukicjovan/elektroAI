import streamlit as st
from database import DB_PATH
import sqlite3

def feedback_form():
    st.subheader("📬 Pošalji povratnu informaciju")

    with st.form("feedback_form"):
        rating = st.slider("Oceni aplikaciju", 1, 5, 3)
        comment = st.text_area("Komentar (opciono)")
        submitted = st.form_submit_button("Pošalji")

        if submitted:
            user_id = st.session_state.get("user", {}).get("username", "anonimni")
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO feedback (user_id, rating, comment)
                VALUES (?, ?, ?)
            """, (user_id, rating, comment))
            conn.commit()
            conn.close()

            st.success("✅ Hvala na povratnoj informaciji!")
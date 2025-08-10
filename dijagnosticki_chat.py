# dijagnosticki_chat.py

import streamlit as st
from datetime import datetime
from dijagnostika_ai import analiziraj_opis_nlp

def prikazi_dijagnosticki_chat(komponente):
    st.subheader("🤖 Interaktivni chat dijagnoza")

    # Inicijalizuj istoriju poruka u sesiji
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Prikaži prethodne poruke
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**Ti:** {msg['text']}")
        else:
            st.markdown(f"**Asistent:** {msg['text']}")

    # Unos nove poruke
    user_input = st.text_input("Unesi pitanje ili opis kvara:", key="chat_input")
    if st.button("▶️ Pošalji"):
        if not user_input.strip():
            st.warning("⚠️ Molim te, unesi tekst pre slanja.")
        else:
            # Dodaj korisničku poruku u istoriju
            st.session_state.chat_history.append({
                "role": "user",
                "text": user_input,
                "time": datetime.now().strftime("%H:%M")
            })

            # Generiši odgovor – koristimo dijagnostika_ai
            diag = analiziraj_opis_nlp(user_input, komponente)
            prioritet = diag.get("prioritet", "nepoznat")
            akcija = diag.get("akcija", "")
            skor = int(diag.get("skor", 0) * 100)

            # Prilagodjeni, prijateljski odgovor
            reply = (
                f"Razumem. Stavio sam to kao prioritet **{prioritet.upper()}** "
                f"(pouzdanost {skor}%).\n\n"
                f"Preporuka: {akcija}"
            )

            # Sačuvaj odgovor u istoriju
            st.session_state.chat_history.append({
                "role": "assistant",
                "text": reply,
                "time": datetime.now().strftime("%H:%M")
            })

            # Očisti unos
            st.session_state.chat_input = ""
            # Rerender poruke
            st.experimental_rerun()
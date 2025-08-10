import streamlit as st
import requests
import json

def ai_ui(aktivni_projekat):
    st.markdown("### 🤖 Postavi pitanje lokalnoj AI")

    dostupni_modeli = ["llama3", "mistral"]
    model = st.selectbox("Model", dostupni_modeli, key="model_izbor")

    temperature = st.slider("Temperature (kreativnost odgovora)", min_value=0.0, max_value=1.0, value=0.4, step=0.1)

    pitanje = st.text_area("Unesi pitanje")

    if st.button("📨 Pošalji pitanje"):
        if not pitanje.strip():
            st.warning("Unesi pitanje.")
            return

        kontekst_shema = aktivni_projekat.get("shema_tekst", "")
        kontekst_dokumentacija = aktivni_projekat.get("dokumentacija_tekst", "")
        kontekst = f"[ŠEMA]\n{kontekst_shema}\n\n[DOKUMENTACIJA]\n{kontekst_dokumentacija}"

        payload = {
            "model": model,
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": "Ti si stručni elektroinženjer koji pomaže u analizi elektroinstalacija."},
                {"role": "user", "content": f"Kontekst:\n{kontekst}"},
                {"role": "user", "content": pitanje}
            ],
            "stream": False
        }

        try:
            response = requests.post("http://localhost:11434/api/chat", data=json.dumps(payload))
            odgovor = response.json().get("message", {}).get("content", "")
            st.success("Odgovor AI:")
            st.write(odgovor)
        except Exception as e:
            st.error(f"Greška pri komunikaciji sa lokalnim modelom: {e}")

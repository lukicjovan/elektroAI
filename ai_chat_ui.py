import streamlit as st
import requests

def ai_chat_ui():
    st.markdown("### 🤖 Postavi pitanje lokalnoj AI")

    # Izbor modela
    model = st.selectbox("🧠 Odaberi model", ["llama3", "mistral"], index=0, key="model_selector")

    # Izbor temperature
    temperature = st.slider("🔥 Kreativnost odgovora (temperature)", 0.0, 1.5, 0.7, step=0.1, key="temp_selector")

    user_question = st.text_area("📝 Unesi pitanje:", key="user_input")

    if st.button("📤 Pošalji pitanje"):
        if not user_question.strip():
            st.warning("Unesi pitanje pre slanja.")
            return

        with st.spinner("AI razmišlja..."):
            response = pozovi_lokalni_model(user_question, model, temperature)
            st.markdown("### 📥 Odgovor:")
            st.info(response)

# --- Pomoćna funkcija za slanje upita lokalnom modelu
def pozovi_lokalni_model(prompt, model="llama3", temperature=0.7):
    try:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "temperature": temperature
        }
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        if response.status_code == 200:
            return response.json().get("response", "Nema odgovora.")
        else:
            return f"Greška: {response.status_code} – {response.text}"
    except Exception as e:
        return f"Greška pri povezivanju: {str(e)}"

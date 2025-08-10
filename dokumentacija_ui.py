import streamlit as st
from upload_zone import render_upload
from storage import save_dokumentacija, get_available_dokumentacija
import os

def dokumentacija_ui(projekat):
    st.subheader("📑 Dokumentacija")

    uploaded_files = render_upload(
        allowed_types=["png", "jpg", "jpeg", "pdf"],
        multiple=True,
        key="dokumentacija_upload"
    )

    if uploaded_files:
        for uploaded_file in uploaded_files:
            name = uploaded_file.name.rsplit(".", 1)[0]
            preview_path = save_dokumentacija(uploaded_file, name, projekat["naziv"])
            st.success(f"Sačuvana dokumentacija: {uploaded_file.name}")
            st.text(f"Preview: {preview_path}")

    # Prikaz dostupne dokumentacije za aktivni projekat
    docs = get_available_dokumentacija(projekat["naziv"])
    if docs:
        st.markdown("#### 📂 Dostupna dokumentacija:")
        for doc in docs:
            st.markdown(f"- `{doc}`")

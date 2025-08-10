import streamlit as st
import os

GALLERY_FOLDER = "gallery"

def render_sidebar_gallery():
    st.sidebar.subheader("🖼️ Galerija šema")

    if not os.path.exists(GALLERY_FOLDER):
        st.sidebar.warning(f"📁 Folder '{GALLERY_FOLDER}' ne postoji.")
        return

    files = [f for f in os.listdir(GALLERY_FOLDER) if f.endswith((".png", ".jpg", ".jpeg"))]
    if not files:
        st.sidebar.info("📂 Nema dostupnih slika u galeriji.")
        return

    selected_file = st.sidebar.selectbox("Izaberi šemu", files)
    image_path = os.path.join(GALLERY_FOLDER, selected_file)
    st.sidebar.image(image_path, caption=selected_file, use_column_width=True)
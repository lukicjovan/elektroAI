import streamlit as st
from upload_zone import render_upload
from storage import save_shema, get_available_sheme
import os

def preview_shema(fajl_path):
    ext = fajl_path.split(".")[-1].lower()
    if ext in ["png", "jpg", "jpeg"]:
        st.image(fajl_path, caption=os.path.basename(fajl_path), use_column_width=True)
    elif ext == "pdf":
        st.markdown(f"📄 PDF fajl: `{os.path.basename(fajl_path)}`")
    else:
        st.warning("Nepodržan format.")

def shema_ui(projekat):
    st.markdown("## 🗂 Elektro šeme")

    uploaded_files = render_upload(allowed_types=["png", "jpg", "jpeg", "pdf"], multiple=True, key="shema_upload")

    if uploaded_files:
        for uploaded_file in uploaded_files:
            name = uploaded_file.name.rsplit(".", 1)[0]
            st.markdown(f"**✅ Učitana šema:** `{uploaded_file.name}`")
            preview_path = save_shema(uploaded_file, name, projekat["naziv"])
            st.markdown("**📎 Pregled:**")
            preview_shema(preview_path)

    st.markdown("### 📂 Sačuvane šeme")
    fajlovi = get_available_sheme(projekat["naziv"])
    if fajlovi:
        for f in fajlovi:
            path = os.path.join("projekti", projekat["naziv"], "sheme", f)
            preview_shema(path)
    else:
        st.info("Nema sačuvanih šema u ovom projektu.")

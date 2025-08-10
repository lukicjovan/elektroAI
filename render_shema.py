import streamlit as st
from PIL import Image
import fitz  # PyMuPDF

@st.cache_data
def preview_shema(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        preview_pdf(uploaded_file)
    else:
        preview_image(uploaded_file)

def preview_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        page = doc.load_page(0)
        pix = page.get_pixmap()
        img_bytes = pix.tobytes("png")
        st.image(img_bytes, caption="PDF Preview")

def preview_image(uploaded_file):
    img = Image.open(uploaded_file)
    st.image(img, caption="Image Preview", use_column_width=True)

def prikazi_shemu():
    st.warning("⚠️ Funkcija 'prikazi_shemu' koristi UI prikaz i nije direktno pozivna.")

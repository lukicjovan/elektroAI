import streamlit as st
from PIL import Image
import fitz  # PyMuPDF
import os

def preview_shema(file):
    if file.type == "application/pdf":
        preview_pdf_all_pages(file)
    elif file.type.startswith("image/"):
        preview_image(file)
    else:
        st.warning("Nije podržan format fajla.")

def preview_pdf_all_pages(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        num_pages = doc.page_count
        st.info(f"PDF sadrži {num_pages} stranica.")

        os.makedirs("preview", exist_ok=True)

        for i in range(num_pages):
            page = doc.load_page(i)
            pix = page.get_pixmap(dpi=150)
            img_path = os.path.join("preview", f"preview_page_{i+1}.png")
            pix.save(img_path)
            st.image(img_path, caption=f"Stranica {i+1}", use_column_width=True)

    except Exception as e:
        st.error(f"Greška prilikom prikaza PDF-a: {e}")

def preview_image(file):
    try:
        image = Image.open(file)
        st.image(image, caption="Pregled slike", use_column_width=True)
    except Exception as e:
        st.error(f"Greška prilikom prikaza slike: {e}")

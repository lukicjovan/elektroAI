import os
import shutil
from PIL import Image
from PyPDF2 import PdfReader
import streamlit as st

# === SHEME ===

@st.cache_data
def save_shema(uploaded_file, name, projekat_naziv):
    sheme_dir = os.path.join("projekti", projekat_naziv, "sheme")
    preview_dir = "preview"
    os.makedirs(sheme_dir, exist_ok=True)
    os.makedirs(preview_dir, exist_ok=True)

    path = os.path.join(sheme_dir, uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    img = Image.open(uploaded_file)
    img.thumbnail((300, 300))
    preview_path = os.path.join(preview_dir, f"{name}_preview.png")
    img.save(preview_path)

    return preview_path

@st.cache_data
def save_shema_from_path(file_path, name, projekat_naziv):
    sheme_dir = os.path.join("projekti", projekat_naziv, "sheme")
    preview_dir = "preview"
    os.makedirs(sheme_dir, exist_ok=True)
    os.makedirs(preview_dir, exist_ok=True)

    shutil.copy(file_path, sheme_dir)

    img = Image.open(file_path)
    img.thumbnail((300, 300))
    preview_path = os.path.join(preview_dir, f"{name}_preview.png")
    img.save(preview_path)

    return preview_path

@st.cache_data
def get_available_sheme(projekat_naziv):
    sheme_dir = os.path.join("projekti", projekat_naziv, "sheme")
    if not os.path.exists(sheme_dir):
        return []
    return [f for f in os.listdir(sheme_dir) if f.endswith(".png") or f.endswith(".pdf")]

# === DOKUMENTACIJA ===

@st.cache_data
def save_dokumentacija(uploaded_file, name, projekat_naziv):
    doc_dir = os.path.join("projekti", projekat_naziv, "dokumentacija")
    preview_dir = "preview"
    os.makedirs(doc_dir, exist_ok=True)
    os.makedirs(preview_dir, exist_ok=True)

    path = os.path.join(doc_dir, uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if uploaded_file.name.lower().endswith(".pdf"):
        try:
            pdf = PdfReader(path)
            page = pdf.pages[0]
            text = page.extract_text()[:300] if page else "Nema teksta"
        except:
            text = "Greška pri učitavanju PDF-a"
    else:
        text = "Preview nije podržan"

    preview_path = os.path.join(preview_dir, f"{name}_preview.txt")
    with open(preview_path, "w", encoding="utf-8") as f:
        f.write(text)

    return preview_path

@st.cache_data
def save_dokumentacija_from_path(file_path, name, projekat_naziv):
    doc_dir = os.path.join("projekti", projekat_naziv, "dokumentacija")
    preview_dir = "preview"
    os.makedirs(doc_dir, exist_ok=True)
    os.makedirs(preview_dir, exist_ok=True)

    shutil.copy(file_path, doc_dir)

    if file_path.lower().endswith(".pdf"):
        try:
            pdf = PdfReader(file_path)
            page = pdf.pages[0]
            text = page.extract_text()[:300] if page else "Nema teksta"
        except:
            text = "Greška pri učitavanju PDF-a"
    else:
        text = "Preview nije podržan"

    preview_path = os.path.join(preview_dir, f"{name}_preview.txt")
    with open(preview_path, "w", encoding="utf-8") as f:
        f.write(text)

    return preview_path

@st.cache_data
def get_available_dokumentacija(projekat_naziv):
    doc_dir = os.path.join("projekti", projekat_naziv, "dokumentacija")
    if not os.path.exists(doc_dir):
        return []
    return [f for f in os.listdir(doc_dir) if f.endswith((".pdf", ".txt", ".png", ".jpg"))]

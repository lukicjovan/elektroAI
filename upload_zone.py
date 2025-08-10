import streamlit as st

def render_upload(allowed_types=None, multiple=False, key=None):
    """
    Komponenta za upload fajlova u Streamlit aplikaciji.

    :param allowed_types: Lista dozvoljenih ekstenzija (npr. ["png", "jpg", "pdf"]).
    :param multiple: Dozvoljava izbor više fajlova ako je True.
    :param key: Jedinstveni ključ za komponentu (neophodno kod višestrukih upotreba).
    :return: Jedan fajl (ako multiple=False) ili lista fajlova (ako multiple=True).
    """
    return st.file_uploader(
        label="📤 Učitaj fajl",
        type=allowed_types,
        accept_multiple_files=multiple,
        key=key
    )

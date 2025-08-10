import importlib
import sys

MODULI = [
    "torch",
    "transformers",
    "PIL",
    "pdf2image",
    "bs4",
    "requests",
    "cv2",
    "streamlit",
    "numpy",
    "json"
]

def proveri_module():
    print("\n🧪 Provera Python biblioteka:\n")
    for modul in MODULI:
        try:
            importlib.import_module(modul)
            print(f"✅ {modul} je instaliran")
        except ImportError:
            print(f"❌ {modul} NIJE instaliran — koristi: pip install {modul}")

if __name__ == "__main__":
    proveri_module()
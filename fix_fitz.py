import subprocess
import sys

def proveri_fitz():
    try:
        import fitz
        print("✅ Modul 'fitz' je uspešno učitan.")
    except ImportError:
        print("❌ Modul 'fitz' nije instaliran. Pokušavam instalaciju...")
        install_fitz()

def install_fitz():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
        print("✅ 'pymupdf' je instaliran. Pokušavam ponovni import...")
        import fitz
        print("🚀 'fitz' radi kako treba!")
    except Exception as e:
        print(f"⚠️ Instalacija nije uspela: {e}")
        print("📘 Pokušaj ručno: pip install pymupdf")

if __name__ == "__main__":
    proveri_fitz()
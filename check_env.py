# check_env.py

import sys
import subprocess
import importlib.util

REQUIRED = [
    "streamlit",
    "pandas",
    "numpy",
    "Pillow",
    "matplotlib",
    "seaborn",
    "transformers",
    "torch",
    "scikit-learn",
    "joblib",
    "pytesseract",
    "pyvisa",
    "pymodbus",
    "xknx"
    # dali-controller izbačeno
]

def pip_install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

def ensure_python_packages():
    for pkg in REQUIRED:
        mod = "PIL" if pkg == "Pillow" else pkg
        if importlib.util.find_spec(mod) is None:
            print(f"Instaliram {pkg}…")
            pip_install(pkg)
        else:
            print(f"✅ {pkg} je već instaliran.")

if __name__ == "__main__":
    print(f"Python interpreter: {sys.executable}\n")
    print("🔍 Provera i instalacija obaveznih Python paketa…")
    ensure_python_packages()
    spec = importlib.util.find_spec("joblib")
    print(f"\njoblib dostupan: {'DA' if spec else 'NE'}")
    print("✔️  Svi paketi su obezbeđeni.")
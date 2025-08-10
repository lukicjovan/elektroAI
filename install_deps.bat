@echo off
echo Instalacija Python paketa (Faze 1–17)...
pip install streamlit pandas numpy pillow matplotlib seaborn transformers torch scikit-learn joblib pytesseract pyvisa pymodbus xknx dali-controller

echo Instalacija Tesseract OCR...
choco install tesseract -y || (
  echo ⚠️ Chocolatey ili Tesseract nisu instalirani – molim te instaliraj ih ručno.
)

pause
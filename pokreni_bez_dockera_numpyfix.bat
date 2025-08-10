@echo off
echo [SETUP] Instaliram bazni paket numpy (binarni)...
cd /d %~dp0
pip install numpy==1.26.4

echo [SETUP] Instaliram ostale Python biblioteke...
pip install -r requirements.txt

echo.
echo [START] Pokrećem elektro-analizator...
streamlit run app.py
pause

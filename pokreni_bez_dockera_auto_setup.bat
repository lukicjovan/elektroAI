@echo off
echo [SETUP] Instalacija Python biblioteka...
cd /d %~dp0
pip install -r requirements.txt

echo.
echo [START] Pokrećem elektro-analizator...
streamlit run app.py
pause

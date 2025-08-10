@echo off
echo [START] Pokretanje elektro-analizatora bez Dockera...
cd /d %~dp0
call streamlit run app.py
pause

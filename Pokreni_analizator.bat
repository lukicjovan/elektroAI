@echo off
title ElektroAI - Automatski setup

:: Pravi virtuelno okruženje ako ne postoji
if not exist .venv (
    echo [SETUP] Prvi put pravim virtualno okruzenje...
    python -m venv .venv
)

:: Aktiviraj venv
call .venv\Scripts\activate

:: Postavi ENV varijable (dodaj ovde po potrebi)
set "OPENAI_API_KEY=sk-OVDE_TVOJ_TOKEN"
set "OLLAMA_HOST=localhost:11434"

:: Provera i instalacija Tesseract OCR
where tesseract >nul 2>nul
if %errorlevel% neq 0 (
    echo [SETUP] Tesseract NIJE pronadjen.
    if exist tesseract-setup.exe (
        echo [SETUP] Pronasao lokalni installer. Instaliram...
        start /wait tesseract-setup.exe /SILENT
    ) else (
        echo [SETUP] Preuzimam Tesseract installer sa interneta...
        powershell -Command "Invoke-WebRequest -Uri https://github.com/UB-Mannheim/tesseract/releases/latest/download/tesseract-ocr-w64-setup-5.3.1.20230401.exe -OutFile tesseract-setup.exe"
        start /wait tesseract-setup.exe /SILENT
    )
    echo [SETUP] Tesseract instalacija zavrsena.
) else (
    echo [SETUP] Tesseract OCR je vec instaliran i u PATH-u.
)

:: Instaliraj/updajtuj pip i sve zavisnosti (u venv!)
python -m pip install --upgrade pip
pip install -r requirements.txt

:: Provera Ollama + LLaMA3 i Mistral modela
where ollama >nul 2>nul
if %errorlevel% neq 0 (
    echo [SETUP] Ollama nije pronadjena! Preuzmi je rucno sa https://ollama.com/download i instaliraj.
    pause
) else (
    echo [SETUP] Ollama je pronadjena.
    ollama list | findstr /i llama3 >nul 2>nul
    if %errorlevel% neq 0 (
        echo [SETUP] LLaMA3 model nije pronadjen, automatski povlacim...
        ollama pull llama3
    ) else (
        echo [SETUP] LLaMA3 model je vec dostupan za Ollama.
    )
    ollama list | findstr /i mistral >nul 2>nul
    if %errorlevel% neq 0 (
        echo [SETUP] Mistral model nije pronadjen, automatski povlacim...
        ollama pull mistral
    ) else (
        echo [SETUP] Mistral model je vec dostupan za Ollama.
    )
)

:: Pokreni aplikaciju (Streamlit u venv)
echo [START] Pokrecem elektro-analizator...
::start "" http://localhost:8501
streamlit run app.py

pause

@echo off
python check_env.py
call elektro_env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
@echo off
IF NOT EXIST elektro_env (
    echo ⚙️ Kreiram virtuelno okruženje...
    python -m venv elektro_env
)

echo 🔌 Aktiviram okruženje...
call elektro_env\Scripts\activate

echo 📦 Instaliram pakete ako treba...
pip install -r requirements.txt

echo 🚀 Pokrećem aplikaciju...
streamlit run app.py
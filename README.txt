ELEKTRO ANALIZATOR — Pametni AI sistem za analizu elektro dokumentacije

─────────────────────────────────────────────
🧠 FUNKCIONALNOST:

- Analiza PDF elektro šema
- Obrada slika elektro ormara
- OCR iz fotografisane dokumentacije (TrOCR model)
- Automatska klasifikacija KNX i DALI komponenti
- Detekcija grupnih adresa, gateway modula, magistrala
- Dijagnostika kvarova na osnovu opisa i baze
- Globalna baza svih komponenti u projektima
- Vizualizacija mreže veza među komponentama
- Dashboard sa statistikama i uvidima

─────────────────────────────────────────────
📁 STRUKTURA PROJEKTA:

- app.py — glavna Streamlit aplikacija
- NovaAnaliza.py — analiza PDF šeme
- analiziraj_dokumentaciju.py — obrada PDF/TXT dokumenta
- analiziraj_sliku_dokumentacije.py — OCR sa fotografija dokumentacije
- klasifikuj_pametne_komponente.py — klasifikacija KNX/DALI komponenti
- dijagnostika.py — AI predlozi za kvar
- graf_veza.py — generisanje mrežnog grafa komponenti
- globalna_baza.py — pregled svih komponenti u projektima
- KomponenteDashboard.py — dashboard prikaz
- pokreni_analizator.bat — pokretanje aplikacije
- requirements.txt — liste biblioteka

─────────────────────────────────────────────
💻 POKRETANJE SISTEMA:

1. Instaliraj Python (preporučeno 3.10+)
2. Klikni dvaput na `pokreni_analizator.bat`
3. Aplikacija se pokreće u browseru
4. Kreiraj novi projekat ili otvori postojeći

─────────────────────────────────────────────
📋 NAPOMENE:

- Za OCR iz fotografija koristi se HuggingFace TrOCR model (`microsoft/trocr-base-handwritten`)
- Potrebno je da slike dokumentacije budu čiste, bez senki, u .jpg/.png formatu
- Sve biblioteke se instaliraju automatski preko `requirements.txt`

─────────────────────────────────────────────
👨‍🔧 AUTOR:
Sistem se proširuje dinamično — dodaj svoj modul, funkcionalnost ili proširi klasifikaciju komponenti.  
Pametne zgrade zaslužuju pametne alate.
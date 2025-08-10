# izvestaj_dijagnostike.py
import streamlit as st
import pandas as pd
from datetime import datetime

def prikazi_izvestaj(projekat, rezultat):
    st.subheader("📄 Izveštaj dijagnostike")

    # Podaci za izveštaj
    naziv = projekat.get("naziv", "Nepoznato")
    sada = datetime.now().strftime("%Y-%m-%d %H:%M")
    opis = rezultat.get("opis", "")
    akcija = rezultat.get("akcija", "")
    prioritet = rezultat.get("prioritet", "nepoznat").upper()
    pouzdanost = round(rezultat.get("skor", 0) * 100, 2)

    # Tabela komponenti
    komponente = projekat.get("komponente", [])
    if komponente:
        df_kom = pd.DataFrame(komponente)
        df_kom_html = df_kom.to_html(index=False)
    else:
        df_kom_html = "<p>– Nema registrovanih komponenti –</p>"

    # Istorija dijagnoza
    hist = projekat.get("dijagnoze", [])
    istorija_html = "<ul>"
    for d in hist:
        d_opis = d.get("opis", "")
        d_prio = d.get("prioritet", "").upper()
        d_datum = d.get("datum", "")
        istorija_html += f"<li>{d_datum} – {d_opis} [{d_prio}]</li>"
    istorija_html += "</ul>"

    # Sastavljanje HTML izveštaja
    html = f"""
    <html>
      <head>
        <meta charset="utf-8"/>
        <title>Izveštaj – {naziv}</title>
        <style>
          body {{ font-family: Arial, sans-serif; margin: 20px; }}
          h1, h2 {{ color: #333; }}
          table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
          th, td {{ border: 1px solid #999; padding: 8px; text-align: left; }}
          th {{ background: #eee; }}
        </style>
      </head>
      <body>
        <h1>Izveštaj dijagnostike: {naziv}</h1>
        <p><strong>Datum:</strong> {sada}</p>

        <h2>Rezime analize</h2>
        <p><strong>Opis simptoma:</strong> {opis}</p>
        <p><strong>Predložena akcija:</strong> {akcija}</p>
        <p><strong>Prioritet:</strong> {prioritet}</p>
        <p><strong>Pouzdanost:</strong> {pouzdanost}%</p>

        <h2>Komponente analizirane</h2>
        {df_kom_html}

        <h2>Istorija svih dijagnoza</h2>
        {istorija_html}
      </body>
    </html>
    """

    # Prikaz preview
    st.markdown(html, unsafe_allow_html=True)

    # Dugme za preuzimanje
    st.download_button(
        label="⬇️ Preuzmi HTML izveštaj",
        data=html,
        file_name=f"izvestaj_{naziv.replace(' ', '_')}.html",
        mime="text/html"
    )

def generisi_dijagnosticki_izvestaj(naziv, tekst):
    st.warning("⚠️ Funkcija 'generisi_dijagnosticki_izvestaj' koristi Streamlit UI i nije direktno pozivna.")

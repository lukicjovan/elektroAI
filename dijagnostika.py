
def pokreni_dijagnostiku(opis_kvara, projekat_ime):
    # Lažna dijagnostika radi testiranja
    if "prekid" in opis_kvara.lower():
        return "Mogući prekid napajanja u jednoj zoni."
    elif "svetlo" in opis_kvara.lower():
        return "Proveriti osvetljenje - možda je izgorela sijalica ili neispravan prekidač."
    else:
        return "Kvar nije moguće pouzdano identifikovati. Preporučena dodatna analiza."

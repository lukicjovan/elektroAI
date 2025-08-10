
import random

def predvidi_prioritet_ml(tekst):
    # Lažna predikcija prioriteta radi testiranja
    return random.choice(["Nizak", "Srednji", "Visok"])

def klasifikuj_prioritete(lista_opisa):
    # Dummy klasifikacija više opisa
    return [predvidi_prioritet_ml(opis) for opis in lista_opisa]

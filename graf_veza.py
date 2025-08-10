import networkx as nx
import matplotlib.pyplot as plt
import json
import os

def kreiraj_graf_komponenti(projekat_ime):
    """
    Generiše mrežni graf među komponentama projekta na osnovu oznaka i tipova.
    :param projekat_ime: ime projekta
    :return: graf objekat
    """
    path = os.path.join("prethodni_projekti", projekat_ime, "komponente.json")
    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        komponente = json.load(f)

    G = nx.Graph()

    # Dodaj čvorove
    for k in komponente:
        oznaka = k.get("oznaka", "???")
        tip = k.get("tip", "nepoznato")
        G.add_node(oznaka, label=tip)

    # Dodaj veze (primer heuristika)
    for k1 in komponente:
        for k2 in komponente:
            if k1 == k2:
                continue
            o1, o2 = k1.get("oznaka", ""), k2.get("oznaka", "")
            t1, t2 = k1.get("tip", ""), k2.get("tip", "")

            # Ako je prekidač i kontaktor ili relej — moguće logička veza
            if t1 in ["prekidač", "taster/prekidač"] and t2 in ["kontaktor", "relej"]:
                G.add_edge(o1, o2)
            # Ako je PLC i aktor — veza
            if "PLC" in t1 and t2 in ["kontaktor", "motor", "frekventni regulator"]:
                G.add_edge(o1, o2)
            # Ako su u istom izvoru (OCR slika), poveži
            if k1.get("izvor") == k2.get("izvor") and o1 != o2:
                G.add_edge(o1, o2)

    return G

def prikazi_graf(G, projekat_ime="GrafVeza"):
    """
    Vizualizuje mrežni graf komponenti.
    :param G: graf objekat
    :param projekat_ime: ime projekta
    """
    if G is None or G.number_of_nodes() == 0:
        print("⚠️ Graf je prazan.")
        return

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    tipovi = nx.get_node_attributes(G, "label")

    boje = {
        "prekidač": "#3498db",
        "kontaktor": "#e67e22",
        "relej": "#9b59b6",
        "svetiljka": "#f1c40f",
        "motor": "#1abc9c",
        "PLC jedinica": "#e74c3c",
        "frekventni regulator": "#2ecc71",
        "naponski priključak": "#7f8c8d"
    }

    node_colors = [boje.get(tipovi[n], "#95a5a6") for n in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color="#bdc3c7", node_size=700, font_size=10)
    plt.title(f"🕸️ Graf veza za projekat: {projekat_ime}")
    plt.tight_layout()
    plt.show()
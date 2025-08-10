import urllib.parse

def generisi_link_za_oznaku(oznaka):
    query = f"{oznaka} electrical component datasheet"
    encoded = urllib.parse.quote_plus(query)
    return f"https://www.bing.com/search?q={encoded}"
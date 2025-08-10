import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def dohvati_info_komponente(oznaka, izvor='duckduckgo'):
    query = f"{oznaka} electrical component datasheet"
    rezultati = []

    try:
        if izvor == 'bing':
            url = f"https://www.bing.com/search?q={quote(query)}"
        elif izvor == 'duckduckgo':
            url = f"https://html.duckduckgo.com/html/?q={quote(query)}"
        else:
            url = f"https://www.google.com/search?q={quote(query)}"

        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if "http" in href and not href.startswith('/'):
                links.append(href)
        links = links[:5]  # uzmi prvih 5

        for link in links:
            try:
                resp = requests.get(link, headers=headers, timeout=8)
                page = BeautifulSoup(resp.text, "html.parser")
                title = page.title.string if page.title else ""
                meta = page.find("meta", attrs={"name": "description"})
                opis = meta['content'] if meta and 'content' in meta.attrs else ""
                if ".pdf" in link:
                    datasheet = link
                else:
                    datasheet = next((a['href'] for a in page.find_all('a', href=True) if a['href'].endswith(".pdf")), "")
                rezultati.append({
                    "oznaka": oznaka,
                    "naziv": title.strip(),
                    "opis": opis.strip(),
                    "datasheet": datasheet
                })
            except:
                continue

        return rezultati[0] if rezultati else {"oznaka": oznaka, "naziv": "", "opis": "", "datasheet": ""}
    except Exception as e:
        print(f"[INFO ERROR] → {e}")
        return {"oznaka": oznaka, "naziv": "", "opis": "", "datasheet": ""}
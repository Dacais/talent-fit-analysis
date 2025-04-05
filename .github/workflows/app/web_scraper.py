import requests
from bs4 import BeautifulSoup

def analyze_web_links(links):
    summaries = []
    for url in links:
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            summaries.append(text[:500])
        except Exception as e:
            summaries.append(str(e))
    return summaries

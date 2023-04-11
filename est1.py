import requests
from bs4 import BeautifulSoup
import pprint


URL = "https://ru.wikipedia.org/wiki/"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    invi = soup.find_all('li', class_='mw-list-item')
    article = []
    for item in invi:
        card = {
            'art': item.find('a')
        }
        article.append(card)
    print(article)


html = get_html(URL)
get_data(html.text)
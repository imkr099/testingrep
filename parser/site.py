import requests
from bs4 import BeautifulSoup


class ParserIntel:
    __URL = "https://enter.kg/processory_bishkek/intel-i3-i5-i7_bishkek"
    __HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36 '
    }

    @classmethod
    def get_html(cls, url=None):
        if url is not None:
            req = requests.get(url=url, headers=cls.__HEADERS)
        else:
            req = requests.get(url=cls.__URL, headers=cls.__HEADERS)
        return req

    @staticmethod
    def __get_data(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='row')
        intel = []
        for item in items:
            card = {
                'title': item.find('div', class_='rows').find('a').string,
                'price': item.find('span', class_='price').string
            }
            intel.append(card)
        return intel


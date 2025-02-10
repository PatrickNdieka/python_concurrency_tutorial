import threading
import requests
import random
import time


from lxml import html


class YahooFinanceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super().__init__(**kwargs)
        self._symbol = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f'{base_url}{self._symbol}'
        self.start()
        
    def run(self):
        time.sleep(20 * random.random())
        r = requests.get(self._url)
        if r.status_code != 200:
            return
        
        page_content = html.fromstring(r.text)
        try:
            str_price = page_content.xpath('//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span')[0].text
            price = float(str_price.strip().replace(',', ''))
        except Exception as e:
            price = 'N/A'
        
        print(price)
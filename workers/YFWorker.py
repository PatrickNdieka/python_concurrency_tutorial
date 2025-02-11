import threading
import requests
import random
import time


from lxml import html


class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super().__init__(**kwargs)
        self._input_queue = input_queue
        self.start()

    def run(self):
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break

            yf_finance_worker = YahooFinancePriceWorker(symbol=val)
            price = yf_finance_worker.get_price()
            print(price)
            time.sleep(random.random())


class YahooFinancePriceWorker():
    def __init__(self, symbol, **kwargs):
        super().__init__(**kwargs)
        self._symbol = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f'{base_url}{self._symbol}'

    def get_price(self):
        r = requests.get(self._url)
        if r.status_code != 200:
            return

        page_content = html.fromstring(r.text)
        try:
            str_price = page_content.xpath(
                '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span')[0].text
            price = float(str_price.strip().replace(',', ''))
        except Exception as e:
            price = 'N/A'

        return price

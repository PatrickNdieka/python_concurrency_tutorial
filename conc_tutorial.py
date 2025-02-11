import time

from multiprocessing import Queue

from workers.WikiWorker import WikiWorker
from workers.YFWorker import YahooFinancePriceScheduler


def main():

    symbol_queue = Queue()

    start_time = time.time()

    wikiworker = WikiWorker()
    yf_price_scheduler_threads = []
    yf_price_workers = 5

    for i in range(yf_price_workers):
        yf_price_scheduler = YahooFinancePriceScheduler(
            input_queue=symbol_queue)
        yf_price_scheduler_threads.append(yf_price_scheduler)

    for symbol in wikiworker.get_sp_500_companies():
        symbol_queue.put(symbol)

    for i in range(len(yf_price_scheduler_threads)):
        symbol_queue.put('DONE')

    for i in range(len(yf_price_scheduler_threads)):
        yf_price_scheduler_threads[i].join()

    print('Extracting time took:', round((time.time()-start_time)), 1)


if __name__ == "__main__":
    main()

import time

from workers.WikiWorker import WikiWorker
from workers.YFWorker import YahooFinanceWorker

# def calculate_sum_squares(n):
#     sum_squares = 0
#     for i in range(n):
#         sum_squares += i**2
#     print(sum_squares)
    
# def sleep_a_little(seconds):
#     time.sleep(seconds)
    

def main():
    start_time = time.time()
    
    wikiworker = WikiWorker()
        
    current_workers = []
    
    for symbol in wikiworker.get_sp_500_companies():
        yf_worker = YahooFinanceWorker(symbol=symbol)
        
        current_workers.append(yf_worker)
    
    for i in range(len(current_workers)):
        current_workers[i].join()
        
        
    print('Extracting time took:', round((time.time()-start_time)), 1)

if __name__ == "__main__":
    main()
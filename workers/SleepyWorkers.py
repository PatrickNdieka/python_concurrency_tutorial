import threading
import time

class SleepyWorker(threading.Thread):
    def __init__(self, seconds, *args, **kwargs):
        self._seconds = seconds
        super().__init__(*args, **kwargs)
        
    def _sleep_a_little(self):
        time.sleep(self._seconds)
        
    def run(self):
        self._sleep_a_little()
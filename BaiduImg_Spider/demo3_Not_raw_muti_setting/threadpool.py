
import threading

from demo3_Not_raw_muti_setting.url_Searcher import Searcher


class Threadpool(threading.Thread):
    def __init__(self, searcher):
        super().__init__()
        self.Threads = []
        self.searcher = searcher
        self.start()
        self.join()

    def run(self):
        Searcher.search_in_baidu(self.searcher)
        self.searcher.driver.quit()


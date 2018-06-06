
import threading

from BaiduImg_Spider.demo1_raw.url_Searcher import Searcher


class Searcher_Threadpool(threading.Thread):
    def __init__(self, seacher):
        super().__init__()
        self.Threads = []
        self.seacher = seacher
        self.start()

    def run(self):
        Searcher.search_in_baidu(self.seacher)


import multiprocessing

from BaiduImg_Spider.demo1_raw.downloader import Downloader


class Downloader_multiprocess_pool(multiprocessing.Process):
    def __init__(self, downloader):
        super().__init__()
        self.downloader = downloader
        self.start()

    def run(self):
        Downloader.download(self.downloader, self.downloader.url_queue)
        print('进程退出')




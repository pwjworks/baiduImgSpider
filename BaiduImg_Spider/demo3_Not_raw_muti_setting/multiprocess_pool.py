import multiprocessing

from demo3_Not_raw_muti_setting.downloader import Downloader


class Mpool(multiprocessing.Process):
    def __init__(self, downloader):
        super().__init__()
        self.downloader = downloader
        self.start()

    def run(self):
        Downloader.download(self.downloader, self.downloader.url_queue)
        print('进程退出')




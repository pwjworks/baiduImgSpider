import multiprocessing

from BaiduImg_Spider.demo2_preview.downloader import Downloader


class downloader_muliprocess_pool(multiprocessing.Process):
    def __init__(self, downloader):
        super().__init__()
        self.downloader = downloader
        self.start()

    def run(self):
        """
        开始下载任务
        :return:
        """
        Downloader.download(self.downloader, self.downloader.url_queue)
        print('进程退出')




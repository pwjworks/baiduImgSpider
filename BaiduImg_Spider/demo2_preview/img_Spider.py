from BaiduImg_Spider.demo2_preview import url_Searcher, downloader, searcher_thread_pool, downloader_multiprocess_pool

__author__ = 'pwjworks'
__github__ = 'https://github.com/pwjworks/baiduImgSpider'


class ImgSpider(object):
    """
    下载百度图片预览图的脚本
    基于urllib,selenium并进行多线程优化
    """

    def __init__(self):
        self.url_searcher_threads = []
        self.seacher = url_Searcher.Searcher()
        self.downloader = downloader.Downloader()
        self.downloader_pool = []

    def create_searcher_threads(self):
        """
        创建图片链接爬取器（url_searcher）的线程，并开始任务
        :return:
        """
        for i in range(2):
            self.url_searcher_threads.append(searcher_thread_pool.Threadpool(self.seacher))

    def wait_all_complete(self):
        """
        等待所有url_searcher线程完成任务
        :return:
        """
        for thread in self.url_searcher_threads:
            thread.join()
        self.seacher.driver.quit()

    def create_multiprocessing_pool(self):
        """
        创建图片下载器（url_searcher）的进程，并开始任务
        :return:
        """
        for i in range(3):
            self.downloader_pool.append(downloader_multiprocess_pool.downloader_muliprocess_pool(self.downloader))

    def fill_index_queue(self):
        """
        把爬取到的url数目放入队列中，方便下载器下载
        :return:
        """
        for i in range(1, self.seacher.num):
            self.downloader.index_queue.put(i)

    def fill_downloader_urlQueue(self):
        """
        把爬取到的url队列放入下载器对象的队列（url_queue）中
        :return:
        """
        while not self.seacher.url_queue.empty():
            self.downloader.url_queue.put(self.seacher.url_queue.get())


if __name__ == '__main__':
    spider = ImgSpider()
    spider.create_searcher_threads()
    # 开始爬取url
    spider.wait_all_complete()
    # 等待爬取url工作结束
    spider.fill_downloader_urlQueue()
    spider.fill_index_queue()
    # 将爬取的url放入下载器队列中等待下载
    spider.create_multiprocessing_pool()
    # 开始下载

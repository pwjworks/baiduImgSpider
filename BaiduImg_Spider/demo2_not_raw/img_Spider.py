from demo2_not_raw import url_Searcher, downloader, threadpool, multiprocess_pool


class ImgSpider(object):
    def __init__(self):
        self.threads = []
        self.seacher = url_Searcher.Searcher()
        self.downloader = downloader.Downloader()
        self.pool = []

    def create_searcher_threads(self):
        for i in range(2):
            self.threads.append(threadpool.Threadpool(self.seacher))

    def wait_all_complete(self):
        for thread in self.threads:
            thread.join()
        self.seacher.driver.quit()

    def create_multiprocessing_pool(self):
        for i in range(3):
            self.pool.append(multiprocess_pool.Mpool(self.downloader))

    def fill_index_queue(self):
        for i in range(1, self.seacher.num):
            self.downloader.index_queue.put(i)

    def fill_downloader_urlQueue(self):
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

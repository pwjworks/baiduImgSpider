from demo3_Not_raw_muti_setting import url_Searcher, downloader, threadpool, multiprocess_pool, searcherSetting


class ImgSpider(object):
    def __init__(self):
        self.setting = searcherSetting.SercherSetting()
        self.threads = []
        self.searcher = None
        self.downloader = downloader.Downloader()
        self.pool = []

    def init_searcher_Data(self):
        self.searcher = url_Searcher.Searcher()
        self.searcher.num = self.setting.num
        self.searcher.keyword = self.setting.keyword.pop()
        return self.searcher

    def add_searcher_thread(self, searcher_inited):
        self.threads.append(threadpool.Threadpool(searcher_inited))

    def create_multiprocessing_pool(self):
        for i in range(3):
            self.pool.append(multiprocess_pool.Mpool(self.downloader))

    def fill_index_queue(self):
        for i in range(1, self.setting.num):
            self.downloader.index_queue.put(i)

    def fill_downloader_urlQueue(self):
        while not self.searcher.url_queue.empty():
            self.downloader.url_queue.put(self.searcher.url_queue.get())


if __name__ == '__main__':
    spider = ImgSpider()
    for i in range(spider.setting.keyword_num):
        searcher_inited = spider.init_searcher_Data()
        spider.add_searcher_thread(searcher_inited)
    # 等待爬取url工作结束
    spider.fill_downloader_urlQueue()
    spider.fill_index_queue()
    # 将爬取的url放入下载器队列中等待下载
    spider.create_multiprocessing_pool()
    # 开始下载

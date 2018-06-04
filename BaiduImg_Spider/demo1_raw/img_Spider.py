
from demo1_raw import url_Searcher, decoder, downloader, threadpool, multiprocess_pool


class ImgSpider(object):
    def __init__(self):
        self.threads = []
        self.seacher = url_Searcher.Searcher()
        self.decoder = decoder.Decoder()
        self.downloader = downloader.Downloader()
        self.pool = []

    def create_threads_pool(self):
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

    def decode_url(self):
        while not self.seacher.url_queue.empty():
            self.downloader.url_queue.put(decoder.Decoder.decode_url(self.decoder, self.seacher.url_queue.get()))


if __name__ == '__main__':
    spider = ImgSpider()
    spider.create_threads_pool()
    spider.wait_all_complete()
    spider.decode_url()
    spider.fill_index_queue()
    spider.create_multiprocessing_pool()

from BaiduImg_Spider.demo_raw import url_Searcher, decoder, downloader


class ImgSpider(object):
    """
    下载百度图片预览图的脚本
    基于urllib,selenium
    """

    def __init__(self):
        self._searcher = url_Searcher.Searcher()
        self._decoder = decoder.Decoder()
        self._downloader = downloader.Downloader()
        self.failure_num = 0
        self.parsed = 0

    def start(self):
        url_list = self._searcher.search_in_baidu()

        for each in url_list:
            pic_url = self._decoder.decode_url(each)
            print(pic_url)
            self.failure_num = self._downloader.download(pic_url)
            self.parsed = self.parsed + 1
        print('已经爬取' + str(self.parsed - self.failure_num) + '张图片,' + str(self.failure_num) + '张图片未下载成功')


if __name__ == '__main__':
    spider = ImgSpider()
    spider.start()

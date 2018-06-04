import re
from time import sleep
from urllib.parse import quote

from bs4 import BeautifulSoup
from selenium import webdriver


class Searcher(object):
    def __init__(self):
        self.pn_num = 60
        self.driver = webdriver.PhantomJS()
        self.keyword = input('请输入关键词：')
        self.num = input('请输入爬取张数(必须是60的倍数)：')
        self.url_list = set()

    def search_in_baidu(self):
        while self.pn_num <= int(self.num):
            self.driver.get(
                'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%BD'
                '%A6%E7%89%8C&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=' + quote(self.keyword) +
                '=&height=&face=&istype=&qc=&nc=&fr=&pn=' + str(self.pn_num) + '&rn=60')
            print(self.driver.page_source)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            print(soup.text)

            pic_url = re.findall('"objURL":"(.*?)"', soup.text, re.S)
            for url in pic_url:
                self.url_list.add(url)
                print(url)
            self.pn_num = self.pn_num + 60
            sleep(3)
        self.driver.close()
        return self.url_list


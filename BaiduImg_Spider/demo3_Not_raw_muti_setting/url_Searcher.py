import re
import threading
from queue import Queue
from time import sleep
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium import webdriver


class Searcher(object):
    def __init__(self):
        self.pn_num = 60
        self.driver = webdriver.PhantomJS()
        self.keyword = ""
        self.num = 0
        self.threadLock = threading.RLock()
        self.url_queue = Queue()

    def search_in_baidu(self):
        try:
            while True:
                self.threadLock.acquire()
                page_num = self.get_pn_num()
                self.driver.get(
                    'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%BD'
                    '%A6%E7%89%8C&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=' + quote(self.keyword) +
                    '=&height=&face=&istype=&qc=&nc=&fr=&pn=' + str(page_num) + '&rn=60')
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                print(soup.text)
                self.threadLock.release()
                if page_num > self.num:
                    break
                pic_url = re.findall('"thumbURL":"(.*?)"', soup.text, re.S)
                for url in pic_url:
                    self.url_queue.put(url)
                    print(url)
                sleep(3)
        except Exception as e:
            print(e)
        return self.url_queue

    def get_pn_num(self):
        try:
            print(str(self.pn_num))
            return self.pn_num
        except Exception as e:
            print('exception occur')
        finally:
            self.pn_num += 60



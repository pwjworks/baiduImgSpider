import json


class SercherSetting(object):
    def __init__(self):
        self.keyword_num = 0
        self.keyword = []
        self.num = 0
        self.loadData()

    def loadData(self):
        f = open("setting.json", encoding='utf-8')
        setting = json.load(f)
        self.keyword = setting["keyword"]
        self.num = setting["num"]
        self.keyword_num = setting["keyword_num"]

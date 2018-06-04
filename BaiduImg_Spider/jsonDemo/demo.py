import json


class Demo(object):
    def loadData(self):
        f = open("Setting.json", encoding='utf-8')
        setting = json.load(f)
        data = setting['data']
        print(data)


if __name__ == '__main__':
    d = Demo()
    d.loadData()

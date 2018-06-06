# baiduImgSpider
基于urllib,selenium并进行多线程优化

用scrapy写过几次爬虫，于是就想尝试不用框架实现。

项目里有四个demo

demo_raw是单线程的爬虫，功能是爬取百度图片原图。

demo1_raw是多线程爬虫，功能是多线程爬取百度图片原图。

demo2_preview是多线程爬虫，功能是多线程爬取百度图片预览图。

demo3_preview是多线程爬虫，在demo2_not_raw的基础上更改的，为了利用配置文件设置，功能是多线程爬取百度图片预览图。

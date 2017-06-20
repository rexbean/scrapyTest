#!/usr/bin/python
# _*_ coding: utf-8 _*_

import scrapy
import sys


class Test(scrapy.Spider):
    name = "test"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://weixin.sogou.com/weixin?type=2&query=大数据"
    ]

    def parse(self, response):
        # open(filename, 'wb').write(response.body)
        # h = HTMLParser.HTMLParser()
        # for sel in response.xpath('//ul/li'):
        table = response.xpath('//ul')
        for n in range(9):
            path = '//*[@id="sogou_vr_11002601_summary_'+str(n)+'"]'
            title = table.xpath(path+'/text()')
            msg = repr([x.encode(sys.stdout.encoding) for x in title]).decode('\
            # string-escape')
            print msg

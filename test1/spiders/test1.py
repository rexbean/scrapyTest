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
            titlePath = '//*[@id="sogou_vr_11002601_title_'+str(n)+'"]'
            title = table.xpath(titlePath + '//text()').extract()
            for t in title:
                print 'title==', t
            contentPath = '//*[@id="sogou_vr_11002601_summary_'+str(n)+'"]'
            content = table.xpath(contentPath + '//text()').extract()
            print 'content=='
            for c in content:
                print c

        # contentList = table.xpath('//*[contains(@class,"txt-box")] \
        # /p//text()').extract()
        # print contentList
        # print len(contentList)
        # for a in contentList:
        #     print a

# msg = repr([x.encode(sys.stdout.encoding) for x in contentList]).decode('\
        # string-escape')
        # print msg

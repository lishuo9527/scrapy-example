# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import CrawlSpider

from jandan_crawler.items import JandanCrawlerItem


class jokeSpider(CrawlSpider):
    name = "joke"
    allowed_domains = ["jandan.net"]
    start_urls = [
        "http://jandan.net/duan/page-1",
    ]

    def parse(self, response):
        for page in range(1, 1300):
            url = "http://jandan.net/duan/page-" + str(page)
            yield Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        item = JandanCrawlerItem()
        contents = response.xpath("//li")
        for content in contents:
            item['content'] = content.xpath("//div[@class='text']/p").extract()
        yield item

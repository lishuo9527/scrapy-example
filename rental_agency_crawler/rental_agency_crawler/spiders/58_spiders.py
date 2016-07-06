import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import  Request
from scrapy.spiders import CrawlSpider
from scrapy.loader import ItemLoader 
from rental_agency_crawler.items import RentalAgencyCrawlerItem

class rentalSpider(CrawlSpider):
    name = "58"
    allowed_domains = ["hz.58.com"]
    start_urls = [
        "http://hz.58.com/chuzu/1/pn1",
    ]
    link_extractor = {
        'page': LinkExtractor(allow = r'http://hz.58.com/zufang/*'),
        'nextpage': LinkExtractor(allow = r'http://hz.58.com/chuzu/1/pn\d+'),
    }

    def parse(self, response):
        for link in self.link_extractor['nextpage'].extract_links(response):
            yield Request(url = link.url, callback=self.parse)

        for link in self.link_extractor['page'].extract_links(response):
            yield Request(url = link.url, callback=self.parse_page)

    def parse_page(self, response):
         item = RentalAgencyCrawlerItem()
         item['mobile'] = response.xpath("//div[@class='fl tel cfff']/span[1]/text()").extract()
         item['name']  = response.xpath("//div[@class='fl tel cfff']/span[2]/text()").extract()
         item['company'] = response.xpath("//span[@class='c70 pr20 rzjjr f14']/text()").extract()
         item['area'] = response.xpath("//div[@class='headerLeft pa']/span[3]/a/text()").extract()
         item['serviceArea'] = response.xpath("//span[@class='cb7']").xpath('string(.)').extract()
         yield item
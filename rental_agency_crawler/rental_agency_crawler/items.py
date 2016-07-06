# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RentalAgencyCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    mobile = scrapy.Field()
    company  = scrapy.Field() 
    area = scrapy.Field()
    serviceArea = scrapy.Field()
    
    last_updated = scrapy.Field(serializer=str)

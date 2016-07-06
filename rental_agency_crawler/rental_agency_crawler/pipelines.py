# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from scrapy import signals
from rental_agency_crawler.items import RentalAgencyCrawlerItem
from scrapy.exceptions import DropItem
import json
import re

class RentalAgencyCrawlerPipeline(object):

	def __init__(self,DB_HOST,DB_USER,DB_PWSSWD,DB_DATABASE):
		self.mobiles_seen = set()
		self.DB_HOST = DB_HOST
		self.DB_USER = DB_USER
		self.DB_PWSSWD = DB_PWSSWD
		self.DB_DATABASE = DB_DATABASE

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			DB_HOST=crawler.settings.get('DB_HOST'),
			DB_USER=crawler.settings.get('DB_USER'),
			DB_PWSSWD=crawler.settings.get('DB_PWSSWD'),
			DB_DATABASE=crawler.settings.get('DB_DATABASE')
		)
		
	
	def open_spider(self, spider):
		self.con = MySQLdb.connect(host=self.DB_HOST,user=self.DB_USER,passwd=self.DB_PWSSWD,db=self.DB_DATABASE,port=3306,charset='utf8')
		self.cursor = self.con.cursor()

	def close_spider(self, spider):
		self.con.commit()
		self.cursor.close()
		self.con.close()

	def process_item(self, item, spider):

		mobile =  item['mobile'][0].replace(' ','')
		name = item['name'][0] 
		company = item['company'][0] if len(item['company'])>0  else ''
		area = item['area'][0] if len(item['area'])>0  else ''
		serviceArea = item['serviceArea'][0].replace('\n\t','|').replace('\n',' ') if len(item['serviceArea'])>0  else ''
		temp = re.compile('\s')
		serviceArea = re.sub(temp,'',serviceArea)


		if mobile not in self.mobiles_seen:
			self.mobiles_seen.add(mobile)
			sql = """ INSERT INTO `58_spider` (mobile,company,name,area,service_area) VALUES ('%s','%s','%s','%s','%s') """ % (mobile,company,name,area,serviceArea)
			self.cursor.execute(sql)
			return item
		else:
			raise DropItem("Duplicate item found: %s" % item)
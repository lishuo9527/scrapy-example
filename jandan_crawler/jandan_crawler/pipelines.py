# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class JandanCrawlerPipeline(object):
    # def process_item(self, item, spider):
    #     contents = item['content']
    #     for content in contents:
    #         print content
    #     return item

    def __init__(self, DB_HOST, DB_USER, DB_PWSSWD, DB_DATABASE):
        self.seen = set()
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
        self.con = MySQLdb.connect(host=self.DB_HOST, user=self.DB_USER, passwd=self.DB_PWSSWD, db=self.DB_DATABASE,
                                   port=3306, charset='utf8')
        self.cursor = self.con.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.con.close()

    def process_item(self, item, spider):
        contents = item['content']
        for content in contents:
            content = content.encode('utf-8').strip()
            print content
            if (content not in self.seen):
                self.seen.add(content)
                sql = """ INSERT INTO `jandan_duan` (duan, status) VALUES ('%s','%d') """ % (
                    content, 0)
                self.cursor.execute(sql)
                self.con.commit()
            else:
                print "sssssssssss"
        return item

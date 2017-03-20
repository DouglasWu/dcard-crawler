# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DcardCrawlerPipeline(object):
    def open_spider(self, spider):
        if spider.target != 'comment':
            self.post_file = open('dcard_posts.json', 'w')
        if spider.target != 'post':
            self.comment_file = open('dcard_comments.json', 'w')

    def process_item(self, item, spider):
        target_type, target = item['type'], item['target']
        line = json.dumps(target, ensure_ascii=False) + '\n'
        if target_type=='post':
            self.post_file.write(line)
        else:
            if len(target)>0:
                self.comment_file.write(line)

    def close_spider(self, spider):
        if spider.target != 'comment':
            self.post_file.close()
        if spider.target != 'post':
            self.comment_file.close()
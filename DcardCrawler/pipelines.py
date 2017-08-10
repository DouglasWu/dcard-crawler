# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

POST_LINES_PATH = 'data/dcard_posts_lines.json'
COMMENT_LINES_PATH = 'data/dcard_comments_lines.json'
POST_PATH = 'data/dcard_posts.json'
COMMENT_PATH = 'data/dcard_comments.json'

# convert the dumped data into a real json file
def jsonfy(in_path, out_path):
    with open(in_path, 'r') as fp:
        outfile = open(out_path, 'w')
        outfile.write('[')
        for i, line in enumerate(fp):
            if i>0:
                outfile.write(',')
            outfile.write(line.strip())
        outfile.write(']')
        outfile.close()

class DcardCrawlerPipeline(object):
    def open_spider(self, spider):
        if spider.target != 'comment':
            self.post_file = codecs.open(POST_LINES_PATH, 'w', encoding='utf-8')
        if spider.target != 'post':
            self.comment_file = codecs.open(COMMENT_LINES_PATH, 'w', encoding='utf-8')

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
            jsonfy(POST_LINES_PATH, POST_PATH)
        if spider.target != 'post':
            self.comment_file.close()
            jsonfy(COMMENT_LINES_PATH, COMMENT_PATH)

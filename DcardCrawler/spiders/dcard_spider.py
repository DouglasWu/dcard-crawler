import scrapy
import json, re
from DcardCrawler.spiders.utils import get_forum_urls, post_url, comment_url

class DcardSpider(scrapy.Spider):
    name = "dcard"
    start_urls = get_forum_urls()

    def __init__(self, target='post', end_id=6000, *args, **kwargs):
        super(DcardSpider, self).__init__(*args, **kwargs)
        if target not in ['post', 'comment', 'both']:
            raise Exception('Incorrect target value: '+target)
        self.target = target       # what data we want to get
        self.end_id = int(end_id)  # the id of the oldest post we want to get

    def parse(self, response):
        posts = json.loads(response.body.decode('utf-8'))
        
        if len(posts)==0:
            return
        
        first_id, last_id = int(posts[0]['id']), int(posts[-1]['id'])

        if first_id < self.end_id:
            return
        
        # if we want to crawl post or both
        if self.target != 'comment':
            for p in posts:
                if p['id'] >= self.end_id:
                    yield scrapy.Request(post_url.format(p['id']), callback=self.parse_post)

        # if we want to crawl comment or both
        if self.target != 'post':
            for p in posts:
                if p['id'] >= self.end_id:
                    yield scrapy.Request(comment_url.format(p['id']), callback=self.parse_comment)

        if last_id > self.end_id:
            base_url = response.url.split('&')[0]
            next_list_url = base_url + '&before=' + str(last_id)
            yield scrapy.Request(next_list_url, callback=self.parse)

    def parse_post(self, response):
        post = json.loads(response.body.decode('utf-8'))
        yield {'type':'post', 'target':post}

    def parse_comment(self, response):
        comment = json.loads(response.body.decode('utf-8'))
        yield {'type':'comment', 'target':comment}

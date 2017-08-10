import json
from six.moves import urllib
from bs4 import BeautifulSoup

forum_url = "https://www.dcard.tw/_api/forums/{}/posts?popular=false"
post_url = "https://www.dcard.tw/_api/posts/{}"
comment_url = "https://www.dcard.tw/_api/posts/{}/comments"

# return all the forum names of dcard
def get_forum_names():
    url = "https://www.dcard.tw/_api/forums"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read().decode('utf-8')
    forums = json.loads(response)
    return [f['alias'] for f in forums]

def get_forum_urls():
    forum_names = get_forum_names()
    forum_urls = []
    for fname in forum_names:
        forum_urls.append(forum_url.format(fname))

    return forum_urls

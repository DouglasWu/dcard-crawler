# dcard-crawler

This crawler is implemented using [Scrapy](https://doc.scrapy.org/en/latest/index.html). It can crawl all the posts and comments on [Dcard](https://www.dcard.tw) and save them to json files.

## Prerequisites
- Python3
- Scrapy
- bs4

## Usage
First, clone this project and go to the directory.
```
$ git clone https://github.com/DouglasWu/dcard-crawler.git
$ cd dcard-crawler/
```
If you want to crawl all the posts at this moment, you can simply run:
```
$ scrapy crawl dcard
```
When running, you can check the dumped data at ```data/dcard_posts_lines.json```. Note that the crawler outputs one json string of a post at a line, so the file **does not** follow json format. When completed, the final result is saved at ```data/dcard_posts.json``` and it follows json format.

## Arguments
When you want to crawl not only the posts but also the comments, or you just want to crawl a part of the data, you can run the command with aruguments:
```
$ scrapy crawl dcard -a target=<target> -a end_id=<end_id>
```
```<target>```: Specify whether you want to get the **post**, the **comment** or **both**. Default is post.

```<end_id>```: The post ID of the oldest post you want to include. Default is 6000(there are no dcard posts whose ID is smaller than 6000).

For example, if you want to get all current comments, you can run:
```
$ scrapy crawl dcard -a target=comment
```

If you want to get all the posts and the comments after post ID 226020410, you can run:
```
$ scrapy crawl dcard -a target=both -a end_id=226020410
```
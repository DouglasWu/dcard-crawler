# dcard-crawler

This crawler is implemented using [Scrapy](https://doc.scrapy.org/en/latest/index.html). It can crawl all the posts and comments on [Dcard](https://www.dcard.tw) and save them to json files.

## Prerequisites
- Python2/Python3
- Scrapy
- bs4

## Usage
First, clone this project and go to the directory.
```
$ git clone https://github.com/DouglasWu/dcard-crawler.git
$ cd dcard-crawler/
```
Next, make a new directory named 'data' for the crawled data.
```
mkdir data
```
If you want to crawl all the posts at this moment, you can simply run:
```
$ scrapy crawl dcard
```
When running, you can check the dumped data at ```data/dcard_posts_.json.lines```. Note that the crawler outputs one json string of a post at a line, so the file **does not** follow json format. When completed, the final result is saved at ```data/dcard_posts_.json``` and it follows json format.

## Arguments
When you want to crawl not only the posts but also the comments, or you just want to crawl a part of the data, you can run the command with aruguments:
```
$ scrapy crawl dcard -a target=<target> -a end_id=<end_id> -a forum=<forum> -a file_name=<file_name>
```
```<target>```: Specify whether you want to get the **post**, the **comment** or **both**. Default is post.

```<end_id>```: The post ID of the oldest post you want to include. Default is 6000(there are no dcard posts whose ID is smaller than 6000).

```<forum>```: The forum alias. For example: funny. Default is all the forums.

```<file_name>```: The suffix you want to add to the file name.

For example, if you want to get all current comments, you can run:
```
$ scrapy crawl dcard -a target=comment
```

If you want to get all the posts and the comments in the 'whysoserious' forum after post ID 226020410, you can run:
```
$ scrapy crawl dcard -a target=both -a end_id=226020410 -a forum=whysoserious
```

## API
If you want to get a glimpse of the api used in this crawler, see [dcard-api-test.ipynb](dcard-api-test.ipynb).

---

# dcard爬蟲

用 [Scrapy](https://doc.scrapy.org/en/latest/index.html)實作的爬蟲程式。 能將 [Dcard](https://www.dcard.tw)上所有的文章和留言爬下來，並存成json檔。

## 你必須要有
- Python2/Python3
- Scrapy
- bs4

## 使用方法
首先，把project clone下來，進入該目錄。
```
$ git clone https://github.com/DouglasWu/dcard-crawler.git
$ cd dcard-crawler/
```
新建一個「data」資料夾，存爬下來的資料。
```
mkdir data
```
如果想要爬取dcard目前所有的文章，執行以下指令：
```
$ scrapy crawl dcard
```
執行時，可以在```data/dcard_posts_lines.json```檢查爬下來的資料。要注意的是，爬蟲程式一次寫入一行json字串，所以該檔案並不符合真正的json格式。當執行結束時，符合json格式的檔案會被存到```data/dcard_posts.json```。

## 參數設定
若要同時爬dcard上的留言，或者只爬取一部份的資料，可以在指令中加入參數：
```
scrapy crawl dcard -a target=<target> -a end_id=<end_id> -a forum=<forum> -a file_name=<file_name>
```
```<target>```: 決定您想要爬的資料是 **post**（文章）、**comment**（留言）或是 **both**（兩者），預設是 post.

```<end_id>```: 您想爬取的最早一篇文章的id。 預設是6000（dcard上沒有文章的id小於6000）。

```<forum>```: 想要爬取的看板英文名稱。例如有趣版：funny。預設是所有看板。

```<file_name>```: 輸出檔案的檔名後綴。

例如，如果想要爬目前所有的留言，可以執行：
```
$ scrapy crawl dcard -a target=comment
```
如果想要爬廢文板中文章 id 在 226020410 之後的所有文章和留言，可以執行：
```
$ scrapy crawl dcard -a target=both -a end_id=226020410 -a forum=whysoserious
```

## API
[dcard-api-test.ipynb](dcard-api-test.ipynb)有列出dcard api的一些測試。

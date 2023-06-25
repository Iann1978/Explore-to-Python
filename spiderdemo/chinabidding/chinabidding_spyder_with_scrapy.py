import scrapy
from bs4 import BeautifulSoup


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://www.chinabidding.cc/search/index.html?keyword=%E6%9C%8D%E8%A3%85&h_lx=0&date=90&search_field=0&vague=0&h_province=0&submit=+",
    ]

    def parse(self, response):
        html = response.body.decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        lis = soup.select('#center_box .lists_center li')
        for li in lis:
            tag = li.select('span')[0].text
            loc = li.select('span')[1].text
            title = li.select('a')[0].text
            print("hehe:", tag, loc, title)
            yield {
                "tag": li.select('span')[0].text,
                "loc": li.select('span')[1].text,
                "title": li.select('a')[0].text,
            }
        # for quote in response.xpath("//div[@id='center_box']//div[@class='lists_center']//li"):
        #     yield {
        #         "tag": quote.xpath("span[1]").get(),
        #         "loc": quote.xpath("span[2]").get(),
        #         "title": quote.xpath("a").get(),
        #     }

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
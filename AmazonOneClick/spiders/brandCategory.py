import scrapy
import AmazonOneClick.selfParser as selfParser


class BrandCategorySpider(scrapy.Spider):
    name = "brandCategory"  # 爬虫名字
    allowed_domains = ["amazon.com"]  # 允许的域名
    start_urls = ["https://amazon.com/funkymonkey"]  # 起始url

    def parse(self, response):  # 解析函数，改方法是默认用来处理解析的方法
        logo = selfParser.logo_parser(response)
        print(logo)

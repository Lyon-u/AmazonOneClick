# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazononeclickItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Page(scrapy.Item):
    page_name = scrapy.Field()
    page_href_url = scrapy.Field()
    is_page_parent = scrapy.Field()
    child_pages = scrapy.Field()

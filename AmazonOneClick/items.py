# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonBrandSite(scrapy.Item):
    brand_info = scrapy.Field()
    pages = scrapy.Field()
    task_id = scrapy.Field()
    status = scrapy.Field()


class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stars = scrapy.Field()
    images = scrapy.Field()
    rating_counts = scrapy.Field()
    feature_bullets = scrapy.Field()
    variant_data = scrapy.Field()

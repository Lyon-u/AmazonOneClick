# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import random
import string


class GenerateID:
    def process_item(self, item, spider):
        task_id = GenerateID.generate_id()
        item['task_id'] = task_id
        return item

    @staticmethod
    def generate_id():
        characters = string.ascii_letters + string.digits  # 包含所有字母和数字的字符串
        task_id = ''.join(random.choices(characters, k=8))  # 随机选择8个字符并拼接成字符串
        return task_id


class AmazonOneclickPipelineA:
    def process_item(self, item, spider):
        print(item)
        return item


class UpdateStatus:
    def process_item(self, item, spider):
        spider_name = spider.name
        if spider_name == 'brandSiteSpider':
            item['status'] = 'PipelineA Done'
        if spider_name == 'pageSpider':
            item['status'] = 'PipelineB Done'
        if spider_name == 'productSpider':
            item['status'] = 'PipelineC Done'
        return item

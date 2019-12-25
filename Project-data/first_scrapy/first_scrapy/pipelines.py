# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstScrapyPipeline(object):
    def process_item(self, item, spider):
        if item['h1_tag']:
            v = item['h1_tag'][0].upper()
            item['h1_tag'] = v
            
        return item
        
# -*- coding: utf-8 -*-
import scrapy
from first_scrapy.items import FirstScrapyItem
from scrapy.loader import ItemLoader

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['https://www.inventateq.com/python-training-course-bangalore.php']
    start_urls = (
        'https://www.inventateq.com/python-training-course-bangalore.php',
    )

    def parse(self, response):
        l = ItemLoader(item=FirstScrapyItem(), response=response)

        h1_tag = response.xpath('.//*[@class="h2"]/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)

        return l.load_item()


        return l.load_item()


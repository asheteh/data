# -*- coding: utf-8 -*-
import scrapy


class AmazSpider(scrapy.Spider):
    name = 'amaz'
    allowed_domains = ['amazon.in']
    start_urls = ['http://amazon.in/']

    def parse(self, response):
        pass

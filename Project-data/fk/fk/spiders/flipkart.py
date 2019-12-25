# -*- coding: utf-8 -*-
import scrapy


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['flipkart.com']
    start_urls = ['https://flipkart.com/']

    def __init__(self,search=None,category=None):
        self.search = search 
        self.category = category

    def parse(self, response):
        if self.search and self.category:
            search_product = '/search?q='+self.search
            print(response.urljoin(search_product))
            print("Hello"+self.category)        
# -*- coding: utf-8 -*-
import scrapy


class ShoesSpider(scrapy.Spider):
    name = 'shoes'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/']
    
    def __init__(self,search=None):
        self.search = search 

    def parse(self, response):
        if self.search:
            search_product = '/s?k='+self.search+'&ref=nb_sb_noss'
            print(response.urljoin(search_product))
        
# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request 
import re

class MobilesSpider(scrapy.Spider):
    name = 'mobiles'
    allowed_domains = ['https://www.flipkart.com/']
    start_urls = ['https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off/realme-3i-diamond-blue-64-gb/p/itmfgybq/']

    def parse(self, response):
        mobiles = response.xpath('//a[@class="_31qSD5"]/@href').extract()
        for book in mobiles:
           
            absolute_url = response.urljoin(book)
            #yield{"Phone Name :":absolute_url}
            yield Request(absolute_url, callback=self.parse_book,dont_filter=True)
        next_url = response.xpath('//nav[@class="_1ypTlJ"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_url)
        yield Request(absolute_next_page_url,dont_filter=True)



    def parse_book(self, response):
       title = response.css('span._35KyD6::text').extract_first()
       price = response.xpath('//div[@class="_1vC4OE _3qQ9m1"]/text()').extract_first()
       # Remove Currency Symbol 
       trim = re.compile(r'[^\d.,]+')
       price = trim.sub('', price)
        
       Off  = response.xpath('//div[@class="VGWI6T _1iCvwn"]/span/text()').extract_first()
       Description = response.xpath('//div[@class="_3la3Fn _1zZOAc"]/text()').extract_first()
       Rating  = response.xpath('//div[@class="_1i0wk8"]/text()').extract_first()
       Rating = Rating+"*"
       Rating_Count = response.xpath('//div[@class="col-12-12"]/span/text()').extract_first()
       yield{
           'Title':title,
           'Price':price,
           'Off':Off,
           'Rating':Rating,
           
       }

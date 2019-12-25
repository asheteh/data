# -*- coding: utf-8 -*-
import scrapy
from first_scrapy.items import FirstScrapyItem
from scrapy.loader import ItemLoader
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = (
        'http://quotes.toscrape.com/',
    )

    def parse(self, response):
		l = ItemLoader(items=FirstScrapyItem(),response=response)
		quotes = response.xpath('//*[@class="quote"]')
		
		'''
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            yield{'Text': text,
                  'Author': author,
                  'Tags': tags}

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)
		'''
		l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)

        return l.load_item()


# -*- coding: utf-8 -*-
import scrapy


class TeriSpider(scrapy.Spider):
    name = 'teri'
    allowed_domains = ['https://www.hemantsharmakaushik.com/2019/04/teri-mitti-kesari-song-harmonium-sargam.html']
    start_urls = ['https://www.hemantsharmakaushik.com/2019/04/teri-mitti-kesari-song-harmonium-sargam.html']

    def parse(self, response):
       notes = response.xpath(u'//div[@class="post-body entry-content"]//div/text()').extract()
       f= open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guru99.txt","a",encoding='utf-8')
       for i in notes:
          f.write(i)
		  
        
       f.close()

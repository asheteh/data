# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
class AlibabaSpider(scrapy.Spider):
    name = 'alibaba'
    script = '''
    function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  treat =  require('treat')
  result={}
  for i = 1,10,1
  do
  assert(splash:runjs('document.querySelector(".ui2-pagination-pages a").click()'))
  result[i] = splash.html()
  end
  return treat.as_array(result)
end
'''
    allowed_domains = ['https://www.alibaba.com/products/shoes.html?IndexArea=product_en&page=1']
    
    #def start_request(self):
    start_urls = ['http://https://www.alibaba.com/products/shoes.html?IndexArea=product_en&page=1/']
   	
   	#yield SplashRequest(url=start_urls[0],callback=self.parse,endpoint = 'render.html',args={'wait':0.5})
    	#yield SplashRequest(url=start_urls,callback=self.parse_other_pages,endpoint ='execute',args={'wait':0.5,'lua_source':self.script},dont_filter=True)

    def parse(self, response):
        l = response.xpath("//h2/a/@href").extract()
        yield l


    def parse_other_pages(self,response):
    	for page in response.data:
    		sel = Selector(text=page)
    		l = sel.xpath("//h2/a/@href").extract()
    		yield {'Links':l}

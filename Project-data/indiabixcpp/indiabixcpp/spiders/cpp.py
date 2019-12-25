# -*- coding: utf-8 -*-
import scrapy
import os
import csv
import glob
from scrapy import Spider
import mysql.connector as mysql
from scrapy.http import Request 
import re

class CppSpider(scrapy.Spider):
    name = 'cpp'
    allowed_domains = ['https://www.indiabix.com/aptitude/questions-and-answers/']
    start_urls = ['https://www.indiabix.com/aptitude/questions-and-answers/']

    def parse(self, response):
        links =  response.xpath("//div[@class='div-topics-index']//a/@href").extract()
        for i in links:
            yield Request("https://www.indiabix.com"+i, callback=self.extract_question,dont_filter=True)
    
   
    
    def extract_question(self,response):

        keys = response.xpath("//td[@class='bix-td-qtxt']//text()").extract()
        opt = response.xpath("//td[@class='bix-td-option']/text()").extract()
        n =0
        d =0
        values = response.xpath("//span[@class='jq-hdnakqb mx-bold']/text()").extract()
        for i in range(0,len(keys)):
            try:
                question = keys[i]
                a = opt[d]
                b = opt[d+1]
                c = opt[d+2]
                d1 = opt[d+3]
                ans = values[n]
                n+=1
                d+=4
                yield{
                    'Question':question,
                    'A':a,
                    'B':b,
                    'C':c,
                    'D':d1,
                    'Answer':ans,
            
                }
            except:
                pass
        next_page =  response.xpath("//p[@class='mx-pager mx-lpad-25']//a/@href").extract()
        next_page = next_page[:-1]
       
        for link in next_page:
             yield Request("https://www.indiabix.com/"+link, callback=self.extract_questions,dont_filter=True)
             
    def extract_questions(self,response):
        d=0   
        keys = response.xpath("//td[@class='bix-td-qtxt']//text()").extract()
        opt = response.xpath("//td[@class='bix-td-option']/text()").extract()
        n =0
        values = response.xpath("//span[@class='jq-hdnakqb mx-bold']/text()").extract()
        f= open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\guru99.txt","a",encoding='utf-8')
        for i in range(0,len(keys)): 
                  
            question = keys[i]
            a = opt[d]
            b = opt[d+1]
            c = opt[d+2]
            d1 = opt[d+3]
            ans = values[n]
            d+=4
            n+=1
            yield{
               
                'Question':question,
                'A':a,
                'B':b,
                'C':c,
                'D':d1,
                'Answer':ans,
             }

            


            
        
        
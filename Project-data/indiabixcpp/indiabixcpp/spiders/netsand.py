# -*- coding: utf-8 -*-
import scrapy
import csv
import glob
from scrapy import Spider
import mysql.connector as mysql
from scrapy.http import Request 
import re

class NetsandSpider(scrapy.Spider):
    name = 'netsand'
    allowed_domains = ['https://www.sanfoundry.com/data-structure-questions-answers-array-array-operations/']
    start_urls = ['https://www.sanfoundry.com/data-structure-questions-answers-array-array-operations/']

    def parse(self, response):
        question = response.xpath("//div[@class='entry-content']//p/text()").extract()
        question =  question[1:-2]
        n=0
        ans = response.xpath("//div[@class='collapseomatic_content ']/text()").extract()
        num=[]
        for i in ans:
            f = re.search(r'Answer',i)
            if f :
                num.append(i)
        z=0
        for i in range(0,len(question),6):
            try:
                q = question[i]
                a = question[i+1]
                b = question[i+2]
                c = question[i+3]
                d = question[i+4]
                s = question[i+5]
                an = num[z]
                z+=1
                yield{
                        'Question':q,
                        'A':a,
                        'B':b,
                        'C':c,
                        'D':d,
                        'Answer':an,
                        'Qtype':"DS"
                    
                
                    }
            except:
                pass
        Next = response.xpath("//div[@class='entry-content']//a[contains(text(),'Next')]/@href").extract_first()
        yield Request(Next,dont_filter=True)

   
           

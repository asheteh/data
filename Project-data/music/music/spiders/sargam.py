# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request 
import re
import os
import csv
import glob
from scrapy import Spider
import mysql.connector as mysql
#Output: []
class SargamSpider(scrapy.Spider):
    cnt=0
    name = 'sargam'
    allowed_domains = ['https://www.hemantsharmakaushik.com/']
    start_urls = ['https://www.hemantsharmakaushik.com/']

    def parse(self, response):
        links =  response.xpath("//*[@id='Label1']/div//a/@href").extract()
        for i in links:
            yield Request(i, callback=self.parse_book,dont_filter=True)

    


    def parse_book(self, response):
        
        song_list = response.xpath(u'//h2[@class="post-title entry-title"]//a/@href').extract()
        
        for link in song_list:
             yield Request(link, callback=self.extract_sargam,dont_filter=True)
             
            
        
    def extract_sargam(self,response):
    
        notes = response.xpath(u'//div[@class="post-body entry-content"]//div/text()').extract()
        f = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\guru99.txt","w",encoding='utf-8')
        for i in notes:
            f.write(i)
        
        f.close()
        name =  response.xpath("//title/text()").extract()[0]
        self.cnt+=1

        self.clean_file(name,self.cnt)

    def clean_file(self,name,id):

        with open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\guru99.txt",'r',encoding='utf-8') as myfile:
            result = '\n\n'.join([line.strip() for line in myfile if line.strip()])
        l = result.split("\n")
        f= open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\sargam.txt","w",encoding='utf-8-sig')
       
        for i in l:
            f.write(i+"\n")
        f.close() 
       
       
        db = mysql.connect(
                host = "localhost",
                user = "root",
                passwd ="abhi.239",
                database = "ccatcracker"
            )
        cursor = db.cursor()
        file = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\sargam.txt", 'r',encoding='utf-8-sig')
        file_content = file.read()
        file.close()
        import csv
       
        
        l = name.partition('|')
        
        n = l[0]+'| Abhijeet'
        with open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guitar\\sargams.csv", 'a+', newline='',encoding='utf-8-sig') as file:
            writer = csv.writer(file)
           
            writer.writerow([n,file_content,'new'])
        '''
        query = "INSERT INTO music_sargams VALUES (id,%s,%s,'new')"
        
        l = name.partition('|')
        
        n = l[0]+'| Abhijeet Shete'
        cursor.execute(query, (n,file_content))
        db.commit()
        db.close()
        print("fdf")
        '''
        
       
		
      
        
    

        
    
    
   
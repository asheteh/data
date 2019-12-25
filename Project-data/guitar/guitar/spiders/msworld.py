# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request 
import mysql.connector as mysql

class MsworldSpider(scrapy.Spider):
    name = 'msworld'
    allowed_domains = ['http://msworldsite.com/hindi-songs-guitar-tabs-lead-best-bollywood/']
    start_urls = ['http://msworldsite.com/hindi-songs-guitar-tabs-lead-best-bollywood/']
    cnt=0
    def parse(self, response):
        links =  response.xpath("//div[@class='entry-content']//a/@href").extract()
        links = links[:-1]
        for i in links:
            yield Request(i, callback=self.parse_book,dont_filter=True)

    


    def parse_book(self, response):
        name = response.xpath('//title//text()').extract_first()
        sargam =  response.xpath("//div[@class='entry-content']//p//text()").extract()
        f = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guitar\\guru.txt","w",encoding='utf-8')
        for i in sargam:
            f.write(i)
            f.write("\n\n")
        f.close()
        self.cnt+=1
       
        name = name.replace("Msworldsite","Abhijeet")
        self.send_data(self.cnt,name)

    
    def send_data(self,id,name): 
            
        db = mysql.connect(
                host = "localhost",
                user = "root",
                passwd ="abhi.239",
                database = "ccatcracker"
            )
        cursor = db.cursor()
        file = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guitar\\guru.txt", 'r',encoding='utf-8-sig')
        file_content = file.read()
        file.close()
        import csv
        with open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guitar\\innovators.csv", 'a+', newline='') as file:
            writer = csv.writer(file)
           
            writer.writerow([name,file_content,"New",'new'])

        '''
        query = "INSERT INTO guitar_chords VALUES (id,%s,%s,%s,%s)"
        cursor.execute(query, (name,file_content,"love","new"))
        db.commit()
        db.close()
       
        '''
       
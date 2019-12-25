# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request 
import mysql.connector as mysql

class EnglishSpider(scrapy.Spider):
    name = 'english'
    allowed_domains = ['https://www.guitarchords247.com/popular-guitar-chord-songs/']
    start_urls = ['https://www.guitarchords247.com/popular-guitar-chord-songs/']
    cnt =650
    def parse(self, response):
        link = response.xpath("//ol//li//a/@href").extract()
        link = link[:20]
        for i in link:
            yield Request(i, callback=self.parse_book,dont_filter=True)

    


    def parse_book(self, response):
        name = response.xpath('//title//text()').extract_first()
        sargam =  response.xpath("//div[@class='pop-chords']//text()").extract()
        f = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guitar\\guru.txt","w",encoding='utf-8')
        for i in sargam:
            f.write(i)
            f.write("\n\n")
        f.close()
        self.cnt+=1
       
        name = name.replace("Guitar Chords 247","Abhijeet")
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
           
            writer.writerow([name,file_content,"Eng",'new'])
        '''
        query = "INSERT INTO guitar_chords VALUES (id,%s,%s,%s,%s)"
        cursor.execute(query, (name,file_content,"English","new"))
        db.commit()
        db.close()
        '''
       
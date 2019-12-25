# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request 
import mysql.connector as mysql
class NotesSpider(scrapy.Spider):
    name = 'notes'
    allowed_domains = ['https://www.notesandsargam.com/hindi-songs/']
    start_urls = ['https://www.notesandsargam.com/hindi-songs/']
    cnt=0
    def parse(self, response):
        links = response.xpath('//div[@class="entry-content clr"]//li//a/@href').extract()

        for i in links:
            yield Request(i, callback=self.parse_book,dont_filter=True)

    


    def parse_book(self, response):
        name = response.xpath('//title//text()').extract_first()
        sargam = response.xpath('//div[@class="entry-content clr"]//p//text()').extract()
        f = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\guru.txt","w",encoding='utf-8')
        for i in sargam:
            f.write(i)
            f.write("\n")
        f.close()
        
        self.cnt+=1

        self.send_data(self.cnt,name)

    
    def send_data(self,id,name): 
            
        db = mysql.connect(
                host = "localhost",
                user = "root",
                passwd ="abhi.239",
                database = "ccatcracker"
            )
        cursor = db.cursor()
        file = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\guru.txt", 'r',encoding='utf-8')
        file_content = file.read()
        file.close()
        import csv
        with open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guitar\\sargams.csv", 'a+', newline='',encoding='utf-8-sig') as file:
            writer = csv.writer(file)
           
            writer.writerow([name,file_content,'new'])
        '''
        query = "INSERT INTO music_sargam VALUES (id,%s,%s)"
        cursor.execute(query, (name,file_content))
        db.commit()
        db.close()
        '''
       

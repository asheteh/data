# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request 
import mysql.connector as mysql
class RewindcapsSpider(scrapy.Spider):
    name = 'rewindcaps'
    allowed_domains = ['https://rewindcaps.com/category/chords/guitar-chords/page/1/']
    start_urls = ['https://rewindcaps.com/category/chords/guitar-chords/page/1/']
    cnt = 1
    cnt1= 715
    def parse(self, response):
        link = response.xpath("//h2[@class='entry-title']/a/@href").extract()
        for i in link:
            yield Request(i, callback=self.extract,dont_filter=True)
        self.cnt+=1
        next_url = "https://rewindcaps.com/category/chords/guitar-chords/page/"+str(self.cnt)
        yield Request(next_url,dont_filter=True)

    def extract(self,response):
        name = response.xpath('//title//text()').extract_first()
        name =  name.replace("Rewindcaps","Abhijeet")
        sargam =  response.xpath("//div[@class='entry-content order-position order-position-3']/p/text()").extract()
        f = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guitar\\guru.txt","w",encoding='utf-8')
     
        for i in sargam:
            f.write(i)
            f.write("\n")    
                
        f.close()
        self.cnt1+=1
        self.send_data(self.cnt1,name)

    
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
        cursor.execute(query, (name,file_content,"New","new"))
        db.commit()
        db.close()
        '''
       

# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request 
import mysql.connector as mysql
class NotationSpider(scrapy.Spider):
    name = 'notation'
    allowed_domains = ['https://www.notationsworld.com/search/label/Hindi%20Songs?&max-results=7']
    start_urls = ['https://www.notationsworld.com/search/label/Hindi%20Songs?&max-results=7']
    cnt=363
    def parse(self, response):
        links = response.xpath("//div[@class='blog-pager']//span//a/@href").extract()
        try:
            next_page = max(links, key=len)
            
            if next_page:
                yield Request("https://www.notationsworld.com/search/label/Hindi%20Songs?&max-results=7", callback=self.parse_book,dont_filter=True)
            yield Request(next_page,dont_filter=True)
        except:
            pass
    def parse_book(self, response):
        links =  response.xpath("//h2[@class='post-title entry-title']//a/@href").extract()
        
        for link in links:
            yield Request(link, callback=self.extract_sargam,dont_filter=True)

    def extract_sargam(self,response):
        
        notes = response.xpath("//b//text()").extract()
        notes = notes[2:]
        notes = notes[:-30]
        name  = response.xpath("//title//text()").extract_first()
        s = name.replace("NotationsWorld.com","")

        s = s.split(" ")
        l = ""

        for i in s:
            if i =="Notes":
                break
            else:
                l+=i+" "
    
        f = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\guru99.txt","w",encoding='utf-8')
        for i in notes:
            if i=="\n     (adsbygoogle = window.adsbygoogle || []).push({});\n":
                pass
            else:
                f.write(i)
                f.write("\n")
        
        f.close()
        self.cnt+=1
        self.clean_file(self.cnt,l)

    def clean_file(self,id,name):

        with open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\guru99.txt",'r',encoding='utf-8') as myfile:
            result = '\n\n'.join([line.strip() for line in myfile if line.strip()])
        l = result.split("\n")
        f= open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\sargam.txt","w",encoding='utf-8')
       
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
        file = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\music\\music\\spiders\\sargam.txt", 'r',encoding='utf-8')
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
        print("fdf")
        '''
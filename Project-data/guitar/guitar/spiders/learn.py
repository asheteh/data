# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request 
import mysql.connector as mysql

class LearnSpider(scrapy.Spider):
    name = 'learn'
    allowed_domains = ['https://learnurguitar.com/category/guitar-chords/bollywood-guitar-chords/page/1/']
    start_urls = ['https://learnurguitar.com/category/guitar-chords/bollywood-guitar-chords/page/1/']
    cnt=1
    cnt1=291
    def parse(self, response):
        urls = [ 'https://learnurguitar.com/dil-diyan-gallan-guitar-chords-strumming-pattern-atif-aslam/',
                'https://learnurguitar.com/aaj-se-teri-guitar-chords-strumming-pattern-padman/',
                'https://learnurguitar.com/hawayein-guitar-chords-strumming-pattern-arijit-singh/',
                'https://learnurguitar.com/sang-hoon-tere-guitar-chords-strumming-pattern-bhuvan-bam/',
                'https://learnurguitar.com/humsafar-guitar-chords-strumming-pattern-badrinath-ki-dulhania/',
                'https://learnurguitar.com/meet-guitar-chords-strumming-pattern-arijit-singh/',
                'https://learnurguitar.com/kho-diya-guitar-chords-strumming-pattern-bhoomi/',
                'https://learnurguitar.com/darkhaast-guitar-chords-strumming-pattern-arijit-singh/',
                'https://learnurguitar.com/pehli-nazar-guitar-chords-strumming-pattern-atif-aslam/',
                'https://learnurguitar.com/be-intehaan-guitar-chords-strumming-pattern-race-2/',
                'https://learnurguitar.com/teri-meri-kahani-guitar-chords-strumming-pattern-bb-ki-vines/',
                'https://learnurguitar.com/jhoom-jhoom-ali-zafar-guitar-chords/',
                'https://learnurguitar.com/phir-kabhi-guitar-chords-strumming-pattern/',
                'https://learnurguitar.com/tum-hi-ho-guitar-chords-strumming-pattern-by-arijit-singh-aashiqui-2/',
                'https://learnurguitar.com/jeena-jeena-by-atif-aslam-guitar-chords/',
                'https://learnurguitar.com/tere-sang-yaara-guitar-chords-strumming-pattern-atif-aslam/',
                'https://learnurguitar.com/zehnaseeb-guitar-chords-strumming-pattern-hasee-toh-phasee/',
                'https://learnurguitar.com/main-hoon-hero-tera-guitar-chords-strumming-pattern-hero/',
                'https://learnurguitar.com/iss-qadar-pyar-hai-guitar-chords-strumming-pattern-bhaag-johnny/',
                'https://learnurguitar.com/soch-na-sake-guitar-chords-strumming-pattern-airlift/',
                'https://learnurguitar.com/tumhe-apna-banane-ka-junoon-guitar-chords-strumming-pattern-hate-story-3/',
                'https://learnurguitar.com/bolna-guitar-chords-strumming-pattern-arijit-singh/',
                'https://learnurguitar.com/main-rahoon-ya-na-rahoon-guitar-chords-emraan-hashmi/',
                'https://learnurguitar.com/zara-si-guitar-chords-strumming-pattern-jannat/',
                'https://learnurguitar.com/dekha-hazaro-dafaa-guitar-chords-strumming-pattern-rustom/',
                'https://learnurguitar.com/chal-chale-apne-ghar-guitar-chords-strumming-pattern-woh-lamhe/',
            ]
        '''
        self.cnt+=1
        urls = response.xpath("//h3[@class='g1-gamma g1-gamma-1st entry-title']/a/@href").extract()
        next_url = "https://learnurguitar.com/category/guitar-chords/bollywood-guitar-chords/page/"+str(self.cnt)
        '''
        for i in urls:
             yield Request(i, callback=self.extract,dont_filter=True)
        #yield Request(next_url,dont_filter=True)
    
    def parse_book(self, response):
        url = response.xpath("//h3[@class='g1-gamma g1-gamma-1st entry-title']/a/@href").extract()
        for i in url:
            yield Request(i,callback=self.extract,dont_filter=True)

    def extract(self,response):
        name = response.xpath('//title//text()').extract_first()
        sargam =  response.xpath("//div[@class='g1-content-narrow g1-typography-xl entry-content']/p/text()").extract()
        f = open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guitar\\guru.txt","w",encoding='utf-8')
        l = ['Easy','Medium','Hard','Yes','No','\n',' – Medium',' – Easy',' – Hard',' – Yes',' – No']
        for i in sargam:
            if i in l:
                pass
            else:
                
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
           
            writer.writerow([name,file_content,"Medium",'new'])
        '''
        query = "INSERT INTO guitar_chords VALUES (id,%s,%s,%s,%s)"
        cursor.execute(query, (name,file_content,"Medium","new"))
        db.commit()
        db.close()
        '''
       

import csv

from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re


writer = csv.writer(open('item.csv', 'w',encoding='utf8'))
writer.writerow(['Name', 'Price', 'Off', 'Rating'])
# this is the exe file for chrome driver 
driver = webdriver.Chrome(r"C:\Users\Abhijit.shete\3D Objects\scrapy\chromedriver_win32\chromedriver")


driver.get('https://www.flipkart.com/search?q=mobiles&page=1')

# declaring normal variable to store data 

start_url ="https://www.flipkart.com/search?q=mobiles&page=1"

   

page_number = 1
while(True):
    #url = url.get_attribute('href')    
    mobile_urls = driver.find_elements_by_class_name('_31qSD5')
   
    #driver.get(url)
   
    mobiles = [url.get_attribute('href') for url in mobile_urls]
   
    for m in mobiles:
        driver.get(m)
        
        sel = Selector(driver.page_source)

        Mobile_Name = sel.xpath('//title/text()').extract_first()
        
        price = sel.xpath('//div[@class="_1vC4OE _3qQ9m1"]/text()').extract_first()
       # Remove Currency Symbol 
        trim = re.compile(r'[^\d.,]+')
        price = trim.sub('', price)
    
        Off  = sel.xpath('//div[@class="VGWI6T _1iCvwn"]/span/text()').extract_first()
        
        Rating  = sel.xpath('//div[@class="_1i0wk8"]/text()').extract_first()



        writer.writerow([
                        Mobile_Name,
                        price,
                        Off,
                        Rating]) 
   
    page_number+=1
    try:

        driver.get(start_url)
        url = driver.find_element_by_link_text(str(page_number))
        u = url.get_attribute('href')
        start_url = u
        driver.get(u)

    except:
        print("No More Pages")
   
       
      
    

driver.quit()


''' 
FLipkart Login 

# send keys used to send form data 


username = driver.find_element_by_xpath('//div[@class="_39M2dM JB4AMj"]//input[@type = "username"]')
username.send_keys('username')

password = driver.find_element_by_xpath('//div[@class="_39M2dM JB4AMj"]//input[@type = "password"]')

password.send_keys('password')

sign_in_button = driver.find_element_by_xpath('//button[@class="_2AkmmA _1LctnI _7UHT_c"]')

sign_in_button.click()

driver.find_element_by_xpath('//*[@type="submit"]')

sign_in_button.click()


'''
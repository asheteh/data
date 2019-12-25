from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\\Users\\Abhijit.shete\\3D Objects\\scrapy\\chromedriver_win32\\chromedriver")
# Create your views here.
def index(request):
    # order by used to show most recent home 1st
    return HttpResponse("Hell")

def search(request):
    if 'city' in request.GET:
        m = request.GET['city']
        driver.get('https://www.google.com')
        sleep(3)
        search_query = driver.find_element_by_name('q')
        search_query.send_keys(m)
        sleep(0.5)
        search_query.send_keys(Keys.RETURN)
        sleep(3)

        linkedin_urls = driver.find_elements_by_tag_name('cite')
        linkedin_urls = [url.text for url in linkedin_urls]
        mobile = []
        for i in linkedin_urls:
            if 'flipkart' in i:
                print("yes")
                mobile.append(i)
    
            if 'amazon' in i:
                print("yes")
                mobile.append(i)
    
      
       
        print(linkedin_urls)
    return HttpResponse("FS")
    
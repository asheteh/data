    import mysql.connector as mysql
    db = mysql.connect(
       
                 host = "localhost",
                    user = "root",
                    passwd ="abhi.239",
                    database = "ccatcracker"
                )
    cursor = db.cursor()
        
        
        
        
        
    import csv
    
        
    import codecs
    with codecs.open('sargam.csv', 'r',encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            row =[row.encode('utf-8').strip() for row in row]
            cursor.execute('INSERT INTO music_sargams(song_names, \
              sargam,url )' \
              'VALUES("%s", "%s", "%s")', 
              row)
        
    db.commit()
    db.close()

import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine

df = pd.read_csv('new.csv','utf-8')
print(df)


  
x=b'\xc4\x8c\xc5\xbd'
y=x.decode('utf-8')
print(y)
  
  
import csv
with open(r"C:\\Users\\Abhijit.shete\\3D Objects\\guitar\\innovators.csv", 'a+', newline='') as file:
    writer = csv.writer(file)
           
    writer.writerow([name,file_content,"Eng",'new']) 
  
  
file = open("new.csv","a",newline='',encoding='utf-8')
    
    
with open('innovators.csv','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
         writer = csv.writer(file)
         name = row[0].replace(u'\xa0', u' ')
         sargam = row[1].replace(u'\xa0', u' ')
         name = name.replace(u'\0x97', u' ')
         sargam = sargam.replace(u'\0x97', u' ')
         name = name.replace(u'\0xa0', u' ')
         sargam = sargam.replace(u'0xa0', u' ')
         name = name.replace(u'0x97', u' ')
         sargam = sargam.replace(u'0x97', u' ')
         
         
         writer.writerow([name,sargam,row[2],row[3]]) 
        
file.close()
    
   
    
import mysql.connector as mysql
db = mysql.connect(
       
                 host = "localhost",
                    user = "root",
                    passwd ="abhi.239",
                    database = "ccatcracker"
                )
cursor = db.cursor()
cursor.execute("SELECT * FROM music_sargams")

myresult = cursor.fetchall()

print("Total number of rows in Laptop is: ", cursor.rowcount)
db.commit()
db.close()




  
file = open("sargam.csv","a",newline='',encoding='utf-8')
writer = csv.writer(file)
for i in myresult:
    name = i[0]
    sargam = i[1]
    url = i[2]
    
    writer.writerow([name,sargam,url]) 
    
file.close()












    
    
  
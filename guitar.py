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
with codecs.open('innovators.csv', 'r', encoding='ANSI'
                ) as f:
    reader = csv.reader(f)
    for row in reader:
        cursor.execute('INSERT INTO guitar_chord(song_names, \
          sargam, status,url )' \
          'VALUES("%s", "%s", "%s","%s")', 
          row)
    
db.commit()
db.close()
       
  
  
  
  
  
  
  
  
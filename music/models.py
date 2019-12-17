from django.db import models



   
    
    

class Sargams(models.Model):
    song_names = models.TextField(blank=True)
    sargam = models.TextField(blank=True)
    url = models.TextField(blank=True)
   
    


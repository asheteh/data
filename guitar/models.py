from django.db import models


class chords(models.Model):
    song_names = models.TextField(blank=True)
    sargam = models.TextField(blank=True)
    status = models.CharField(max_length=110)
    url = models.CharField(max_length=300,default="old")
   


class chord(models.Model):
    song_names = models.TextField(blank=True)
    sargam = models.TextField(blank=True)
    status = models.CharField(max_length=110)
    url = models.CharField(max_length=300,default="old")
   
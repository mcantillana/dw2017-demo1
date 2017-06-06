# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


    
class Category(models.Model):
    name = models.CharField(max_length=144)
    sort_order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=144)
    description = models.TextField()
    anio = models.PositiveIntegerField()
    category = models.ForeignKey(Category)
    sort_order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


# class Album(models.Model):
#     name = models.CharField(max_length=144) 
#     anio = models.PositiveIntegerField()
#     # picture = models.ImageField(upload_to='album/', default='album/no-image.jpg')
#     order = models.IntegerField()
    

# class Song(models.Model):
#     name = models.CharField(max_length=144) 
#     minutes = models.PositiveIntegerField()
#     seconds = models.PositiveIntegerField()
#     # track_number = models.PositiveIntegerField()
#     album = models.ForeignKey(Album)

#     def duration(self):
#         return '%d:%d' % (self.minutes,self.seconds)
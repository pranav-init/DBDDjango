from django.db import models
from django.utils import timezone 

class Nice(models.Model):
    niceTitle   = models.CharField(max_length=120)
    niceContent = models.CharField(max_length=200)
    niceAuthor  = models.CharField(max_length=100)
    niceDate    = models.DateTimeField(default=timezone.now,blank=True)

    def __str__(self):
        return self.niceTitle

class Figure(models.Model):
    figTitle = models.CharField(max_length=10)
    figImage = models.ImageField(upload_to='images/',height_field=None,width_field=None,max_length=None)

    def __str__(self):
        return self.figTitle

class Note(models.Model):
    noteTitle = models.CharField(max_length=100)
    noteContent = models.CharField(max_length=300)


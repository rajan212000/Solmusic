from django.db import models
from Subcategory.models import Subcategory

class Song(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete= models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    song = models.FileField(upload_to = 'song/')
    status = models.CharField(max_length=20, choices=(('Movie', 'Movie'), ('Album', 'Album')))
    format = models.CharField(max_length=20, choices=(('Audio', 'Audio'), ('Video', 'Video')))
    singers = models.CharField(max_length=100)
    musiccompany = models.CharField(max_length=100)
    logo = models.ImageField(upload_to = 'song/')
    def __str__(self):
        return self.title
from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='category/')
    def __str__(self):
        return self.name

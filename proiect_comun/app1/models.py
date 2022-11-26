from django.db import models

# Create your models here.

class Cazare(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    author = models.EmailField(max_length=100,default=None, blank=True, null=True)
    adresa = models.URLField(max_length=100, default=None, blank=True, null=True)
    photos = models.ImageField(null=True, blank=True, upload_to="media/cazare/media")
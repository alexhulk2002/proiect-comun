from django.db import models

# Create your models here.

class Cazare(models.Model):
    title = models.CharField(max_length=100)
    descriere = models.CharField(max_length=100)
    descriere = ' '
    author = models.EmailField(max_length=100)
    author= ' '
    adresa = models.URLField(max_length=100)
    adresa= ' '
    photos = models.ImageField(null=True, blank=True, upload_to="media/")
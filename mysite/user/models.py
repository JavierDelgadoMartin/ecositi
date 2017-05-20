from django.db import models

# Create your models here.

class User (models.Model):
    name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=40)
    email = models.EmailField()
    point = models.IntegerField()
    birth_date = models.DateField()
    photo = models.ImageField()

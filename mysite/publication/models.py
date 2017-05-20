from django.db import models

# Create your models here.

class Publication (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    like = models.IntegerField()
    approved = models.BooleanField()
    dislike = models.IntegerField()
    image = models.ImageField()

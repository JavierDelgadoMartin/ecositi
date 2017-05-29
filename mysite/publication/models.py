from django.db import models
from user.models import Perfil

# Create your models here.

class Publication (models.Model):
    perfil_fk = models.ForeignKey(Perfil, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50)
    description = models.TextField()
    like = models.IntegerField()
    approved = models.BooleanField()
    dislike = models.IntegerField()
    image = models.ImageField()


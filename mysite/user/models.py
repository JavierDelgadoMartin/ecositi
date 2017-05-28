from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, default=None)
    last_name = models.CharField(max_length=30, blank=False, default=None)
    city = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False)
    birth_date = models.DateField()
    point = models.IntegerField()
    photo = models.ImageField(blank=False)


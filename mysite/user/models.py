from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser


# Create your models here.

class User (AbstractBaseUser,PermissionsMixin):
    username = models.Charfield()
    passwd = AbstractUser.password()
    email = models.EmailField()
    point = models.IntegerField()
    birth_date = models.DateField()
    photo = models.ImageField()
    city = models.CharField(max_length=20,default='')
    state = models.CharField(max_length=50,default='')

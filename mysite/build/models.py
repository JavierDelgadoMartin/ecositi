from django.db import models
from user.models import Perfil
from prize.models import Prize

class Build(models.Model):
    perfil_fk = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    prize_fk = models.ForeignKey(Prize,on_delete=models.CASCADE)
    date = models.TimeField(auto_now=True)
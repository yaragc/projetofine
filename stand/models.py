from django.db import models

class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.FloatField()


from django.db import models

class Pessoa(models, Model):
    nome = models.CharField(max_lenght=50)
    idade = models.IntegerField()
    sexo = models.CharField(max_lenght=10)
    telefone = models.CharField(max_lenght=20)
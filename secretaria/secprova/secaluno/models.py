from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveBigIntegerField(null=True)
    cpf = models.CharField(null=True, max_length=11)
    dataNascimento = models.DateField(null=True)


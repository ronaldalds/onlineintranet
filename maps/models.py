from django.contrib.auth.models import User
from django.db import models

from compartilhamento.models import Cabo, Ponto, Rota


# Create your models here.
class Ligacao(models.Model):
    cabo = models.ForeignKey(Cabo, on_delete=models.SET_NULL, null=True)
    rota = models.ForeignKey(
        Rota,
        on_delete=models.CASCADE,
        related_name='rota_ligacao')

    ponto_a = models.ForeignKey(
        Ponto,
        on_delete=models.CASCADE,
        null=True,
        related_name='ponto_a_ligacao')

    ponto_b = models.ForeignKey(
        Ponto,
        on_delete=models.CASCADE,
        null=True,
        related_name='ponto_b_ligacao')

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.ponto_a} <-> {self.ponto_b} <-> Cabo {self.cabo}'


class Trajeto(models.Model):
    nome = models.CharField(max_length=64)
    ligacao = models.ManyToManyField(Ligacao)
    rota = models.ForeignKey(
        Rota,
        on_delete=models.CASCADE,
        related_name='rota_trajeto')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Tipo(models.Model):
    tipo = models.CharField(max_length=64)


class Poste(models.Model):
    REDE_CHOICES = (
        ('BT', 'Baixa'),
        ('BT/IP', 'Baixa/Iluminação'),
        ('MT', 'Média'),
        ('MT/IP', 'Média/Iluminação'),
        ('MT/BT', 'Média/Baixa'),
        ('MT/BT/IP', 'Média/Baixa/Iluminação')
    )

    proprietario = models.CharField(max_length=64)
    descricao = models.TextField()
    altura = models.CharField(max_length=64)
    tracao = models.IntegerField()
    rede = models.CharField(
        max_length=8, choices=REDE_CHOICES, blank=False, null=False)
    casa = models.IntegerField()
    comercio = models.IntegerField()
    predio = models.IntegerField()
    equipamento = models.CharField(max_length=256)
    codigo_csi = models.CharField(max_length=64)
    ocupacao = models.CharField(max_length=64)
    imagem = models.ImageField(upload_to='uploads/poste/%Y/%m/%d')
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    aprovacao_data = models.DateTimeField()
    aprovacao = models.BooleanField(default=False)
    protocolo_aprovacao = models.CharField(max_length=64)
    latitude = models.FloatField()
    longitude = models.FloatField()
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)

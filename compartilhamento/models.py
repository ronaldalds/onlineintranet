from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=64)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)


class Tipo(models.Model):
    nome = models.CharField(max_length=64)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome


class Rede(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.CharField(max_length=64)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)


class Cidade(models.Model):
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=2)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)


class Aprovacao(models.Model):
    protocolo = models.CharField(max_length=64)
    data = models.DateTimeField()
    n_poste = models.IntegerField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)


class Equipamento(models.Model):
    nome = models.CharField(max_length=64)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)


class Cabo(models.Model):
    nome = models.CharField(max_length=64)
    cabo = models.CharField(max_length=64)
    n_fibra = models.IntegerField()
    as_fibra = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)


class Poste(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    altura = models.IntegerField()
    tracao = models.IntegerField()
    casa = models.IntegerField()
    comercio = models.IntegerField()
    predio = models.IntegerField()
    codigo_csi = models.CharField(max_length=64)
    cabo = models.ManyToManyField(Cabo)
    ocupacao = models.ManyToManyField(Empresa)
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(upload_to='uploads/poste/%Y/%m/%d')
    aprovacao = models.ForeignKey(
        Aprovacao, on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
    rede = models.ForeignKey(Rede, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

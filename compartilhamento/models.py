from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=64)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True,)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome


class Rede(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome


class Aprovacao(models.Model):
    protocolo = models.CharField(max_length=64)
    data = models.DateTimeField()
    n_poste = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.protocolo


class Equipamento(models.Model):
    nome = models.CharField(max_length=64)
    # incluir coluna com obejto do equipamento serializado: dist
    datasheet = models.JSONField()
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome


class Cabo(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.TextField(blank=True)
    n_fibra = models.IntegerField()
    as_fibra = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome


class Imagem(models.Model):
    origem = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=128)
    descricao = models.TextField()
    file = models.ImageField(upload_to='uploads/poste/%Y/%m/%d')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.titulo} - {self.origem}'


class Ponto(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=128, blank=True, null=True)
    descricao = models.TextField(blank=True)
    altura = models.IntegerField(blank=True, null=True)
    tracao = models.IntegerField(blank=True, null=True)
    casa = models.IntegerField(blank=True, null=True)
    comercio = models.IntegerField(blank=True, null=True)
    predio = models.IntegerField(blank=True, null=True)
    codigo_csi = models.CharField(max_length=64, blank=True)
    cabo = models.ManyToManyField(Cabo, blank=True)
    ocupacao = models.ManyToManyField(Empresa, blank=True)
    equipamento = models.ManyToManyField(Equipamento, blank=True)
    imagem = models.ManyToManyField(Imagem, blank=True)
    aprovacao = models.ForeignKey(
        Aprovacao, on_delete=models.SET_NULL, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=2)
    endereco = models.CharField(max_length=64, blank=True)
    rede = models.ForeignKey(
        Rede, on_delete=models.SET_NULL, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        if self.nome:
            return self.nome
        return f'{self.id}'


class Ligacao(models.Model):
    cabo = models.ForeignKey(Cabo, on_delete=models.SET_NULL, null=True)
    ponto_a = models.ForeignKey(
        Ponto, on_delete=models.PROTECT, null=True, related_name='ponto_a_ligacao')
    ponto_b = models.ForeignKey(
        Ponto, on_delete=models.PROTECT, null=True, related_name='ponto_b_ligacao')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.ponto_a} <-> {self.ponto_b} <-> Cabo {self.cabo}'


class Trajeto(models.Model):
    nome = models.CharField(max_length=64)
    ligacao = models.ManyToManyField(Ligacao)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome

from django.urls import path

from . import views

# app_name = 'compartilhamento'

urlpatterns = [
    path('uteis/', views.compartilhamento,
         name='projeto-rede-compartilhamento'),
    path('descricao/', views.descricao, name='descricao-form'),
    path('mapa/', views.maps, name='projeto-rede-mapa'),
    path('manutencao/', views.manutencao, name='manutencao'),
]

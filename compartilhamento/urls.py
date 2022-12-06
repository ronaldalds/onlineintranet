from django.urls import path

from . import views

urlpatterns = [
    path('', views.compartilhamento, name='projeto-rede-compartilhamento'),
    path('descricao/', views.descricao, name='descricao-form'),
    path('mapa/', views.mapa, name='projeto-rede-mapa'),
]

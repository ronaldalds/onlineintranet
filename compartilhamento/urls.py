from django.urls import path

from . import views

urlpatterns = [
    path('', views.compartilhamento, name='projeto-rede-compartilhamento'),
]

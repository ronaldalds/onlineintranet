from django.urls import path

from . import views

urlpatterns = [
    path('', views.informacoes, name='projeto-rede-informacoes'),
]

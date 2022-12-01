from django.urls import path

from . import views

urlpatterns = [
    path('', views.projeto_rede, name='projeto-rede'),

]

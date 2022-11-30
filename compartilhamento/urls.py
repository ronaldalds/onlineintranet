from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('conversor/', views.conversor, name='conversor-coordenadas'),
]

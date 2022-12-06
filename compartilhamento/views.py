import folium
from django.shortcuts import render

# Create your views here.


def compartilhamento(request):
    return render(request, 'projeto-rede-compartilhamento.html')


def descricao(request):
    cont = {
        'name': '9/300 C12 B2 P3*2'
    }
    return render(request, template_name='descricao-form.html', context=cont)


def mapa(request):
    center_lng = -5.176168
    center_lat = -40.680138
    map = folium.Map(
        location=[center_lat, center_lng],
        zoom_start=8,
    )
    map.save()

    return render(request, 'map.html')

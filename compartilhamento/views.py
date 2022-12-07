import os

import folium
from django.conf import settings
from django.shortcuts import render
from folium import plugins

from . import models

# Create your views here.


def compartilhamento(request):
    return render(request, 'projeto-rede-compartilhamento.html')


def descricao(request):
    cont = {
        'name': '9/300 C12 B2 P3*2'
    }
    return render(request, template_name='descricao-form.html', context=cont)


def mapa(request):
    queryPolyline = models.Trajeto.objects.all()
    queryPop = models.Ponto.objects.filter(nome__icontains="POP")
    queryPosteEnel = models.Ponto.objects.filter(tipo__nome__icontains="POSTE")

    print(queryPosteEnel)
    base = (-4.193510, -40.476361)
    m = folium.Map(
        width='100%', height='100%',
        location=base,
        zoom_start=18,
    )
    for i in queryPop:
        folium.Marker(
            (i.latitude, i.longitude),
            popup=i.descricao,
            tooltip=i.nome,
            icon=folium.Icon(color="red", icon="home", prefix='fa'),

        ).add_to(m)
    for i in queryPosteEnel:
        folium.Marker(
            (i.latitude, i.longitude),
            popup=i.descricao,
            tooltip=i.nome,
            icon=plugins.BeautifyIcon(
                icon_shape='rectangle-dot',
                border_width=5,
            ),

        ).add_to(m)
    for i in queryPolyline:
        for t in i.ligacao.all():
            folium.PolyLine(
                ((t.ponto_a.latitude, t.ponto_a.longitude),
                 (t.ponto_b.latitude, t.ponto_b.longitude)),
                popup=i.nome,
                tooltip=i.nome,
                color="cyan",
                weight=6,
            ).add_to(m)

    # map.add_child(folium.LatLngPopup())
    # plugins.Draw(export=True,
    #              filename='my_data.geojson',
    #              position='topleft',
    #              draw_options={'polyline': {'allowIntersection': True}},
    #              edit_options={'poly': {'allowIntersection': True}}
    #              ).add_to(m)
    # plugins.LocateControl().add_to(m)
    m.save(os.path.join(
        settings.TEMPLATES[0]['DIRS'][0], 'partials/map.html'))

    return render(request, 'projeto-rede-mapa.html')

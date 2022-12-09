
import os

import folium
from django.conf import settings
from django.shortcuts import render
from folium.plugins import BeautifyIcon, Draw, MiniMap

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
    queryPop = models.Ponto.objects.filter(tipo__nome__icontains="POP")
    queryPosteEnel = models.Ponto.objects.filter(
        tipo__nome__icontains="POSTE ENEL")
    base = (-5.176168, -40.680138)
    pontos = folium.FeatureGroup('Pontos',)
    linhas = folium.FeatureGroup('Linhas',)
    # metro = folium.FeatureGroup('Metro')
    # poste = folium.FeatureGroup('Poste')
    # bkb = folium.FeatureGroup('BkB')
    # bkh = folium.FeatureGroup('BkH')
    # varjota = folium.FeatureGroup('Varjota')

    m = folium.Map(
        width='100%', height='100%',
        location=base,
        zoom_start=18,
        tiles=None,
    )

    folium.raster_layers.TileLayer(
        tiles='http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='google',
        name='Google Satélite',
        max_zoom=20,
        subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
        overlay=False,
        control=True,
    ).add_to(m)

    folium.raster_layers.TileLayer(
        tiles='http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr='google',
        name='Google Maps',
        max_zoom=20,
        subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
        overlay=False,
        control=True,
    ).add_to(m)

    for i in queryPop:
        folium.Marker(
            (i.latitude, i.longitude),
            popup=i.descricao,
            tooltip=i.nome,
            icon=folium.Icon(color="red", icon="home", prefix='fa'),

        ).add_to(pontos)

    for i in queryPosteEnel:
        folium.Marker(
            (i.latitude, i.longitude),
            popup=i.descricao,
            tooltip=i.nome,
            icon=BeautifyIcon(
                icon_shape='rectangle-dot',
                border_width=5,
            ),

        ).add_to(pontos)
    cabos = []
    for i in queryPolyline:
        for t in i.ligacao.all():
            cabos.append([
                (t.ponto_a.latitude, t.ponto_a.longitude),
                (t.ponto_b.latitude, t.ponto_b.longitude)
            ])

    folium.PolyLine(
        cabos,
        popup=folium.Html('<a href="#">asdf</a>'),
        tooltip=i.nome,
        color="cyan",
        weight=6,
        dash_array='5,15',
    ).add_to(linhas)
    pontos.add_to(m)
    linhas.add_to(m)
    Draw(
        export=True
    ).add_to(m)
    MiniMap(position='bottomleft').add_to(m)
    folium.LayerControl().add_to(m)
    m.save(os.path.join(
        settings.TEMPLATES[0]['DIRS'][0], 'partials/map.html'))

    return render(request, 'projeto-rede-mapa.html')

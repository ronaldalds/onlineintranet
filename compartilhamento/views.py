
import os
import xml.etree.ElementTree as ET

import folium
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from folium.plugins import BeautifyIcon, Draw, HeatMap, MiniMap

from .models import Tipo
from .utils import LayerFactory


# Create your views here.
def compartilhamento(request):
    return render(request, 'projeto-rede-compartilhamento.html')


def manutencao(request):
    return render(request, 'partials/manutencao.html')


def descricao(request):
    cont = {
        'name': '9/300 C12 B2 P3*2'
    }
    return render(request, template_name='descricao-form.html', context=cont)


def maps(request):

    # file = 'static/poste.kml'
    # site = '{http://www.opengis.net/kml/2.2}'
    # doc = ET.parse(file)
    # root = doc.getroot()
    # pop = Tipo.objects.get(id=1)
    # ponto = Tipo.objects.get(id=2)

    # for i in root.iter(f'{site}Placemark'):
    #     for t in i.iter(f'{site}Point'):
    #         coord = t.findtext(f'{site}coordinates').split(',')
    #         tipo = ponto
    #         user = request.user
    #         poste = Ponto()
    #         poste.usuario = user
    #         poste.tipo = tipo
    #         poste.latitude = float(coord[1])
    #         poste.longitude = float(coord[0])
    #         poste.save()
    # queryPolyline = Trajeto.objects.all()

    # queryPop = Ponto.objects.filter(tipo__nome__icontains="POP")
    # queryPosteEnel = Ponto.objects.filter(tipo__nome__icontains="POSTE ENEL")
    # queryPosteEnel = ponto.tipo_ponto.all()

    base = (-5.176168, -40.680138)
    pop = folium.FeatureGroup('PoP',)
    bkb = folium.FeatureGroup('BkB',)

    m = folium.Map(
        width='100%', height='100%',
        location=base,
        zoom_start=10,
        tiles=None,
    )
    db = pd.read_csv("static/manutencao.csv")
    coordenadas = []

    for lat, lng in zip(db.Latitude.values, db.Longitude.values):
        coordenadas.append([lat, lng])

    file = 'static/Estacoes.kml'
    site = '{http://www.opengis.net/kml/2.2}'
    doc = ET.parse(file)
    root = doc.getroot()
    for i in root.iter(f'{site}Placemark'):
        nomePop = i.findtext(f'{site}name')
        for t in i.iter(f'{site}Point'):
            coord = t.findtext(f'{site}coordinates').split(',')
            folium.Marker(
                (float(coord[1]), float(coord[0])),
                popup=nomePop,
                tooltip=nomePop,
                icon=folium.Icon(color="red", icon="home", prefix='fa'),

            ).add_to(pop)

    file = 'static/Fibras.kml'
    site = '{http://www.opengis.net/kml/2.2}'
    doc = ET.parse(file)
    root = doc.getroot()
    for i in root.iter(f'{site}Placemark'):
        nome = i.findtext(f'{site}name')
        cabo = []
        for t in i.iter(f'{site}LineString'):
            coord = t.findtext(f'{site}coordinates').split()
            for cod in coord:
                latLng = cod.split(',')
                cabo.append([float(latLng[1]), float(latLng[0])])

        folium.PolyLine(cabo, popup=nome,
                        tooltip=nome,
                        color="cyan",
                        weight=2,
                        # dash_array='5,15',
                        ).add_to(bkb)

    # for i in queryPosteEnel:
    #     folium.Marker(
    #         (i.latitude, i.longitude),
    #         popup=i.descricao,
    #         tooltip=i.nome,
    #         icon=BeautifyIcon(
    #             icon_shape='rectangle-dot',
    #             border_color='#0000FF',
    #             border_width=5,
    #         ),

    #     ).add_to(m)
    m.add_child(HeatMap(coordenadas, radius=20, name='Manutenção BKB'))
    pop.add_to(m)
    bkb.add_to(m)

    Draw().add_to(m)
    satelite = LayerFactory()
    satelite.get_layer_google_satelite().gerar_layer(m)
    satelite.get_layer_google_maps().gerar_layer(m)
    MiniMap(position='bottomleft').add_to(m)
    folium.LayerControl().add_to(m)
    m.save(os.path.join(
        settings.TEMPLATES[0]['DIRS'][0], 'partials/map.html'))

    return render(request, 'projeto-rede-mapa.html')

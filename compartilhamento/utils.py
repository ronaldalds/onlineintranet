from abc import ABC, abstractmethod

from folium.raster_layers import TileLayer


class Mapa(ABC):  # ABC Mapa ###############################
    @abstractmethod
    def gerar_mapa(self) -> None: pass


class Poste(Mapa):
    def gerar_mapa(self) -> None:
        print('')


class BkbFibra(Mapa):
    def gerar_mapa(self) -> None:
        print('Carro de luxo ZN está buscando o cliente...')


class Pop(Mapa):
    def gerar_mapa(self) -> None:
        print('Moto de luxo ZN está buscando o cliente...')


class RedeAcesso(Mapa):
    def gerar_mapa(self) -> None:
        print('Carro de luxo ZS está buscando o cliente...')


class AlimentadorSecundario(Mapa):
    def gerar_mapa(self) -> None:
        print('Moto de luxo ZS está buscando o cliente...')


class AlimentadorPrimario(Mapa):
    def gerar_mapa(self) -> None:
        print('Moto de luxo ZS está buscando o cliente...')


class MapaFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_bkb_fibra() -> Mapa: pass

    @staticmethod
    @abstractmethod
    def get_pop() -> Mapa: pass

    @staticmethod
    @abstractmethod
    def get_rede_acesso() -> Mapa: pass

    @staticmethod
    @abstractmethod
    def get_alimentador_secundario() -> Mapa: pass

    @staticmethod
    @abstractmethod
    def get_alimentador_primario() -> Mapa: pass


class NordesteMapaFactory(MapaFactory):
    @staticmethod
    def get_bkb_fibra() -> Mapa:
        return BkbFibra()

    @staticmethod
    def get_pop() -> Mapa:
        return Pop()

    @staticmethod
    def get_rede_acesso() -> Mapa:
        return RedeAcesso()

    @staticmethod
    def get_alimentador_secundario() -> Mapa:
        return AlimentadorPrimario()

    @staticmethod
    def get_alimentador_primario() -> Mapa:
        return AlimentadorSecundario()


class NorteMapaFactory(MapaFactory):
    @staticmethod
    def get_bkb_fibra() -> Mapa:
        return BkbFibra()

    @staticmethod
    def get_pop() -> Mapa:
        return Pop()

    @staticmethod
    def get_rede_acesso() -> Mapa:
        return RedeAcesso()

    @staticmethod
    def get_alimentador_secundario() -> Mapa:
        return AlimentadorPrimario()

    @staticmethod
    def get_alimentador_primario() -> Mapa:
        return AlimentadorSecundario()


class MapaLayer(ABC):
    @abstractmethod
    def gerar_layer(self) -> None: pass


class LayerGoogleSatelite(MapaLayer):
    @staticmethod
    def gerar_layer(mapa):
        return TileLayer(
            tiles='http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            attr='google',
            name='Google Satélite',
            max_zoom=20,
            subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
            overlay=False,
            control=True,
        ).add_to(mapa)


class LayerGoogleMaps(MapaLayer):
    @staticmethod
    def gerar_layer(mapa):
        return TileLayer(
            tiles='http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
            attr='google',
            name='Google Maps',
            max_zoom=20,
            subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
            overlay=False,
            control=True,
        ).add_to(mapa)


class LayerFactory:
    def get_layer_google_satelite(self) -> MapaLayer:
        return LayerGoogleSatelite()

    def get_layer_google_maps(self) -> MapaLayer:
        return LayerGoogleMaps()

import sys
import os

# Adiciona o diretório "sistema" ao sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sistema_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(sistema_dir)

from sistema.destinos import Destino

from sistema.gestorDestinos.add_destino import add_destino
from sistema.gestorDestinos.destinos_mais_procurados import destinos_mais_procurados
from sistema.gestorDestinos.get_destinos import get_destinos
from sistema.gestorDestinos.load_destinos import load_destinos
from sistema.gestorDestinos.obter_novos_voos import obter_novos_voos
from sistema.gestorDestinos.save_fila import save_fila
from sistema.gestorDestinos.save_pesquisas import save_pesquisas
from sistema.gestorDestinos.search_destinos import search_destinos
from sistema.gestorDestinos.show_destino import show_destino
from sistema.gestorDestinos.show_json import show_json

class GestorDestinos:
    def __init__(self, destinos):
        if not destinos:
            destinos = []
        self._destinos = destinos
        
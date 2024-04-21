import json
from sistema.destinos import Destino
from sistema.gestorDestinos.add_destino import add_destino

def load_destinos(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for destino_data in data:
                destino = Destino(**destino_data)
                add_destino(self, destino)
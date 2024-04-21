import json
from sistema.destinos import Destino

def obter_novos_voos(self, demo_file, fila_file):
    novos_voos = []

    with open(demo_file, 'r', encoding='utf-8') as file:
        demo_data = json.load(file)

    try:
        with open(fila_file, 'r', encoding='utf-8') as file:
            fila_data = json.load(file)
    except FileNotFoundError:
        fila_data = []

    nomes_fila = {destino['name'] for destino in fila_data}

    for info_voo in demo_data:
        if info_voo['name'] not in nomes_fila:
            novo_voo = Destino(**info_voo)
            novos_voos.append(novo_voo)
    
    return novos_voos 
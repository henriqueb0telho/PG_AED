import json
from sistema.insertion_sort import insertion_sort
from sistema.destinos.get import get_name, get_country, get_city, get_coordinates, get_near_airport, get_url, get_searches, get_next

def save_fila(self, file_name):
        insertion_sort(self._destinos)
        with open(file_name, 'w', encoding='utf-8') as file:
            destinos_data = []
            for destino in self._destinos:
                destino_data = {
                    'name': get_name(destino),
                    'country': get_country(destino),
                    'city': get_city(destino),
                    'near_airport': get_near_airport(destino),
                    'coordinates': get_coordinates(destino),
                    'url': get_url(destino),
                    'searches': get_searches(destino),
                    'next': get_next(destino)
                }
                destinos_data.append(destino_data)
            json.dump(destinos_data, file, ensure_ascii=False, indent=4)

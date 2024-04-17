import json
from style import text, background, char

# Classes
class Destino:
    def __init__(self, name, country, city, near_airport, coordinates, url, next=None):
        self._name = name
        self._country = country
        self._city = city
        self._near_airport = near_airport
        self._coordinates = coordinates
        self._url = url
        self._next = next
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_country(self):
        return self._country
    
    def set_country(self, country):
        self._country = country
    
    def get_city(self):
        return self._city

    def set_city(self, city):
        self._city = city
    
    def get_near_airport(self):
        return self._near_airport

    def set_near_airport(self, near_airport):
        self._near_airport = near_airport
    
    def get_coordinates(self):
        return self._coordinates

    def set_coordinates(self, coordinates):
        self._coordinates = coordinates
    
    def get_url(self):
        return self._url

    def set_url(self, url):
        self._url = url

    def get_next(self):
        return self._next
    
    def set_next(self, next):
        self._next = next

class GestorDestinos:
    def __init__(self, destinos=[]):
        self._destinos = destinos

    def add_destino(self, destino):
        self._destinos.append(destino)

    def get_destinos(self):
        return self._destinos

    def load_destinos(self, file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for destino_data in data:
                    destino = Destino(**destino_data)
                    self.add_destino(destino)

    def save_file(self, contents, file_name='queue.json'):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(contents, file, ensure_ascii=False, indent=4)

    def search_destinos(self, country=None, city=None, proximity=None):
        results = []
        for destino in self._destinos:
            if (not country or destino._country.lower() == country.lower()) and \
               (not city or destino._city.lower() == city.lower()) and \
               (proximity is None or destino._near_airport == proximity):
                results.append(destino)
        return insertion_sort(results)

    def show_destino(self, resultado):
        print('-'*50)
        print(f'{text.bold}{text.green}{resultado.get_name()}{text.reset}\n')
        print(f' {char.dot} País: {resultado.get_country()}')
        print(f' {char.dot} Cidade: {resultado.get_city()}')
        print(f' {char.dot} Coordenadas: {resultado.get_coordinates()}')
        print(f' {char.dot} Proximidade de aeroporto:', f'{text.green}Sim{text.reset}' if resultado.get_near_airport() else f'{text.red}Não{text.reset}')
        print(f' {char.dot} Url: {resultado.get_url()}')

    def show_json(self):
        for destino in self._destinos:
            self.show_destino(destino)

# Funções de apoio
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j]._name > key._name:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
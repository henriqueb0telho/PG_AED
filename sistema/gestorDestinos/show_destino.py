from sistema.style.text import text
from sistema.style.background import background
from sistema.style.char import char

from sistema.destinos.get import get_name, get_country, get_city, get_coordinates, get_near_airport, get_url

def show_destino(resultado):
        print('-'*50)
        print(f'{text.bold}{text.green}{get_name(resultado)}{text.reset}\n')
        print(f' {char.dot} País: {get_country(resultado)}')
        print(f' {char.dot} Cidade: {get_city(resultado)}')
        print(f' {char.dot} Coordenadas: {get_coordinates(resultado)}')
        print(f' {char.dot} Proximidade de aeroporto:', f'{text.green}Sim{text.reset}' if get_near_airport(resultado) else f'{text.red}Não{text.reset}')
        print(f' {char.dot} Url: {get_url(resultado)}')
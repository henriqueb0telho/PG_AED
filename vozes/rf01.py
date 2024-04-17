import json
from style import text, background, char

# Função que abre o ficheiro com os destinos e devolve um dicionário com as informações dos mesmos.
def load_destinos(file_name:str):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            print(f'\nFicheiro \'{file_name}\' foi carregado com sucesso!')
            return json.load(file)
    except FileNotFoundError:
        print(f'\nO arquivo \'{file_name}\' não foi encontrado.')
        try:
            file_name = str(input('Introduza o nome do ficheiro a abrir: '))
            with open(file_name, 'r', encoding='utf-8') as file:
                print(f'\nFicheiro \'{file_name}\' foi carregado com sucesso!')
                return json.load(file)
        except FileNotFoundError:
            print(f'\nO arquivo \'{file_name}\' não foi encontrado.\nA sair do programa!\n')
            exit()

def search_destinos(json_file, country=None, city=None, proximity=None):
    results = []

    for destino in json_file:
        if (not country or destino.get('country').lower() == country.lower()) and (not city or destino.get('city').lower() == city.lower()) and (proximity is None or destino.get('near_airport') == proximity):
            results.append(destino)

    # Ordenando o array usando o insertion sort
    arr = results
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)
    print(results)
    return arr
   

def save_fila(fila, file_name:str='p2/queue.json'):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(fila, file)

def show_destino(resultado):
    print('-'*50)
    print(f'{text.bold}{text.green}{resultado['name']}{text.reset}\n')
    print(f' {char.dot} País:', resultado['country'])
    print(f' {char.dot} Cidade:', resultado['city'])
    print(f' {char.dot} Coordenadas GPS:', resultado['coordinates'])
    print(f' {char.dot} Próximo de um aeroporto?:', f'{text.green}Sim{text.reset}' if resultado['near_airport'] else f'{text.red}Não{text.reset}')
    print(f' {char.dot} URL:', resultado['url'])

def show_json(json_file):
    for destino in json_file:
        show_destino(destino)
import json
from style import text, background, char

# Função que abre o ficheiro com os destinos e devolve um dicionário com as informações dos mesmos.
def load_destinos(file_name:str):

    # Tenta abrir o ficheiro
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            print(f'\nFicheiro \'{file_name}\' foi carregado com sucesso!')
            return json.load(file)
    except FileNotFoundError:
        # Se o ficheiro não for encontrado ele avisa ee pergunta ao utilizador o caminho correto e tenta novamente abrir, caso não consiga sai do programa.
        print(f'\nO arquivo \'{file_name}\' não foi encontrado.')
        try:
            file_name = str(input('Introduza o nome do ficheiro a abrir: '))
            with open(file_name, 'r', encoding='utf-8') as file:
                print(f'\nFicheiro \'{file_name}\' foi carregado com sucesso!')
                return json.load(file)
        except FileNotFoundError:
            print(f'\nO arquivo \'{file_name}\' não foi encontrado.\nA sair do programa!\n')
            exit()

# Função para salvar um dicionário num ficheiro JSON.
def save_fila(fila, file_name:str='./output.json'):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(fila, file)

# Função para a procura de destino por país, cidade e proximidade, devolvendo um dicionário com os resultados.
def search_destinos(json_file, country=None, city=None, proximity=None):
    results = []

    # Vê destino a destino no dicionário de destinos e verifica se corresponde com o pedido, caso sim adiciona o destino ao dicionário de resultados.
    for destino in json_file:
        if (not country or destino.get('country').lower() == country.lower()) \
            and (not city or destino.get('city').lower() == city.lower()) \
                and (proximity is None or destino.get('near_airport') == proximity):
            results.append(destino)

    arr = results
    n = len(arr)

    # Ordenando os resultados por ordem alfabética utilizando o algoritmo de ordenação insertionsort.
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j]['name'] > key['name']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def show_destino(resultado):
    print('-'*50)
    print(f'{text.bold}{text.green}{resultado['name']}{text.reset}\n')
    print(f' {char.dot} País:', resultado['country'])
    print(f' {char.dot} Cidade:', resultado['city'])
    print(f' {char.dot} Coordenadas GPS:', resultado['coordinates'])
    print(f' {char.dot} Próximo de um aeroporto?:', f'{text.green}Sim{text.reset}' if resultado['near_airport'] else f'{text.red}Não{text.reset}')
    print(f' {char.dot} URL:', resultado['url'])
import sistema as b
from style import text, background, char
from interface import menu

def main():
    fila_consultas = []
    a = b.GestorDestinos()
    a.load_destinos('demo.json')

    while True:
        option = menu()

        match option:
            case '0':
                a.save_file([{key[1:]: value for key, value in vars(destino).items()} for destino in a.get_destinos()], 'fila.json')
                a.save_file(fila_consultas, 'pesquisas.json')
                break
            case'1':
                    city = input('\n Digite a cidade (pressione Enter para pular): ').strip()
                    country = input(' Digite o país (pressione Enter para pular): ').strip()
                    prox = str(input(' Deve ser próximo de um aeroporto? ([s] / n): ').strip())

                    if (prox == 'S' or prox == 's' or prox == ''):
                        proximity = True
                    elif (prox == 'N' or prox == 'n'):
                        proximity = False
                    else:
                        print(f'{text.black}{background.red}Opção inválida{background.reset}{text.reset}.')
                        continue

                    resultados = a.search_destinos(country, city, proximity)

                    if resultados:
                        print('\nResultados da pesquisa:')
                        for resultado in resultados:
                            a.show_destino(resultado)
                    else:
                        print('Nenhum destino encontrado para os critérios fornecidos.')

                    fila_consultas.append({
                    'country': country if country else 'N/A',
                    'city': city if city else 'N/A',
                    'proximity_to_airport': prox
                })
            case '9':
                # a.show_json()
                # a.save_fila("imacula")
                print(fila_consultas)
            case _:
                    print(f'{text.black}{background.red}Opção inválida{background.reset}{text.reset}. Tente novamente.')


main()
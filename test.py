import sistema.gestorDestinos as b
import sistema.style as s
import sistema.destinos as d
from interface.menu import menu

def main():
    fila_consultas = []
    a = b.GestorDestinos([])
    b.load_destinos(a, 'demo.json')
    while True:
        option = menu()

        match option:
            case '0':
                b.save_fila(a, 'fila.json')
                b.save_fila(a, 'demo.json')
                b.save_pesquisas(a, fila_consultas, 'pesquisas.json')
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
                        print(f'{s.text.black}{s.background.red}Opção inválida{s.background.reset}{s.text.reset}.')
                        continue

                    resultados = b.search_destinos(a, country, city, proximity)

                    if resultados:
                        print('\nResultados da pesquisa:')
                        for resultado in resultados:
                            b.show_destino(resultado)
                    else:
                        print('Nenhum destino encontrado para os critérios fornecidos.')

                    fila_consultas.append({
                        'country': country if country else 'N/A',
                        'city': city if city else 'N/A',
                        'proximity_to_airport': prox
                    })
            case '2':
                novos_destinos = b.obter_novos_voos(a, 'demo.json','fila.json')
                if not novos_destinos:
                    print('\nNão há novos destinos disponíveis.')
                else:
                    for destino in novos_destinos:
                        b.show_destino(destino)
            case'3':
                print("Top 10 most searched destinations:")
                for destination, count in b.destinos_mais_procurados(a):
                    print(f"{destination}: {count} searches")
            case '9':
                b.show_json(a)
            case _:
                    print(f'\n{s.text.black}{s.background.red} Opção inválida {s.background.reset}{s.text.reset} Tente novamente.')


main()
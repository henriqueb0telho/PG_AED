from rf01 import *

json_file = load_destinos('./demo.json')

# Função principal
def main():
    fila_consultas = []

    while True:
        print(f'\n\n\t\t{text.bold}{text.underline}MENU{text.reset}\n')
        print(f' {char.dot} 1. Pesquisar destinos turísticos')
        print(f' {char.dot} 9. Mostrar todos os destinos')
        print(f' {char.dot} 0. Sair')

        option = str(input(f'\n   {text.bold}{text.underline}Escolha uma opção{text.reset}: '))

        match option:
            case '0':
                nome_arquivo = input('Digite o nome do arquivo para salvar os registros: ')
                save_fila(fila_consultas, nome_arquivo)
                print(f'Fila de consultas registrada em {nome_arquivo}. Saindo...')
                break
            case '1':
                city = input(' Digite a cidade (pressione Enter para pular): ').strip()
                country = input(' Digite o país (pressione Enter para pular): ').strip()
                prox = str(input(' Deve ser próximo de um aeroporto? ([s] / n): ').strip())

                if (prox == 'S' or prox == 's' or prox == ''):
                    proximity = True
                elif (prox == 'N' or prox == 'n'):
                    proximity = False
                else:
                    print(f'{text.black}{background.red}Opção inválida{background.reset}{text.reset}.')
                    continue

                resultados = search_destinos(json_file, country, city, proximity)

                if resultados:
                    print('\nResultados da pesquisa:')
                    for resultado in resultados:
                        show_destino(resultado)
                        
                else:
                    print('Nenhum destino encontrado para os critérios fornecidos.')
                fila_consultas.append({
                    'country': country if country else 'N/A',
                    'city': city if city else 'N/A',
                    'proximity': proximity if proximity else 'N/A',
                    'results': resultados if resultados else 'N/A'
                })
            case '9':
                for destino in json_file:
                    show_destino(destino)

            case _:
                print(f'{text.black}{background.red}Opção inválida{background.reset}{text.reset}. Tente novamente.')

if __name__ == '__main__':
    main()

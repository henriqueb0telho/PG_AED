from style import text, background, char

def menu():
    print(f'\n\t\t{text.bold}{text.underline}MENU{text.reset}\n')
    print(f'  {char.dot} 1. Pesquisar destinos turísticos')
    print(f'  {char.dot} 9. Mostrar todos os destinos')
    print(f'  {char.dot} 0. Sair')

    return str(input(f'\n    {text.bold}{text.underline}Escolha uma opção:{text.reset} '))
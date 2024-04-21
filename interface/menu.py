from sistema.style.text import text
from sistema.style.background import background
from sistema.style.char import char

def menu():
    print(f'\n\t\t{text.bold}{text.underline}MENU{text.reset}\n')
    print(f'  {char.dot} 1. Pesquisar destinos turísticos')
    print(f'  {char.dot} 2. Pesquisar novos destinos turísticos')
    print(f'  {char.dot} 3. Mostrar os 10 destinos mais procurados')
    print(f'  {char.dot} 0. Sair')

    return str(input(f'\n    {text.bold}{text.underline}Escolha uma opção:{text.reset} '))
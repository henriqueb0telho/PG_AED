import json

import  sistema.style as s

def avaliar_app():
    aval = int(input('\n Avalie a nossa aplicação de 1 a 4 (1 - Terrível | 4-Muito Boa): '))
    while aval < 1 or aval > 4:
        print(f'\n {s.text.black}{s.background.red}Introduza um valor de 1 a 4!{s.text.reset}')
        aval = int(input('\n Avalie a nossa aplicação de 1 a 4 (1 - Terrível | 4-Muito Boa): '))
    try:
        with open('avaliacoes.json', 'r', encoding='utf-8') as file:
            data = file.read()
            avaliacoes = json.loads(data) if data else []
            file.close()
    except FileNotFoundError:
        avaliacoes = []
    with open('avaliacoes.json', 'w', encoding='utf-8') as file:
        content = {'aval': aval}
        avaliacoes.append(content)
        json.dump(avaliacoes, file, ensure_ascii=False, indent=4)
        file.close()
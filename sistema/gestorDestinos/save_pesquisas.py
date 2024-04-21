import json

def save_pesquisas(self, contents, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(contents, file, ensure_ascii=False, indent=4)

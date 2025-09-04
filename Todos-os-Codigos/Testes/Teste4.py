# ---------------------------------------- Bibliotecas ----------------------------------------

from os import system as console
import time
import json

# ideia: pegar e adicionar uma chave a um .json existente se ouver, se não ouver crie um

def diciona():
    dicionario = []
    while True:
        nome_adicao = input('Digite o nome da lista que deseja dicionar: ')
        console('cls')
        nome_lista = input('Digite o nome do arquivo: ')
        console('cls')
        try:
            with open(fr'Todos-os-Codigos/Testes/{nome_lista}.json', 'r') as lista:
        except Exception:
            resul = input('Arquivo não encontrado, deseja criar um novo: ').lower().replace('sim', 's')
            if resul == 's':
                novo_arquivo = input('Digite o nome do arquivo: ').strip().lower()
                with open(fr'Todos-os-Codigos/Testes/{novo_arquivo}', 'w') as new_lista:
                    json.dump(dicionario, novo_arquivo, ensure_ascii=False, indent = 2)



diciona()

# Bibliotecas
import os
import json
import time

# Funções
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def jsom():
    with open(fr'Todos-os-Codigos/Testes/Dados.json', 'w', encoding='utf-8') as open:
        banco = dict(json.load(open))
    

# Bibliotecas
import os
import json
import time

# Definir o local do arquivo
ARQUIVO = 'Aulas/Aula_7/Banco.json'

# limpar a tela
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Funções de Apoio

def carregar():                                 
    # Carrega as contas do arquivo JSON
    if os.path.exists(ARQUIVO):                                         # Verifica se o arquivo existe
        with open(ARQUIVO, 'r', encoding='utf-8') as f:                 # Abre o arquivo no modo de leitura
            try:
                return json.load(f)                                     # Retorna o os dados do arquivo
            except json.JSONDecodeError:                                
                return []
    return[]
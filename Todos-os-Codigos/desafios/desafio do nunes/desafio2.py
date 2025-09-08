# Banco de dados da turma

import os
import json
import time

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Listas
lista = []

# Funções
def tela():
    while True:
        limpar()
        bm = print('Bem vindo ao banco de dados do 2° DS\n')
        tb = lambda: limpar(), bm
        print('Qual operação deseja fazer?')
        o = input('1 | Cadastro\n2 | Busca\n3 | Alteração de dados\n')
        o = int(o)
        match o:
            case 1:
                tb()
                n = input('Digite o nome do Aluno: ')
                i = input('Digite a idade do Aluno: ')
                m = input('Digite o email do Aluno: ')
                lista.append(n, i, m)
                return lista
            case 2:
                n
                return a
            case 3:
                return a
            case _:
                print('Digite um numero valido')
                time.sleep(1)
                continue
def sistema():
    while True:
        n = tela


def banco():
    with open(fr'Todos-os-Codigos/desafios/Bancos/Bancodf1.json', 'r', encoding='utf-8') as f:
        op = json.load(f)
    with open(fr'Todos-os-Codigos/desafios/Bancos/Bancodf1.json', 'w', encoding='utf-8') as d:
        json.dump(lista, d, indent=2, ensure_ascii=False)
tela()
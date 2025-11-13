import json
import os
import sys
import time
from datetime import date
from datetime import datetime

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
dta = date.today()
dt = dta.strftime("%d/%m/%Y")
hta = datetime.now().time()
ht = hta.strftime("%H:%M")

def carregar():
    try:
        with open(fr'Aulas/Aula_9/Dados.json', 'r', encoding='utf-8') as f:
            dado = json.load(f)
            return dado
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def carregarl():
    try:
        with open(fr'Aulas/Aula_9/Livros.json', 'r', encoding='utf-8') as f:
            dado = json.load(f)
            return dado
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save(dados):
    with open(fr'Aulas/Aula_9/Dados.json', 'w', encoding='utf-8') as fs:
        json.dump(dados, fs, indent=2, ensure_ascii=False)

def savel(dados):
    with open(fr'Aulas/Aula_9/Livros.json', 'w', encoding='utf-8') as fs:
        json.dump(dados, fs, indent=2, ensure_ascii=False)

def texto(palavra,v=0.02):
    for i in palavra:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(v)  # Ajuste o tempo conforme desejado
        
def interface():
    while True:
        limpar()
        print(20 * "*", 'Sistema de gerenciamento da biblioteca', 20 * "*")
        texto('1 | Gerenciar Livros\n')             # Colocar a devolução dentro dele
        texto('2 | Gerenciar Pessoas\n')
        texto('3 | Emprestimo de livro\n')
        texto('4 | Sair\n')
        i = int(input())

        if i > 4:
            print('Digite um numero valido')
            time.sleep(1)
            continue
        match i:
            case 1:
                grl()           # Gerenciamento de livros
            case 2:
                grp()           # Gerenciamento de Pessoas
            case 3:
                while True:
                    limpar()
                    lista = carregarl()
                    texto("Digite o nome do livro(ENTER para sair): ")
                    nl = input().title()
                    if nl == '':
                        break
                    if nl not in lista:
                        texto('Livro não encotrado')
                        time.sleep(1)
                        continue
                    texto('Digite o nome do Cliente: ')
                    np = input()
                    emprestimo(np,nl)    # Emprestimo do livro
            case 4:
                break

def grl():                      # Gerenciamento de livro
    while True:
        limpar()
        texto('1 | Devolução de livro\n')
        texto('2 | Cadastar novos livros\n')
        texto('3 | Remover Livros\n')
        texto('4 | Listar livros\n')
        texto('5 | Sair\n')

        i = int(input())

        if i > 5:
            print('Digite um numero valido')
            time.sleep(1)
            continue
        match i:
            case 1:             # Pegar a lista e verificar o livro
                ...
            case 2:
                limpar()
                texto('Digite o nome do livro a ser cadastrado: ')
                n = input().title()
                limpar()
                cadastrar(n)
                continue
            case 3:
                lista = carregarl()
                texto("Digite o nome do livro a ser removido: ")
                i = input().title()
                input(i)
                if i in lista:
                    remover(i)

                else:
                    print('Livro não cadastrado')
                    time.sleep(1)
                    continue
                break
            case 4:             # Listar livros
                lista = carregarl()
                input(lista)

            case 5:
                break


def grp():
    ...

def emprestimo(Np,Nl):
    dado = carregar()
    ds = dta.strftime("%d")
    ds = int(ds)
    ds += 7
    dd = {'Nome da Pessoa':Np,
          'Nome do Livro': Nl,
          'Data de devolução':ds,
          'Data': dt,
          'Hora': ht
         }
    dado.append(dd)
    save(dado)
    
def remover(nomel):
    lista = carregarl()
    indice_do_item = lista.index(nomel)
    lista.remove(indice_do_item)
    input(nomel, 'Foi removido com sucesso')

def cadastrar(n):
    lista = carregarl()
    lista.append(n)
    with open('Aulas/Aula_9/Livros.json', 'w', encoding='utf-8') as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)
    print(n)
    texto('Foi adicionado com sucesso')
    input()

interface()

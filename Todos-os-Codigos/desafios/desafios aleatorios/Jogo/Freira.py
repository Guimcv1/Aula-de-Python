import os
import time
import sys
import json
from datetime import date
from datetime import datetime

hta = datetime.now().time()
ht = hta.strftime("%H:%M")
dta = date.today()
dt = dta.strftime("%d/%m/%Y")
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')



def caregar():
    try:
        with open(fr'Todos-os-Codigos/desafios/Bancos/Freira.json', 'r', encoding='utf-8') as f:
            dado = json.load(f)
            return dado
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save(dados):
    with open(fr'Todos-os-Codigos/desafios/Bancos/Freira.json', 'w', encoding='utf-8') as fs:
        json.dump(dados, fs, indent=2, ensure_ascii=False)

def inicio():
    while True:
        save = caregar()
        limpar()
        print(save)
        print(f"{20 * '*'} As Irmãs {20 * "*"}")
        s = int(input('1 | Iniciar\n2 | Config\n3 | Sair\n'))
        nn = list(range(len(save)))  # Mostra uma lista com todos os índices possíveis
        input(nn)
        if s >= nn + 1:                         # nn é a variavel que damos a quantidade de indexs na lista
            print('Digite um numero valido.')
            time.sleep(1)
            continue
        else:
            ...
        limpar()
        match s:
            case 1:
                dado = caregar()                            # Fazer um sistema para imprimir no terminal e excluir saves
                if dado == caregar(): 
                    i = df()
                    limpar()
                    match i:
                        case 1:
                            n = input('Digite o nome do save: ')
                            print(f"lista: {dado}")
                            dd = {'Nome': n,
                                  'Data': dt,
                                  'Hora': ht,
                                  'Estado': 0}
                            dado.append(dd)
                            return dado 
                        case 2:
                            return save
                else:
                    print(dado)
        break

def texto(palavra,v=0.1):
    for i in palavra:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(v)  # Ajuste o tempo conforme desejado
        
def salvar(save,num):
    dado = caregar()
    dd = {'Nome': save,
          'Data': dt,
          'Hora': ht,
          'Estado': num}
    dado.append(dd)
    save(dado)

def cap1():
    texto('Teste de palavras')

def df():
    lis = caregar()
    num_lis = len(lis)  # Mostra uma lista com todos os índices possíveis
    num_lis = int(num_lis)
    print(num_lis)
    print(f'1 | Novo Jogo')
    nn = 2
    for i in num_lis:
        nn += 1
        print(f'{i+2} | {lis[i]['Nome']}')
    i = int(input(f'{nn} | Sair\n'))

def Jogo():
    while True:
        dados = inicio()
        save(dados)
        # Carrega o save atualizado
        save_data = caregar()
        print(save_data)
        if save_data and 'Estado' in save_data[0]:
            estado = save_data[0]['Estado']
        else:
            estado = None
        match estado:     # ira pegar o numero do 'Estado'
            case 0:
                texto('Capitulo 1\n')
                cap1()
            case 1:
                texto('Capitulo 2\n')
                cap2()
            case 2:
                texto('Capitulo 3\n')
                cap3()
            case 3:
                texto('Capitulo 4\n')
                cap4()
            case 4:
                texto('Capitulo 5\n')
                cap5()
            case 5:
                texto('Capitulo 6\n')
                cap6()
            case _:
                print('Erro')
        break
df()
Jogo()
dado = caregar()
print(dado)

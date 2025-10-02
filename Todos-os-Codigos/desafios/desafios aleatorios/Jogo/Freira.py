import os
import time
import sys
<<<<<<< HEAD
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
        saves = caregar()  # Corrigido: não usa mais 'save'
        limpar()
        print(f"{20 * '*'} As Irmãs {20 * '*'}")
        s = int(input('1 | Iniciar\n2 | Config\n3 | Sair\n'))
        nn = list(range(len(saves)))  # Corrigido aqui também
        ns = 1 + len(nn)
        if s > ns:
            print('Digite um numero Valido.')
            time.sleep(1)
            continue
        else:
            ...
        limpar()
        dado = caregar()
        match s:
            case 1:
                limpar()
                i = df()
                if i <= ns:
                    match i:
                        case 1:
                            nome = input('Digite o nome do save: ')
                            salvar(nome)   
                else:
                    print('Digite um numero valido.')
                    time.sleep(1)
                    continue
            case 2:
                ...
            case 3:
                break
        
        
        
    

def texto(palavra,v=0.1):
    for i in palavra:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(v)  # Ajuste o tempo conforme desejado
        
def salvar(Nsave,num=0):
    dado = caregar()
    
    dd = {'Nome': Nsave,
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
    
    print(f'1 | Novo Jogo')
    nn = 2
    for i in range(num_lis):
        nn += 1
        print(f'{i+2} | {lis[i]['Nome']}')
    i = int(input(f'{nn} | Sair\n'))
    return i

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


Jogo()
dado = caregar()
print(dado)
=======

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def inicio():
    while True:
        limpar()
        print(f"{20 * '*'} As Irmãs {20 * "*"}")


def texto(palavra):
    for i in palavra:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)  # Ajuste o tempo conforme desejado
        

inicio()
>>>>>>> 675609c1e16924cdcfc59caa3ded69266d767794

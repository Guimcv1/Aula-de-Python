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

dado = []

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
        print(f"{20 * '*'} As Irmãs {20 * "*"}")
        s = int(input('1 | Iniciar\n2 | Config\n3 | Sair\n'))
        if s >= 4:
            print('Digite um numero valido.')
            time.sleep(1)
            continue
        else:
            ...
        limpar()
        num = 0
        match s:
            case 1:
                if dado == []:
                    
                    if save and 'Nome' in save[num]:
                        i = int(input(f'1 | Novo Jogo\n2 | {save[num]['Nome']}\n3 | Sair\n'))
                    else:
                        i = int(input('1 | Novo Jogo\n2 | Sair\n'))
                    limpar()
                    match i:
                        case 1:
                            n = input('Digite o nome do save: ')
                            dd = {'Nome': n,
                                  'Data': dt,
                                  'Hora': ht,
                                  'Estado': 0}
                            dado.append(dd)
                            return dado 
                        case 2:
                            continue
                else:
                    print(dado)
        break

def texto(palavra):
    for i in palavra:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)  # Ajuste o tempo conforme desejado
        

def Jogo():
    while True:
        dados = inicio()
        save(dados)
        break
Jogo()
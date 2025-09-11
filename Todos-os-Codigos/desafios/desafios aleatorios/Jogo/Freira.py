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
        print(f"{20 * '*'} As Irmãs {20 * "*"}")
        s = int(input('1 | Iniciar\n2 | Config\n3 | Sair\n'))
        
        if s >= 5:
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
                    match save and 'Nome' in save[0]:
                        case True:
                            match save and 'Nome' in save[1] == '':
                                case True:
                                    i = int(input(f'1 | Novo Jogo\n2 | {save[0]['Nome']} {save[0]['Data']} {save[0]['Hora']}\n3 | {save[1]['Nome']} {save[1]['Data']} {save[1]['Hora']}\n4 | Sair\n'))
                                case _:
                                    i = int(input(f'1 | Novo Jogo\n2 | {save[0]['Nome']} {save[0]['Data']} {save[0]['Hora']}\n3 | Sair\n'))
                        case _:
                            i = int(input('1 | Novo Jogo\n2 | Sair\n'))
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




def Jogo():
    while True:
        dados = inicio()
        input(dados)
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

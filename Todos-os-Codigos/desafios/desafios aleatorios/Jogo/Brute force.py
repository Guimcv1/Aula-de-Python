import os
import sys
import time
from random import randint

def texto(palavra, velocidade=0.01):
    for i in palavra:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(velocidade)

lista_completa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', 
                  0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

texto('Digite a sua senha: \n')
senha = input('')
senha_descoberta = ''
while(senha_descoberta!=senha):
    senha_descoberta = ''
    for letra in range(len(senha)):
        tentativa = lista_completa[randint(0,17)]
        senha_descoberta = str(tentativa)+str(senha_descoberta)
        print(senha_descoberta)
        print('Tentando senhas... por favor espere!')
        os.system('cls')
texto(f'Sua senha é: {senha_descoberta}')
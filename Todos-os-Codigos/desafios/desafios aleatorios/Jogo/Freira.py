import os
import time
import sys

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
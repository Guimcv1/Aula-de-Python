from os import system as console
import os
import time
import sys

limpar = lambda: console("cls" if os.name == "nt" else "clear")

def texto(palavra,v=0.03):
    for i in palavra:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(v)  # Ajuste o tempo conforme desejado

def tela():
    limpar()
    print(20 * "-", "Explorador de Arquivo", 20 * "-")
    console("cd teste")
    console('dir')
    os.path()
    
    
    
    

tela()
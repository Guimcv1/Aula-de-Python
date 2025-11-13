import os

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
limpar()

def caso():
    numf = fatorador()
    if numf == 0:
        pass
    else:
        return numf

def fatorador():
    while True:
        
        print(20*'-', ' Bem vindo ao fatorador ', 20*'-')
        num = input('Digite o numero a ser fatorado: ')
        num = int(num)
        while True:
            if num % 2 == 0:
                if numf <= 1:
                    while True:
                        numf = num/2
                        print(numf)
                        caso()
                        return numf
            elif num % 3 == 0:
                numf = num/3
                print(numf)
                caso()
                return numf
            else:
                print('erro')
fatorador()
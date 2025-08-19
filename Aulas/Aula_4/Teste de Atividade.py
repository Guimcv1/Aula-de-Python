'''
Sistema de sorteio
'''

import random # biblioteca de sistema aleatorio 

def Sorteio():
    nome1 = input("Digite o primeiro nome: ")
    nome2 = input("Digite o Segundo nome: ")
    nome3 = input("Digite o Terceiro nome: ")
    nome4 = input("Digite o Quarto nome: ")
    nome5 = input("Digite o Quinto nome: ")

    lista_de_nomes = [nome1, nome2, nome3, nome4, nome5]

    escolhido = random.choice(lista_de_nomes)               # choice é ussado para randomizar quando é uma string
    print(escolhido)

def Sorteio2():
    lista = []
    sair = False
    while sair == False:
        nome_candidato = input('Digite os nomes para o sorteio ou ENTER para sair:')
        if nome_candidato != "":
            lista.append(nome_candidato)                    # adiciona uma variavel a lista
        else:
            sair = True
    escolhido = random.choice(lista)
    print('O escolhido foi: ', escolhido)

def Sorteio3():

    # importando Bibliotecas
    import random 
    import os
    import time
    
    # Criando Variaveis
    lista_nomes = []
    lista_sorteados = []

    while True:                                             # Ele ira se repetir enquanto 
        nome = input("Digite o nome para o sorteio: ")
        if nome:
            lista_nomes.append(nome)
        else:
            break
    while True:
        if lista_nomes:
            os.system('cls')
            escolhido = random.choice(lista_nomes)      # Sorteia um nome da lista de nomes     
            lista_sorteados.append(escolhido)           # Adiciona ele na lista                          
            lista_nomes.remove(escolhido)               # Remove ele da Lista 
            print(f"O ecolhido foi: {escolhido}")  
            opcao = input('Deseja sortear outros nome?\n S - Sim \n| N - Não\n').lower()
            os.system('cls')                            # Limpa a tela

            if opcao == 's':
                continue
            else:
                print('Não a nomes para serem sorteados!')
                break
    print("Programa Finalizado")
    print(f"Os sorteados foram: {lista_sorteados}")


'''
pop - função, remove pelo indice - Remove indices primarios ou novos

    pop() - remover o ultimo indice
    pop(0) - remove o indice 0

del - Instrução, remover item pelo indice com quantidades, mais de 1 item - Remove por grupos
    del[3] - vai buscar pelo indice 3
    del[2:10] - vai remover os indices do 2 ao 10
    del[escolhido]

remove - remove a partir de uma variavel - remove indices especificos 
    lista.remove(variavel)

'''

def Sorteio4():
    from random import randint          # Ele gera um numero aleatorio
    from os import system
    from time import sleep as tempo 
    
    while True: 
        print('Tente adivinhar o numero!')
        num1 = int(input("Digite um numero: "))
        num_secreto = randint(1,100)
        if num1 == num_secreto:
            print('Parabens você venceu o jogo')
        else:
            print("Você errou, o numero era: ", num_secreto)
            input("")
            system('cls')

def Sorteio5():
    import random                             # Ele gera um numero aleatorio
    from os import system
    from time import sleep as tempo 
    numero_secreto = random.randint(1,100)
    max_tentativas = 10
    acertou = False
    print(30*"-",'Bem Vindo ao Tigrinho', 30*"-")
    tentativa=int(input("Digite um numero: "))
    print("Você tem: ", max_tentativas, "tentativas de adivinhar")
    print("Vamos começar? ")

    while tentativa < max_tentativas:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Por favor, digite um número valido. ")
            continue    
        tentativa += 1

        # Verificar palpite
        if palpite == numero_secreto:
            acertou = True
            break
        elif palpite < numero_secreto:
            print("Tente um número maior!")
            tempo(2)
            system('cls')
        elif palpite > numero_secreto:
            print("Tente um número menor")
            tempo(2)
            system('cls')
            

Sorteio5()


'''
del(nome_lista[posição]) deleta uma possição espesifica
    # ValueError                               Exeção de Valor - correção de erro 




    separador = ","

    nome_string = separador.join(nomes_lista)

    

    mese_string = ['janeiro Fevereiro Março Abril Maio Junho]
    messes_Lista = messe_string.spli ('')

    for mes in messe_lista
    print(mes)

    somar 
    numeros = [1,2,3,4,5,6,7,8,9,10]
    print(sum(numeros))

    numeros.sort(reverse=True)          # Ordenar números de uma lista 
    print(numeros)
'''
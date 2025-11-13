# Lista



nomes_lista = ['Fulado', 'Ciclano', 'Beltrano', 'Joana', 'Maria', 'Mariana']

#imprime lista na tela
print(nomes_lista)

print(nomes_lista[0]) # imprime o Fulano
print(nomes_lista[2]) # imprime o Beltrano
print(nomes_lista[4]) # imprime a Maria

# Com laço de repetição

for nome in nomes_lista:
    print(nome)

'''
Fulado
Ciclano
Beltrano
Joana
Maria
Mariana
'''
# Variavel contadora 
range(1,100,10)     # Ele vai conar de 1 á 100 de 10 em 10
# Usando o len ele sere para contar quantos elementos eu tenho em algo
for i in range(len(nomes_lista)):
    print(f'{i+1}° nome da lista: {nomes_lista[i]}')

'''
1° nome da lista: Fulado
2° nome da lista: Ciclano
3° nome da lista: Beltrano
4° nome da lista: Joana
5° nome da lista: Maria
6° nome da lista: Mariana
'''
nome = "Joãozinho"
for i in nome:
    print(i)

nomes_lista.sort() # Serve para sortear os nomes na lista

nome = input('Informe o nome que deseja encontrar: ')

if nome in nomes_lista: # Procurar algo especifico em uma lista
    print(nome)
else:
    print(f'{nome} nome não encontrado.')

# Procurar elementos em uma lista INDEX 
indice = nomes_lista.index(nome)        # neste casso ele ira informar o primeiro termo da lista no caso da lista "Fulano"

#retorno do resultado
try:                                                        # Usado para fazer tratamento de erro se algo de certo 
    print(f'{nome} encontrado no índice {indice}')
except:                                                        # Se algo não de certo
    print(f'{nome} não encontrado')

# Usado para contar quantos vezes o termo aparece 
quantidade = nomes_lista.count(nome)

try:
    print(f'{nome} foi encontrado na lista {quantidade} vezes')
except:
    print(f'{nome} não foi encontrado.')

# Substituição de lista

nomes_lista[0] = 'Alex'         #subtituir o termo 0 da lista pelo o 'Alex'
for nome in nomes_lista:
    print(nome)

nome_a_alterar = input('Informe o nome a ser substituido: ')
nomes_lista[nomes_lista.index(nome_a_alterar)] = input('Informe o novo nome') # Dentro de nome Lista ele irar procurar dentro de nome lista o nome a ser alterado 

for nome in nomes_lista:
    print(nome)

# Tabuada

numero = int(input('Digite o numro: '))
for i in range(1, 11):                          # Dentro do i ele vai de 1á 11 tendo como resultado o numero * i então ele vai ir de 1 á 11 multiplicando o numero 
    resultado = numero * i
    print(f'{i} X {numero} = {resultado}')



# Bibliotecas

# Biblioteca Nativa

import os
from os import system  
import time 
from time import sleep as tempo  # "as" é usado para abreviar uma biblioteca
system('cls')

# Sistema de contagem

cont = input("Digite um numero inteiro")

try:
    cont_int = int(cont)
    while cont_int >= 0:
        print(f"Contagem regressiva: {cont_int}...")
        tempo(1)
        cont_int -= 1


except:
    print("Digite um numero Valido")


print("Fim da contagem!")


'''
except Exception:
    print(KeyError)
    ...

'''


#--------------------------------------------------------------------------------------------------------------------------------------------


'''
Sistema de sorteio
'''

import random # biblioteca de sistema aleatorio 

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o Segundo nome: ")
nome3 = input("Digite o Terceiro nome: ")
nome4 = input("Digite o Quarto nome: ")
nome5 = input("Digite o Quinto nome: ")

lista_de_nomes = [nome1, nome2, nome3, nome4, nome5]

escolhido = random.choice(lista_de_nomes)
print(escolhido)
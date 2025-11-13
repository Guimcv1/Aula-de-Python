'''
Fazer um sistema onde ele pega os numeros e inverte eles criptografando eles tipo abc --> 262425
e depois ele era trasnforma em binario e integrar valores 

lista.reverse 

'''

# Biblioteca
import os
import json


# Lamba
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
limpar()

# listas
lista = []
numeros = [i for i in range(47,73)]
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
val = input('Digite a criptografia:\n')
vazio = []
numeros.reverse()

# Funções

for i in val:                           # Ele ira passar por toda a resposta do usuario
    if i in alfabeto:                   # ira ver todo o input e ver se ele esstá dentro da lista de caracter
        x = alfabeto.index(i)           # x vai pegar o index do input correspondente ao alfabeto
        vazio.append(numeros[x])        # Adiciona os numeros corespondentes a eles de acordo com o index
print(vazio)                            # imprime a lista



lista = []              # lista principal onde fica os index pai
lista2 = []             # Lista final já com as substituições
lista3 = []             # Lista de substituição
nova_lista = []         # Lista onde guarda os indexs
input('Digite algo')    # input

# Pega os valores de uma lista e substitui por outra lista seguindo o mesmo index
for i in input:                                 # ira se repetir enquanto tiver valores dentro de input em que ele pasara letra por letra
    if i in lista:                              # se tem o valor de i dentro de lista
        nova_lista = lista.index(i)             4# pega o index do input dentro la lista e dar o valor a uma variavel
        lista2.append(lista3[nova_lista])       # adiciona a lista 2 o valor já substituido da lista de acordo com o index













from os import system as console
import json
def teste1():
    input('')



# Uma tabela de quatro colunas/quatro linhas ‒ uma matriz bidimensional (4x4)
 
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'







my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")
 

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list.sort()
i = True
lista=[]
print("A lista com os elementos exclusivos aqui")
while i == True:
    if my_list[0] == my_list[1]:
        del my_list[1]
        lista = my_list.pop(0)
    else:
        i = False
        continue
for i in range(lista):
    print(i)


def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")
 

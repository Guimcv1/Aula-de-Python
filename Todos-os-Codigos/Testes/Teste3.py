from os import system as console
clear = lambda: console('cls')


# Exemplo 1
palavra = ["Python", "João", "matheus"]
for letter in palavra:                  # ira se repitir se tiver algum valor dentro dele
    print(letter)                       # imprime um nome, repete e imprime o outro nome até acabar os nomes 
    print(letter, end="*")              # imprime uma letra, quebra de linha e imprime a proxima letra | end= substitui a quebra de linha por *

input('')    
input(clear())
# Exemplo 2
for i in range(1, 11):                  # ira repetir até passar por todos os numero entre 1 e 10             
    if i % 2 == 0:                      # imprime apenas os numeros divisiveis de 2 dentro de 1 a 10
        print(i)                        # imprime o numero

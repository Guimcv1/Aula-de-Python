#------------------------- Este é um Repositorio de Códigos Python-------------------------

#*********************************** Codigos Simples ***********************************

#----------------------------------- Códigos de Debug ----------------------------------- 

# Codigo para execultar no terminal
'''
python nome_do_arquivo.py

'''
#---------------------------- Codigo para gerenciar as pastas ----------------------------
# Abrir uma pasta
'''
cd Nome_da_pasta

'''
# Voltar uma pasta
'''
cd ..

'''


#**************************************** Prints ****************************************

# print() - imprime algo no terminal podendo ser uma variavel ou um texto

print()

# Se colocar '' ou "" você pode imprimir um texto

print("Olá mundo!")

# Usando Varíavel 

Joao:str = "Olá Mundo!"
print(Joao)

# Usando Texto com variavel - colocar a virgula colocara um espaço entre elas automaticamente

Joao:str = "Olá Mundo!"
print(Joao, "Olá mundo 2.0")

# Usando Texto com variavel com substituição da virgula 
# Ele ira substituir a virgula com qualquer coisa dentro do sep=

Joao:str = "Olá Mundo!"
print(Joao, "Olá mundo 2.0",sep=" /// ")

# Usando o f

juntas="Conectadas"
print(f"Posso colocar texto e variavel {juntas} sem o uso de virgulas")

# Imprimir o tipo de variavel - Usando o codigo type é possivel verificar 
# qual é o tipo de variavel dentro dos parenteses

inteiro = 10
print(type(inteiro))

# inputs com print e definição de tipo

Variavel:int=input("Digite um Numero: ")

# ou

Var = float(input("Escreva um numero: "))

#--------------------------------------------- Operações dentro do print -------------------------------------------

print(50*"Olá")

Juninho="Olá Pessoas"
print(Juninho*2)

#---------------------------------------------------- Variaveis ----------------------------------------------------

# Inteira - Números inteiros

Num:int
Num=12

# Texto - String 

Texto:str
Texto="Opá pessoal"

# Numeros quebrados - float

Num_quebrado:float
Num_quebrado=14.2566

# Verdadeiro ou falso - bool
# Sera Verdadeiro ou falso dependendo se tem valor atribuido a ele, se tiver texto ou numero ele sera verdadeiro


sera=(bool(input("Digite ou não Digite: ").replace("Não","")))
print(sera)

# Vai dar verdadeiro

'''
Substituição de variavel
'''
palavra:str="153"

palavra = int(palavra)

print(palavra+10/2)

# Substituição de Caracteres
# Ultilizando o .replace() você substitui o primeiro caracter dentro dele pelo o segundo 

peso = float(input('digite o seu peso: '.replace(",",".")))

# Caixa alta ou caixa baixa

Tab=(input("Qual o seu nome: ").upper()) #caixa Alta
print(Tab)

Tab=(input("Qual o seu nome: ").lower()) #caixa Baixa
print(Tab)

#-------------------------------- laço de repetição --------------------------------

#declaração de variavel


#loop
def Loop():
    numero:int=100
    while numero >= 0:
        print(numero*"*")
        numero -= 1


#Break - Quebra o loop mesmo que as condições estejam sendo atendidas
def Break():
    cont = 0
    while cont < 15:
        cont+= 1
        if cont % 2 == 0:
            print(cont)
        elif cont >=7:
            break
        else:
            continue

# Laços com FOR 

nome="Gomes"
for i in nome:
    print(i.replace(i,"*"))


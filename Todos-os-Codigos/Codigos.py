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


sera=bool(input("Digite ou não Digite: ").replace("Não",""))
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

# Caixa alta ou caixa baixa e remoção de espaços 

Tab=(input("Qual o seu nome: ").upper()) #caixa Alta
print(Tab)

Tab=(input("Qual o seu nome: ").lower()) #caixa Baixa
print(Tab)

Tab=(input("Qual o seu nome: ").strip()) #Remove os espaços a mais
print(Tab)

#------------------------------------- if e else -------------------------------------

if 10 > 5:  # Se 10 for maior que 5
    print("10 é maior que 5")  # Imprime se a condição for verdadeira
else:  # Se a condição for falsa
    print("10 não é maior que 5")  # Imprime se a condição for
# falsa

print('compriu a condição') if 10 > 5 else print('não cumpriu a condição')  # Usando o operador ternário



#------------------------------------ laço de repetição --------------------------------------

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

# Verificaçao de operadores

def ver():
    while True:
        prosseguir = input("Deseja continuar? (s/n): ").strip().lower()
        if prosseguir == 's' or prosseguir == 'n':
            break
        else:
            print("Opção inválida.")
    match prosseguir:
        case 'n':
            break


# Laços com FOR 

nome = "Gomes"
for i in nome:                      # 'for' define o nome da variavel que vai ficar dentro dela; e 'in' pega os valores
    print(i.replace(i,"*"))


#----------------------------------------------------- Bibliotecas-------------------------------------------------------

# *********** Importar Bibliotecas

import os                           # Deve -se colocar import Nome_da_Biblioteca
from os import system               # Usa-se o from para importar algo especifico de alguma biblioteca sem importar ela inteira
from os import system as console    # Usa-se o as para substittuir o nome do objeto de importação

# ********** Principais Bibliotecas

system                              #importa funçoes de console no código mais usado para debug


#------------------------------- Biblioteca ----------------

import              # importa uma biblioteca 
from import         # importa algo especifico da biblioteca
from import as      # importa algo especifico da biblioteca e modifica o nome dela

# principais bibliotecas e funções

import time         # funções de tempo
import random       # importa funções de aleatoriedade
import os           # importa funções de controle do console e do sistema
import json         # importa funções de chaves de acesso com valores dentro como lista

# time

time.sleep(5)       # define o tempo para finalizar o programa a partir dela
time.perf_counter() # Usado para ver quanto tempo o comando usa do inicio até o final

# random
lista = []
random.randint(1,100,10)                                # Ele vai gerar um numero de 1 á 100 e vai pular de 10 em 10
random.uniform(2.4,5.9)                                 # Gera um ponto uniforme entre eles
random.choice('banana', 'abacaxi', 'maça')              # Sorteia um nome dentro dele
random.choices(['banana', 'abacaxi', 'maça'], k=3)      # Sorteia um nome dentro dele com uma quantidade de uma vez k=
random.sample(range(1, 10), 3)                          # sorteia k numeros dentro de um paremetro EX: entre 1 á 10 k=3 (2,5,4)
random.shuffle(lista)                                   # Embaralha uma lista
random.randrange(1, 10, 2)                              # Sorteia numeros dentro dos paremetron

# os

os.getcwd()                     # Retorna o diretório de trabalho atual
os.chdir()                      # Altera o diretório de trabalho
os.listdir()                    # Lista os arquivos e pastas em um diretório
os.remove()                     # Remove um arquivo
os.rename('antigo', 'novo')     # Renomeia ou move um arquivo
os.path.exists()                # Verifica se um caminho existe
os.name                         # Retorna o nome do sistema operacional
os.system                       # Execulta comando dieretamente no terminal
os.mkdir()                      # Cria um novo diretorio
os.rmdir()                      # Remove um diretorio vazio
EncodingWarning

# OS - gerenciamento de arquivos

def Manager():
    with open(fr'Diretorio/{nome_do_arquivo}.tipo de arquivo (.txt;.json;.pdf)', 'tipo de operação CRUD (w,c,r)', enconding='utf-8') as f:

                                                            # encodint 'utf-8' refere-se ao layout de texto, tipo abnt2; e o 'as f:' refere-se ao nome dado a toda a operação
        f.write('Texto que deseja escrever no arquivo')     # 'w' escreve no arquivo, 'r' lê o arquivo, 'a' adiciona ao final do arquivo
        f.read()                                            # Lê o arquivo
        f.close()                                           # Fecha o arquivo após a operação

        


# json

# Pode se usar o nome: gui --> chave : porta que a chave abre
# 
with open(f'{arquivo}.json', 'r', encoding="utf-8") as f:
            dados = json.load(f)
print(f"{dados['nome']} - {dados['idade']} anos")     #  Imprime o nome e a idade de cada dado no arquivo JSON

#------------------------------ Lista ------------------------------

lista = [1,2,3,4,5,6,7,8,9,10]        # Definir o nome da lista e os intens que tem dentro dela
print(lista)                          # Imprimir os inntens da lista
print(random.choices(lista, k=3))     # Imprime k=3 nome aleatorio da lista 
lista.append(11)                      # adiciona um objeto na lista na ultima possição Ex: 11
lista.copy                            # Ele copia uma lista
lista.pop                             # Recorta o objeto (copia e deleta da lista)
lista.remove                          # Ele remove um objeto da lista
lista.reverse                         # Ele inverte os dados da lista 
lista.sort                            # Ele organiza a lista (Alfabeticamente, numericamente, ...)
lista.insert                          # Insere um valor em uma possição especifica na lista

# ----------------------------------------------------- Json --------------------------------------------------------





# -------------------------------------------------- Swicht Case ----------------------------------------------------

nome = input('Digite um nome')
match nome:
    case 'joao':
        print('joaozinho')
    case 'cleber':
        print('clebinho')
    case _:                                         # Usa-se o _: para ele usar caso nenhuma das opções anteriores forem validas
        print('nome sem zinho')



# -------------------------------------------------- Verificação de erro ----------------------------------------------------
try:
    print()
except Exception as e:                                      # A função Exception relata o erro ocorrido no codigo
            print(f"Erro ao gravar o arquivo: {e}")

# -------------------------------------------------- lambda ----------------------------------------------------

# função de Linha porsso dar o valor de uma linha

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
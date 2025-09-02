# Bibliotecas
import os
import json
import time

# Lista
Contas = {
    'Nome' : [],
    'CPF' : [],
    'Data' : [],
    'Dinheiro' : [],
    'Senha': []
}
                                                                                                                # Contas["Chave"].append(variavel)          Adicionar
                                                                                                                # i = Contas['Chave'].index(variavel)       Verifica o cpf
                                                                                                                # del(Contas["Chave"][i])                   Deleta a chave

# lambda

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Variaveis Globais
opcao = int

# Funções
def inicio():
    while True:
        try:
            print(20*'-','BANCO',20*'-')
            opcao = int(input('1 | Cadastrar Conta\n2 | Entrar na conta\n'))
            if opcao >= 3:
                print('Digite um numero valido')       
                time.sleep(1)
                limpar()
                continue
            match opcao:
                case 1:
                    limpar()
                    return 1
                case 2:
                    limpar()
                    return 2
            return opcao
        except Exception:
            print('Digite um numero válido')
            limpar()

def criar():

    while True:
        if inicio == 1:
            n = input('Digite o nome completo: ').title()
            dt = input('Digite a data de nascimento: ').replace(' ', '/')                                               
            cpf = input('Digite o CPF: ').replace(' ', '-')
            email = input('Digite o email: ').lower()
            dindin = 0.0
            Contas["Nome"].append(n)
            Contas["CPF"].append(cpf)
            Contas["Data"].append(dt)
            Contas["Email"].append(email)
            while True:
                senha = input('Digite a senha para a conta: ')
                senha2 = input('Digite a senha novamente: ')
                if senha != senha2:
                    limpar()
                    print('As senhas não coencidem tente novamente')
                    continue
                Contas["Senha"].append(senha)
            


def gravar():

    ...

def acesso():
    ...

def debitar():

    ...

def creditar():

    ...

def exlucao():

    ...


print(inicio())
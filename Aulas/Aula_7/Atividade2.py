# Bibliotecas
import os
import json
import time

# Lista
Contas = {
    'Nome' : [],
    'CPF' : [],
    'Data' : [],
    'Email' : [],
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
            limpar()
            print(20*'-','BANCO',20*'-')
            opcao = int(input('1 | Cadastrar Conta\n2 | Entrar na conta\n'))
            match opcao:
                case 1:
                    return 1
                case 2:
                    return 2
                case _:
                    print('Digite um numero válido')
                    time.sleep(1)
                    continue       
            return opcao
        except Exception:
            print('Digite um numero válido')
            time.sleep(1)

def criar():

    while True:
        n = input('Digite o nome completo: ').title()
        dt = input('Digite a data de nascimento: ').replace(' ', '/')                                               
        cpf = input('Digite o CPF: ').replace(' ', '-')
        email = input('Digite o email: ').lower()
        dindin = 0.0
        
        Contas["Nome"].append(n)
        Contas["CPF"].append(cpf)
        Contas["Data"].append(dt)
        Contas["Email"].append(email)
        Contas["Dinheiro"].append(dindin)
        while True:
            senha = input('Digite a senha para a conta: ')
            senha2 = input('Digite a senha novamente: ')
            if senha != senha2:
                limpar()
                print('As senhas não coencidem tente novamente')
                continue
            Contas["Senha"].append(senha)
            break
        break
        
def gravar():
    with open(fr'Aulas/Aula_7/Banco.json', 'r') as adicao:
        dados = json.load(adicao)
        json.dump(Contas, adicao, indent=2, ensure_ascii=False) 
    dados["Nome"].extend(Contas["Nome"])
    dados["CPF"].extend(Contas["CPF"])
    dados["Data"].extend(Contas["Data"])
    dados["Email"].extend(Contas["Email"])
    dados["Dinheiro"].extend(Contas["Dinheiro"])
    dados["Senha"].extend(Contas["Senha"])                   
    with open(fr'Aulas/Aula_7/Banco.json', 'w') as adicao:
        json.dump(Contas, adicao, indent=2, ensure_ascii=False)
    for i in Contas:
        Contas[i].clear()
def acesso():
    while True:
        limpar()
        cpf = input('Digite o seu CPF: ').replace(' ', '-')
        senha = input('Digite a sua senha: ')
        with open('Aulas/Aula_7/Banco.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)


        if cpf in dados.get('CPF', []):                                         #FIXME
            i = dados['CPF'].index(cpf)
            if senha == dados['Senha'][i]:
                print(f"{'-'*20} USUÁRIO ENCONTRADO {'-'*20}")
                print(f"Nome: {dados['Nome'][i]}")
                print(f"Data de Nascimento: {dados['Data'][i]}")
                print(f"Email: {dados['Email'][i]}")
                print(f"Dinheiro: {dados['Dinheiro'][i]}")
                print(f"CPF: {dados['CPF'][i]}")
                input('')
                return i
            else:
                print('Senha incorreta, tente novamente')
                time.sleep(1)
                continue
        else:
            print('CPF não encontrado, tente novamente')
            time.sleep(1)
            continue

def debitar():

    ...

def creditar():

    ...

def exlucao():

    ...
def Banco():

    ini = inicio()
    match ini:
        case 1:
            criar()
            input(Contas)
            gravar()
        case 2:
            acesso()






Banco()
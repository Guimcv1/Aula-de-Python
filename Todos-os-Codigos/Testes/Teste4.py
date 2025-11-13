# ---------------------------------------- Bibliotecas ----------------------------------------

from os import system as console
import time
import json

# ideia: pegar e adicionar uma chave a um .json existente se ouver, se não ouver crie um

<<<<<<< HEAD
'''def diciona():
=======
def diciona():
>>>>>>> 675609c1e16924cdcfc59caa3ded69266d767794
    dicionario = []
    while True:
        nome_adicao = input('Digite o nome da lista que deseja dicionar: ')
        console('cls')
        nome_lista = input('Digite o nome do arquivo: ')
        console('cls')
        try:
            with open(fr'Todos-os-Codigos/Testes/{nome_lista}.json', 'r') as lista:
        except Exception:
            resul = input('Arquivo não encontrado, deseja criar um novo: ').lower().replace('sim', 's')
            if resul == 's':
                novo_arquivo = input('Digite o nome do arquivo: ').strip().lower()
                with open(fr'Todos-os-Codigos/Testes/{novo_arquivo}', 'w') as new_lista:
                    json.dump(dicionario, novo_arquivo, ensure_ascii=False, indent = 2)
<<<<<<< HEAD
'''
import os
import json
import time

# Estrutura inicial
Contas = {
    'Nome': [],
    'CPF': [],
    'Data': [],
    'Email': [],
    'Dinheiro': [],
    'Senha': []
}

# Função para limpar tela
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Carregar dados do JSON (se existir)
def carregar():
    global Contas
    if os.path.exists('Aulas/Aula_7/Banco.json'):
        with open('Aulas/Aula_7/Banco.json', 'r', encoding='utf-8') as f:
            Contas = json.load(f)

# Gravar dados no JSON
def gravar():
    with open('Aulas/Aula_7/Banco.json', 'w', encoding='utf-8') as f:
        json.dump(Contas, f, indent=2, ensure_ascii=False)

# Menu inicial
def inicio():
    while True:
        try:
            limpar()
            print(20*'-','BANCO',20*'-')
            opcao = int(input('1 | Cadastrar Conta\n2 | Entrar na conta\n'))
            if opcao in [1,2]:
                return opcao
            else:
                print('Digite um número válido!')
                time.sleep(1)
        except:
            print('Digite um número válido!')
            time.sleep(1)

# Criar conta
def criar():
    carregar()
    n = input('Digite o nome completo: ').title()
    dt = input('Digite a data de nascimento (dd/mm/aaaa): ')
    cpf = input('Digite o CPF: ').replace(' ', '')
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
            print('As senhas não coincidem, tente novamente')
        else:
            Contas["Senha"].append(senha)
            break

    gravar()
    print('Conta criada com sucesso!')
    time.sleep(2)

# Acesso
def acesso():
    carregar()
    while True:
        limpar()
        cpf = input('Digite o seu CPF: ').replace(' ', '')
        senha = input('Digite a sua senha: ')
        
        if cpf in Contas['CPF']:
            i = Contas['CPF'].index(cpf)
            if senha == Contas['Senha'][i]:
                print(f"{'-'*20} USUÁRIO ENCONTRADO {'-'*20}")
                print(f"Nome: {Contas['Nome'][i]}")
                print(f"Data de Nascimento: {Contas['Data'][i]}")
                print(f"Email: {Contas['Email'][i]}")
                print(f"Dinheiro: R$ {Contas['Dinheiro'][i]:.2f}")
                print(f"CPF: {Contas['CPF'][i]}")
                input('Pressione Enter para continuar...')
                return i
            else:
                print('Senha incorreta, tente novamente')
        else:
            print('CPF não encontrado, tente novamente')
        time.sleep(1)

# Programa principal
def Banco():
    ini = inicio()
    if ini == 1:
        criar()
    elif ini == 2:
        acesso()

Banco()
=======



diciona()
>>>>>>> 675609c1e16924cdcfc59caa3ded69266d767794

import os
import json
import time

# Arquivo onde vamos salvar os dados
ARQUIVO = "Aulas/Aula_7/Banco.json"

# Função para limpar tela
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')


# --------------------------------------------------------------------
# Funções de apoio
# --------------------------------------------------------------------

def carregar():                                                     # Ler os arquivos
    """Carrega as contas do arquivo JSON."""
    if os.path.exists(ARQUIVO):                                     # Verifica se o arquivo existe 
        with open(ARQUIVO, "r", encoding="utf-8") as f:             # Abre o arquivo no modo de leitura
            try:
                return json.load(f)                                 # Retorna o valor os dados que etsão no .json
            except json.JSONDecodeError:                            # Retorna Vazio caso o arquivo não tenha nada ou ele não exista
                return []
    return []


def gravar(dados):                                                  # Grava os arquivos
    """Grava todas as contas no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:                 # Abre o arquivo no modo de escrita
        json.dump(dados, f, indent=2, ensure_ascii=False)           # Insere os dados dentro do .json


# --------------------------------------------------------------------
# Funções principais
# --------------------------------------------------------------------

def inicio():                                                       # Seleção de contas
    """Menu inicial."""
    while True:
        try:
            limpar()
            print(20*"-", "BANCO", 20*"-")
            opcao = int(input("1 | Cadastrar Conta\n2 | Entrar na Conta\n3 | Sair\n"))
            if opcao in [1, 2, 3]:                                  #  verifica se foi selecionado uma opção válida
                return opcao
            else:
                print("Digite um número válido")
                time.sleep(1)
        except ValueError:
            print("Digite um número válido")
            time.sleep(1)


def criar():                                                        # Cria um novo perfil
    """Cria uma nova conta."""
    dados = carregar()

    n = input("Digite o nome completo: ").title()
    dt = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF: ").replace(" ", "")
    email = input("Digite o email: ").lower()

    # Evita CPF duplicado
    if any(conta["CPF"] == cpf for conta in dados):                 # any() Retorna Verdadeiro se pelo menos 1 elemento estiver verdadeiro
        print("Já existe uma conta com esse CPF!")                  # Compara o CPF informado com o CPF de cada conta já cadastrada.
        time.sleep(2)
        return

    while True:
        senha = input("Digite a senha para a conta: ")
        senha2 = input("Digite a senha novamente: ")
        if senha != senha2:
            print("As senhas não coincidem, tente novamente")
        else:
            break

    nova_conta = {
        "Nome": n,
        "CPF": cpf,
        "Data": dt,
        "Email": email,
        "Dinheiro": 0.0,
        "Senha": senha
    }

    dados.append(nova_conta)
    gravar(dados)

    print("Conta criada com sucesso!")
    time.sleep(2)


def acesso():
    """Acessa uma conta existente."""
    dados = carregar()
    if not dados:
        print("Nenhuma conta cadastrada ainda.")
        time.sleep(2)
        return None

    while True:
        limpar()
        cpf = input("Digite o seu CPF: ").replace(" ", "")
        senha = input("Digite a sua senha: ")

        conta = next((c for c in dados if c["CPF"] == cpf), None)

        if conta:
            if senha == conta["Senha"]:
                print(f"{'-'*20} USUÁRIO ENCONTRADO {'-'*20}")
                print(f"Nome: {conta['Nome']}")
                print(f"Data de Nascimento: {conta['Data']}")
                print(f"Email: {conta['Email']}")
                print(f"Dinheiro: R$ {conta['Dinheiro']:.2f}")
                print(f"CPF: {conta['CPF']}")
                input("Pressione Enter para continuar...")
                return conta  # retorna o dicionário da conta
            else:
                print("Senha incorreta, tente novamente")
        else:
            print("CPF não encontrado, tente novamente")

        time.sleep(1)


def debitar(conta):
    """Debita um valor da conta."""
    try:
        valor = float(input("Digite o valor para sacar: R$ "))
        if valor <= 0:
            print("Valor inválido!")
        elif valor > conta["Dinheiro"]:
            print("Saldo insuficiente!")
        else:
            conta["Dinheiro"] -= valor
            print(f"Saque realizado! Saldo atual: R$ {conta['Dinheiro']:.2f}")
            atualizar_conta(conta)
    except ValueError:
        print("Digite um número válido.")
    time.sleep(2)


def creditar(conta):
    """Credita um valor na conta."""
    try:
        valor = float(input("Digite o valor para depositar: R$ "))
        if valor <= 0:
            print("Valor inválido!")
        else:
            conta["Dinheiro"] += valor
            print(f"Depósito realizado! Saldo atual: R$ {conta['Dinheiro']:.2f}")
            atualizar_conta(conta)
    except ValueError:
        print("Digite um número válido.")
    time.sleep(2)


def excluir(conta):
    """Exclui a conta do banco."""
    dados = carregar()
    dados = [c for c in dados if c["CPF"] != conta["CPF"]]
    gravar(dados)
    print("Conta excluída com sucesso!")
    time.sleep(2)


def atualizar_conta(conta):
    """Atualiza os dados de uma conta no arquivo."""
    dados = carregar()
    for i, c in enumerate(dados):
        if c["CPF"] == conta["CPF"]:
            dados[i] = conta
            break
    gravar(dados)


def menu_conta(conta):
    """Menu depois do login."""
    while True:
        limpar()
        print(20*"-", "MENU CONTA", 20*"-")
        print("1 | Consultar saldo")
        print("2 | Depositar")
        print("3 | Sacar")
        print("4 | Excluir conta")
        print("5 | Sair")

        try:
            op = int(input("Escolha uma opção: "))
            if op == 1:
                print(f"Saldo atual: R$ {conta['Dinheiro']:.2f}")
                input("Pressione Enter para continuar...")
            elif op == 2:
                creditar(conta)
            elif op == 3:
                debitar(conta)
            elif op == 4:
                excluir(conta)
                break
            elif op == 5:
                break
            else:
                print("Opção inválida!")
                time.sleep(1)
        except ValueError:
            print("Digite um número válido")
            time.sleep(1)


def Banco():
    """Programa principal."""
    while True:
        ini = inicio()
        if ini == 1:
            criar()
        elif ini == 2:
            conta = acesso()
            if conta:
                menu_conta(conta)
        elif ini == 3:
            print("Saindo do banco...")
            break


# Executar
Banco()

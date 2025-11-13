def Banco():
    # Bibiliotecas
    import json
    import os
    import datetime
    # Função
    limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

    def user():
        # Entrada do usuário
        cpf = input('Digite o seu CPF: ')
        senha = input('Digite a sua senha: ')
        # Abre o arquivo JSON com os dados
        with open('Aulas/Aula_7/Banco.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)

        print(f"{'-'*20} USUÁRIO ENCONTRADO {'-'*20}")
        print(f"{dados.get('Nome')}")
        print(f"{dados.get('Data')}")
        print(f"{dados.get('Email')}")
        print(f"{dados.get('Money')}")
        print(f"{dados.get('Conta')}")
        input('')

    while True:
        limpar()    
        print('Bem vindo ao Banco')
        print('Qual operação deseja fazer?')
        opcao = int(input('1 | Cadastrar\n2 | Entrar na conta\n'))
        def op():
            match opcao:
                case 1:
                    n = input('Digite o nome completo: ').title()
                    dt = input('Digite a data de nascimento: ').replace(' ', '/')                                               
                    cpf = input('Digite o CPF: ').replace(' ', '-')
                    email = input('Digite o email: ').lower()
                    dindin = 0.0
                    limpar()
                    while True:
                        senha = input('Digite a senha para a conta: ')
                        senha2 = input('Digite a senha novamente: ')
                        if senha != senha2:
                            limpar()
                            print('As senhas não coencidem tente novamente')
                            continue
                        dados_pessoais = {}
                        dados_pessoais[cpf] = {
                        'Senha': senha,
                        'Nome': n,
                        'Data': dt,
                        'Email': email,
                        'Money': dindin
                                            }
                        with open(fr'Aulas/Aula_7/Banco.json', 'w') as adicao:
                            json.dump(dados_pessoais, adicao, indent=2)             # dump(nome a ser adicionado, banco a ser adicionado, e tabeamento)
                        break
                case 2:
                    user()
                    '''
            if numero in contas:
                contas[numero]['saldo'] += dindin
                    '''
        op()
    
Banco()




# Usar como lista

nome = dict(json.load(arquivo))
json.dump(logins, escrever, indent=2)

def jsom():
    
    import os
    import json

    usuarios = []
    novo_arquivo = ''
    limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        limpar()
        usuario = {}                                                # Toda vez que o programa iniciar ele ira reiniciar o dicionario
        print('1 | Cadastrar novo usuario.')
        print('2 | Salvar arquivo JSON.')
        print('3 | Fazer leitura JSON.')
        print('4 | Sair do sistema.')

        opcao = input('Informe a opção desejada:')
        limpar()
<<<<<<< HEAD
        
=======

>>>>>>> 675609c1e16924cdcfc59caa3ded69266d767794
        match opcao:
            case '1':
                usuario["nome"] = input('Informe o nome: ').strip().title()         # Chave dentro do dicionario usuario e o .title() deixa a primeira como maiuscula e o resto como minusculo
                usuario['idade'] = input('Informe a idade: ').strip()               # Chave dentro do dicionario usuario
                usuario['email'] = input('Digite o email: ').strip().lower()        # Chave dentro do dicionario usuario
                usuarios.append(usuario)
                limpar()
                print('Ususario cadastrado com sucesso!')
            case '2':
                novo_arquivo = input('Informe o nome do arquivo: ').strip().lower()
                if novo_arquivo:
                    with open(fr'Aulas/Aula_6/{novo_arquivo}.json', 'r', encoding = 'utf-8') as f:
                        dados_existentes = json.load(f)   
<<<<<<< HEAD
                dados_existentes.extend(usuarios)                                   # Pega todos os dados de uma lista e coloca no final de outra lista
=======
                dados_existentes.extend(usuarios)       
>>>>>>> 675609c1e16924cdcfc59caa3ded69266d767794

                with open(fr'Aulas/Aula_6/{novo_arquivo}.json', 'w', encoding = 'utf-8') as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)            # ensure_ascii=False --> fala que não está dentro da norma culta inglesa
                    limpar()
                    print('Arquivo JSON salvado com sucesso!')
                    continue
            case '3':
                if not novo_arquivo:
                    novo_arquivo = input('Digite o nome do arquivo: ').strip().lower()
                with open(fr'Aulas/Aula_6/{novo_arquivo}.json', 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                print(f'{'-'*20} USUARIOS {'-'*20} ')
                input('')
<<<<<<< HEAD
                for usuario in dados:
=======
                for usario in dados:
>>>>>>> 675609c1e16924cdcfc59caa3ded69266d767794
                    for chave in usuario:
                        print(f'{chave().capitalize()}: {usuario.get(chave)}')
                        input('')
                    print(40*"-")
                continue
            case '4':
                print('Saindo do Sistema!')
                break
            case _:
                print('Opção invalida!')
                input('')
                continue


def dicionario():
    #dicionario
    usuario = {                                 # Lista dicionario
        'nome' : 'Gomes',
        'idade' : 26
    }
    usuarios = ['gomes', 'nunes', 'cris']       # Apenas lista
    print(type(usuario))
    print(usuario)
    def dif():
        print(f'Nome: {usuario['nome']}')
        print(f'Idade: {usuario['idade']}')
    print(f'Nome: {usuario[0]}')                # indice 0

    print(f'Nome {usuario.get('nome')}')        # ler a lista


def app2():
    
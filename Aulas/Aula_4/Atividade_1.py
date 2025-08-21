def Atividade1():
    from os import system as console
    import time
    lista = []
    ativo = True
    while ativo == True:
        console('cls')
        print('Qual operação deseja iniciar?\n1 - Adicionar nome\n2 - Remover nome\n3 - Procurar nome')
        decisao=int(input(""))
        if decisao == 1:
            while True:
                console('cls')
                nome=input("Qual nome deseja adicionar?\n")
                if nome == "":
                    break
                else:
                    lista.append(nome)
                    print(lista)
                    time.sleep(1)
        if decisao == 2:
            while True:
                console('cls')
                nome=input('Qual nome deseja remover?\n')
                if nome == '':
                    break
                else:
                    lista.remove(nome)
                    print(lista)
                    time.sleep(1)
        if decisao == 3:
            while True:
                console('cls')
                nome=input('Qual nome deseja procurar?\n')
                if nome == '':
                    break
                elif nome in lista: # Procurar algo especifico em uma lista
                    print(nome, 'Foi encontrado na lista')
                    input('')
                else:
                    print(f'{nome} nome não encontrado.')
                    print(lista)
                    time.sleep(1)
                
            
Atividade1()
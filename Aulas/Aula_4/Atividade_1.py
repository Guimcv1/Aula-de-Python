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
def Atividade2():
    import time
    from os import system as console
    lista=[]
    print(30*'-','Bem vindo ao oirganizador',30*'-')
    while True:
        numero=str(input('Digite o Numero:\n').replace(',','.'))
        console('cls')
        if numero == '':
            decisao=input('Deseje imprimir a lista numerica organinzada?\n').upper().replace('SIM', '').replace('S','')
            print(decisao)
            decisao = bool(decisao)
            print(type(decisao))
            console('cls')
            if decisao == False:
                lista.sort()
                print(lista)
                d=input('Deseja adicionar mais numeros?\n').upper().replace('SIM','').replace('S','')
                d = bool(d)
                if d == False:
                    continue
                else:
                    break
            else:
                continue
        else:
            numero = float(numero)
            lista.append(numero)
            numero = str(numero)
            continue
def Atividade3():
    import time
    from os import system as console
    print(30*'-','Bem vindo ao calculador de média',30*'-')
    lista = []
    vez = -1
    while True:
        console('cls')
        nota = input('Digite a Nota: ')
        lista.append(nota)
        vez += 1
        if nota == '':
            lista.pop()
            lista_t =[]
            for x in lista:
                lista_t.append(int(x))
            print(lista_t)
            result = (sum(lista_t)/vez)
            print('A média da sua nota é: ',result)
            if result >= 7:
                print('Você passou de Ano')
                input('')
            else:
                print("Você reprovou de Ano")
                input('')
        else:
            continue
        
    
Atividade3()
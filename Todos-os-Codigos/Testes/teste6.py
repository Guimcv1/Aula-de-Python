import os
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def crip():
    limpar()
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç','$','!','@','#','%']
    numeros = [i for i in range(36,80)]
    lista = []
    lista2 = []
    numeros.reverse()
    var = input('Digite algo: ')

    for i in var:
        if i in alfabeto:
            lista = alfabeto.index(i)
            lista2.append(numeros[lista])
    print(*lista2, sep='')

def des():
    lista2 = []
    alfabeto =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç','$','!','@','#','%']
    numero = [str(i) for i in range(36,80)]
    conplat =[]
    espaco = ' '
    while True:
        conp = input('Digite o arquivo criptografado\n')
        if conp == "":
            break
        else:
            conplat.append(conp)

    #numero.reverse()

    for i in conplat: 
        if i in numero:
            numero.reverse()
            lista = numero.index(i)
            lista2 = espaco.join([conplat[i:i+2] for i in range(0, len(conplat), 2)]) 
            lista2.append(alfabeto[lista])
            
    print(*lista2)
crip()
des()
    
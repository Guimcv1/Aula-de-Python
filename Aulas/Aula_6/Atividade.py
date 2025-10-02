# Crie uma lista com 10 números e exiba a lista com o dobro de cada um dos numero.

# Q - 6

def Questao6():
    lista=[]
    var = 0
    while var <= 10:
        num=int(input('Digite um numero: '))
        num2 = num * 2
        var += 1
        lista.append(num2)
        continue
    print(lista)


# Solicite dois números e verifique se o segundo é menor que o primeiro.

# Q - 7

def Questao7():
    while True:
        num1 = input('Digite o primeiro numero: ').strip()
        num2 = input('Digite o segundo numero: ').strip()
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            input('Digite um numero Valido')
            continue

        num1 = int(num1)
        num2 = int(num2)
        
        if num1 > num2:
            input(f'O numero {num1} é maior que o numero {num2}')
        elif num2 > num1:
            input(f'O numero {num2} é maior que o numero {num1}')
        elif num1 == num2:
            input("Os números são iguais")
        else:
            input('Digite um número váldo')
            continue

# Solicite o nome e sobrenome de dois usuários e imprima o nome do primeiro com o sobrenome do segundo e o nome do segundo com o sobrenome do primeiro.

# Q - 8

def Questao8():
    nome1 = input("Digite o primeiro nome (sem o sobrenome): ").title()
    sobre1 = input('Digite o sobrenome: ').title()
    nome2 = input("Digite o outro nome (sem o sobrenome): ").title()
    sobre2 = input('Digite o sobrenome: ').title()

    print(f'Nome: {nome1} {sobre2}')
    print(f'Nome: {nome2} {sobre1}')


# Peça um número e exiba a metade dele.

#Q - 9

def Questao9():
    num=input('Digite um número: ')
    num = int(num)
    print(f'A metade de {num} é: {num/2}')

# Solicite a altura e a largura de um retângulo e exiba a área.

# Q - 10

def Questao10():
    altura=int(input('Digite a altura do triangulo: '))
    largura=int(input('Digite a largura do triangulo: '))
    area = (altura*largura)/2
    print(f'A área do Triangulo é: {area}')


altura=float(input('Digite a altura do triangulo: ').replace(',','.'))
largura=float(input('Digite a largura do triangulo: ').replace(',','.'))
area = (altura*largura)/2
<<<<<<< HEAD
print(f'A área do Triangulo é: {area}')
=======
print(f'A área do Triangulo é: {area}')

>>>>>>> 675609c1e16924cdcfc59caa3ded69266d767794

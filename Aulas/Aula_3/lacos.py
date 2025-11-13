#-------------------------------- laço de repetição --------------------------------

#declaração de variavel


#loop
def Loop():
    numero:int=100
    while numero >= 0:
        print(numero*"*")
        numero -= 1


#Break - Quebra o loop mesmo que as condições estejam sendo atendidas
def Break():
    cont = 0
    while cont < 15:
        cont+= 1
        if cont % 2 == 0:
            print(cont)
        elif cont >=7:
            break
        else:
            continue

# FOR - Laço de repetição com numero de repetições definidos
def FOR():
    for n in range(5):
        print(n)

# Atividade - Triangulo Retangulo

def Triangulo():
    Base=(int(input("Digite um Numero: ")))
    at:int=1
    
    while Base != 0:
        if Base != 0:
            print(Base*"* ")
            Base -= 1

            if Base == 0:
                print('Triangulo retangulo pronto!')
        
def triangulo():
    Base=(int(input("Digite um Numero: ")))
    print()
    num:int = 0
    
    while Base != num:
        if Base != num:
            num += 1
            print(num*"* ")

            if num == Base:
                print("\n",30*"-",'Triangulo retangulo pronto!',30*"-","\n")
                break

# tem q pegar o numero e somar 1 até ficar igual a base

def Arvore_de_Natal():

    i=1
    linha = 15

    while i <= linha:
        espacos = linha - i
        estrelas:int = 2 * i - 1
        print(' ' * espacos + "^" * estrelas)
        i += 1



def Senhas():
    erro = 1
    while erro == 1:
        erro = 0    
        senha=(str(input("Qual a senha: ")))
        senha2=(str(input("Repita a senha: ")))

        while senha != senha2:
                if senha != senha2:
                    print("As senhas não coincidem, tente novamente. ")
                    erro = 1
                    break 
                else:
                    return senha
                
def Login2():
    user1=(input("Digite o nome do Usuario: "))
    return user1

def Login3():
    senha3=(input("Digite a Senha: "))
    return senha3


def sistema_de_Login():
    erro:int=1
    print(20*"-", 'Bem Vindo ao Sistema de Registro',20*"-" )
    while erro == 1:
        erro = 0
        user=(str(input("Qual nome de usuario: ")))
        while user == "":
            if user == "":
                print(30*"*","Digite um Nome Válido",30*"*")
                erro = 1 
                break
        else:        
            Senhas()       
            print(30*"-","informações Pessoais",30*"-","\n")
            dt=(input('Qual a sua data de nascimento: '))
            nome=(input('Digite o seu Nome completo: '))
            email=(input('Digite o seu Email: '))
            print()
            print(50*"*",'Reiniciando o Sistema',50*"*")
            print()
            print(40*"-","Login",40*"-")
            print()
            print(30*"_","Bem Vindo ao Sistema de Login",30*"_")
            Login2()
            Login3()
            while (Login3 != user) or (Senhas != Login2): 
                print("Usuario ou senha incorreto")
            def Login2():
                user1=(input("Digite o nome do Usuario: "))
                senha3=(input("Digite a Senha: "))
                erro=0

                                                                           
                
            print(f"Bem Vindo {nome}")
            print(f"Data de Nascimento: {dt}")
            print(f"Email: {email}")

sistema_de_Login()
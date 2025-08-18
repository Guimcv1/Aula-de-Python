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
            pass
    
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
            print(30*"-","informações Pessoais",30*"-","\n")
            dt=(input('Qual a sua data de nascimento?\n = '))
            nome=(input('Digite o seu Nome completo: '))
            email=(input('Digite o seu Email: \n'))
            print(50*"*",'Reiniciando o Sistema',50*"*")
            print()
            print(40*"-","Login",40*"-")
            print(30*"_","Bem Vindo ao Sistema de Login",30*"_")
            user1=(input("Digite o nome do Usuario: "))
            senha3=(input("Digite a Senha: "))
            erro=1
            while erro == 1:
                if (user1 != user) or (senha != senha3):
                    print("Usuario ou senha incorreto")
                    break                                                               #FIXME
                else:
                    pass
            print(f"Bem Vindo {nome}")
            print(f"Data de Nascimento: {dt}")
            print(f"Email: {email}")
        

  z  

sistema_de_Login()
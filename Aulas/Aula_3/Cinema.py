
print()
print(40*"-", "Bem vindo",40*"-")
print()
Idade=int(input("Digite a sua idade: "))
cont = 1
erro = 1
while erro == 1:
    erro = 0
    print(36*"-","Catálogo do Cinema", 36*"-", "\n")
    print(40*"*","Filmes +18 ",40*"*")
    print("1 | Corra que a policia Vem ai")
    print("2 | Os caras Malvados 2","")
    print(40*"*","Filmes Livres ",40*"*","")
    print("3 | F1 o filme")
    print("4 | Flow")
    print("5 | Quarteto Fantastico")
    print("6 | Interestelar","\n")
    filme=int(input("Selecione um filme: "))
    erro = 1
    tipo=(input("Filme 3D (SIM/NÃO)\n").upper())
    if tipo == "SIM":
        valor = 40.0
    else:
        valor = 22.0
    if filme <= 2 and Idade < 18 or filme > 6:
        while filme <= 2 and Idade < 18 or filme > 6:
            erro = 1
            if filme > 6:
                print("Selecione um filme Existente")
                erro = 1
                break
            else:
                if filme <= 2 and Idade < 18:
                    print("Filme Inapropriado para a idade, selecione outro filme\n")
                    erro = 1  
                    break
                else:
                    pass
    else:
            pass


            while cont == 1:
                print(30*"-","Salas disponiveis",30*"-")
                print("1 | Sala 1")
                print("2 | Sala 2 | Sala indisponivel!")
                print("3 | Sala 3")
                print("4 | Sala 4 | Sala indisponivel! ")
                print("5 | Sala 5")
                print("6 | Sala 6")
                sala=int(input(": "))
                if sala == 2 or sala == 4:
                    while sala == 2 or sala == 4:
                        if sala == 2 or sala == 4:
                            print("Sala indisponivel, Selecione outra!")
                            break
                        else:
                            cont = 0
                    else:
                        erro = 0
                        break
                else:
                    erro = 0
                    break

verific=(input("Deseja imprimir o seu tiket?\n").upper())
if filme == 1:
    filme = str("Corra que  a policia vem ai")
elif filme == 2:
    filme = str("Os caras Malvados 2")
elif filme == 3:
    filme = str("F1 o Filme")
elif filme == 4:
    filme = str("Flow")
elif filme == 5:
    filme = str("Quarteto Fantastico")
elif filme == 6:
    filme = str("Interestelar")

if verific == "SIM":
    print(30*"/","Tiket",30*"/")
    print("|","Cinema Sorocaba", 48*"_", "|")
    print(f"| Filme: {filme}", 44*"_", "|")
    print(f"| Sala: {sala}", 56*"_", "|")
    print(f"| Filme 3D: {tipo}", 53*"_", "|")
    print("|",64*" ","|")
    print("| Valor: R$", valor,49*"_","|")
    print(66*"/")
else:
    s=input("Deseja cancelar a compra?\n")
    if s == "sim":
        print(48*"-", " Operação Cancelada ", 48*"-")
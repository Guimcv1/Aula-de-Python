#------------------------------------ Atividade ------------------------------------

'''
    Problema: crie um sistem que calcule o indice de massa corporal(IMC) 
    do ussuario, mostre o valor do IMC na tela, e retorne se o ussuario 
    deve emagrecer ou engordar 
'''
def IMC_Calculadora():
    print(30*'*','Caulculadora de IMC', 30*'*')
    peso=(input('Digite o seu peso: ').replace(",","."))
    altura=(input('Digite a sua altura: ').replace(",","."))
    peso = float(peso)
    altura = float(altura)
    IMC = peso/(altura*altura)

    if IMC <= 18.5:
        print("Magreza - Engorde")
        print(f"Seu IMC é: {IMC:.1f}")
    elif IMC <= 24.9:
        print("Normal")
        print(f"Seu IMC é: {IMC:.1f}")
    elif IMC <= 29.9:
        print("Sobrepesso - Emagresa")
        print(f"Seu IMC é: {IMC:.1f}")
    elif IMC <= 39.9:
        print("Obesidade - Emagresa")
        print(f"Seu IMC é: {IMC:.1f}")
    else:
        print("Obesidade Grave - Emagresa")
        print(f"Seu IMC é: {IMC:.1f}")

'''
Problema 2: Um elevador de carga possui capacidade para 200kg.
Crie um programa que receba do usuario seu peso e o peso da carga 
e verifica se a carga está autorizada a usar o elevador ou não
'''
def Elevador():
    print('\n',40*'*','Balança do Elevador', 40*'*','\n')
    pessoa=float(input("Digite o Seu Peso: ").replace(",","."))
    carga=float(input('Digite o Peso da carga: ').replace(",","."))

    total=pessoa+carga

    if total > 200:
        print('\n',40*'-','Acima do Peso, Elevador inoperante',40*'-','\n')
    else:
        print('\n',40*'-',"Elevador Operante", 40*'-','\n')

Elevador()
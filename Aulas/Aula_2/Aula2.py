'''

dez : int
print("Oiiiiiiiiiiiiiii")
dez = input("Fala Galerinha:\n")
print (dez)

'''
'''
numero1 = float(input("digite o primeiro numer: "))
numero2 = float(input("digite o segundo numer: "))
print("a soma é: ", numero1 + numero2)

print("olaaaaaaaa","macarão",sep="")

#FIXME - contatenação com f-string

Nome:str = ""
Idade:float
Idade = float(input("achdsfbaihufchsdvc hcsdu8hdjksc9sghwyccgx iyschsvscsoucgsç"))
print(f'Olá, Meu nome é {type(Nome)} e tenho {Idade + 1} anos de idade')
print('O sabio sabia', end="")
print("dxosnvdçslnbvdjçdsnvidjvbjvnbvlkvosvvdffhv ds~vscdsçkvsdvspv\nuhsbvóxvdsvçdsfvisvsc~snvhshgspvdshsçslsnsdhvsmç", end="")
print("kdsnosdnvfdn dflvdfvjdfnvfdjvpdfkvlifvdfjvdf~dfihvdfjhvidfvdfj\nviydfhvçdfmlvdfvdfnvdfvhdfvlofdjdfvdfbvdf bdbndfojhdobhdfhodfi\njvosdcodhsigsdvhdshvsdoihv")

valor = 12.51654988

print(f'{valor:,.2f}')



print(30*"*")
heingh = input("digite o seu peso: ").replace(',','.')
heingh = float(heingh)
print(f'{heingh:.2f}'.replace('.',','))



#FIXME Atividade

print(50*"/")

Numero = int(input("digite o seu numero? \n"))
Peso = float(input("digite o seu peso? \n").replace(",","."))
Nome = str(input("digite o seu nome? \n"))
Cassado = bool(input('Você é casado? \n').replace("Sim","True").replace("Não",""))
print(f'O seu nome é: {Nome}, Seu peso é: {Peso}, o seu numero é: {Numero} e você é casado: {Cassado}')

print(50*"/")

print("O resultado da Primeira operação é:", 12+7)
print("O resultado da Segunda operação é:", 15%4)
print("O resultado da Terceira operação é:", 3**2)

print(50*"/")

print(50*"=")
input("Qual o Seu User Name?\n")
print(50*"=")
print(10*"*","Boas Vindas",10*"*",sep="")
print(50*"=")

print(50*"/")

N2 = str(input("digite o seu numero?\n"))
N2 = int(N2)
print("A soma desses numeros é :", N2 + 5)





#if e else

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

if idade >= 18 and idade <= 65:
    print("Você é maior de idade")
elif idade >= 65:
  print("Você é idoso")
else :
  print ("Você é menor de idade")


'''


#trinagulo retangulo
# Pegar o numero e começar do 1 e ir repetido até o numero for igual ao numero escolhido
print(80*"_")
print("Triangulo Retangulo")
print(80*"_")
Base = int(input("Digite o numero da base do retangulo: "))
print(80*"/")

def triangulo():
    at:int
    at = 1
    if at != Base:
        at=+1
        print(at*"*",'\n')

    elif at == Base:
        print('O seu triangulo está pronto')
    while at == Base:
        print()




#Operador Ternario
nome=input('qual o seu nome: ')
idade=input("qual a sua idade: ")
idade = int(idade)
print(nome,' é maior de idade' if idade >= 16 else ' é menor de idade')
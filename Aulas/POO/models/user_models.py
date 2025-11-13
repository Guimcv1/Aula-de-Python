class User:
    def __init__(self, nome, nivel, dinheiro=0):
        self.nome = nome
        self.nivel = nivel
        self.dinheiro = dinheiro
        if nivel == "Prata":
            dinheiro = 100
    
    # Definir comportamentos
    def comprar(self, dinheiro):
        i = int(input("Qual é o valor do produto: "))
        if i > dinheiro:
            print("Saldo insuficiente")
        dinheiro = dinheiro-i
        print("Produto comprado com sucesso!")
    
    def vender(self):
        i = int(input("Qual o valor do seu produto: "))
        a = input("Deseja vender o produto mesmo? (S/N)").upper().strip()
        if a == "S":
            self.dinheiro = self.dinheiro + i
            print("Venda efetuada com sucesso!")
        else:
            print("Compra cancelada")

Pessoa1 = User("Fernando", "Cobre")
Pessoa2 = User("Pedro", "Prata")

Pessoa2.vender()
print(Pessoa2.dinheiro)


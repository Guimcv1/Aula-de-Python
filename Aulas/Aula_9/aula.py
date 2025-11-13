# Classe - descrição de um formao geral que os objetos devem ter
# Atributos - as variaveis da clase, que são unicas para cada instancia dela (Caracteristicas do objeto)
# Métodos - Funções, as ações que os objetos devem realizar

#nome e vida - atacar
# self quando quero me referir a algum atributo da classe
# construtor - quando quero atacar algum objeto, chamo o atributo

# Atributos publicos podem ser acessado por outras classes
# Ecapsulamento - self._ protegido - self.__ privado
class Personagem:
    # construtor
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

    # definindo GET e SET 

    # definindo GET   
    @property
    def nome(self):
        return self.__nome
    
    # definindo SET
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, nova_vida):
        self.__vida = nova_vida

    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida, e agora esta com {personagem.vida}')

personagem1 = Personagem("Gandof",100)
print(f'Personagem: {personagem1.nome}')
print(f'Vida: {personagem1.vida}')

personagem2 = Personagem('Cleitinho do grau',250)
print(f'Personagem: {personagem2.nome}')
print(f'Vida: {personagem2.vida}')

class Guerreiro(Personagem):                        # Herança - Herdando de persongem
    def __init__(self, nome, vida, resistencia=10): # resistencia padrão de 10
        super().__init__(nome, vida)                # construtor da classe pai - o super() é uma função que chama os método do pai
        self.__resistencia = resistencia
    @property
    def resistencia(self):
        return self.__resistencia
    @resistencia.setter
    def resistencia(self, resistencia):
        self.__resistrencia = resistencia
    def atacar(self, personagem):                   # ira reescrever o (atacar) do pai
        personagem.vida -= 30
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida, e agora esta com {personagem.vida}')

    def protecao(self, personagem):
        self.__vida += 10

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    def curar(self, personagem):
        personagem.vida += 35
        print(f'{self.nome} usou poder de cura em {personagem.nome}')
        print(f'A vida de {personagem.nome} foi para {personagem.vida}')

vader = Mago('Darth Vader', 250)
jhonas = Guerreiro('jhonas', 250)
maginho = Mago('Patolino',500)

vader.atacar(jhonas)
jhonas.atacar(vader) 
maginho.curar(jhonas)


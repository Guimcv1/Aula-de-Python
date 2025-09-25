# jogo de RPG de um mago de fogo
import sys
import time
import os

clear = lambda: os.system( 'cls' if os.name == 'nt' else 'clear')


class Personagem:
    # construtor
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida
 
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, nova_vida):
        self.__vida = nova_vida

    def atacar(self, personagem):                   # ira reescrever o (atacar) do pai
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida, e agora esta com {personagem.vida}')

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
        personagem.vida -= 25
        print(f'{self.nome} atacou {personagem.nome} e tirou 25 pontos de vida, e agora esta com {personagem.vida}')

    def protecao(self, personagem):
        self.__vida += 10

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self._cura_usos = 0                         # Cura
        self._fireball_usos = 0                     # Bola de fogo
        self._lancagelo_usos = 0                    # Lança de gelo
        self._relampago_usos = 0                    # Relampago

    def curar(self, personagem):  # limite de 5 usos por personagem
        clear()
        if self._cura_usos < 5:
            self._cura_usos += 1
            personagem.vida += 60
            print(f'{self.nome} usou poder de cura em {personagem.nome}')
            print(f'A vida de {personagem.nome} foi para {personagem.vida}')
            print(f'Cura usada {self._cura_usos}/5 vezes')
            
        else:
            print('Cura indisponível para', self.nome)
            print(f'Cura já usada {self._cura_usos}/5 vezes')
            

    def FireBall(self, personagem):  # limite de 2 usos por personagem
        clear()
        if self._fireball_usos < 2:
            self._fireball_usos += 1
            personagem.vida -= 60
            print(f'{self.nome} lançou uma bola de fogo em {personagem.nome}')
            print(f'A vida de {personagem.nome} foi para {personagem.vida}')
            print(f'FireBall usada {self._fireball_usos}/2 vezes')
            
        else:
            print('Bola de fogo indisponível para', self.nome)
            print(f'FireBall já usada {self._fireball_usos}/2 vezes')
            

    def LancaGelo(self, personagem):  # limite de 6 usos por personagem
        clear()
        if self._lancagelo_usos < 6:
            self._lancagelo_usos += 1
            personagem.vida -= 10
            print(f'{self.nome} lançou uma lança de gelo em {personagem.nome}')
            print(f'A vida de {personagem.nome} foi para {personagem.vida}')
            print(f'Lança de Gelo usada {self._lancagelo_usos}/6 vezes')
            
        else:
            print('Lança de gelo indisponível para', self.nome)
            print(f'Lança de gelo já usada {self._lancagelo_usos}/6 vezes')
            

    def Relampago(self, personagem):  # limite de 2 usos por personagem
        clear()
        if self._relampago_usos < 2:
            self._relampago_usos += 1
            personagem.vida -= 120
            print(f'{self.nome} lançou uma Relampago em {personagem.nome}')
            print(f'A vida de {personagem.nome} foi para {personagem.vida}')
            print(f'Relampago usada {self._relampago_usos}/2 vezes')
            
        else:
            print('Relampago indisponível para', self.nome)
            print(f'Relampago já usada {self._relampago_usos}/2 vezes')
            

# RNG
# import random
# random.randint(1,100)

class Arqueiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self._tirocurto_usos = 0                    # Tiro curto
        self._firearrow_usos = 0                    # Flecha de fogo
        self._lancagelo_usos = 0                    # Lança de gelo
        self._relampago_usos = 0                    # Relampago

    def TiroCurto(self, personagem):  # limite de 20 usos por personagem
        if self._tirocurto_usos < 20:
            self._tirocurto_usos += 1
            personagem.vida -= 15
            print(f'{self.nome} usou poder de cura em {personagem.nome}')
            print(f'A vida de {personagem.nome} foi para {personagem.vida}')
            print(f'Cura usada {self._tirocurto_usos}/20 vezes')
            time.sleep(6)
        else:
            print('Tiro Curto indisponível para', self.nome)
            print(f'Tiro Curto já usada {self._tirocurto_usos}/20 vezes')
            time.sleep(6)

    def FireArrow(self, personagem):  # limite de 4 usos por personagem
        if self._firearrow_usos < 4:
            self._firearrow_usos += 1
            personagem.vida -= 40
            print(f'{self.nome} lançou uma flecha de fogo em {personagem.nome}')
            print(f'A vida de {personagem.nome} foi para {personagem.vida}')
            print(f'Flecha de Fogo usada {self._firearrow_usos}/4 vezes')
            time.sleep(6)
        else:
            print('Flecha de fogo indisponível para', self.nome)
            print(f'Flecha de Fogo já usada {self._firearrow_usos}/4 vezes')
            time.sleep(6)

    def LancaGelo(self, personagem):  # limite de 10 usos por personagem
        if self._lancagelo_usos < 6:
            self._lancagelo_usos += 1
            personagem.vida -= 10
            print(f'{self.nome} lançou uma bola de fogo em {personagem.nome}')
            print(f'A vida de {personagem.nome} foi para {personagem.vida}')
            print(f'FireBall usada {self._fireball_usos}/2 vezes')
        else:
            print('Bola de fogo indisponível para', self.nome)
            print(f'FireBall já usada {self._fireball_usos}/2 vezes')

    def Relampago(self, personagem):  # limite de 2 usos por personagem
        if self._relampago_usos < 1:
            self._relampago_usos += 1
            personagem.vida -= 50
            print(f'{self.nome} lançou uma bola de fogo em {personagem.nome}')
            print(f'A vida de {personagem.nome} foi para {personagem.vida}')
            print(f'FireBall usada {self._fireball_usos}/2 vezes')
        else:
            print('Bola de fogo indisponível para', self.nome)
            print(f'FireBall já usada {self._fireball_usos}/2 vezes')

def texto(palavra,v=0.03):
    for i in palavra:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(v)  # Ajuste o tempo conforme desejado
       
def inicio():
    while True:
        clear()
        texto('Medieval Battle\n')
        print('Defina os seus personagens')
        texto('1 | Mago\n')
        texto('2 | Arqueiro\n')
        n = int(input())

        match n :
            case 1:
                clear()
                texto('Digite o nome do seu personagem\n: ')
                name = input().title()
                persona1 = Mago(name, 100)
                return persona1
            case 2:
                clear()
                texto('Digite o nome do seu personagem\n: ')
                name = input().title()
                persona1 = Arqueiro(name, 100)
                return persona1
            case _:
                texto('Digite um numero válido...')
                time.sleep(2)
                continue
            
def Batalha():
    i = inicio()
    clear()
    texto('Um montro Apareceu ',0.2)
    texto('é ',0.25)
    texto('um ',0.3)
    time.sleep(2)
    texto('GIGANTE',0.4)
    gigante = Personagem('Gigante',500)
    while gigante.vida > 0:
        clear()
        texto('O que deseja fazer\n')
        if isinstance(i, Mago):
            texto('1 | Auto Curar\n',0.02)
            texto('2 | Bola de Fogo\n',0.02)
            texto('3 | Lança de Gelo\n',0.02)
            texto('4 | Relampago\n',0.02)
            texto('5 | Desistir\n',0.02)
            id = int(input())

            match id:
                case 1:
                    i.curar(i)
                    gigante.atacar(i)
                    input(f'A vida do gigante é: {gigante.vida}')
                    continue
                case 2:
                    i.FireBall(gigante)
                    gigante.atacar(i)
                    input(f'A vida do gigante é: {gigante.vida}')
                    continue
                case 3:
                    i.LancaGelo(gigante)
                    gigante.atacar(i)
                    input(f'A vida do gigante é: {gigante.vida}')
                    continue
                case 4:
                    i.Relampago(gigante)
                    gigante.atacar(i)
                    input(f'A vida do gigante é: {gigante.vida}')
                    continue
                case 5:
                    texto('Voce morreu!!!', 0.1)
                    break
                case _:
                    texto('Digite um numero válido...')
                    time.sleep(2)
        else:
            texto('1 | Tiro Curto\n',0.02)
            texto('2 | Flexa de Fogo\n',0.02)
            texto('3 | Desistir\n',0.02)
            id = input()
            match id:
                case 1:
                    i.TiroCurto(i)
                    gigante.atacar(i)
                    input(f'A vida do gigante é: {gigante.vida}')
                    continue
                case 2:
                    i.FireArrow(gigante)
                    gigante.atacar(i)
                    input(f'A vida do gigante é: {gigante.vida}')
                    continue
                case 3:
                    texto('Voce morreu!!!', 0.1)
                    break
                case _:
                    texto('Digite um numero válido...')
                    time.sleep(2)


Batalha()
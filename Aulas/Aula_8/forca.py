import random
import os
import json

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
texto = "escolha um tema:\n1 | Animais\n2 | Dev\n3 | Nomes\n4 | Cria um novo tema\n"

def escolher_palavra():         
    while True:    
        banco = []
        tema = int(input(texto))


        with open("Aulas/Aula_8/Banco8.json", "r", encoding="utf-8") as f:
            banco = dict(json.load(f))

        match tema:
            case 1:
                return random.choice(banco["animais"])                                  # Seleciona a chave de animais e pega um valor dele e seleciona um aleatorio
            case 2:         
                return random.choice(banco["dev"])                                      # Seleciona a chave de dev e pega um valor dele e seleciona um aleatorio
            case 3:         
                return random.choice(banco["nomes"])                                    # Seleciona a chave de nomes e pega um valor dele e seleciona um aleatorio
            case 4:         
                nome = input('Digite o nome do tema: ')         
                temas = input('Digite os itens: ')          
                lst_tema = []                                                           # Lista vazia
                lst_tema.append(temas)                                                  # Adiciona o tema na lista vazia
                banco.setdefault(nome, lst_tema)                                        # junta o banco com a lista
                with open("Aulas/Aula_8/Banco8.json", "w", encoding="utf-8") as f:                 
                    json.dump(banco, f, indent=2, ensure_ascii=False)   
                return random.choice(banco[nome])
            case _:
                input("Digite um numero valido\n")
                continue

    

def jogar_forca():
    while True:
        palavra = escolher_palavra()
        letras_coretas = []
        letras_erradas = []
        tentativas = 6
        while True:
            palavra_escondida =''
            for letra in palavra:
                if letra in letras_coretas:
                    palavra_escondida += letra
                else:
                    palavra_escondida += '_'
            limpar()
            print(palavra_escondida)
            print(letras_erradas)
            print(f'você tem: {tentativas} tentativas restantes')
            
            if palavra_escondida == palavra:
                print('Parabens você achou a palavra escondida')
                break
            elif tentativas == 0:
                print(f'Você perdeu a palavra era {palavra}')
                break
            letra_usuario = input('Digite uma letra: ')

            if letra_usuario in palavra:
                print('Letra correta')
                letras_coretas.append(letra_usuario)
            else:
                print('Letra errada')
                letras_erradas.append(letra_usuario)
                tentativas -= 1

        opcao = input('Deseja ir de novo: ').lower().replace('não','n')
        if opcao == 'n':
            break
        else:
            limpar()
            continue



if __name__ == '__main__':
    limpar()
    print('Bem vindo ao jogo da forca')
    jogar_forca()
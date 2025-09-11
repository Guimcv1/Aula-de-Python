# Arquivo onde ira ficar os execultaveis dos arquivos

import random
import string
import os


limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
limpar()

def gerar_senha(comprimento=12, incluir_maiusculo = True, incluir_minusculo = True,
                incluir_numero = True, incluir_caracter = True):
    caracteres =''
    if incluir_maiusculo:
        caracteres += string.ascii_uppercase
    if incluir_minusculo:
        caracteres += string.ascii_lowercase
    if incluir_numero:
        caracteres += string.digits
    if incluir_caracter:
        caracteres += string.punctuation
    if not caracteres:
        return ValueError('Deve ter pelo menos um tipo de caractere')
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f'Senha: {senha}')
    return senha

def main():
    print('Gerador de senhas fortes')
    comprimento = int(input('Digite o comprimento da senha (padrão 12): ')or 12)
    incluir_maiusculo = input('Deseja incluir maiuscula Sim | Não: ').lower() != 'não'
    incluir_minuscula = input('Deseja incluir minuscula Sim | Não: ').lower() != 'não'
    incluir_numeros = input('Deseja incluir numeros Sim | Não: ').lower() != 'não'
    incluir_caractere = input('Deseja incluir caractere especial Sim | Não: ').lower() != 'não'

    senha = gerar_senha(comprimento, incluir_maiusculo, incluir_minuscula,
                        incluir_numeros, incluir_caractere)
    print(f'A senha foi gerada: {senha}')

    with open('Aulas/Aula_8/senha.txt', 'a', encoding='utf-8') as s:
        s.write(f'\n{senha}')

if __name__ == '__main__':
    main()
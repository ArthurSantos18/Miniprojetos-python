# Módulos
from random import randint
from modulo import leiaInt
from time import sleep
from os import system, name

# Contadores
cont = 1

# Apagar a tela
system('cls' if name == 'nt' else 'clear')

while True: 
    print(f'{" JOGO DE ADVINHAÇÃO ":=^50}')

    # Inserção dos valores maior e menor
    menorN = leiaInt('Digite o menor número: ')
    maiorN = leiaInt('Digite o maior número: ')
    while maiorN <= menorN :
        maiorN = leiaInt('Digite um número maior que o menor número: ')
    numero = randint(menorN, maiorN)

    print('-' * 50)
    print('Você tem apenas 7 chances para acertar o número!!!')

    # Algoritmo do Jogo
    while cont < 7:
        jogador = leiaInt('Escolha um número: ')
        while jogador < menorN or jogador > maiorN:
            jogador = leiaInt('Digite um número dentro do intervalo: ')
        
        if jogador > numero:
            sleep(1)
            print('Tente novamente! Você adivinhou muito alto...')
            print('-' * 50)
            cont += 1
        elif jogador < numero:
            sleep(1)
            print('Tente novamente! Você adivinhou muito baixo...')
            print('-' * 50)
            cont += 1
        else:
            sleep(1)
            break

    # Resultado do Jogo
    print('-' * 50)
    if cont == 7:
        print('Que pena...Você perdeu :(')    
    else:
        print(f'PARABÉNS! VOCÊ CONSEGUIU COM {cont} TENTATIVAS')
    
    # Deseja continuar? 
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    print('-' * 50)
    system('cls' if name == 'nt' else 'clear')
    if resp in 'N':
        print('-' * 50)
        print('Programa Encerrado! Volte sempre <3')
        print('-' * 50)
        break

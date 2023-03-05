from madlibs import parque, ferias, viagem
import random
import os

print('BEM VINDO AO RANDOMLIB')

while True:
    game = random.choice([parque, ferias, viagem])
    game.madlib()
    for c in range (0,3):
        print()
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SNsn':
            print('Digite S ou N! ',end='')
        else:
            break
    if resp == 'N':
        break  
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

os.system('cls' if os.name == 'nt' else 'clear')
print('Obrigado! Volte sempre.')

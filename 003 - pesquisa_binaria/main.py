from random import randint

def pesquisa_binaria(lista, valor, inicio = 0, final = None):
    # Indicação do índice final da lista
    if final == None:
        final = len(lista) - 1
    # Pesquisa do índice do valor expressado    
    if inicio <= final:
        # Pesquisa Binária 
        meio = (inicio + final) // 2
        # Pesquisa encontra o valor no meio
        if lista[meio] == valor:
            return meio
        # Vetor varre a esquerda
        if valor < lista[meio]:
            return pesquisa_binaria(lista, valor, inicio, meio - 1)
        # Vetor varre a direita
        else:
            return pesquisa_binaria(lista, valor, meio + 1, final)
    # Retorna None para uma lista inválida ou um valor que não existe
    return None

lista = []

print('-=' * 30)
print(f'{"BEM VINDO A BUSCA BINÁRIA":^60}')
print('-=' * 30)

# Preenchimento da lista
randomlista = False
quantlista = int(input('Quantos valores você quer na lista? [0 para lista random] '))
if quantlista == 0:
    quantlista += randint(1, 50)
    randomlista = True

for c in range(0, quantlista):
    if randomlista:
        lista.append(randint(1, 50))
    else:    
        lista.append(int(input(f'Digite o {c + 1}° valor: ')))
lista.sort()
print('-=' * 30)

# Pesquisa da lista
while True:
    print(lista)

    pesquisa = int(input('Qual valor você quer encontrar? '))
    posicao = pesquisa_binaria(lista, pesquisa)

    if posicao != None:
        print(f'O valor {pesquisa} está na posição {posicao}')
    else:
        print(f'O valor não existe')
    print('-' * 60)

    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SNsn':
            print('Digite S ou N! ',end='')
        else:
            break
    if resp == 'N':
        break  


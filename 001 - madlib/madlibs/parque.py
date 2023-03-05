from time import sleep

def madlib():
    adj1 = str(input("Adjetivo 1: ")).lower()
    adj2 = str(input("Adjetivo 2: ")).lower()
    verbgen1 = str(input('Verbo no Gerúndio 1: ')).lower()
    verbgen2 = str(input('Verbo no Gerúndio 2: ')).lower()
    verbfin = str(input('Verbo no Infinitivo: ')).lower()
    adj3 = str(input("Adjetivo 3: ")).lower()
    adj4 = str(input("Adjetivo 4: ")).lower()

    madlib = f'''
"Uma aventura no parque"

Hoje, eu acordei bem {adj1}. Decidi ir ao parque para passar o dia. Assim que cheguei lá, comecei a me sentir {adj2} porque o sol estava muito forte. Então, decidi me sentar em um banco e {verbgen1} as pessoas ao meu redor.

Enquanto eu estava {verbgen2}, uma criança se aproximou de mim e perguntou se eu queria {verbfin} com ela no balanço. Eu aceitei o convite e começamos a nos divertir.

De repente, começou a chover {adj3}. A criança correu para se abrigar e eu decidi esperar um pouco na esperança de que a chuva parasse. Infelizmente, a chuva só piorou e eu fiquei completamente {adj4}.

Finalmente, a chuva parou e eu decidi ir para casa. Apesar do tempo ruim, eu me diverti muito no parque e com certeza voltarei lá em breve!'''

    for letra in madlib:
        print(letra,end='', flush = True)
        sleep(0.01)
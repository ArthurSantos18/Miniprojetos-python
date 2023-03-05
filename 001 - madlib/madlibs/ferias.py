from time import sleep

def madlib():
    adj1 = str(input("Adjetivo 1: ")).lower()
    adj2 = str(input("Adjetivo 2: ")).lower()
    verbfin = str(input('Verbo no Infinitivo: ')).lower()
    adj3 = str(input("Adjetivo 3: ")).lower()
    verbgen1 = str(input('Verbo no Gerúndio 1: ')).lower()
    verbgen2 = str(input('Verbo no Gerúndio 2: ')).lower()

    madlib = f'''
"Uma viagem de férias"

Nas minhas férias, eu decidi fazer uma viagem para um lugar {adj1}. Eu estava muito animado para explorar novos lugares e culturas.

Quando cheguei ao meu destino, fiquei hospedado em um hotel {adj2} no centro da cidade. No primeiro dia, comecei a {verbfin} pela cidade e visitei os pontos turísticos mais famosos. Fiquei impressionado com a beleza da cidade e sua história fascinante.

No segundo dia, decidi fazer uma excursão para um lugar {adj3} fora da cidade. Lá, eu fiz algumas atividades emocionantes, como {verbgen1} e {verbgen2}. Foi uma experiência incrível que nunca vou esquecer.

Durante a minha estadia, experimentei muitas comidas deliciosas e conheci pessoas muito interessantes. Eu me diverti muito e mal posso esperar para voltar e explorar mais no futuro.'''

    for letra in madlib:
        print(letra,end='', flush = True)
        sleep(0.01)
        
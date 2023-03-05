from time import sleep

def madlib():
    nome = str(input('Nome: ')).lower()
    obj = str(input('Objeto de viagem: ')).lower()
    evt = str(input('Evento: ')).lower()
    mt = str(input('Meio de transporte: ')).lower()
    npc = str(input('Personagem: ')).lower()
    obs = str(input('Obstáculos')).lower()

    madlib = f'''
"Uma viagem inesperada"

Um belo dia, {nome} decidiu fazer uma viagem. Empolgado, ele/ela arrumou sua {obj} e partiu rumo ao desconhecido.

Depois de algumas horas, {nome} chegou a uma cidade pequena e charmosa. Ao descer do {mt}, ele/ela foi surpreendido por uma música alta e contagiante, que vinha de uma praça próxima. Curioso, {nome} decidiu seguir o som e descobriu que estava acontecendo um {evt}.

Empolgado, {nome} se juntou à multidão e começou a dançar. De repente, ele/ela foi abordado por um {npc} misterioso, que lhe entregou um papel e disse: "Você foi escolhido para participar de uma missão importante. Siga as instruções e salve o mundo!"

Sem saber muito bem o que fazer, {nome} decidiu seguir as instruções do papel e partiu em uma jornada cheia de aventuras. Ele/ela enfrentou {obs} e superou seus medos, até finalmente chegar ao seu destino final.

Exausto, mas feliz, {nome} percebeu que sua viagem inesperada havia mudado sua vida para sempre. Ele/ela voltou para casa com muitas histórias para contar e uma nova perspectiva sobre o mundo.'''

    for letra in madlib:
        print(letra,end='', flush = True)
        sleep(0.01)

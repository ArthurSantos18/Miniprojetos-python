def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arquivo):
    a = open(arquivo, 'wt+')

def cadastrar(arquivo, login = 'desconhecido', senha = '0'):
    a = open(arquivo, 'at')
    a.write(f'{login};{senha},')

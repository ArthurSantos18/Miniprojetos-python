import PySimpleGUI as sg
from auxArquivos import arquivoExiste, criarArquivo, cadastrar

def tela():
    sg.theme('Reddit')
    # Layout
    layout = [
        [sg.Text('Login', size=(5,0)), sg.Input(size=(15,0), key='login')],
        [sg.Text('Senha', size=(5,0)), sg.Input(size=(15,0), key='senha')],
        [sg.Button('Entrar'), sg.Button('Sair'), sg.Button('Criar Conta')]
    ]
    # Retorno da Tela
    return sg.Window('Login', layout, finalize=True)

def telaCad():
    sg.theme('Reddit')
    # Layout
    layout = [
        [sg.Text('Novo Login', size=(10,0)), sg.Input(size=(15,0), key='novoLogin')],
        [sg.Text('Nova Senha', size=(10,0)), sg.Input(size=(15,0), key='novaSenha')],
        [sg.Button('Cadastrar'), sg.Button('Voltar'), sg.Button('Sair')]
    ]
    # Retorno da Tela
    return sg.Window('Cadastro', layout, finalize=True)

# Criação da tela
telaLogin, telaCadastro = tela(), None
arquivo = 'cadastro.txt'

# Loop da tela
while True:
    # Telas, eventos e valores com todas as telas
    telas, evento, valores = sg.read_all_windows()
    
    # Configuração dos botões (tela de login)
    if telas == telaLogin:
        login = valores['login']
        senha = valores['senha']

        if evento == 'Sair' or evento == sg.WIN_CLOSED:
            break

        elif evento == 'Criar Conta':
            telaCadastro = telaCad()
            telaLogin.hide()

    # Configuração dos botões (tela de cadastro)
    if telas == telaCadastro:
        login = valores['novoLogin']
        senha = valores['novaSenha']

        if evento == 'Sair' or evento == sg.WIN_CLOSED:
            break

        elif evento == 'Voltar':
            telaCadastro.hide()
            telaLogin.un_hide()

        elif evento == 'Cadastrar':
            if not arquivoExiste(arquivo):
                criarArquivo(arquivo)
            cadastrar(arquivo, login, senha)
            sg.popup('Cadastro feito com sucesso')

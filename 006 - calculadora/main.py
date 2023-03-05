import PySimpleGUI as sg

# Layout
layout = [
    [sg.Text('')],
    [sg.Text('')],
    [sg.Button('1', size=(3, 1)), sg.Button('2', size=(3, 1)), sg.Button('3', size=(3, 1)), sg.Button('+', size=(3, 1))],
    [sg.Button('4', size=(3, 1)), sg.Button('5', size=(3, 1)), sg.Button('6', size=(3, 1)), sg.Button('-', size=(3, 1))],
    [sg.Button('7', size=(3, 1)), sg.Button('8', size=(3, 1)), sg.Button('9', size=(3, 1)), sg.Button('x', size=(3, 1))],
    [sg.Button('0', size=(3, 1)), sg.Button('<-', size=(3, 1)), sg.Button('=', size=(3, 1)), sg.Button('/', size=(3, 1))]
]

tela = sg.Window('Calculadora', layout)

while True:
    eventos, valores = tela.Read()  

    if eventos == sg.WINDOW_CLOSED:
        break
    
    for c in range(0, 9):
        if eventos == str(c):
            aux = str(c)

            print(n)

import PySimpleGUI as sg
from math import trunc

# Layout
layout = [
    [sg.Input('0', size=(16, 1), key='visor'), sg.Button('<-', size=(3, 1))],
    [sg.Button('1', size=(3, 1)), sg.Button('2', size=(3, 1)), sg.Button('3', size=(3, 1)), sg.Button('+', size=(3, 1))],
    [sg.Button('4', size=(3, 1)), sg.Button('5', size=(3, 1)), sg.Button('6', size=(3, 1)), sg.Button('-', size=(3, 1))],
    [sg.Button('7', size=(3, 1)), sg.Button('8', size=(3, 1)), sg.Button('9', size=(3, 1)), sg.Button('x', size=(3, 1))],
    [sg.Button('0', size=(3, 1)), sg.Button('C', size=(3, 1)), sg.Button('=', size=(3, 1)), sg.Button('/', size=(3, 1))]
]
# Tela
tela = sg.Window('Calculadora', layout)
# Variável de operadores
operador = ''
calc = n1 = n2 = aux = 0
#Loop da tela
while True:
    eventos, valores = tela.Read()  

    if eventos == sg.WINDOW_CLOSED:
        break
    
    # Números no visor
    for c in range(1, 10):
        if eventos == str(c):
            if valores['visor'] == '0':
                tela['visor'].update(value = str(c))
            else:
                tela['visor'].update(value = valores['visor'] + str(c))

    # Backarrow
    if eventos == '<-':
        if valores['visor'] != '0':
            tela['visor'].update(value = valores['visor'][:-1])
    
    # C
    if eventos == 'C':
        calc = 0
        tela['visor'].update(value = calc)

    # Soma
    if eventos == '+':
        if operador == '':
            n1 = int(valores['visor'])
            operador = '+'
            tela['visor'].update(value = 0)
        else:
            n2 = int(valores['visor'])
            s = n1 + n2
            tela['visor'].update(value = calc)
            operador = ''
    
    # Subtração
    if eventos == '-':
        if operador == '':
            n1 = int(valores['visor'])
            operador = '-'
            tela['visor'].update(value = 0)
        else:
            n2 = int(valores['visor'])
            calc = n1 - n2
            tela['visor'].update(value = calc)
            operador = '' 

    # Multiplicação
    if eventos == 'x':
        if operador == '':
            n1 = int(valores['visor'])
            operador = 'x'
            tela['visor'].update(value = 0)
        else:
            n2 = int(valores['visor'])
            calc = n1 * n2
            tela['visor'].update(value = calc)
            operador = ''    
    
    # Divisão
    if eventos == '/':
        if operador == '':
            n1 = int(valores['visor'])
            operador = '/'
            tela['visor'].update(value = 0)
        else:
            n2 = int(valores['visor'])
            try: 
                calc = n1 / n2
            except ZeroDivisionError:
                calc = 0
            if calc % 2 == 0:
                try:
                    aux = n1 / n2
                except ZeroDivisionError:
                    calc = 0
                calc = trunc(aux)
            tela['visor'].update(value = calc)
            operador = '' 
    
    # Igual
    if eventos == '=':
        if operador == '+':
            n2 = int(valores['visor'])
            calc = n1 + n2
            tela['visor'].update(value = calc)
            operador = '' 
        elif operador == '-':
            n2 = int(valores['visor'])
            calc = n1 - n2
            tela['visor'].update(value = calc)
            operador = ''             
        elif operador == 'x':
            n2 = int(valores['visor'])
            calc = n1 * n2
            tela['visor'].update(value = calc)
            operador = '' 
        elif operador == '/':
            n2 = int(valores['visor'])
            calc = n1 / n2
            if calc % 2 == 0:
                aux = n1 / n2
                calc = trunc(aux)
            tela['visor'].update(value = calc)
            operador = ''            

from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*',size=(21,1))],
    [sg.Checkbox('Salvar Login?')],
    [sg.Button('Entrar')]
    ]
janela = sg.Window('Tela de Login', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Randson' and valores['senha'] == '123456789':
            print('Bem vindo ao Sistema')

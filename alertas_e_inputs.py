import pyautogui

pyautogui.alert(text='clique confirmar para continuar.', title='tela de alerta teste', button='confirmar')

login = pyautogui.prompt(text='digite o login', title='tela de login')

senha = pyautogui.password(text='digite a senha', title='tela de login', mask='*')

resp = pyautogui.confirm(text='escolha a opcão desejada.', title='tela de confirmacão', buttons=['continuar', 'voltar ao login.'])


while resp == 'voltar ao login.':

    login = pyautogui.prompt(text='digite o login', title='tela de login')

    senha = pyautogui.password(text='digite a senha', title='tela de login', mask='*')

    resp = pyautogui.confirm(text='escolha a opcão desejada.', title='tela de confirmacão', buttons=['continuar', 'voltar ao login.'])
    

print(f'bem vindo: {login.upper()}')




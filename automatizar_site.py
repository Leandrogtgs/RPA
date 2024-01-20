import webbrowser
import pyautogui
from time import sleep
import pyperclip

def escrever(txt):

    texto = txt

    for l in texto:

        pyperclip.copy(l)

        pyautogui.hotkey('ctrl', 'v')

# navegar até o site

webbrowser.open('https://cursoautomacao.netlify.app/')

sleep(1)

# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome

pyautogui.click(1054,197, duration=2)

sleep(1)

pyautogui.scroll(-1600)

nome_alerta = pyautogui.locateCenterOnScreen('nome_alerta.png')

pyautogui.click(nome_alerta[0], nome_alerta[1], duration=2)

escrever('Leandro')

# 3) Clique em alerta, para gerar a alerta

bt_alerta = pyautogui.locateCenterOnScreen('bt_alerta.png')

pyautogui.click(bt_alerta[0], bt_alerta[1], duration=1)

# 4) Feche a alerta

pyautogui.click(x=1235,y=190, duration=2)

sleep(1)

# 5) Suba a página totalmente para cima

pyautogui.scroll(5000)

sleep(1)

# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém 
# os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos 
# arquivos excel e pdf.

pyautogui.scroll(-3100)

sleep(1)

# baixando arquivo excel

arq_excel = pyautogui.locateCenterOnScreen('arq_excel.png')

pyautogui.moveTo(arq_excel[0], arq_excel[1], duration=2)

pyautogui.move(0, 35, duration=1)

pyautogui.click()


sleep(1)


# baixando arquivo pdf

arq_pdf = pyautogui.locateCenterOnScreen('arq_pdf.png')

pyautogui.moveTo(arq_pdf[0], arq_pdf[1], duration=2)

pyautogui.move(0, 35, duration=1)

pyautogui.click()

sleep(1)

# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"

pyautogui.scroll(1500)

sleep(1)

nome_alerta = pyautogui.locateCenterOnScreen('nome_alerta.png')

pyautogui.click(x=nome_alerta[0], y=nome_alerta[1], duration=1)

sleep(1)

escrever('VOCÊ TERMINOU')

bt_alerta = pyautogui.locateCenterOnScreen('bt_alerta2.png')

pyautogui.click(x=bt_alerta[0], y=bt_alerta[1], duration=2)

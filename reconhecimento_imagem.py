import webbrowser

import pyautogui

from time import sleep

webbrowser.open('https://google.com/recaptcha/api2/demo')

sleep(2)

# localizando imagem na tela

#captcha = pyautogui.locateOnScreen('capcha.png')

#localizando centro de uma imagem na tela

capcha = pyautogui.locateCenterOnScreen('capcha.png')

print(capcha)

pyautogui.click(capcha[0], capcha[1], duration=2)

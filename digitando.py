import pyautogui

import pyperclip

from time import sleep

def escrever(txt):

    frase = txt


    for l in frase:

        pyperclip.copy(l)

        pyautogui.hotkey('ctrl', 'v')

        sleep(0.6)

        

pyautogui.moveTo(945,199, duration=2)

pyautogui.click()

escrever('olá mundo!')

#pyautogui.typewrite('ola, mundo!')
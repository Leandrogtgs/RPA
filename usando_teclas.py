import pyautogui
import pyperclip
from time import sleep


""" def escrever(txt):

    frase = txt

    for l in frase:

        pyperclip.copy(l)

        pyautogui.hotkey('ctrl', 'v')

        sleep(0.1) """

def escrever(txt):

    frase = txt.lower()

    for l in frase:

        pyautogui.hotkey(f'{l}')


pyautogui.click(x=963, y=201, duration=2)

escrever('Minusculo')

sleep(1)

pyautogui.hotkey('enter')

pyautogui.hotkey('capslock')

escrever('maiusculo')

pyautogui.hotkey('capslock')

sleep(1)

pyautogui.hotkey('enter')

escrever('minusculo')

sleep(1)

pyautogui.moveTo(1169,181, duration=1)

pyautogui.hotkey('ctrl', 'a')

sleep(1)

pyautogui.hotkey('backspace')
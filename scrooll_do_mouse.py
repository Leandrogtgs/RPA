import webbrowser

import pyautogui

from time import sleep

webbrowser.open('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal')

sleep(2)

pyautogui.moveTo(622,549, duration=2)


pyautogui.scroll(-5000)

sleep(1)

pyautogui.scroll(5000)

pyautogui.moveTo(705,20, duration=1)

pyautogui.click(button='middle', clicks=7, interval=1)


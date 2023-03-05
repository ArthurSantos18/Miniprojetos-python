import pyautogui
from time import sleep

def click_esquerdo(x, y, texto):
    pyautogui.PAUSE = 0.5
    pyautogui.moveTo(x, y, 0.2)
    pyautogui.leftClick(x, y)
    pyautogui.typewrite(texto)
    pyautogui.typewrite(['enter'])

click_esquerdo(175, 750, 'Google Chrome')
sleep(1.5)
click_esquerdo(260, 53, 'Twitter')

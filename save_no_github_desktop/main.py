import pyautogui
from time import sleep


if __name__ == '__main__':
    pyautogui.alert('Por favor retire as mão do teclado e do mouse')
    sleep(1)
    pyautogui.press('win')
    sleep(1)
    pyautogui.write('github desktop')
    sleep(1)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.moveTo(x=2195, y=665)
    pyautogui.click()
    pyautogui.write('update')
    sleep(1.5)
    pyautogui.moveTo(x=2165, y=817)
    pyautogui.click()
    sleep(2)
    pyautogui.moveTo(x=2660, y=233)
    pyautogui.click()
    sleep(5)
    pyautogui.hotkey('alt', 'f4')
    pyautogui.alert('Pode voltar as suas tarefas ao normal!')


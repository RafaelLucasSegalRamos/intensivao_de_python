import pyautogui
from time import sleep
# abrir o arquivo Login.xlsx
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
pyautogui.PAUSE = 1.5

width_pos = screenWidth * 0.25

pyautogui.alert('O progama irá tomar controle do mouse e teclado por favor retire a mão')
pyautogui.press('win')
pyautogui.write('Login.xlsx')
pyautogui.press('backspace')
pyautogui.press('enter')
sleep(3)
pyautogui.moveTo(width_pos, 340)
pyautogui.click()
pyautogui.write('rafaelsegalramos@gmail.com')
pyautogui.moveTo(width_pos, 390)
pyautogui.click()
pyautogui.write('123_456')
pyautogui.moveTo(width_pos, 450)
pyautogui.click()
pyautogui.alert('login efetuado com sucesso')



# preencher o login
# preencher a senha
# Clicar em login

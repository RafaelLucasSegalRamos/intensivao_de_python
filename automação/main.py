import pyautogui
import time
# abrir o terabox no computador
pyautogui.PAUSE = 1.5
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
poswid = screenWidth * 0.95
poshei = screenHeight * 0.05
meiowid = (screenWidth * 0.5) * -1
meiohei = screenHeight * 0.5
# abrir a área de trabalho e arrastar o arquivo
# enquanto segurar o arquivo mudar para o terabox no chrome.
# e largar o arquivo lá
# esperar 5 segundos.
pyautogui.alert('Por favor, tire as mãos do tecldo e mouse, pois o código ira controla-los')
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/folders/1_B96cZDRflPvavkvXEqSAwJRA0RruwsR')
pyautogui.press('Enter')
pyautogui.hotkey('win', 'd')
pyautogui.moveTo(poswid, poshei)
pyautogui.hotkey('alt', 'tab')
time.sleep(3)
pyautogui.drag(meiowid, meiohei, duration=0.5)
pyautogui.alert('O processo do código terminou. Pode voltar a utilizar o computador')


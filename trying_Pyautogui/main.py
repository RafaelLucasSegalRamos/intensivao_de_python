import pyautogui
import pyautogui as pa
from time import sleep

pa.PAUSE = 1
pa.FAILSAFE = True

# lo1 = pa.locateOnScreen("teste.png")
# lo2 = pa.locateCenterOnScreen("teste.png")
# pa.moveTo(lo1[0],lo1[1], duration=1)
# pa.click(lo2[0],lo2[1], duration=1)

# pa.click(clicks=10, button="middle", interval=1)
# pa.doubleClick()

# pa.scroll(-10000)

# pa.keyDown("win")
# pa.press("down")
# pa.press("left")
# pa.press("right", presses=2, interval=1)
# pa.press("up")
# pa.press("up")

# pa.keyUp("win")

# with pyautogui.hold("win"):
#     pa.press("down")
#     pa.press("left")
#     pa.press("right", presses=2, interval=1)
#     pa.press("up")
#     pa.press("up")
#
# pa.hotkey("ctrl", "win", "d")
# pa.hotkey("ctrl", "win", "left")
# # pa.hotkey("win", "m")
# pa.hotkey("ctrl", "win", "right")
# pa.hotkey("ctrl", "win", "f4")
# pa.alert("Hello World", "Alerta")

# teste = pa.confirm("Qual você prefere?", "Confirm" , buttons=["abacate", "manga"])
# print(teste)

# promt = pa.prompt("Qual seu nome?", "Prompt", default="e.g John Doe")
# print(promt)

passw = pa.password("Digite sua senha", "Password", mask="9")
print(passw)

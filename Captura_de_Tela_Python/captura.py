import cv2
import numpy as np
import pyautogui as pag
import time
import keyboard as kb


fps = 15 # Por algum motivo se eu coloco qualque valor acima de 15 fps o video fica bugado e fica muito mais rápido do
# que deveria, por exemplo quando eu coloco 60 fps, o video fica como se fosse 4x

tamanho_tela = tuple(pag.size())

codec = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter("testando.avi", codec, fps, tamanho_tela)


while True:
    frame = pag.screenshot()
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video.write(frame)
    if kb.is_pressed("esc"):
        break

video.release()


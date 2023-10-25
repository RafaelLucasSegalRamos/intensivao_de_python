import time
import pyotp
from aleatório import Key
import keyboard
import qrcode

master_key = Key(1).master_key

codigo = pyotp.TOTP(master_key)


cod_usu = input("Digite o código: ")

veri = codigo.verify(cod_usu)

if veri:
    print("Código válido!")
else:
    print("Código inválido!")

link = pyotp.TOTP(master_key).provisioning_uri("Teste", issuer_name="você sabe que não vou usar esse cod pra nada certo?")

# qrcode.make(link).save("qrcode.png")


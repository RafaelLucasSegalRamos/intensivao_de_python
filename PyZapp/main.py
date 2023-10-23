from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import urllib

nav = webdriver.Chrome()
tabela = pd.read_excel("myExel.xlsx")
nav.get("https://web.whatsapp.com/")
sleep(8)

nav.find_element(by="xpath", value='/html/body/div[1]/div/div/div[3]/div[1]/div/div/div[3]/div/span').click()
sleep(3.5)

nav.find_element(by="xpath", value='/html/body/div[1]/div/div/div[3]/div[1]/div/div[3]/div[2]/div/div/div/form/input').send_keys("(**)*****-****")
sleep(3.5)

nav.find_element(by="xpath", value='/html/body/div[1]/div/div/div[3]/div[1]/div/div[3]/div[3]').click()
sleep(30)
for linha in tabela.index:
    nome = tabela.loc[linha, "nome"]
    mensagem = tabela.loc[linha, "mensagem"]
    numero = tabela.loc[linha, "telefone"]
    arquivo = tabela.loc[linha, "Arquivo"]
    mensagem = mensagem.replace("[nome]", nome)
    mensagem = urllib.parse.quote(mensagem)
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    nav.get(link)
    sleep(8)

    if arquivo != "N":
        pass



nav.quit()

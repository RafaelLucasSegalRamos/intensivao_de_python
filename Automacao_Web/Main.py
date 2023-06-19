from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

if __name__ == '__main__':
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    # Se o nevegador escolhido fosse o chrome se usaria chromedrivermanager
    # Se o nevegador escolhido fosse o firefox se usaria geckodrivermanager

    navegador.get('https://www.unip.br/aluno/central/')

    navegador.find_element('xpath', '/html/body/unip-root/unip-login/main/div/form/div[1]/input').send_keys('G797752')
    navegador.find_element('xpath', '/html/body/unip-root/unip-login/main/div/form/div[2]/input').send_keys('Ra311079@')
    navegador.find_element('xpath', '/html/body/unip-root/unip-login/main/div/form/div[3]/button').click()

    time.sleep(1000)
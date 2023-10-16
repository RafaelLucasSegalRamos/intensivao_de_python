from selenium import webdriver
"""from webdriver_manager.chrome import ChromeDriverManager"""
from selenium.webdriver.chrome.service import Service
from time import sleep

# video de onde saiu isso : https://youtu.be/8AMNaVt0z_M?si=N0F1JwtlUXLg86U8
# servico = Service(ChromeDriverManager().install()) # Aparentemente isso já não é mais necessário, mas vou manter para acompanhar certinho o video

driver = webdriver.Chrome()  # service=servico
"""driver2 = webdriver.Firefox()
driver3 = webdriver.Edge()"""

driver.get(
    'https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&nonce=638326465966118843.e8f0d495-7cfe-41eb-88a9-699e1644ae02&msaredir=1&client-request-id=96ffe339-e5e4-3c1a-99aa-a190087f0ca0&protectedtoken=true&claims=%7b"id_token"%3a%7b"xms_cc"%3a%7b"values"%3a%5b"CP1"%5d%7d%7d%7d&prompt=select_account&state=DYu9DoIwGABB34UNaaGUdiAOJsYBjUENyEL685loREgpEN7eDnfTne953taxcfjIyctowpKYEppySjFmjCQ7YC-kCU_DTL0gJBhkyJjgIeUcMCVEAIp9985Rv4hoP5i-G2w-wheUbYVS_fSzgVD2ttjcmgmC0QoLOQ4M6Ldx0b3PxalE6nSmxcpnXZejjLkpOt413ffT3NKPjNEsq-MgD6x9Vhf0SDS61uWqq8cf')
"""driver2.get("https://www.google.com")
driver3.get("https://www.google.com")"""
sleep(1)
driver.find_element('xpath',
                    '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(
    '**********@****.com')
driver.find_element('xpath',
                    '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input').click()
sleep(2)
driver.find_element('xpath',
                    '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys(
    '#########')
driver.find_element('xpath',
                    '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input').click()
sleep(5)

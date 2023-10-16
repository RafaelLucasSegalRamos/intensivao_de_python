from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from time import sleep


driver = webdriver.Chrome()

driver.get('https://books.toscrape.com/')

sleep(1)
stock_List = []
title_List = []
pos = 0
try:
    for i in range(1, 51):
        titList = driver.find_elements('tag name', 'a')[54:94:2]

        for i in titList:
            pos += 1
            print(f'{pos}° Titulo: '+i.get_attribute('title'))
            title_List.append(i.get_attribute('title').title())
            i.click()
            sleep(0.5)
            stock = driver.find_element("class name", 'instock')
            stock_List.append(int(stock.text.replace('In stock (', '').replace(' available)', '')))

            driver.back()
            sleep(0.5)
        procura = driver.find_elements('tag name', 'a')
        for i in procura:
            if i.text == 'next':
                i.click()
                sleep(1)

except KeyboardInterrupt:
    print('O usuário interrompeu o programa')
    pass

except Exception as error:
    print(error)
    print('Fim da lista')
    pass

finally:


    """per = int(input('Qual livro deseja ver? '))
    titulo_esc = titList[per - 1].get_attribute('title')
    print(f'O livro {titulo_esc} tem {stock_List[per - 1]} unidades em estoque')"""

    sleep(2)

    dictDF = {'Titulo': title_List, 'Estoque': stock_List}

    print(pd.DataFrame(dictDF))

    driver.back()

    driver.quit()

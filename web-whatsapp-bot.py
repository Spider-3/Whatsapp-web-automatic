from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

os.system("cls")

try:
    os.system("pip install selenium")
    os.system("pip install webdriver_manager")
except:
    print("nescessario instalar python primeiro :3 ")


print(r"""    

        
 .oooooo..o             o8o        .o8                     
d8P'    `Y8             `"'       "888                     
Y88bo.      oo.ooooo.  oooo   .oooo888   .ooooo.  oooo d8b 
 `"Y8888o.   888' `88b `888  d88' `888  d88' `88b `888""8P 
     `"Y88b  888   888  888  888   888  888ooo888  888     
oo     .d8P  888   888  888  888   888  888    .o  888     
8""88888P'   888bod8P' o888o `Y8bod88P" `Y8bod8P' d888b    
             888                                           
            o888o                                          
                                                              """)

time.sleep(5)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com")


os.system("cls")

print("ele ira abrir o whatsapp web, voce precisa de pegar seu celular e autenticar no whatsapp web")
time.sleep(2)

print("responda embaixo com sim quando terminar")
os.system("cls")

autenticação = input("ja autenticou no site do whatsapp? ")

while True:
    if autenticação == "sim" or "s" or "si":
        print("continuando script")
        break
    else:
        print("errado")
        exit()

os.system("cls")



while True:
    escolha = input("voce deseja enviar mensagem a um grupo ou a um contato? ")
    if escolha == "contato" or "cntt":
        os.system("cls")
        contato = input("qual o nome do contato?")
        os.system("cls")
        mensagem_contato = input("qual mensagem voce deseja enviar ao contato?")
        os.system("cls")
        break
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(contato)
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(mensagem_contato)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        
    

while True:
    if escolha == "grupo":
        print("ok, o senhor é quem manda ")
        os.system("cls")
        grupo = input("qual o nome do grupo?")
        os.system("cls")
        mensagem = input("qual a mensagem que deseja enviar?")
        break
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(grupo)
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(mensagem)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        os.system("cls")

        escolha2 = input("deseja encerrar o programa? ")
        if escolha2 == "sim" or "s":
            os.system("cls")
            os.system("python instagram.py")

        else:
            exit()

input()


#obrigado sempre pela ajuda, satan...
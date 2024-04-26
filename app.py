# instalar a bibioteca selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from time import sleep

driver = webdriver.Chrome()

#Nevegar ate o site usando o selenium 
driver.get('https://google.com.br')
sleep(5)

#encontrar elementos da tela 
pesquisar = driver.find_element(By.XPATH, "//textarea[@name='q']")
sleep(2)
pesquisar.send_keys('Teste de Velocidade de internet')

#clicar no botao pesquisar 
botao_pesquisar = driver.find_element(By.XPATH, "//input[@name='btnK']")
sleep(2)
botao_pesquisar.click()

#aguardar o resultado
sleep(10)
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

url = 'https://www.enquefase.cl/'

# abriendo el browser
driver = webdriver.Chrome(executable_path="/home/jorge/Documentos/interviews/testScrapy/src/chromedriver_binary")
driver.implicitly_wait(5)
#obteniendo url
driver.get(url)

# abriendo menu Listado de la izquierda
listado = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/ul/li[3]/a")
listado.click()

#validando existencia de Google Adds
if driver.current_url.find('#google_vignette') != -1:
    driver.back()
    listado.click()

# obtendiendo informacion de comunas y sus estados
rows = driver.find_elements_by_xpath('/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr')
comunaData = []
for i in range(1, len(rows) + 1):
    comuna = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr[" + str(i) + "]/td[1]").text
    fase = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr[" + str(i) + "]/td[2]").text
    estado = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr[" + str(i) + "]/td[3]").text
    comunaData.append({
        'comuna': comuna,
        'fase': fase,
        'estado': estado
    })

# filtrando a region metropolitana
rm = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[6]/div/div[2]/div/table/tbody/tr[13]/td[2]/a")
rm.click()

#accediendo a la comuna Quilicura
quili = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr[39]/td[1]/a")
quili.click()

#accediendo al detalle quilicura
detalleQuili = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[3]/div/div/a[1]")
detalleQuili.click()


    

#//*[@id="main-wrapper"]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr[1]
#/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr[2]

#/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr[1]/td[1]


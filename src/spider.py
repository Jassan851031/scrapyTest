import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time
from db_config import insertData


url = 'https://www.enquefase.cl/'

def getCookees():
    driver = webdriver.Chrome()
    driver.get(url)
    cookies_list = driver.get_cookies()
    cookies_dict = {}
    for cookie in cookies_list:
        cookies_dict[cookie['name']] = cookie['value']
    print(cookies_dict)


# abriendo el browser
driver = webdriver.Chrome(executable_path="/home/jorge/Documentos/interviews/testScrapy/src/chromedriver_binary")
driver.implicitly_wait(5)
#obteniendo url
driver.get(url)
getCookees()

# abriendo menu Listado de la izquierda
listado = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/ul/li[3]/a")
listado.click()

#validando existencia de Google Adds
if driver.current_url.find('#google_vignette') != -1:
    driver.back()
    listado.click()
url = 'https://www.enquefase.cl/listado-de-comunas'
getCookees()

# obtendiendo informacion de comunas y sus estados
rows = driver.find_elements_by_xpath('/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr')
comunaData = []
# for i in range(1, len(rows) + 1):
#     comuna = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr[" + str(i) + "]/td[1]").text
#     fase = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr[" + str(i) + "]/td[2]").text
#     estado = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[30]/div/div/div/table/tbody/tr[" + str(i) + "]/td[3]").text
#     comunaData.append({
#         'comuna': comuna,
#         'fase': fase,
#         'estado': estado
#     })

#insertData(comunaData)

# filtrando a region metropolitana
rm = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[6]/div/div[2]/div/table/tbody/tr[13]/td[2]/a")
rm.click()

#validando existencia de Google Adds
if driver.current_url.find('#google_vignette') != -1:
    driver.back()
    rm.click()
url = 'https://www.enquefase.cl/region/metropolitana-de-santiago'
getCookees()

#accediendo a la comuna Quilicura
quili = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr[39]/td[1]/a")
quili.click()
url = 'https://www.enquefase.cl/quilicura'
getCookees()

#accediendo al detalle quilicura
detalleQuili = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[3]/div/div/a[1]")
detalleQuili.click()
url = 'https://www.enquefase.cl/calculadora-de-permisos-para-viajar-desde/quilicura'
getCookees()

#accediendo a permisos para viajar desde quilicura a pichilemu
selectorComuna = driver.find_element_by_id('select2-single-select-target-container').click()
permisoPichilemu = driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[221]')
permisoPichilemu.click()
url = 'https://www.enquefase.cl/calculadora-de-permisos-para-viajar-de/quilicura/a/pichilemu'
getCookees()

driver.close()




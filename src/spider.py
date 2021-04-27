import selenium
from selenium import webdriver


url = 'https://www.enquefase.cl/'

# abriendo el browser
driver = webdriver.Chrome(executable_path="/home/jorge/Documentos/interviews/testScrapy/src/chromedriver_binary")

#obteniendo url
driver.get(url)

# abriendo menu Listado de la izquierda
listado = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/ul/li[3]/a")
listado.click()


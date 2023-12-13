from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#setup webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options)
action_chains = ActionChains(driver)
driver.maximize_window()
driver.get('https://www.leroymerlin.com.br/')


button_departamentos = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//span[contains(text(),"Departamentos")]')))

if driver.find_element(By.XPATH, '//div[@class="relative z-10 px-3 py-3 text-md"]//div//div//button[contains(text(),"Continuar")]'):
    button_continuar = driver.find_element(
        By.XPATH, '//div[@class="relative z-10 px-3 py-3 text-md"]//div//div//button[contains(text(),"Continuar")]')
    button_continuar.click()
    
button_departamentos.click()

button_ferramentas = driver.find_element(By.XPATH, '//span[contains(text(),"Ferramentas")]')
button_ferramentas.click()

# button_ferramentas_manuais = driver.find_element(By.XPATH, '//span[contains(text(),"Ferramentas Manuais")]')
button_ferramentas_manuais = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//span[contains(text(),"Ferramentas Manuais")]')))
button_ferramentas_manuais.click()

# img_alicates = driver.find_element(By.CSS_SELECTOR, 'img[title="Alicates"]')
img_alicates = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[title="Alicates"]')))
img_alicates.click()

# lista_add_favoritos = driver.find_elements(By.CLASS_NAME, 'inline-flex')
lista_add_favoritos = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,'inline-flex')))

if lista_add_favoritos:
    item_desejado = lista_add_favoritos[1]
    item_desejado.click()
else:
    print('Lista esta vazia') 

sleep(20)
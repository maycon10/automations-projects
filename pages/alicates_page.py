from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AlicatesPage:
    def __init__(self, driver):
        self.driver = driver
        self.lista_add_favoritos = (By.CLASS_NAME,'inline-flex')
    
    def clicar_add_favorito(self):
        self.itens_add_favoritos = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.lista_add_favoritos))
        
        if self.itens_add_favoritos:
            self.driver.find_element(self.itens_add_favoritos[1]).click()
     
    def aguardar_pagina_carregar(self):
        sleep(20)


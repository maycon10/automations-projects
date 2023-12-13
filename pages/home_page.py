from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.button_continuar_locator = (By.XPATH, '//div[@class="relative z-10 px-3 py-3 text-md"]//div//div//button[contains(text(),"Continuar")]')
        self.button_departamentos_locator = (By.XPATH, '//span[contains(text(),"Departamentos")]')
        self.button_ferramentas_locator = (By.XPATH, '//span[contains(text(),"Ferramentas")]')
        self.button_ferramentas_manuais_locator = (By.XPATH, '//span[contains(text(),"Ferramentas Manuais")]')
            
    def aguardar_button_departamentos(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.button_departamentos_locator))
    
    def clicar_button_continuar(self):
        if self.driver.find_element(*self.button_continuar_locator):
            self.driver.find_element(*self.button_continuar_locator).click()
            
    def clicar_button_departamentos(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_departamentos_locator))
        self.driver.find_element(*self.button_departamentos_locator).click()

    def clicar_button_ferramentas(self):
        self.driver.find_element(*self.button_ferramentas_locator).click()

    def clicar_button_ferramentas_manuais(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.button_ferramentas_manuais_locator))
        self.driver.find_element(*self.button_ferramentas_manuais_locator).click()
        
    def aguardar_pagina_carregar(self):
        sleep(20)

            

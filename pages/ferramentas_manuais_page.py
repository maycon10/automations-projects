from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class FerramentasManuaisPage:
    def __init__(self, driver):
        self.driver = driver
        self.imagem_alicates_locator = (By.CSS_SELECTOR, 'img[title="Alicates"]')
        
    def clicar_imagem_alicates(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.imagem_alicates_locator))
        self.driver.find_element(*self.imagem_alicates_locator).click()

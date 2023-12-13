import sys
sys.path.append("C://projects-python//automacao-db")
from selenium import webdriver
from pages.home_page import HomePage
from pages.ferramentas_manuais_page import FerramentasManuaisPage
from pages.alicates_page import AlicatesPage

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.get('https://www.leroymerlin.com.br/')

home_page = HomePage(driver)
home_page.aguardar_button_departamentos()
home_page.clicar_button_continuar()
home_page.clicar_button_departamentos()
home_page.clicar_button_ferramentas()
home_page.clicar_button_ferramentas_manuais()

ferramentas_manuais_page = FerramentasManuaisPage(driver)
ferramentas_manuais_page.clicar_imagem_alicates()

alicates_page = AlicatesPage(driver)
alicates_page.clicar_add_favorito()
alicates_page.aguardar_pagina_carregar()
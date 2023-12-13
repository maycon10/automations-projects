import sys
sys.path.append("C://projects-python//automacao-db")
from selenium import webdriver
from pages.alicates_page import AlicatesPage

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')
driver = webdriver.Chrome(chrome_options)

alicates_page = AlicatesPage(driver)
alicates_page.clicar_add_favorito()
alicates_page.aguardar_pagina_carregar()




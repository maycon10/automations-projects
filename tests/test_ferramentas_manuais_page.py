import sys
sys.path.append("C://projects-python//automacao-db")
from selenium import webdriver
from pages.ferramentas_manuais_page import FerramentasManuaisPage

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')
driver = webdriver.Chrome(chrome_options)

ferramentas_manuais_page = FerramentasManuaisPage(driver)
ferramentas_manuais_page.clicar_imagem_alicates()


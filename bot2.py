from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

navegador.get('https://m.212820.com/#/login')
navegador.find_element('xpath',
                       '//*[@id="app"]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/input').send_keys('mgn3712')

import time as time

from selenium import webdriver

url = 'https://m.212820.com/#/login'
user = "mgn3712"
password = "M3712h"

driver = webdriver.Chrome()
driver.get(url)


driver.find_element('xpath',
                    '//*[@id="app"]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/input').send_keys(user)
driver.find_element('xpath',
                    '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/input').send_keys(password)
driver.find_element('xpath',
                    '//*[@id = "app"]/div[2]/div[2]/div[2]/div[3]/button').click()

driver.implicitly_wait(10)

driver.find_element('xpath',
                    '/html/body/div[7]/div/div/div/div/div[2]/i').click()
driver.find_element('xpath',
                    '//*[@id="theme-wangzhuan-home"]/div[2]/div[5]/div/div[1]/div[1]').click()

# começar o foor


for i in range(50):
    time.sleep(3)
    driver.find_element(
        'xpath', '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]').click()

    time.sleep(8)
    driver.find_element(
        'xpath', '//*[@id="notranslate"]/div[8]/div/div/div/div/div/div[6]/div[2]/span').click()

    time.sleep(1)
    driver.find_element(
        'xpath', '//*[@id="94"]/div[2]/div/div[2]/div[1]').click()

    time.sleep(2)

driver.close()

driver = webdriver.Chrome(
    "C:\\Users\\etc\\Desktop\\Selenium+Python\\chromedriver.exe")
driver.maximize_window()
wait = WebDriverWait(driver, 30)
driver.get("https://www.nike.com.br/cosmic-unity-153-169-211-324680")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cc-allow'))).click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//label[@for='tamanho__id40']"))).click()
wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, 'button#anchor-acessar-unite-oauth2'))).click()
wait.until(EC.frame_to_be_available_and_switch_to_it(
    (By.ID, "nike-unite-oauth2-iframe")))
wait.until(EC.element_to_be_clickable(
    (By.NAME, 'emailAddress'))).send_keys("test@gmail.com")
wait.until(EC.element_to_be_clickable(
    (By.NAME, 'password'))).send_keys("mypass")
wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[value='ENTRAR']"))).click()

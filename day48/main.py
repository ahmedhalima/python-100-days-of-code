from selenium import webdriver
from selenium.webdriver.common.by import By

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=driver_options)

try:
    driver.get('https://www.selenium.dev/documentation/webdriver/getting_started/first_script/')
    title = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/main/div/h1')
    print(title.text)
finally:
    driver.quit()




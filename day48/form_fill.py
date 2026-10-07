from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option('detach', True)
driver = webdriver.Chrome()
url = "https://appbrewery.github.io/fake-newsletter-signup/"

try:
    driver.get(url)
    fName = driver.find_element(By.NAME, 'fName')
    fName.send_keys('Ahmed')
    lName = driver.find_element(By.NAME, 'lName')
    lName.send_keys('Maher')
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('phpcodertop@gmail.com')

    btn = driver.find_element(By.CSS_SELECTOR, '#signup-form button')
    btn.click()
    sleep(1000)
finally:
    driver.quit()
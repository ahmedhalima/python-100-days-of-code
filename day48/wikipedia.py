from selenium import webdriver
from selenium.webdriver.common.by import By

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=driver_options)

try:
    driver.get('https://en.wikipedia.org/wiki/Main_Page')

    articles_count = driver.find_element(By.CSS_SELECTOR, '#mwDw')
    print(articles_count.text)
finally:
    driver.quit()
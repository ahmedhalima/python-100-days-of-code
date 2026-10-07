from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://appbrewery.github.io/Zillow-Clone/"
form_url = "https://docs.google.com/forms/d/e/1FAIpQLScyacFFtALXHzKKZKrYnjSXbCiyYXIzXgsd_jNTqDaGFNS7Qw/viewform"

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=driver_options)

driver.get(url)

# get list of listings
listings_links = driver.find_elements(By.CSS_SELECTOR, '.ListItem-c11n-8-84-3-StyledListCardWrapper .StyledPropertyCardDataWrapper a')
listings_prices = driver.find_elements(By.CSS_SELECTOR, '.PropertyCardWrapper__StyledPriceLine')
listings_address = driver.find_elements(By.CSS_SELECTOR, '.ListItem-c11n-8-84-3-StyledListCardWrapper address')

links = [link.get_attribute('href') for link in listings_links]
prices = [link.text for link in listings_prices]
addresses = [link.text for link in listings_address]



def insert_to_form(myDriver, link, price, address):

    myDriver.get(form_url)
    price_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    price_field.send_keys(price)

    address_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    address_field.send_keys(address)

    link_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    link_field.send_keys(link)

    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))
    )
    btn.click()

    # /html/body/div[1]/div[2]/div[1]/div/div[4]/a
    driver.implicitly_wait(3000)
    btn2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))
    )
    btn2.click()


for n in range(0, len(links)):
    insert_to_form(myDriver=driver, price=prices[n], link=links[n], address=addresses[n])

driver.quit()
from datetime import datetime
from dateutil.parser import parse
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=driver_options)

try:
    driver.get('https://www.python.org/')
    events_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget  time')
    events_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget  li a')
    events = {}
    for n in range(0, len(events_times)):
        event_time = parse(events_times[n].get_attribute('datetime'))
        events[n] = {
            'name' : events_names[n].text,
            'date': datetime.strftime(event_time, "%d-%m-%Y")
        }
    print(events)
finally:
    driver.quit()
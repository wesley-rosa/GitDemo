import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.skyscanner.com.br")

driver.find_element_by_id("fsc-origin-search").send_keys(Keys.BACKSPACE)
time.sleep(2)
word = "gua"
driver.find_element_by_id("fsc-origin-search").send_keys(word)

airports = driver.find_elements_by_css_selector("li[role='option'] span")
time.sleep(2)

for airport in airports:
    if airport.txt == "rulhos Cumbica SP (GRU)":
        print("Suuucesso")
    #     airport.click()
    #     break



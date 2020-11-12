import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

actions = ActionChains(driver)

# righ click
actions.context_click(driver.find_element_by_id("double-click")).perform()
time.sleep(3)
# double click
actions.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text

alert.accept()

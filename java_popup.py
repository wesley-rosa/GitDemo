import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("option3")
driver.find_element_by_id("alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

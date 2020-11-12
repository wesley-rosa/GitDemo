from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

title = driver.find_element_by_xpath("//h1[contains(text(),'Practice Page')]").text
assert "Practice Page" == title

driver.find_element_by_

driver.close()
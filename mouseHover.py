from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
action.move_to_element(driver.find_element_by_id("mousehover")).perform()
action.move_to_element(driver.find_element_by_link_text("Top")).click().perform()
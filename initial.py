from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/")
driver.maximize_window()

print(driver.title)

driver.get("https://www.rahulshettyacademy.com/#/practice-project")
driver.back()

driver.close()
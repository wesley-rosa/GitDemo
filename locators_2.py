from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.implicitly_wait(10)

# to access dropdown menu, it is necessary to create an object with Select() and import its library
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
# dropdown.select_by_index(1) - This is the same as to select female.




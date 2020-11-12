from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Testing")

# How to retrieve the information from "Name" field?

# 1. Using Selenium:
print(driver.find_element_by_name("name").get_attribute("value"))

# 2. By using JavaScript
# 2.1 In Web Page, Inspect Element -> Console -> ...
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# How to scroll down? It is not possible using Selenium, so we can relay on JS to do that

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# driver.close()
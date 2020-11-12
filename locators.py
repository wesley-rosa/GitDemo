from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/#/practice-project")

driver.implicitly_wait(15)

driver.find_element_by_xpath("//a[text()='About Us']").click()

driver.implicitly_wait(3)

driver.back()

# init = driver.find_element_by_xpath("//h2[contains(text(),'Join now to Practice')]").text
# assertEqual(init, "Join now to Practic")

# the same way to access the same item

driver.find_element_by_xpath("//input[@name='name']").send_keys("Wesley - xpath")
# driver.find_element_by_css_selector("#name").send_keys("Wesley Who")
# driver.find_element_by_css_selector("input[name='name']").send_keys("Wesley o Cara")
# driver.find_element_by_name("name").send_keys("Wesley")




driver.find_element_by_name("email").send_keys("wesley1984@gmail.com")

driver.implicitly_wait(3)

driver.find_element_by_id("agreeTerms").click()
driver.find_element_by_xpath("//button[@type='submit']")

driver.implicitly_wait(10)

driver.maximize_window()

driver.implicitly_wait(5)

driver.back()

# driver.find_element_by_xpath("//button[@id='form-submit']").click()



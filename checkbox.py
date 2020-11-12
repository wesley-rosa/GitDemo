from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(checkboxes)

for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()

# if you want to select one specific checkbox, this is a clean way to do so:

# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") == "option1":
#         checkbox.click()
#         assert checkbox.is_selected()

# or, using list:
# checkboxes[1].click()

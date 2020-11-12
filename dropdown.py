import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("aus")
time.sleep(2)

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "Austria":
        time.sleep(2)
        country.click()
        break


# result = driver.find_element_by_id("autosuggest").text // This option could be used, however it does not work in this specific website

result = driver.find_element_by_id("autosuggest").get_attribute("value")
assert "Austria" == result

driver.close()



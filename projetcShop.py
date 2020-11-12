import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")

# //button[@class='btn btn-info']/parent::div/parent::div/div/h4/a  -- Product Name

driver.implicitly_wait(2)

button = driver.find_elements_by_xpath("//button[@class='btn btn-info']")

for item in button:
    if item.find_element_by_xpath("parent::div/parent::div/div/h4/a").text == "Blackberry":
        product_name = item.find_element_by_xpath("parent::div/parent::div/div/h4/a").text
        product_price = item.find_element_by_xpath("parent::div/parent::div/div/h5").text
        item.click()

driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()

# Asserts
product_name_in_cart = driver.find_element_by_xpath("//h4[@class='media-heading']/a").text
product_price_in_cart = driver.find_element_by_xpath("//td[3]/strong").text

try:
    assert product_name == product_name_in_cart
    assert product_price == product_price_in_cart
except Exception as e:
    print(e)

driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("chi")

# Explicity wait to select the country.
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div.suggestions')))

countries = driver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")

for country in countries:
    if country.text == "China":
        country.click()

value_country = driver.execute_script("return document.getElementById('country').value")

assert value_country == "China"

driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()

driver.find_element_by_css_selector("input[class='btn btn-success btn-lg']").click()

success_msg = driver.find_element_by_class_name("alert-success").text
test_msg = "Success! Thank you! Your order will be delivered in next few weeks :-)."

# "Success! Thank you! Your order will be delivered in next few weeks :-)."

assert test_msg in success_msg

driver.get_screenshot_as_file("test.png")

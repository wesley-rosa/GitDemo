import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("nut")
time.sleep(2)

addtocart = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# or
# addtocart = driver.find_elements_by_xpath("//button[contains(text(),'ADD TO CART')]")

assert len(addtocart) == 2

for item in addtocart:
    item.click()

# click on cart icon
driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()

# click to checkout
driver.find_element_by_xpath("//div[@class='action-block']/button").click()

# explicit wait works directly to one specific action
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"input.promoCode")))

# inserting promo code to cart
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

# explicit wait being applied again
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))

# confirmation message
msg = driver.find_element_by_css_selector("span.promoInfo").text
print(msg)
assert msg == "Code applied ..!"

print("Congrats, Wesley!")

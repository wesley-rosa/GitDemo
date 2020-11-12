import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("nut")
time.sleep(2)

addtocart = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# or
# addtocart = driver.find_elements_by_xpath("//button[contains(text(),'ADD TO CART')]")

# //div[@class='product-action']/button/parent::div/parent::div/h4

assert len(addtocart) == 2
itemname = []

for item in addtocart:
    itemname.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
    item.click()


# click on cart icon
driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()

# click to checkout
driver.find_element_by_xpath("//div[@class='action-block']/button").click()

# Let's check if products are okay in cart

insidecart = driver.find_elements_by_css_selector("p.product-name")
item2 = []
for item in insidecart:
    item2.append(item.text)

assert itemname in item2

# inserting promo code to cart
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

# confirmation message
msg = driver.find_element_by_css_selector("span.promoInfo").text
assert msg == "Code applied ..!"

print("Congrats, Wesley!")

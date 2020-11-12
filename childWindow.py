from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

driver.implicitly_wait(3)
driver.find_element_by_link_text("Click Here").click()

#in order to go to child page, this is necessary to use this windo handles. The position 0 is de first window created... if we have two windows, we can use
# index 1, por example.
childwindow = driver.window_handles[1]
# (parentwindow, childwindow)
driver.switch_to.window(childwindow)

print(driver.find_element_by_tag_name("h3").text)

driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)
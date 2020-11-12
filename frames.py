from selenium import webdriver
# iframes, frameset and fram - tagnames that indicate frames.
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com")

driver.find_element_by_link_text("Frames").click()

driver.find_element_by_link_text("iFrame").click()
# frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("I really can automate that")

driver.switch_to.default_content()
assert "An iFrame containing the TinyMCE WYSIWYG Editor" == driver.find_element_by_tag_name("h3").text

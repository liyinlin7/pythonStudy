from capability import *

driver.find_element_by_id("com.tal.kaoyan:id/login_register_text").click()
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_userheader").click()

images=driver.find_elements_by_id("com.tal.kaoyan:id/item_image")
images[3].click()
driver.find_element_by_id("com.tal.kaoyan:id/save").click()
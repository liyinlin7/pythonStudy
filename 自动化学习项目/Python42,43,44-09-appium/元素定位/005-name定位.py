from capability import *

driver.find_element_by_name("请输入用户名").clear()
driver.find_element_by_name("请输入用户名").send_keys("DAwang001")
driver.find_element_by_name("请输入密码").send_keys("DAwang001")
driver.find_element_by_name("登录").click()

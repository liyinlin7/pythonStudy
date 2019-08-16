from selenium import webdriver
# 调用keys模块
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(1)
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(2)
driver.find_element_by_id("kw").send_keys("WANG")
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(2)
# driver.find_element_by_id("su").click()
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()

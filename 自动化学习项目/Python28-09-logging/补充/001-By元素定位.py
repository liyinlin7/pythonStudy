from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(5)

# # 原先定位模式
# driver.find_element_by_id("kw").send_keys("selenium")

# By元素定位
# driver.find_element(By.ID,"kw").send_keys("selenium")
# driver.find_element(By.NAME,"wd").send_keys("selenium")
driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("selenium")

driver.find_element(By.ID, "su").click()
sleep(3)

driver.quit()

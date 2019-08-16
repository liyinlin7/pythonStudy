from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
url = r"D:\Python项目\自动化学习项目\Python31-09-鼠标操作\鼠标左键\test_1.html"
driver.get(url)
div = driver.find_element_by_id("div1")
# 在id属性值为“div1”的元素上执行按下的鼠标左键，并保持
ActionChains(driver).click_and_hold(div).perform()
time.sleep(2)
# 释放按下的鼠标左键
ActionChains(driver).release(div).perform()

time.sleep(2)
driver.quit()


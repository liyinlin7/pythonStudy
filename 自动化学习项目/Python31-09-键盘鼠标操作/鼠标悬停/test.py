from selenium import webdriver
from selenium.webdriver import ActionChains
import time
'''
鼠标操作的常用方法：
perform()：执行
context_click()：右击
click_and_hold()：左击
double_click():双击
drag_and_drop()：拖动
move_to_element():鼠标悬停
'''

driver = webdriver.Chrome()
url = r"D:\Python项目\自动化学习项目\Python31-09-鼠标操作\鼠标悬停\test_2.html"
driver.get(url)

link1 = driver.find_element_by_link_text("鼠标指过来1")
link2 = driver.find_element_by_link_text("鼠标指过来2")
p = driver.find_element_by_xpath("//p")

ActionChains(driver).move_to_element(link1).perform()
time.sleep(2)
ActionChains(driver).move_to_element(p).perform()
time.sleep(2)
ActionChains(driver).move_to_element(link2).perform()
time.sleep(2)
ActionChains(driver).move_to_element(p).perform()
time.sleep(2)

driver.quit()

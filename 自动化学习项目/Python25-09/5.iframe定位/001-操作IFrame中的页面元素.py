#encoding=utf-8
from selenium import webdriver
import unittest
import time
import os

driver = webdriver.Chrome()
url = 'file:///' + os.path.abspath('frameset.html')
#访问自定义的HTML网页
driver.get(url)
driver.switch_to.frame(0)
assert u"这是左侧frame页面上的文字" in driver.page_source
driver.switch_to.frame(driver.find_element_by_id("showIfame"))
assert u"这是iframe页面上的文字" in driver.page_source
driver.switch_to.default_content()#退出当前frame，能够进入其他的frame框
assert u"frameset页面"==driver.title
driver.switch_to.frame(1)
assert u"这是中间frame页面上的文字" in driver.page_source
driver.switch_to.default_content()#退出当前frame，能够进入其他的frame框

driver.quit()

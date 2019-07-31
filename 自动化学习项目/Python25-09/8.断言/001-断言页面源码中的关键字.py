#encoding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "http://www.baidu.com"
#访问百度首页
driver.get(url)
driver.find_element_by_id("kw" ).send_keys(u"selenium")
driver.find_element_by_id("su").click()
time.sleep(4)
#通过断言页面是否存在某些关键字来确定页面按照预期加载
assert "selenium" in driver.page_source,u"页面源码中不存在该关键字！"

driver.quit()

import time
from selenium import webdriver

driver=webdriver.Chrome()
url="http://www.sogou.com"
driver.get(url)
try:
    result=driver.get_screenshot_as_file(r"u:\test.png")
    print(result)
except IOError as e:
    print(e)
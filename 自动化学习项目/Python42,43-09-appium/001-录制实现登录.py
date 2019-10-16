# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:62001"
caps["appPackage"] = "com.tal.kaoyan"
caps["appActivity"] = "com.tal.kaoyan.ui.activity.SplashActivity"
caps["noReset"] = "true"  # 非首次运行，不以第一次状态启动。  因为APP软件，第一启动，和非第一次启动， 页面有区别

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext")
el1.send_keys("DAwang001")
el2 = driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext")
el2.send_keys("DAwang001")
el3 = driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn")
el3.click()

driver.quit()
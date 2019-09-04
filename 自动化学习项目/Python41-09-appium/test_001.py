from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'   # 操作系统
desired_caps['platformVersion'] = '6.0'    # 系统版本
desired_caps['deviceName'] = '192.168.178.101:5555'  # 链接手机的IP和端口   通过  adb devices
desired_caps['appPackage'] = 'com.android.calculator2'  # 要测试的包名
desired_caps['appActivity'] = '.Calculator'  # 当前页面：Activity

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 链接 appium  “/wd/hub” 固定目录

driver.find_element_by_id("com.android.calculator2:id/digit_7").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_3").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
driver.quit()


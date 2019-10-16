from appium import webdriver

# 设置设备
desired_cape={}
desired_cape['platformName'] = 'Android'
desired_cape['deviceName'] = '127.0.0.1:62001'
desired_cape['platformVersion'] = '5.1.1'
desired_cape['app'] = r'd:\kaoyan3.1.0.apk'  # 如果移动端没有安装APP， 设置后，如果没有安装，就会安装
desired_cape['appPackage'] = 'com.tal.kaoyan'
desired_cape['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
desired_cape['noReset'] = 'true'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cape)
driver.implicitly_wait(5)

# 定位“取消”按钮
driver.find_element_by_id('android:id/button2').click()
# 定位“跳过”按钮
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()

driver.quit()

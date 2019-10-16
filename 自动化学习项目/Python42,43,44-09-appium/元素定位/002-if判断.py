from appium import webdriver


# 不能用 if 判断是否找到  元素 定位

# 设置设备
desired_cape={}
desired_cape['platformName']='Android'
desired_cape['deviceName']='127.0.0.1:62001'
desired_cape['platformVersion']='5.1.1'
desired_cape['app']=r'd:\kaoyan3.1.0.apk'
desired_cape['appPackage']='com.tal.kaoyan'
desired_cape['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'
desired_cape['noReset']='true'

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cape)
driver.implicitly_wait(5)

# 定位“取消”按钮
cancelBtn=driver.find_element_by_id('android:id/button2')
# 定位“跳过”按钮
skipBtn=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')

if cancelBtn:
    cancelBtn.click()
else:
    print("没有'取消'按钮")

if skipBtn:
    skipBtn.click()
else:
    print("没有'跳过'按钮")

driver.quit()

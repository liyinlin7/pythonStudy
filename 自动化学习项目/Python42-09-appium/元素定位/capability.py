from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

# 设置设备
desired_cape={}
desired_cape['platformName']='Android'
desired_cape['deviceName']='127.0.0.1:62025'
desired_cape['platformVersion']='7.1.2'
desired_cape['app']=r'd:\kaoyan3.1.0.apk'
desired_cape['appPackage']='com.tal.kaoyan'
desired_cape['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'
desired_cape['noReset']='true'

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cape)
driver.implicitly_wait(5)

def check_cancelBtn():
    print("check_cancelBtn")
    try:
        # 定位“取消”按钮
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print("没有“取消”按钮")
    else:
        cancelBtn.click()

def check_skipBtn():
    print("check_skipBtn")
    try:
        # 定位“跳过”按钮
        skipBtn = driver.find_element_by_name('跳过 > ')
    except NoSuchElementException:
        print("没有“跳过”按钮")
    else:
        skipBtn.click()

check_cancelBtn()
check_skipBtn()


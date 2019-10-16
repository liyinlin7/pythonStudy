from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

desired_cape={}
desired_cape['platformName']='Android'
desired_cape['deviceName']='127.0.0.1:62001'
desired_cape['platformVersion']='7.1.2'
desired_cape['app']=r'd:\mymoney.apk'
desired_cape['appPackage']='com.mymoney'
desired_cape['appActivity']='com.mymoney.biz.splash.SplashScreenActivity'
desired_cape['noReset']='true'

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cape)
driver.implicitly_wait(5)

# 获取屏幕尺寸
def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y

# 向左滑动
def swipeLeft():
    l = get_size()
    x1=int(l[0]*0.9)
    x2=int(l[0]*0.2)
    y1=int(l[0]*0.5) 
    driver.swipe(x1,y1,x2,y1,1000)

# 向上滑动
def swipeUp():
    l = get_size()
    x1=int(l[0]*0.5)
    y1=int(l[0]*0.8)
    y2=int(l[0]*0.3)
    driver.swipe(x1,y1,x1,y2,1000)

# 等待启动页面元素，然后向左滑动两次，跳过引导页面
WebDriverWait(driver,6).until(lambda x:x.find_element_by_id("com.mymoney:id/next_btn"))
for i in range(2):
    swipeLeft()
    sleep(0.5)

# 点击“开始随手记”按钮
driver.find_element_by_id("com.mymoney:id/begin_btn").click()

# 检测是否有升级提示，出现后捕获

# 点击“更多”菜单
driver.find_element_by_xpath("//*[@id=com.mymoney:id/nav_setting_btn]").click()

# 等待界面菜单加载出来，然后向上滑动
WebDriverWait(driver,6).until(lambda x:x.find_element_by_id("com.mymoney:id/content_container_ly"))
swipeUp()

# 点击“高级”菜单
driver.find_element_by_id("com.mymoney:id/title_tv").click()
# 点击“密码与手势”菜单
driver.find_element_by_id("com.mymoney:id/password_protected_briv").click()
# 点击“手势密码与保护”
driver.find_element_by_id("com.mymoney:id/lock_pattern_or_not_sriv").click()

# 连续滑动两次设置图案密码
for i in range(2):
    TouchAction(driver).press(x=210,y=286).wait(1000)\
        .move_to(x=360,y=291).wait(1000)\
        .move_to(x=358,y=438).wait(1000)\
        .move_to(x=362,y=586).wait(1000)\
        .release().perform()

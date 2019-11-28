from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):
    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')

    # 判断“取消”按钮
    def check_cancelBtn(self):
        logging.info("=======check_cancelBtn=====")
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            print("no cancelBtn")
        else:
            cancelBtn.click()

    # 判断“跳过按钮”
    def check_skipBtn(self):
        logging.info("========check_skipBtn========")
        try:
            # 定位“跳过”按钮
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            print("no skipBtn")
        else:
            skipBtn.click()

    # 获取屏幕大小
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动
    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        x2 = int(l[0] * 0.2)
        y1 = int(l[0] * 0.5)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 获取脚本执行时间
    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    # 截屏
    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png'%(module,time)
        logging.info('get %s screenshot'%module)
        self.driver.get_screenshot_as_file(image_file)

    # 读取csv文件数据
    def get_csv_data(self,csv_file,line):
        logging.info('========get_scv_data=======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):  # enumerate(a,start) a是可迭代对象，start是计数起始数字
                if index==line:
                    return row



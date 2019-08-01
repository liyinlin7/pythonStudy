#-*-coding:utf-8 -*-
import time
from selenium import webdriver
import os


driver = webdriver.Chrome()
driver.maximize_window()
# url = r"C:\Users\YXtimes_Wang\Desktop\js弹出框\index.html"
url = 'file:///' + os.path.abspath('index.html')
driver.get(url)
'''获取alert对话框的按钮,点击按钮,弹出alert对话框'''
driver.find_element_by_xpath('/html/body/div/input[2]').click()
'''获取alert对话框'''
alert = driver.switch_to_alert()
# alert = driver.switch_to.alert
'''添加等待时间'''
time.sleep(2)
'''获取警告对话框的内容'''
print(alert.text)  # 打印警告对话框内容
alert.accept()   # alert对话框属于警告对话框，我们这里只能接受弹窗
'''添加等待时间'''
time.sleep(2)
driver.quit()

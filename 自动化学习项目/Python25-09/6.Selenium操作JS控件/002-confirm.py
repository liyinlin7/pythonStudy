#-*-coding:utf-8 -*-
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
url=r"C:\Users\YXtimes_Wang\Desktop\js弹出框\index.html"
driver.get(url)
'''获取confirm对话框的按钮,点击按钮,弹出confirm对话框'''
driver.find_element_by_xpath('/html/body/div/input[3]').click()
'''获取confirm对话框'''
dialog_box = driver.switch_to_alert()
'''添加等待时间'''
time.sleep(2)
'''获取对话框的内容'''
print (dialog_box.text)  #打印警告对话框内容
'''点击【确认】显示"您为何如此自信？"'''
dialog_box.accept()   #接受弹窗
print (driver.find_element_by_xpath('//*[@id="textSpan"]/font').text)
time.sleep(2)
'''再次获取confirm对话框的按钮,点击按钮,弹出confirm对话框'''
driver.find_element_by_xpath('/html/body/div/input[3]').click()
'''再次获取confirm对话框'''
dialog_box = driver.switch_to_alert()
'''点击【取消】显示"您为何如此谦虚？"'''
time.sleep(2)
dialog_box.dismiss()  #关闭获取取消对话框
print (driver.find_element_by_xpath('//*[@id="textSpan"]/font').text)
driver.quit()
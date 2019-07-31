#-*-coding:utf-8 -*-
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
'''获取对话框输入2，并且点击【确认】,文本框内提示<左哥是真笨啊>,点击【取消】文本框内提示<您没有按要求输入，请重新输入>'''
url=r"C:\Users\YXtimes_Wang\Desktop\js弹出框\index.html"
driver.get(url)
'''获取prompt对话框的按钮,点击按钮,弹出confirm对话框'''
driver.find_element_by_xpath('/html/body/div/input[1]').click()
'''获取prompt对话框'''
dialog_box = driver.switch_to_alert()
'''添加等待时间'''
time.sleep(2)
'''获取对话框的内容'''
print (dialog_box.text)  #打印警告对话框内容
dialog_box.send_keys("2")  #弹出框内输入2
dialog_box.accept()  #接受
print (driver.find_element_by_xpath('//*[@id="textSpan"]/font').text)  #获取关闭弹窗结果  #获取确认弹窗结果
'''这里等待几秒在测试取消'''
time.sleep(2)
#************************点击【取消】,并且获取显示结果**********************
driver.find_element_by_xpath('/html/body/div/input[1]').click()
'''获取prompt对话框'''
dialog_box = driver.switch_to_alert()
'''添加等待时间'''
time.sleep(2)
dialog_box.dismiss()  #关闭对话框
print (driver.find_element_by_xpath('//*[@id="textSpan"]/font').text)  #获取关闭弹窗结果
time.sleep(2)
driver.quit()
# DATE: 2023/2/21
# Name:zhanglingling
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://test.zhthh.com/lvpao/#/login?redirect=%2Fhome")
sleep(3)
# driver.find_element(By.CSS_SELECTOR,"[placeholder='请输入用户名']").clear()
# driver.find_element(By.CSS_SELECTOR,"[placeholder='请输入用户名']").send_keys("123")
# sleep(5)
# driver.find_element(By.CSS_SELECTOR,"[placeholder='请输入密码']").clear()
# driver.find_element(By.CSS_SELECTOR,"[placeholder='请输入密码']").send_keys("1234")
#el-button submit_login el-button--primary el-button--large
driver.find_element(By.XPATH,"//span[contains(text(),'登 录')]").click()
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div/button/span').click()
# driver.find_element(By.CSS_SELECTOR,'#app>div>div>button').click()
sleep(2)
driver.find_element(By.XPATH,"//span[contains(text(),'系统管理')]").click()
sleep(1)
driver.find_element(By.XPATH,"//span[contains(text(),'账户管理')]").click()
sleep(5)
driver.quit()
driver.close()
#//标签名[(text()='内容')]

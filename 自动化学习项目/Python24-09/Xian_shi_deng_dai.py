from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
# 导入显示等待需要的包
from selenium.webdriver.support.wait import WebDriverWait
# 导入预期条件类
from selenium.webdriver.support import expected_conditions as EC

def xian_shi_deng_dai():
    """
    24天第45节课
    显式等待
    :return:
    """
    driver = webdriver.Chrome()
    url = r"D:\Python项目\自动化学习项目\Python22-09\static\html\注册A.html"
    driver.get(url)
    driver.maximize_window()
    # 在设置的时间内找我们要的元素，在这个时间内找到了，就会继续执行代码；如果没有找到会报错，可以写try异常来处理
    # 显示等待_查找方式：程序每隔xx检查一次，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间
    # 默认检查时间为 0.5 秒一次
    a = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'userA')))
    a.send_keys("显示等待")
    # 超时时间为10秒，每0.2秒检查一次，直到 id = passwordA 的元素出现
    b = WebDriverWait(driver, 10, 0.2).until(EC.presence_of_element_located((By.ID, 'passwordA')))
    # 使用lambda 函数来判断 显示等待
    # WebDriverWait(driver, 6).until(lambda x: x.find_element_by_id("passwordA"))
    b.send_keys("11111")
    sleep(3)
    driver.quit()


if __name__ == "__main__":
    xian_shi_deng_dai()


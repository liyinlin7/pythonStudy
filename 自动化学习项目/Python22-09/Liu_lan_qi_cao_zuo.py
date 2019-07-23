from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def liu_lan_qi_cao_zuo():
    """
    23天第46节课
    浏览器的操作方法
    :return:
    """
    driver = webdriver.Chrome()
    url = r"http://www.baidu.com"
    driver.get(url)
    sleep(3)
    driver.maximize_window()  # 浏览器最大化
    driver.set_window_size(2000, 1000)  # 设置浏览器大小，2000px宽，1000px高
    sleep(2)
    driver.refresh()  # 刷新
    sleep(2)
    driver.back()  # 后退
    sleep(2)
    driver.forward()  # 前进
    sleep(2)

    # 控制窗口滑动（不要用百度的地址测试）
    js1 = 'window.scrollTo(0, 10000)'
    js2 = 'window.scrollTo(0, 0)'
    driver.execute_async_script(js1)
    sleep(3)
    driver.execute_async_script(js2)
    sleep(3)

    driver.quit()  # 关闭所有的webdriver窗口
    # driver.close()  # 关闭单个窗口


if __name__ == '__main__':
    liu_lan_qi_cao_zuo()

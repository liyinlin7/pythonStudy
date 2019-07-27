from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def chuang_kou_ju_bin():
    """
    23天第46节课
    iframe 的定位
    :return:
    """

    driver = webdriver.Chrome()
    url = r"D:\Python项目\自动化学习项目\Python22-09\static\html\注册实例.html"
    driver.get(url)
    sleep(3)
    # 获取当前的窗口句柄
    # handle = '句柄'
    cur_handle = driver.current_window_handle
    print(cur_handle)
    # 点击“注册A”的超链接
    driver.find_element_by_css_selector("#ZCA").click()
    sleep(3)
    # 获取所有的窗口句柄
    cur_handleS = driver.window_handles
    cur_handleA = 'a'
    handles = []
    for handle in cur_handleS:
        print(handle)
        handles.append(handle)
        if handle != cur_handle:
            # 定位到“注册A页面”的句柄，可以操作“注册A”页面
            driver.switch_to.window(handle)
            driver.find_element_by_id("userA").send_keys("注册A页面")
            # 获取注册A页面的句柄
            cur_handleA = driver.current_window_handle
    print(cur_handleA)
    print(handles)
    sleep(3)

    # 关闭了句柄“注册A页面”
    driver.close()

    # 定位到“注册实例”HTML页面，
    sleep(3)
    driver.switch_to.window(handles[0])
    driver.find_element_by_css_selector("#ZCB").click()
    sleep(3)
    driver.quit()


if __name__ == '__main__':
    chuang_kou_ju_bin()

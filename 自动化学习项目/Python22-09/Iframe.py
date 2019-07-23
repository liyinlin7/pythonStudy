from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def iframe():
    """
    23天第46节课
    iframe 的定位
    :return:
    """
    driver = webdriver.Chrome()
    url = r"D:\Python项目\自动化学习项目\Python22-09\static\html\注册实例.html"
    driver.get(url)
    sleep(3)

    # 去A的页面
    driver.switch_to.frame("myframe1")
    driver.find_element_by_css_selector("#userA").send_keys("myframe1")
    sleep(3)

    # 先退出A的iframe，回到主页面
    driver.switch_to.default_content()
    sleep(2)

    # 再去B的页面
    driver.switch_to.frame("myframe2")
    driver.find_element_by_css_selector("#userB").send_keys("myframe2")
    sleep(3)

    driver.quit()


if __name__ == '__main__':
    iframe()

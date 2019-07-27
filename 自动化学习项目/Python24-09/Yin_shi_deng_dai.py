from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def yin_shi_deng_dai():
    """
    24天第45节课
    隐式等待
    :return:
    """
    driver = webdriver.Chrome()
    url = r"D:\Python项目\自动化学习项目\Python22-09\static\html\注册A.html"
    driver.get(url)
    driver.maximize_window()
    # 隐式等待,找到后不会等待；没找到到会在 设置的时间内 继续找，时间内没找到会报错，可以写try异常处理
    # 隐式等待_查找方式：一次没找到，就不会找到了，到了时间，就会得到找到不元素的结果
    # 设置一个等待时间，如果在这个等待时间内，网页加载完成，则执行下一步；否则一直等待时间截止，然后再执行下一步。
    # 这样也就会有个弊端，程序会一直等待整个页面加载完成，直到超时，但有时候我需要的那个元素早就加载完成了，
    # 只是页面上有个别其他元素加载特别慢，我仍要等待页面全部加载完成才能执行下一步。
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#userA").send_keys("隐式等待")

    sleep(3)
    driver.quit()


if __name__ == "__main__":
    yin_shi_deng_dai()

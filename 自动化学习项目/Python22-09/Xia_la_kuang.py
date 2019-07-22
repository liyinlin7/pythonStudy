from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def xia_la_kuang():
    """
    下拉框选择
    :return:
    """
    driver = webdriver.Chrome()
    url = r"D:\Python项目\自动化学习项目\Python22-09\static\html\注册A.html"
    driver.get(url)
    sleep(3)

    # 方法一 根据TEXT的内容选择
    options = driver.find_elements_by_tag_name("option")
    for a in options:
        if a.text == "A上海":
            a.click()
        print(a)
    sleep(3)

    # 方法二 根据value的值选择， get_attribute获取元素的属性值
    options = driver.find_elements_by_tag_name("option")
    for a in options:
        if a.get_attribute("value") == "cq":
            a.click()
        print(a)
    sleep(3)

    driver.quit()


if __name__ == '__main__':
    xia_la_kuang()

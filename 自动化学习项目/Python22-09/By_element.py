from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def byElement():
    """
    find_element()
    find_element_by_
    获取文本，获取title，获取<a>标签的链接地址
    获取当前页面的地址，获取css的size值
    :return:
    """
    driver = webdriver.Chrome()
    url = r"D:\Python项目\自动化学习项目\Python22-09\static\html\注册A.html"
    driver.get(url)
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#userA").send_keys("By.CSS_SELECTOR")
    # driver.find_element_by_css_selector("#userA").send_keys("selector")

    driver.find_element(By.XPATH, "//*[@id='passwordA']").send_keys("By.XPATH")
    # driver.find_element_by_xpath("//*[@id='passwordA']").send_keys("xpath")

    # driver.find_element(By.CLASS_NAME)
    # driver.find_element(By.ID)
    # driver.find_element(By.NAME)
    # driver.find_element(By.LINK_TEXT)
    # driver.find_element(By.PARTIAL_LINK_TEXT)
    # driver.find_element(By.TAG_NAME)

    # 获取弹框的内容
    driver.find_element_by_css_selector("#alert").click()
    sleep(3)
    alert = driver.switch_to.alert
    # 读取弹框的内容
    text = alert.text
    print(text)
    # 点击弹框的同意
    alert.accept()
    # 点击取消
    # alert.dismiss()
    sleep(3)
    driver.quit()

    # 获取size的大小
    size = driver.find_element_by_id("userA").size
    print(size)

    # 获取文本
    text1 = driver.find_element_by_id("fwA").text
    print(text1)

    # 获取title
    title = driver.title
    print(title)

    # 获取当前页面的地址
    curl = driver.current_url
    print(curl)

    # 获取超链接<a>标签的属性值
    a = driver.find_element_by_id("fwA").get_attribute("href")
    print(a)


if __name__ == "__main__":
    byElement()


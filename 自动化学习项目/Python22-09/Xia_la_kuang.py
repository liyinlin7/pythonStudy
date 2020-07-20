from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


def xia_la_kuang():
    """
    22天第43节课和23天第45节课
    下拉框选择
    :return:
    """

    # ----不打开浏览器的前提下运行selenium--------
    chrome_options = Options()
    # chrome_options.add_argument("--headless")   # 不打开浏览器的前提下运行selenium
    # chrome_options.add_argument('--disable-gpu')   # 作用是针对现有bug的work around
    # chrome_options.add_argument('--remote-debugging-port=9222')  # 作用则是允许我们可以在另外一个浏览器中debug
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # ----不打开浏览器的前提下运行selenium--------

    # driver = webdriver.Chrome()
    url = r"E:\python项目\pythonStudy\自动化学习项目\Python22-09\static\html\注册A.html"
    driver.get(url)
    driver.maximize_window()  # 浏览器最大化
    # driver.set_window_size(2000, 1000)  # 设置浏览器大小，2000px宽，1000px高

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

    # 方法三 根据CSS,css_selector
    driver.find_element_by_css_selector("[value='gz']").click()
    sleep(3)

    # 方法四  select
    from selenium.webdriver.support.select import Select
    select = Select(driver.find_element_by_css_selector("#selectA"))
    select.select_by_visible_text("A北京")  # 包含点击click
    sleep(3)

    driver.quit()  # 关闭所有的webdriver窗口
    # driver.close()  # 关闭单个窗口


if __name__ == '__main__':
    xia_la_kuang()

from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


def chuang_kou_ju_bin():
    """
    23天第46节课
    iframe 的定位
    :return:
    """
    chrome_options = Options()
    # path = read_path.up_path
    chromdriver_path = r'D:\python\feitu_spark_selenium\Driver\chromedriver.exe'
    # ----不打开浏览器的前提下运行selenium--------
    # chrome_options.add_argument("--headless")   # 不打开浏览器的前提下运行selenium
    # chrome_options.add_argument('--disable-gpu')   # 作用是针对现有bug的work around
    # chrome_options.add_argument('--remote-debugging-port=9222')  # 作用则是允许我们可以在另外一个浏览器中debug
    # ----不打开浏览器的前提下运行selenium--------
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromdriver_path)
    # driver = webdriver.Chrome()
    url = r"D:\python\pythonStudy\自动化学习项目\Python22-09\static\html\注册A.html"
    driver.get(url)
    sleep(3)
    # 获取当前的窗口句柄
    # handle = '句柄'
    cur_handle = driver.current_window_handle
    print(cur_handle)
    s = driver.find_elements_by_css_selector("p[class='abc']")
    d = s[1].find_element_by_tag_name('label').get_attribute('innerHTML')
    # 点击“注册A”的超链接
    print(d)



if __name__ == '__main__':
    chuang_kou_ju_bin()

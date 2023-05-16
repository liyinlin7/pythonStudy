from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def Qreater_Chrome():
    chrome_options = Options()
    # ----不打开浏览器的前提下运行selenium--------
    # chrome_options.add_argument("--headless")   # 不打开浏览器的前提下运行selenium
    # chrome_options.add_argument('--disable-gpu')   # 作用是针对现有bug的work around
    # chrome_options.add_argument('--remote-debugging-port=9222')  # 作用则是允许我们可以在另外一个浏览器中debug
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 规避浏览器检查selenium脚本
    # ----不打开浏览器的前提下运行selenium--------
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver


if __name__ == "__main__":
    Qreater_Chrome()



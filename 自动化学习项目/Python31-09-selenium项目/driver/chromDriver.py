from selenium import webdriver
import logging
import logging.config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Common import read_path


# 读取日志配置文件
# upPath = read_path.up_path
# CON_LOG = upPath +'/Config/log.conf'
# logging.config.fileConfig(CON_LOG)
# logging = logging.getLogger()


def Qreater_Chrome():
    chrome_options = Options()
    path = read_path.up_path
    # chromdriver_path = path + '/Driver/chromedriver'  # Linux的
    chromdriver_path = path + '/Driver/chromedriver_118.exe'
    service = Service( chromdriver_path )
    # ----不打开浏览器的前提下运行selenium--------
    chrome_options.add_argument("--headless")   # 不打开浏览器的前提下运行selenium
    # chrome_options.add_argument( '--no-sandbox' ) # linux
    # chrome_options.add_argument( '--disable-dev-shm-usage' ) # linux
    # chrome_options.add_argument('--disable-gpu')   # 作用是针对现有bug的work around
    # chrome_options.add_argument('--remote-debugging-port=9222')  # 作用则是允许我们可以在另外一个浏览器中debug
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 规避浏览器检查selenium脚本
    # ----不打开浏览器的前提下运行selenium--------
    # driver = webdriver.Chrome(options=chrome_options, executable_path=chromdriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # driver = webdriver.Chrome(options=chrome_options)
    return driver


# if __name__ == "__main__":
#     from selenium.webdriver.Common.by import By
#     Driver = Qreater_Chrome()
#     Driver.maximize_window()
#     Driver.get("http://192.168.0.70/#/login")
#     a = Driver.find_element(By.NAME, 'userName')
#     a.send_keys("1231231231")


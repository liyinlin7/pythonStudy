# 创建基础页面类
from time import sleep


class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost"
        self.timeout = 10

    def _open(self, url):
        url_ = self.base_url+url
        print("被测试页url是：%s" % url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_, "不是我们要的地址!"

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

from selenium.webdriver.common.by import By
from pages.basePage import Page


# 百度搜索page，继承基础的Page类
class SearchPage(Page):
    # 创建搜索输入框及点击搜索按钮对象
    search_input = (By.ID, "kw")
    search_button = (By.ID, "su")

    def __init__(self, driver, base_url="http://www.baidu.com"):
        Page.__init__(self, driver, base_url)

    def gotoBaiduHomePage(self):
        print("打开首页", self.base_url)
        self.driver.get(self.base_url)

    def input_search_text(self, text="selenium"):
        print("输入搜索关键字：selenium")
        self.input_text(self.search_input, text)

    def click_search_btn(self):
        print("点击百度一下按钮")
        self.click(self.search_button)

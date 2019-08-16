import unittest
from selenium import webdriver
from pages.searchPage import SearchPage


# 百度搜索测试
class TestSearchPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Search(self):
        driver = self.driver
        url = "http://www.baidu.com"
        text = "selenium"
        # 期望验证的标题
        assert_title = "selenium_百度搜索"
        search_Page = SearchPage(driver, url)
        # 启动浏览器，访问百度首页
        search_Page.gotoBaiduHomePage()
        # 输入搜索词
        search_Page.input_search_text(text)
        # 单击“百度一下”
        search_Page.click_search_btn()
        # 验证标题
        self.assertEqual(search_Page.get_title(), assert_title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

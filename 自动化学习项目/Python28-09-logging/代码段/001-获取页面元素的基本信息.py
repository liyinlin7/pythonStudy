from selenium import webdriver
import unittest
import time


class New_Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Baidu(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        newElement = self.driver.find_element_by_xpath("//a[text()='新闻']")
        print('元素的标签名：', newElement.tag_name)
        print('元素的size:', newElement.size)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

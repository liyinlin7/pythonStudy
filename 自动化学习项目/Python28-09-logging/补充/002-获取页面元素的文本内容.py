from selenium import webdriver
import unittest
import time


class two_Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu1(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        aElement = self.driver.find_element_by_xpath("//*[@class='mnav'][2]")
        a_text = aElement.text
        self.assertEqual(a_text, "hao123")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

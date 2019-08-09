from selenium import webdriver
import unittest
import time


class N_Sogou(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def test_Baidu2(self):
        url="http://www.sogou.com"
        self.driver.get(url)
        searshBox = self.driver.find_element_by_id("query")
        print(searshBox.get_attribute("name"))
        searshBox.send_keys("selenium")
        print(searshBox.get_attribute("value"))
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

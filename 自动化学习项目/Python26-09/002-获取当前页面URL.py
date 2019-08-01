from selenium import webdriver
import time
import unittest


class VisitSogou(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def test_getCurrent(self):
        url="http://www.sogou.com/"
        self.driver.get(url)
        currentPageUrl=self.driver.current_url
        print(currentPageUrl)
        self.assertEqual(currentPageUrl,"https://www.sogou.com/","当前网页网址非预期")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()




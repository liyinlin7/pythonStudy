import unittest
from model import function, myunit
from page_object.LoginPage import *
from time import sleep


class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        print("test_login1_normal正在执行")
        po = LoginPage(self.driver)
        po.Login_action('wang', 'wang123456')
        sleep(5)
        function.insert_img(self.driver, "wang_001.png")
        self.assertEqual(po.type_loginPass_hint(), '我的空间')

        print("test_login1_normal执行结束")

    def test_login2_PasswdError(self):
        print("test_login2_PasswdError开始执行")
        po=LoginPage(self.driver)
        po.Login_action("wang", "wang")
        sleep(5)
        function.insert_img(self.driver, "wang_002_passwdError.png")
        self.assertEqual(po.type_loginErr_hint(), '加入收藏')

        print("test_login2_PasswdError执行结束")

    def test_login3_empty(self):
        print("test_login3_empty开始执行")
        po=LoginPage(self.driver)
        po.Login_action('', '')
        sleep(5)
        function.insert_img(self.driver, "wang_empty.png")
        self.assertEqual(po.type_loginErr_hint(), '加入收藏')

        print("test_login3_empty执行结束")


if __name__ == '__main__':
    unittest.main()




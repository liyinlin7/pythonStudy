from testcase.myunit import StartEnd
import unittest
import logging

class TestLogin(StartEnd):
    # csv_file='../test_data/account.csv'

    def test_login_001(self):
        logging.info('====test_login_001====')
        # l=LoginView(self.driver)
        # test_data=l.get_csv_data(self.csv_file,1)
        # l.login_action(test_data[0],test_data[1])
        # self.assertTrue(l.check_loginStatus())

    def test_login_002(self):
        logging.info('====test_login_002===')
        # l=LoginView(self.driver)
        # test_data=l.get_csv_data(self.csv_file,2)
        # l.login_action(test_data[0],test_data[1])
        # self.assertTrue(l.check_loginStatus())

    def test_login_error(self):
        logging.info('====test_login_error====')
        # l=LoginView(self.driver)
        # test_data=l.get_csv_data(self.csv_file,3)
        # l.login_action(test_data[0],test_data[1])
        # self.assertTrue(l.check_loginStatus(),msg='login fail!')

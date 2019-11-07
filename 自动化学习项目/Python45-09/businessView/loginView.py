import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):
    # 页面元素定位
    username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')

    button_mysefl=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    RightButton=(By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    logoutBtn=(By.ID,'com.tal.kaoyan:id/setting_logout_text')
    tipBtn=(By.ID,'com.tal.kaoyan:id/tip_commit')

    # 登录操作
    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('loging_action')
        logging.info('username is : %s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is : %s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

    # 判断登录是否成功
    def check_loginStatus(self):
        logging.info('check_loginStatus')

        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login fail')
            self.getScreenShot('LoginFail')
            return False
        else:
            logging.info('login success!')
            self.logout_action()
            return True

    # 退出登录
    def logout_action(self):
        logging.info('logout_action')
        self.driver.find_element(*self.RightButton).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tipBtn).click()






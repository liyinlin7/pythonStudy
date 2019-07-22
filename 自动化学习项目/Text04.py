from selenium import webdriver
import time


class DengLu(object):
    # 登陆的自动化
    __username = "admin"
    __password = "123456"
    __driver = webdriver.Chrome()

    @staticmethod
    def dengLu01():
        DengLu.getDriver().get("https://test.ececloud.cn/bos/#/login")
        time.sleep(7)
        DengLu.getDriver().find_element_by_name("username").clear()
        DengLu.getDriver().find_element_by_name("password").clear()
        # 填写用户密码，点击登陆
        DengLu.getDriver().find_element_by_xpath("//*[@id='app']/div/div/form/div[2]/div/div/input").send_keys(
            DengLu.getUsername())
        DengLu.getDriver().find_element_by_xpath("//*[@id='app']/div/div/form/div[3]/div/div/input").send_keys(
            DengLu.getPassword())
        DengLu.getDriver().find_element_by_xpath("//*[@id='app']/div/div/form/div[4]/div/button").click()
        time.sleep(10)
        # 点击机构列表
        DengLu.jiGouliebiao()

        DengLu.getDriver().quit()

    # 机构列表功能
    @staticmethod
    def jiGouliebiao():
        DengLu.getDriver().find_element_by_xpath("//*[@id='app']/div/div[2]/ul/div/a[1]/li").click()
        time.sleep(5)

    @classmethod
    def setUsername(cls, new_name):
        cls.__username = new_name

    @classmethod
    def getUsername(cls):
        return cls.__username

    @classmethod
    def setPassword(cls, new_password):
        cls.__password = new_password

    @classmethod
    def getPassword(cls):
        return cls.__password

    @classmethod
    def setDriver(cls, new_driver):
        cls.__driver = new_driver

    @classmethod
    def getDriver(cls):
        return cls.__driver


a = DengLu()
a.dengLu01()

from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Course:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://hz.lanhanba.com/demand/hall')
        self.driver.maximize_window()

    def get_first_category(self):
        """
        选择城市

        :return:
        """
        # self.select_list = Select(self.driver.find_element_by_id("select-test"))
        self.driver.find_element_by_xpath("//*[@id='vue-hall-filter']/div/div[2]/div/div[1]/input").click()
        time.sleep(2)
        # first_categories = self.driver.find_elements(By.XPATH, "/html/body/div[18]/div[1]/div[1]/ul/li")
        # print(len(first_categories))
        try:
            WebDriverWait(self.driver, 5).until(lambda x: x.find_elements(By.XPATH, "/html/body/div[19]/div[1]/div[1]/ul/li"))
        except Exception:
            print("没有找到")
        else:
            first_categories = self.driver.find_elements_by_xpath("/html/body/div[18]/div[1]/div[1]/ul/li")
            # time.sleep(2)
            print(len(first_categories))
            #
            # num = random.randint(0, len(first_categories) - 1)
            # # self.driver.find_elements()
            # print(num)
            # time.sleep(5)
            # first_categories[num].click()
            # first_category = first_categories[num]
            time.sleep(2)
            # return first_category


if __name__ == '__main__':
    course = Course()
    course.get_first_category()

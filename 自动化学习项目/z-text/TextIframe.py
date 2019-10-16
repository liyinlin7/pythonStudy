from selenium import webdriver
import time


def Text10():
    driver = webdriver.Chrome()
    driver.get("https://mail.163.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element_by_id("lbNormal").click()
    iframe = driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
    # driver_iframe =
    driver.switch_to.frame(iframe)
    # //*[@id='login-form']
    # driver.find_element_by_xpath("/html/body/div[2]/div[2]//from/div/div[1]/div[2]/input").send_keys("1600000000")
    driver.find_element_by_xpath("//*[@id='login-form']/div/div[1]/div[2]/input").send_keys("liyinlin77")
    driver.find_element_by_xpath("//*[@id='login-form']/div/div[3]/div[2]/input[2]").send_keys("pandannicc.")
    # driver.find_element_by_css_selector("[type='password']").send_keys("liyinlin77.")
    driver.find_element_by_id("dologin").click()
    # driver.switch_to.default_content()
    time.sleep(3)
    # 断言
    assert "liyinlin77@163.com" in driver.page_source, u"登录失败"
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    Text10()

from selenium import webdriver
import time


def Text10():
    driver = webdriver.Chrome()
    driver.get("https://mail.163.com/")
    driver.maximize_window()
    time.sleep(5)
    iframe = driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
    # driver_iframe =
    driver.switch_to.frame(iframe)
    #//*[@id='login-form']
    # driver.find_element_by_xpath("/html/body/div[2]/div[2]//from/div/div[1]/div[2]/input").send_keys("1600000000")
    driver.find_element_by_xpath("//*[@id='login-form']/div/div[1]/div[2]/input").send_keys("1600000000")
    time.sleep(20)

if __name__ == "__main__":
    Text10()

from capability import *

# xpath  //className+text
driver.find_element_by_xpath("//android.widget.EditText[@text='请输入用户名']").send_keys("DAwang001")

driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='3']").send_keys("DAwang001")

driver.find_element_by_xpath("//*[@ class='android.widget.Button']").click()
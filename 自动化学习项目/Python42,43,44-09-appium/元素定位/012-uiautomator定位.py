from capability import driver

# 第一种写法：
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys("DAwang002")
# 第二种写法：
username='new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")'
driver.find_element_by_android_uiautomator(username).send_keys("DAwang001")

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys("DAwang002")

driver.find_element_by_android_uiautomator\
    ('new UiSelector().className("android.widget.Button")')[1].click()
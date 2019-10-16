from capability import *
import random

# 进入注册界面 选择设置头像
driver.find_element_by_id("com.tal.kaoyan:id/login_register_text").click()
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_userheader").click()

images=driver.find_elements_by_id("com.tal.kaoyan:id/item_image")
images[3].click()
driver.find_element_by_id("com.tal.kaoyan:id/save").click()

# 填写注册信息
username='DAwang'+str(random.randint(1000,9999))
print('username:%s'%username)
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_username_edittext").send_keys(username)

password='DAwang'+str(random.randint(1000,9999))
print('password:%s'%password)
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_password_edittext").send_keys(password)

email='DAwang'+str(random.randint(1000,9999))+'@163.com'
print('email:%s'%email)
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_email_edittext").send_keys(email)

driver.find_element_by_id("com.tal.kaoyan:id/activity_register_register_btn").click()

# 院校选择
driver.find_element_by_id("com.tal.kaoyan:id/perfectinfomation_edit_school_name").click()
# 选择省份
driver.find_elements_by_id("com.tal.kaoyan:id/more_forum_title")[1].click()
# 选择具体院校
driver.find_elements_by_id("com.tal.kaoyan:id/university_search_item_name")[1].click()
# 选择专业
driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_major").click()
# 选择具体专业
driver.find_elements_by_id("com.tal.kaoyan:id/major_subject_title")[1].click()
driver.find_elements_by_id("com.tal.kaoyan:id/major_group_title")[2].click()
driver.find_elements_by_id("com.tal.kaoyan:id/major_search_item_name")[1].click()
# 点击进入考研帮
driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_goBtn").click()


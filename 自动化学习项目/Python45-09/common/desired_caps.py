from appium import webdriver
import yaml
import logging
import logging.config
import os

# 读取日志配置文件
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    # 读取yaml配置文件
    with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
        data=yaml.load(file)

    desired_cape = {}
    desired_cape['platformName'] = data['platformName']
    desired_cape['deviceName'] = data['deviceName']
    desired_cape['platformVersion'] = data['platformVersion']
    #     找到括号内的上一级路径（找到当前文件的绝对路径）  __file__ 魔法方法，指的的是当前文件
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 当前文件路径的上一级路径
    app_path = os.path.join(base_dir, 'app', data['appname'])  # 拼接路径
    desired_cape['app'] = app_path

    desired_cape['appPackage'] = data['appPackage']
    desired_cape['appActivity'] = data['appActivity']
    desired_cape['noReset'] = data['noReset']

    logging.info('start app...')
    driver = webdriver.Remote("http://"+str(data['ip'])+":"+str(data['port'])+"/wd/hub", desired_cape)
    driver.implicitly_wait(5)
    return driver

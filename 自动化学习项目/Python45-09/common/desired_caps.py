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

    base_dir=os.path.dirname(os.path.dirname(__file__))
    app_path=os.path.join(base_dir,'app',data['appname'])
    desired_cape['app'] =app_path

    desired_cape['appPackage'] = data['appPackage']
    desired_cape['appActivity'] = data['appActivity']
    desired_cape['noReset'] = data['noReset']

    logging.info('start app...')
    driver = webdriver.Remote("http://"+str(data['ip'])+":"+str(data['port'])+"/wd/hub", desired_cape)
    driver.implicitly_wait(5)
    return driver

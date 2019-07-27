import configparser  # 读取配置文件需要的包
import os  # 文件操作


class configTool(object):

    def __init__(self):
        self.conf = configparser.ConfigParser()

    # 得到配置文件当前路径
    def getCurrentPath(self):
        # 读取当前路径
        os.path.dirname(os.path.realpath(__file__))

    # 读取配置文件的路径
    def buid(self, configPath):
        self.conf.read(configPath)

    # 得到配置文件里的值
    def get(self, area, key):
        return self.conf.get(area, key)








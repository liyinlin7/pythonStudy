import yaml
import logging
import logging.config
import os

# 读取日志配置文件
CON_LOG = '../conf/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


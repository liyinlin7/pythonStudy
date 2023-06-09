import logging.config

# 读取日志配置文件
CON_LOG = '../conf/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


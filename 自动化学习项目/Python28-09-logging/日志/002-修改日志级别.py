import logging


# logging的默认级别为WANGING，只会显示WARNING，ERROR，CRITICAL级别的日志信息
logging.basicConfig(
    level=logging.DEBUG,  # 修改BUG的级别
    format="%(asctime)s %(name)s %(levelname)s %(message)s",  # 修改输出错误信息的内容
    datefmt="%Y-%m-%d %H:%M:%S",  # format用到了 asctime这个属性才有意义
    filename=r"d:\test.log",  # log日志输出的路径
    filemode="w"  # 清空文件内容，重新写新的日志信息；不要filemode的属性时，日志输出会向文件内容结尾处追加
)

try:
    print(4/2)
    logging.info("整除运算成功")
except:
    logging.error("除数不能为零")

import operator
import time
import logging
from demo.common import my_logger


def count_time(func):
    """
    :param func: 接收被装饰的函数
    """

    def wrapper(*args, **kwargs):
        # 函数调用之前获取一下当前的实际：start_time
        start_time = time.time()
        # 调用原功能函数
        res = func(*args, **kwargs)
        # 函数调用之后：再获取一下当前时间 end_time
        end_time = time.time()
        logging.info('{} 函数运行的时间为：{}'.format(func.__name__, end_time - start_time))
        return res
    return wrapper


if __name__ == '__main__':
    print(1)

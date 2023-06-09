import mysql.connector
from common.read_config import ReadConfig
from common import read_path
import logging
# from common import desired_caps
from common import my_logger


class DoMySql(object):
    '''
        链接mysql
    '''

    def __init__(self):
        self.test_mysql = eval(ReadConfig().read_config(read_path.conf_path, 'TEST_MYSQL', 'config'))
        self.pro_mysql = eval(ReadConfig().read_config(read_path.conf_path, 'PRO_MYSQL', 'config'))
        self.test_mysql_basketball = eval(ReadConfig().read_config(read_path.conf_path, 'TEST_MYSQL', 'basketball'))
        self.pro_mysql_basketball = eval(ReadConfig().read_config(read_path.conf_path, 'PRO_MYSQL', 'basketball'))
        self. test_mysql_rate = eval(ReadConfig().read_config(read_path.conf_path, 'TEST_MYSQL', 'config'))
        self.pro_mysql_rate = eval(ReadConfig().read_config(read_path.conf_path, 'PRO_MYSQL', 'rate'))

    def connect_mysql(self, env_flag):
        config = None
        if env_flag == 0:
            config = self.test_mysql
        elif env_flag == 1:
            config = self.pro_mysql
        cnn_bool = True
        cnn_conut = 0
        while cnn_bool:
            try:
                logging.info('开始连接数据库---------')
                cnn = mysql.connector.connect(**config)  # 建立连接
                logging.info('数据库连接成功')
                cnn_bool = False
                return cnn
            except Exception as e:
                cnn_conut += 1
                logging.error('第{}次连接数据库失败：{}'.format(cnn_conut, e))

    def connect_mysql_basketball(self, env_flag):
        config = None
        if env_flag == 0:
            config = self.test_mysql_basketball
        elif env_flag == 1:
            config = self.pro_mysql_basketball
        cnn_bool = True
        cnn_conut = 0
        while cnn_bool:
            try:
                logging.info('开始连接数据库---------')
                cnn = mysql.connector.connect(**config)  # 建立连接
                logging.info('数据库连接成功')
                cnn_bool = False
                return cnn
            except Exception as e:
                cnn_conut += 1
                logging.error('第{}次连接数据库失败：{}'.format(cnn_conut, e))

    def connect_mysql_rate(self, env_flag):
        config = None
        if env_flag == 0:
            config = self.test_mysql
        elif env_flag == 1:
            config = self.pro_mysql_rate
        cnn_bool = True
        cnn_conut = 0
        while cnn_bool:
            try:
                logging.info('开始连接数据库---------')
                cnn = mysql.connector.connect(**config)  # 建立连接
                logging.info('数据库连接成功')
                cnn_bool = False
                return cnn
            except Exception as e:
                cnn_conut += 1
                logging.error('第{}次连接数据库失败：{}'.format(cnn_conut, e))

    def test_connection(self, cnn):
        """测试数据库是否正常连接"""
        try:
            cnn.ping()
            logging.info('ping成功')
            result = True
        except Exception as e:
            logging.info('ping失败：{}'.format(e))
            result = False
        return result

    def select(self, cnn, sql, env_flag, state=0):
        """
        查询数据库
        :param cnn: 数据库连接对象
        :param sql: 执行的sql
        :param state: 如果只查询一条数据，传1；查询多条数据，传0
        :return:返回查询结果，嵌套字典列表形式，key为对应的字段名，如：[{'team_id': 1107}, {'team_id': 1108}]
        """
        # 判断数据库能否正常连接，如果不能连接，则重新建立连接
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect_mysql(env_flag=env_flag)
        cursor = db.cursor()  # 创建一个游标
        # logging.info('开始执行sql：{}'.format(sql))
        cursor.execute(sql)  # 执行SQL语句
        desc = cursor.description  # 得到域的名字
        if state == 1:
            res = cursor.fetchone()  # 返回的数据类型是元组
        else:
            res = cursor.fetchall()  # 返回的数据类型是列表,里面的元素是元组
        # print(res)
        data_dic = [dict(zip([col[0] for col in desc], row)) for row in res]
        cursor.close()
        return data_dic

    def select_basketball(self, cnn, sql, env_flag, state=0):
        """
        查询数据库
        :param cnn: 数据库连接对象
        :param sql: 执行的sql
        :param state: 如果只查询一条数据，传1；查询多条数据，传0
        :return:返回查询结果，嵌套字典列表形式，key为对应的字段名，如：[{'team_id': 1107}, {'team_id': 1108}]
        """
        # 判断数据库能否正常连接，如果不能连接，则重新建立连接
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect_mysql_basketball(env_flag=env_flag)
        cursor = db.cursor()  # 创建一个游标
        # logging.info('开始执行sql：{}'.format(sql))
        cursor.execute(sql)  # 执行SQL语句
        desc = cursor.description
        if state == 1:
            res = cursor.fetchone()  # 返回的数据类型是元组
        else:
            res = cursor.fetchall()  # 返回的数据类型是列表,里面的元素是元组
        data_dic = [dict(zip([col[0] for col in desc], row)) for row in res]
        cursor.close()
        return data_dic

    def select_rate(self, cnn, sql, env_flag, state=0):
        """
        查询数据库
        :param cnn: 数据库连接对象
        :param sql: 执行的sql
        :param state: 如果只查询一条数据，传1；查询多条数据，传0
        :return:返回查询结果，嵌套字典列表形式，key为对应的字段名，如：[{'team_id': 1107}, {'team_id': 1108}]
        """
        # 判断数据库能否正常连接，如果不能连接，则重新建立连接
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect_mysql_rate(env_flag=env_flag)
        cursor = db.cursor()  # 创建一个游标
        # logging.info('开始执行sql：{}'.format(sql))
        cursor.execute(sql)  # 执行SQL语句
        desc = cursor.description  # 得到域的名字
        if state == 1:
            res = cursor.fetchone()  # 返回的数据类型是元组
        else:
            res = cursor.fetchall()  # 返回的数据类型是列表,里面的元素是元组
        # print(res)
        data_dic = [dict(zip([col[0] for col in desc], row)) for row in res]
        cursor.close()
        return data_dic


if __name__ == '__main__':
    Do = DoMySql()
    Do.connect_mysql_basketball(1)

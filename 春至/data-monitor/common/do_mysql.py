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
        self.env = ReadConfig().read_config(read_path.conf_path, 'ENV', 'env')
        self.mysql_host_centon = ReadConfig().read_config(read_path.conf_path, 'MYSQL', 'host_centon')
        self.mysql_user = ReadConfig().read_config(read_path.conf_path, 'MYSQL', 'user')
        self.mysql_pwd = ReadConfig().read_config(read_path.conf_path, 'MYSQL', 'password')
        self.mysql_port = ReadConfig().read_config(read_path.conf_path, 'MYSQL', 'port')
        self.mysql_auth_plugin = ReadConfig().read_config(read_path.conf_path, 'MYSQL', 'auth_plugin')
        self.myysql_centon_config = {'host': self.mysql_host_centon,
                                       'user': self.mysql_user,
                                       'password': self.mysql_pwd,
                                       'port': int(self.mysql_port),
                                       'auth_plugin': self.mysql_auth_plugin}
        self.mysql_host_basic = ReadConfig().read_config(read_path.conf_path, 'MYSQL', 'host_basic')
        self.myysql_basic_config = {'host': self.mysql_host_basic,
                                     'user': self.mysql_user,
                                     'password': self.mysql_pwd,
                                     'port': int(self.mysql_port),
                                     'auth_plugin': self.mysql_auth_plugin}
        self.cnn_centon = self.connect_mysql_centon()
        self.cnn_basic = self.connect_mysql_basic()

    def cnn_centon_def(self):
        return self.cnn_centon

    def cnn_basic_def(self):
        return self.cnn_basic

    def connect_mysql_centon(self):
        config = self.myysql_centon_config
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

    def connect_mysql_basic(self):
        config = self.myysql_basic_config
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
            # logging.info('ping成功')
            result = True
        except Exception as e:
            logging.info('ping失败：{}'.format(e))
            result = False
        return result

    def select_centon(self, cnn, sql, state=0):
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
            db = self.connect_mysql_centon()
            self.cnn_centon = db
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

    def select_basic(self, cnn, sql, state=0):
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
            db = self.connect_mysql_basic()
            self.cnn_basic = db
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

    def update_centon(self, cnn, sql):
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect_mysql_centon()
        cursor = db.cursor()  # 创建一个游标
        # logging.info('开始执行sql：{}'.format(sql))
        try:
            cursor.execute(sql)  # 执行SQL语句
            db.commit()
            print(cursor.rowcount, "条修改成功。")
        except Exception as e:
            logging.error('修改失败:{}'.format(e))
            logging.error('出错SQL是：{}'.format(sql))
        cursor.close()
        db.close()

    def update_basic(self, cnn, sql):
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect_mysql_basic()
        cursor = db.cursor()  # 创建一个游标
        # logging.info('开始执行sql：{}'.format(sql))
        try:
            cursor.execute(sql)  # 执行SQL语句
            db.commit()
            print(cursor.rowcount, "条修改成功。")
        except Exception as e:
            logging.error('修改失败:{}'.format(e))
            logging.error('出错SQL是：{}'.format(sql))
        cursor.close()
        db.close()

    def delted_basic(self, cnn, sql):
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect_mysql_basic()
        cursor = db.cursor()  # 创建一个游标
        # logging.info('开始执行sql：{}'.format(sql))
        try:
            cursor.execute(sql)  # 执行SQL语句
            db.commit()
            print(cursor.rowcount, "条删除成功。")
        except Exception as e:
            logging.error('删除失败:{}'.format(e))
            logging.error('出错SQL是：{}'.format(sql))
        cursor.close()
        db.close()

if __name__ == '__main__':
    Do = DoMySql()
    Do.connect_mysql_centon()

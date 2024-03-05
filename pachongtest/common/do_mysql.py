import mysql.connector
from common.read_config import ReadConfig
from common import read_path


class DoMySql(object):
    '''
        链接mysql
    '''

    def __init__(self):
        self.mysql = eval(ReadConfig().read_config(read_path.conf_path, 'TEST_MYSQL', 'config'))

    def connect_mysql(self):
        config = self.mysql
        cnn_bool = True
        cnn_conut = 0
        while cnn_bool:
            try:
                # print('开始连接数据库---------')
                cnn = mysql.connector.connect(**config)  # 建立连接
                # print('数据库连接成功')
                cnn_bool = False
                return cnn
            except Exception as e:
                cnn_conut += 1
                print('第{}次连接数据库失败：{}'.format(cnn_conut, e))

    def test_connection(self, cnn):
        """测试数据库是否正常连接"""
        try:
            cnn.ping()
            # print('ping成功')
            result = True
        except Exception as e:
            print('ping失败：{}'.format(e))
            result = False
        return result

    def select(self, cnn, sql, state=0):
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
            db = self.connect_mysql()
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

    def insert(self, cnn, sql):
        """插入数据库"""
        # 判断数据库能否正常连接，如果不能连接，则重新建立连接
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect_mysql()
        cursor = db.cursor()  # 创建一个游标
        try:
            cursor.execute(sql)  # 执行SQL语句
            print(cursor.rowcount, "记录插入成功。")
        except Exception as e:
            print('记录插入失败:{}'.format(e))
            print('出错SQL是：{}'.format(sql))
        cnn.commit()
        return cursor.lastrowid


if __name__ == '__main__':
    Do = DoMySql()
    Do.connect_mysql()

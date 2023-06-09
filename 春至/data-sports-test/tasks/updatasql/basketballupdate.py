import mysql.connector
import logging
from common import my_logger


class BasketBallUpdate(object):
    '''
        篮球数据库修改操作表
    '''
    def __init__(self, env_flag):
        self.PRO_config = {'host': '172.16.0.121',   # 172.16.0.121:3306 内网； 47.57.231.50:11236  外网
                  'user': 'root',
                  'password': '0TNU0ogYb7TcrCfs',    # 修改权限密码
                  'port': 3306,
                  'auth_plugin': 'mysql_native_password'
                  }
        self.TEST_config = {'host': '42.194.216.189',
                      'user': 'root',
                      'password': 'Winter123',
                      'port': 3306,
                      'auth_plugin': 'mysql_native_password'
                      }
        self.env_flag = env_flag

    def connect_mysql_update(self, env_flag):
        config = None
        if env_flag == 0:
            config = self.TEST_config
        elif env_flag == 1:
            config = self.PRO_config
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

    def update_mysql_basic(self, cnn, sql):
        '''
            修改语句
        :param cnn:
        :param sql:
        :return:
        '''
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect_mysql_update(self.env_flag)
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


    def update_basketball_mathc(self):
        sql = '''
            update  `sports-basketball`.ex_series set audit =3 where  match_start_time <= unix_timestamp()  - 3600*2 and audit=1 and p_id = 0;
        '''
        cnn = self.connect_mysql_update(env_flag=self.env_flag)
        self.update_mysql_basic(cnn=cnn, sql=sql)


if __name__ == '__main__':
    f = BasketBallUpdate(1)
    f.update_basketball_mathc()


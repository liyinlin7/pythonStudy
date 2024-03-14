from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from common import read_path
from common.read_config import ReadConfig
import logging
from common import my_logger


class MySqlDriver(object):
    '''
        链接mysql
    '''

    def __init__(self):
        self.test_mysql = eval(ReadConfig().read_config(read_path.conf_path, 'TEST_MYSQL', 'Config'))
        # self.engine = create_engine('mysql+pymysql://username:password@localhost/dbname')

    def connect_mysql(self, env_flag):
        config = None
        if env_flag == 0:
            config = self.test_mysql
        username = config.get("user")
        password = config.get("password")
        local_address = config.get("host")
        dbname = config.get("database")
        cnn_bool = True
        cnn_conut = 0
        while cnn_bool:
            try:
                logging.info('开始连接数据库---------')
                engine = create_engine( f'mysql+pymysql://{username}:{password}@{local_address}/{dbname}' )  # 建立连接
                logging.info('数据库连接成功')
                cnn_bool = False
                Session = sessionmaker( bind=engine )
                session = Session()
                return engine, session
            except Exception as e:
                cnn_conut += 1
                logging.error('第{}次连接数据库失败：{}'.format(cnn_conut, e))

    def test_connection(self, engine):
        """测试数据库是否正常连接"""
        try:
            engine.connect()
            logging.info('ping成功')
            result = True
        except Exception as e:
            logging.info('ping失败：{}'.format(e))
            result = False
        return result

if __name__ == '__main__':
    Do = MySqlDriver()
    engine, session = Do.connect_mysql(0)
    Do.test_connection(engine)

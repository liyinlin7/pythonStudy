import logging
import mysql.connector


class StatMysqlOperation(object):
    '''
        统计表数据操作
    '''
    def __init__(self):
        self.myysql_basic_config = {'host': 'rm-3ns8nci2q9lg6t9855o.mysql.rds.aliyuncs.com',
                                    'user': 'winter',
                                    'password': '0TNU0ogYb7TcrCfs',
                                    'port': 3306,
                                    'auth_plugin': 'mysql_native_password'}  # 线上外网链接
        # self.myysql_basic_config = {'host': '121.196.18.148',
        #                             'user': 'root',
        #                             'password': 'WinterData123',
        #                             'port': 3306,
        #                             'auth_plugin': 'mysql_native_password'
        #                             }  # 测试外网链接

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
            logging.info('ping成功')
            result = True
        except Exception as e:
            logging.info('ping失败：{}'.format(e))
            result = False
        return result

    def delted_mysql_basic(self, cnn, sql):
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

    def data_stat(self, match_id):
        '''
            根据小局ID删除统计表相关小局数据
        :return:
        '''
        # sql = f'''delete  FROM `data-stats`.dota_team where match_id in ({match_id});
        #     delete  FROM `data-stats`.dota_player where match_id in ({match_id});
        #     delete  FROM `data-stats`.dota_hero where match_id in ({match_id});
        #     delete  FROM `data-stats`.dota_event where match_id in ({match_id});'''
        sql = f'''delete  FROM `data-stats`.dota_team where series_id in ({match_id});
                    delete  FROM `data-stats`.dota_player where series_id in ({match_id});
                    delete  FROM `data-stats`.dota_hero where series_id in ({match_id});
                    delete  FROM `data-stats`.dota_event where series_id in ({match_id});'''
        # sql = f'''delete  FROM `data-stats`.csgo_team where series_id in ({match_id});
        #             delete  FROM `data-stats`.csgo_player where series_id in ({match_id});
        #             delete  FROM `data-stats`.csgo_map where series_id in ({match_id});
        #             delete  FROM `data-stats`.csgo_event where series_id in ({match_id});'''
        a = sql.split("\n            ")
        print(a)
        cnn = self.connect_mysql_basic()
        for i in a:
            self.delted_mysql_basic(cnn=cnn, sql=i)


if __name__ == '__main__':
    cc = StatMysqlOperation()
    cc.data_stat(1607418768)   #48543,48544

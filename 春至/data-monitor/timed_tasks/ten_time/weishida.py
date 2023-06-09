from common.do_mysql import DoMySql


class WeiShiDa(object):
    '''
    卫视达1个小时待审核数据
    '''

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.doMysql = mysql_cnn


    def weishida_examine(self):
        sql = '''
            SELECT * FROM `data-center`.ex_series where source = 10 and  start_time >= unix_timestamp() and  start_time <=  unix_timestamp() + 3600 and p_id = 0 and audit != 3;
        '''
        datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        if len(datas) > 0:
            return "电竞卫视达1个小时内有待审核比赛"
        else:
            return ''

if __name__ == '__main__':
    WeiShiDa = WeiShiDa('release', DoMySql().cnn_centon, DoMySql().cnn_basic, DoMySql()).weishida_examine

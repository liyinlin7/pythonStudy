from common.do_mysql import DoMySql


class WeiShiDa(object):
    '''
       卫视达
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_basketball = self.do_mysql.connect_mysql_basketball(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn_football = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn_rate = self.do_mysql.connect_mysql_rate(env_flag=env_flag)  # 0是测试，1是线上


    def weishida_others_examine(self):
        sql = '''
            SELECT * FROM `sports-others`.ex_series where source = 10 and  match_start_time >= unix_timestamp()  and   match_start_time <= unix_timestamp() + 3600 and p_id = 0 and audit != 3;
        '''
        datas = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        if len(datas) > 0:
            return "其他体育卫视达1个小时内有待审核比赛；"
        else:
            return ''

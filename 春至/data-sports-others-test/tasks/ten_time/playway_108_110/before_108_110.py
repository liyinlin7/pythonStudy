from common.do_mysql import DoMySql


class Before108_110(object):
    '''
       赛前盘指数数据
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_basketball = self.do_mysql.connect_mysql_basketball(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn_football = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn_rate = self.do_mysql.connect_mysql_rate(env_flag=env_flag)  # 0是测试，1是线上

    def before_option_status_108_110(self):
        ex_match_sql = '''
            SELECT * FROM `sports-others`.ex_series where p_id  != 0 and audit not in (1,3) and sport_id in (108,109,110) and source = 2  and status not in (1,3,4,5);
        '''
        mathcs = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=ex_match_sql, env_flag=self.env_flag)
        ex_mathc_ids = set()
        for i in mathcs:
            ex_mathc_ids.add(i['ex_id'])
        match_ex_id_tuple = tuple(ex_mathc_ids)
        if len(match_ex_id_tuple) == 1:
            match_ex_id_tuple = str(match_ex_id_tuple).replace(',', '')
        else:
            match_ex_id_tuple = match_ex_id_tuple
        # print(match_ex_id_tuple)
        market_id_sql = f'''
                    SELECT * FROM `sports-rate-center`.option where market_type_id in 
                    (SELECT id FROM `sports-rate-center`.market_type where level_id in {match_ex_id_tuple}  and is_inplay=1);
                '''
        if self.env_flag == 0:
            option_datas = self.do_mysql.select(cnn=self.cnn, sql=market_id_sql, env_flag=self.env_flag)
        else:
            option_datas = self.do_mysql.select_rate(cnn=self.cnn_rate, sql=market_id_sql, env_flag=self.env_flag)
        err_option_ex_id = set()
        for i in option_datas:
            if i['option_status'] == 1:
                err_option_ex_id.add(i['ex_id'])
        # print(err_option_ex_id)
        if len(err_option_ex_id) != 0:
            print(f"排台棒：比赛已经开始，但是赛前盘的选项还是开盘（option_ex_id）：{err_option_ex_id}")
            return f"排台棒：比赛已经开始，但是赛前盘的选项还是开盘（option_ex_id）：{err_option_ex_id}"
        else:
            return ''


if __name__ == '__main__':
    f = Before108_110(1)
    f.before_option_status_108_110()
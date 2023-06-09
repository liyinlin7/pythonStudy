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
        # self.cnn_rate = self.do_mysql.connect_mysql_rate(env_flag=env_flag)  # 0是测试，1是线上

    def weishida_foot_basket_examine(self):
        msg = self.weishida_football_examine() + self.weishida_basketball_examine()
        print(msg)
        if msg != '':
            return msg
        else:
            return ''

    def weishida_football_examine(self):
        sql = '''
            SELECT * FROM `sports-soccer-match`.ex_match where source not in (2,4) and  match_start_time >= unix_timestamp()  and   match_start_time <= unix_timestamp() + 3600 and p_id = 0 and audit != 3;
        '''
        datas = self.do_mysql.select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        if len(datas) > 0:
            return "足球1个小时内有待审核比赛；"
        else:
            return ''

    def weishida_basketball_examine(self):
        sql = '''
                    SELECT * FROM `sports-basketball`.ex_series where source not in (2,4) and  match_start_time >= unix_timestamp()  and   match_start_time <= unix_timestamp() + 3600 and p_id = 0 and audit != 3;
                '''
        datas = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        if len(datas) > 0:
            return "篮球1个小时内有待审核比赛；"
        else:
            return ''


if __name__ == '__main__':
    WeiShiDa(1).weishida_foot_basket_examine()
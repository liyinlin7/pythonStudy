from common.do_mysql import DoMySql


class SeriesStatausThirty_football(object):
    '''
        根据系列赛判断指数玩法和选项状态
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_basketball = self.do_mysql.connect_mysql_basketball(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn_rate = self.do_mysql.connect_mysql_rate(env_flag=env_flag)  # 0是测试，1是线上

    def series_status_market_status_onehours(self):
        '''
            赛程开始时间后3个小时
        :return:
        '''
        sql = '''
            SELECT * FROM `sports-soccer-match`.ex_match  where source in (6,7)  and p_id != 0
            and match_start_time >  UNIX_TIMESTAMP() - 3600 * 36  and match_start_time + 3600 *6 < unix_timestamp()
			order by ex_id desc;
        '''
        ex_id_set = set()
        data = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `sports-lottery-center`.market where level_id in {level_id_tuple} order by level_id desc;
            '''
            if self.env_flag == 0:
                play_datas = self.do_mysql.select(cnn=self.cnn, sql=play_sql, env_flag=self.env_flag)
            else:
                play_datas = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=play_sql, env_flag=self.env_flag)
            # print(len(play_datas))
            err_market_status_1 = set()
            err_market_status_2 = set()
            for i in level_id_tuple:
                for y in play_datas:
                    if i == y['level_id']:
                        if y['market_status'] == 1:
                            err_market_status_1.add(y['market_id'])
                        elif y['market_status'] == 2:
                            err_market_status_2.add(y['market_id'])
            if len(err_market_status_1) > 0:
                err_str += f'足球：赛程开始时间后3个小时,玩法状态还是1的数据为（market_type的market_id）：{err_market_status_1}'
            if len(err_market_status_2) > 0:
                err_str += f'足球：赛程开始时间后3个小时,玩法状态还是2的数据为（market_type的market_id）：{err_market_status_2}'
            if len(err_str) > 0:
                return err_str
            else:
                return ''
        else:
            return ''

    def series_status_option_status_onehours(self):
        '''
            比赛结束后6小时
        :return:
        '''
        sql = '''
             SELECT * FROM `sports-soccer-match`.ex_match  where source in (6,7)  and p_id != 0
            and match_start_time >  UNIX_TIMESTAMP() - 3600 * 36  and match_start_time + 3600 *6 < unix_timestamp()
			order by ex_id desc;
        '''
        ex_id_set = set()
        data = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `sports-lottery-center`.option where market_id in (
                SELECT id FROM `sports-lottery-center`.market where level_id in {level_id_tuple} order by level_id desc);
            '''
            if self.env_flag == 0:
                play_datas = self.do_mysql.select(cnn=self.cnn, sql=play_sql, env_flag=self.env_flag)
            else:
                play_datas = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=play_sql, env_flag=self.env_flag)
            print(len(play_datas))
            err_option_status_1 = set()
            err_option_status_2 = set()
            err_option_status_3 = set()
            for y in play_datas:
                if y['option_status'] == 1:
                    err_option_status_1.add(y['ex_id'])
                elif y['option_status'] == 2:
                    err_option_status_2.add(y['ex_id'])
                elif y['option_status'] == 3:
                    err_option_status_3.add(y['ex_id'])
            if len(err_option_status_1) > 0:
                err_str += f'足球：赛程开始时间后6个小时,选项状态还是1的数据为（option的ex_id）：{err_option_status_1}'
            if len(err_option_status_2) > 0:
                err_str += f'足球：赛程开始时间后6个小时,选项状态还是2的数据为（option的ex_id）：{err_option_status_2}'
            if len(err_option_status_3) > 0:
                err_str += f'足球：赛程开始时间后6个小时,选项状态还是3的数据为（option的ex_id）：{err_option_status_3}'
            if len(err_str) > 0:
                    print(err_str)
                    return err_str
            else:
                return ''
        else:
            return ''


if __name__ == '__main__':
    ss = SeriesStatausThirty_football(1)
    ss.series_status_market_status_onehours()
    ss.series_status_option_status_onehours()
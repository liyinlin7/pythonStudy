from common.do_mysql import DoMySql


class TwoHoursSeries(object):
    '''
        系列赛开始时间为当前时间前后1小时
    '''

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.doMysql = mysql_cnn

    def today_series_id(self):
        '''
            系列赛开始时间为当前时间前后1小时
        :param env_flag:
        :return:
        '''
        sql = '''
                SELECT * FROM `data-center`.ex_series where deleted=1 and p_id != 0 and source =1 and start_time >= (UNIX_TIMESTAMP() - 3600)  
                and start_time <= (UNIX_TIMESTAMP() + 3600) ;
            '''
        datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        series_ex_id_list = set()
        series_ex_id_str = None
        for data in datas:
            series_ex_id_list.add(data.get('ex_id'))
        if len(series_ex_id_list) == 1:
            series_ex_id_str = str(tuple(series_ex_id_list)).replace(',', '')
        elif len(series_ex_id_list) > 1:
            series_ex_id_str = str(tuple(series_ex_id_list))
        if len(series_ex_id_list) != 0:
            mark_sql = '''
                        SELECT * FROM `data-rate-center`.market_type where level_id in {};
                    '''.format(series_ex_id_str)
            print(mark_sql)
            if self.env_flag == 'release':
                market_res = self.doMysql.select_basic(cnn=self.cnn_basic, sql=mark_sql)
            elif self.env_flag == 'develop':
                market_res = self.doMysql.select_centon(cnn=self.cnn_centon, sql=mark_sql)
            market_err = self.market_history_2hours(market_res)
            print("错误数据:", market_err)
            if market_err is None:
                pass
            else:
                return market_err
        else:
            pass

    def market_history_2hours(self, market_res):
        '''
            market_history 表
        :return:
        '''
        market_id_list = set()
        for data in market_res:
            market_id_list.add(data.get('market_id'))
        option_history_sql = '''
                SELECT * FROM `data-rate-center`.market_history where market_id in {};                
            '''.format(tuple(market_id_list))
        if self.env_flag == 'release':
            option_history_res = self.doMysql.select_basic(cnn=self.cnn_basic, sql=option_history_sql)
        elif self.env_flag == 'develop':
            option_history_res = self.doMysql.select_centon(cnn=self.cnn_centon, sql=option_history_sql)
        option_id_null = set()
        option_creattime_null = set()
        option_rate_null = set()
        option_is_winner_null = set()
        option_market_status_null = set()
        option_option_status_null = set()
        option_market_status5_is_winner_null = set()
        option_is_winner_market_status5_null = set()
        market_type_id_list = set()
        err_str = '系列赛开始时间为当前时间前后1小时，market_history中（market_id）：'
        old_err_str_len = len(err_str)
        for data in option_history_res:
            market_type_id_list.add(data.get('market_id'))
            # 指数变化option_id为null
            if data.get('option_id') is None or data.get('option_id') == '':
                option_id_null.add(data.get('market_id'))
            # 指数变化create_time为null
            if data.get('create_time') is None or data.get('create_time') == '':
                option_creattime_null.add(data.get('market_id'))
            # 指数变化rate为null
            if data.get('rate') is None or data.get('rate') == '':
                option_rate_null.add(data.get('market_id'))
            # 指数变化is_winner不等于（3, 1, 2）
            if data.get('is_winner') is None or data.get('is_winner') == '' or data.get('is_winner') not in (1, 2, 3):
                option_is_winner_null.add(data.get('market_id'))
            # 指数变化 market_status不等于（1,2,3,4,5）
            if data.get('market_status') is None or data.get('market_status') == '':
                option_market_status_null.add(data.get('market_id'))
            # 指数变化option_status不等于（1, 2, 3, 4, 5）
            if data.get('option_status') is None or data.get('option_status') == '':
                option_option_status_null.add(data.get('market_id'))
            # 指数变化option_status为5，is_winner不等于（3, 2）
            if data.get('option_status') == 5:
                if data.get('is_winner') not in (3, 2):
                    option_market_status5_is_winner_null.add(data.get('market_id'))
            # 指数变化is_winner为3或2，option_status不等于5
            if data.get('is_winner') in (3, 2):
                if data.get('option_status') != 5:
                    option_is_winner_market_status5_null.add(data.get('market_id'))
        if len(option_id_null) != 0:
            err_str += f'指数变化option_id为null的数据为：{str(option_id_null)}；\n'
        if len(option_creattime_null) != 0:
            err_str += f'指数变化create_time为null的数据为：{str(option_creattime_null)}；\n'
        if len(option_rate_null) != 0:
            err_str += f'指数变化rate为null的数据为：{str(option_rate_null)}；\n'
        if len(option_is_winner_null) != 0:
            err_str += f'指数变化is_winner不等于（3, 1, 2）的数据为：{str(option_is_winner_null)}；\n'
        if len(option_market_status_null) != 0:
            err_str += f'指数变化 market_status不等于（1,2,3,4,5）的数据为：{str(option_market_status_null)}；\n'
        if len(option_option_status_null) != 0:
            err_str += f'指数变化option_status不等于（1, 2, 3, 4, 5）的数据为：{str(option_option_status_null)}；\n'
        if len(option_market_status5_is_winner_null) != 0:
            err_str += f'指数变化option_status为5，is_winner不等于（3, 2）的数据为：{str(option_market_status5_is_winner_null)}；\n'
        if len(option_is_winner_market_status5_null) != 0:
            err_str += f'指数变化is_winner为3或2，option_status不等于5的数据为：{str(option_is_winner_market_status5_null)}；\n'
        if len(err_str) > old_err_str_len:
            return err_str + '\n'
        else:
            pass


if __name__ == '__main__':
    t = TwoHoursSeries(1)
    t.today_series_id()


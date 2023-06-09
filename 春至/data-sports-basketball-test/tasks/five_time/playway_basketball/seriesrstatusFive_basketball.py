from common.do_mysql import DoMySql


class SeriesStatausFive_basketball(object):
    '''
        根据赛程判断指数玩法和选项状态
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_basketball = self.do_mysql.connect_mysql_basketball(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn_rate = self.do_mysql.connect_mysql_rate(env_flag=env_flag)  # 0是测试，1是线上


    def series_status_market_status_basketball(self):
        sql = '''
            SELECT * FROM `sports-basketball`.ex_series where source in (6,7)  and p_id != 0 and match_start_time > unix_timestamp()-3600*24*3 and status=10 order by ex_id desc;
        '''
        ex_id_set = set()
        data = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        print(level_id_tuple)
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `sports-lottery-center`.market where level_id in {level_id_tuple} order by level_id desc;
            '''
            if self.env_flag == 0:
                play_datas = self.do_mysql.select(cnn=self.cnn, sql=play_sql, env_flag=self.env_flag)
            else:
                play_datas = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=play_sql, env_flag=self.env_flag)
            print(len(play_datas))
            err_market_status = set()
            for i in level_id_tuple:
                for y in play_datas:
                    if i == y['level_id']:
                        if y['market_status'] == 1:
                            err_market_status.add(y['market_id'])
            if len(err_market_status) > 0:
                err_str += f'篮球：赛程已结束,玩法状态还是1的数据为（market_type的market_id）：{err_market_status}'
            print(err_str)
            if len(err_str) > 0:
                return err_str
            else:
                return ''
        else:
            return ''

    def series_status_market_null_basketball(self):
        sql = '''
            SELECT * FROM `sports-basketball`.ex_series  where source in (6,7)  and p_id != 0 and match_start_time >= UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE))-3600*8 
            and match_start_time < UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE) + INTERVAL 1 DAY)-3600*8 and status  not in (10,11,12,13,14,15,16,100) order by ex_id desc;
        '''
        ex_id_set = set()
        data = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        if len(level_id_tuple) == 1:
            level_id_tuple = str(level_id_tuple).replace(',', '')
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `sports-lottery-center`.market where level_id in {level_id_tuple} order by level_id desc;
            '''
            print(play_sql)
            if self.env_flag == 0:
                play_datas = self.do_mysql.select(cnn=self.cnn, sql=play_sql, env_flag=self.env_flag)
            else:
                play_datas = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=play_sql, env_flag=self.env_flag)
            print(len(play_datas))
            play_level_id_set = set()
            for i in play_datas:
                play_level_id_set.add(i['level_id'])
            ex_id_list = list(ex_id_set)
            for i in play_level_id_set:
                if i in ex_id_list:
                    ex_id_list.remove(i)
            if len(ex_id_list) > 0:
                err_str += f'篮球：已过审的赛程，无指数详情数据,赛程ex_id为：{ex_id_list}'
            print(err_str)
            if len(err_str) > 0:
                return err_str
            else:
                return ''
        else:
            return ''


if __name__ == '__main__':
    ss = SeriesStatausFive_basketball(1)
    ss.series_status_market_status_basketball()
    ss.series_status_market_null_basketball()
    # ss.series_status_market_null()
from common.do_mysql import DoMySql


class SeriesStataus(object):
    '''
        根据系列赛判断指数玩法和选项状态
    '''

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.doMysql = mysql_cnn

    def series_status_market_status_onehours(self):
        '''
            比赛结束后5分钟
        :return:
        '''
        sql = '''
            SELECT * FROM `data-center`.ex_series where source=1 and deleted=1 and p_id != 0 
            and start_time >= (UNIX_TIMESTAMP() - 3600*24)
			and status=3 having end_time+60*5 < UNIX_TIMESTAMP() order by ex_id desc;
        '''
        ex_id_set = set()
        data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `data-rate-center`.market_type where level_id in {level_id_tuple} order by level_id desc;
            '''
            if self.env_flag == 'release':
                play_datas = self.doMysql.select_basic(cnn=self.cnn_basic, sql=play_sql)
            elif self.env_flag == 'develop':
                play_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=play_sql)
            # print(len(play_datas))
            err_market_status = set()
            for i in level_id_tuple:
                for y in play_datas:
                    if i == y['level_id']:
                        if y['market_status'] in (1, 2):
                            err_market_status.add(y['market_id'])
            if len(err_market_status) > 0:
                err_str += f'系列赛已结束后5分钟,玩法状态还是1,2的数据为（market_type的market_id）：{err_market_status}'
            print(err_str)
            if len(err_str) > 0:
                return err_str
            else:
                return ''
        else:
            return ''

    def series_status_market_status_24hours(self):
        '''
            比赛结束后20小时
        :return:
        '''
        sql = '''
            SELECT * FROM `data-center`.ex_series where source=1 and deleted=1 and p_id != 0 
            and start_time >= (UNIX_TIMESTAMP() - 3600*48)
			and status=3  having end_time+3600*20 < UNIX_TIMESTAMP()  order by ex_id desc;
        '''
        ex_id_set = set()
        data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `data-rate-center`.market_type where level_id in {level_id_tuple} order by level_id desc;
            '''
            if self.env_flag == 'release':
                play_datas = self.doMysql.select_basic(cnn=self.cnn_basic, sql=play_sql)
            elif self.env_flag == 'develop':
                play_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=play_sql)
            # print(len(play_datas))
            err_market_status_1 = set()
            err_market_status_2 = set()
            err_market_status_3 = set()
            for i in level_id_tuple:
                for y in play_datas:
                    if i == y['level_id']:
                        if y['market_status'] == 1:
                            err_market_status_1.add(y['market_id'])
                        elif y['market_status'] == 2:
                            err_market_status_2.add(y['market_id'])
                        elif y['market_status'] == 3:
                            err_market_status_3.add(y['market_id'])
            if len(err_market_status_1) > 0:
                err_str += f'系列赛已结束后20小时,玩法状态还是1的数据为（market_type的market_id）：{err_market_status_1};'
            if len(err_market_status_2) > 0:
                err_str += f'系列赛已结束后20小时,玩法状态还是2的数据为（market_type的market_id）：{err_market_status_2};'
            if len(err_market_status_3) > 0:
                err_str += f'系列赛已结束后20小时,玩法状态还是3的数据为（market_type的market_id）：{err_market_status_3};'
            if len(err_str) > 0:
                print(err_str)
                return err_str
            else:
                return ''
        else:
            return ''

    def series_status_option_status_24hours(self):
        '''
            比赛结束后20小时
        :return:
        '''
        sql = '''
            SELECT * FROM `data-center`.ex_series where source=1 and deleted=1 and p_id != 0
            and start_time >= (UNIX_TIMESTAMP() - 3600*48)
            and status=3  having end_time+3600*20 < UNIX_TIMESTAMP()  order by ex_id desc;
        '''
        ex_id_set = set()
        data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `data-rate-center`.option where market_type_id in (
                SELECT id FROM `data-rate-center`.market_type where level_id in {level_id_tuple} order by level_id desc);
            '''
            if self.env_flag == 'release':
                play_datas = self.doMysql.select_basic(cnn=self.cnn_basic, sql=play_sql)
            elif self.env_flag == 'develop':
                play_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=play_sql)
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
                err_str += f'系列赛已结束后20小时,选项状态还是1的数据为（option的ex_id）：{err_option_status_1}'
            if len(err_option_status_2) > 0:
                err_str += f'系列赛已结束后20小时,选项状态还是2的数据为（option的ex_id）：{err_option_status_2}'
            if len(err_option_status_3) > 0:
                err_str += f'系列赛已结束后20小时,选项状态还是3的数据为（option的ex_id）：{err_option_status_3}'
            if len(err_str) > 0:
                print(err_str)
                return err_str
            else:
                return ''
        else:
            return ''


if __name__ == '__main__':
    doMysql = DoMySql()
    cnn_centon = doMysql.cnn_centon_def()
    cnn_basic = doMysql.cnn_basic_def()
    c = SeriesStataus('develop', cnn_centon, cnn_basic, doMysql)
    # c.series_status_market_status_onehours()
    # c.series_status_market_status_24hours()
    c.series_status_option_status_24hours()
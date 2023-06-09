from common.do_mysql import DoMySql


class SeriesStataus(object):
    '''
        根据系列赛判断指数玩法和选项状态
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.cnn = DoMySql().connect(env_flag=env_flag)  # 0是测试，1是线上

    def series_status_market_status_onehours(self):
        '''
            比赛结束后一小时
        :return:
        '''
        sql = '''
            SELECT * FROM `data-center`.ex_series where source=1 and deleted=1 and p_id != 0 
            and start_time >= (UNIX_TIMESTAMP() - 3600*24)
			and status=3 having end_time+3600 < UNIX_TIMESTAMP() order by ex_id desc;
        '''
        ex_id_set = set()
        data = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `data-rate-center`.market_type where level_id in {level_id_tuple} order by level_id desc;
            '''
            play_datas = DoMySql().select(cnn=self.cnn, sql=play_sql, env_flag=self.env_flag)
            # print(len(play_datas))
            err_market_status = set()
            for i in level_id_tuple:
                for y in play_datas:
                    if i == y['level_id']:
                        if y['market_status'] in (1, 2):
                            err_market_status.add(y['market_id'])
            if len(err_market_status) > 0:
                err_str += f'系列赛已结束后一个小时,玩法状态还是1,2的数据为（market_type的market_id）：{err_market_status}'
            print(err_str)
            if len(err_str) > 0:
                return err_str
            else:
                return ''
        else:
            return ''

    def series_status_market_status_24hours(self):
        '''
            比赛结束后24小时
        :return:
        '''
        sql = '''
            SELECT * FROM `data-center`.ex_series where source=1 and deleted=1 and p_id != 0 
            and start_time >= (UNIX_TIMESTAMP() - 3600*48)
			and status=3  having end_time+3600*24 < UNIX_TIMESTAMP()  order by ex_id desc;
        '''
        ex_id_set = set()
        data = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `data-rate-center`.market_type where level_id in {level_id_tuple} order by level_id desc;
            '''
            play_datas = DoMySql().select(cnn=self.cnn, sql=play_sql, env_flag=self.env_flag)
            # print(len(play_datas))
            err_market_status = set()
            for i in level_id_tuple:
                for y in play_datas:
                    if i == y['level_id']:
                        if y['market_status'] in (1, 2, 3):
                            err_market_status.add(y['market_id'])
            if len(err_market_status) > 0:
                err_str += f'系列赛已结束后24小时,玩法状态还是1,2,3的数据为（market_type的market_id）：{err_market_status}'
            if len(err_str) > 0:
                print(err_str)
                return err_str
            else:
                return ''
        else:
            return ''

    def series_status_option_status_24hours(self):
        '''
            比赛结束后24小时
        :return:
        '''
        sql = '''
            SELECT * FROM `data-center`.ex_series where source=1 and deleted=1 and p_id != 0 
            and start_time >= (UNIX_TIMESTAMP() - 3600*48)
            and status=3  having end_time+3600*24 < UNIX_TIMESTAMP()  order by ex_id desc;
        '''
        ex_id_set = set()
        data = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        if len(level_id_tuple) != 0:
            play_sql = f'''
                SELECT * FROM `data-rate-center`.option where market_type_id in (
                SELECT id FROM `data-rate-center`.market_type where level_id in {level_id_tuple} order by level_id desc);
            '''
            play_datas = DoMySql().select(cnn=self.cnn, sql=play_sql, env_flag=self.env_flag)
            print(len(play_datas))
            err_option_status = set()
            for y in play_datas:
                if y['option_status'] in (1, 2, 3):
                    err_option_status.add(y['ex_id'])
            if len(err_option_status) > 0:
                err_str += f'系列赛已结束后24小时,玩法状态还是1,2,3的数据为（option的ex_id）：{err_option_status}'
            if len(err_str) > 0:
                print(err_str)
                return err_str
            else:
                return ''
        else:
            return ''


if __name__ == '__main__':
    ss = SeriesStataus(1)
    # ss.series_status_market_status_onehours()
    ss.series_status_market_status_24hours()
    ss.series_status_option_status_24hours()
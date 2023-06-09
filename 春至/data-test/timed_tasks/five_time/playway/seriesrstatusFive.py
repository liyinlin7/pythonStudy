from common.do_mysql import DoMySql


class SeriesStatausFive(object):
    '''
        根据系列赛判断指数玩法和选项状态
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.cnn = DoMySql().connect(env_flag=env_flag)  # 0是测试，1是线上

    def series_status_market_status(self):
        sql = '''
            SELECT * FROM `data-center`.ex_series where source=1 and deleted=1 and p_id != 0 and start_time > unix_timestamp()-3600*24*3 and status=3 order by ex_id desc;
        '''
        ex_id_set = set()
        data = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        play_sql = f'''
            SELECT * FROM `data-rate-center`.market_type where level_id in {level_id_tuple} order by level_id desc;
        '''
        play_datas = DoMySql().select(cnn=self.cnn, sql=play_sql, env_flag=self.env_flag)
        print(len(play_datas))
        err_market_status = set()
        for i in level_id_tuple:
            for y in play_datas:
                if i == y['level_id']:
                    if y['market_status'] == 1:
                        print(i)
                        err_market_status.add(y['market_id'])
        if len(err_market_status) > 0:
            err_str += f'系列赛已结束,玩法状态还是1的数据为（market_type的market_id）：{err_market_status}'
        print(err_str)
        if len(err_str) > 0:
            return err_str
        else:
            return ''

    def series_status_market_null(self):
        sql = '''
            SELECT * FROM `data-center`.ex_series where source=1 and deleted=1 and p_id != 0 and start_time >= UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE))-3600*8 
            and start_time < UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE) + INTERVAL 1 DAY)-3600*8 and status!=4 order by ex_id desc;
        '''
        ex_id_set = set()
        data = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        for i in data:
            ex_id_set.add(i['ex_id'])
        level_id_tuple = tuple(ex_id_set)
        err_str = ''
        play_sql = f'''
            SELECT * FROM `data-rate-center`.market_type where level_id in {level_id_tuple} order by level_id desc;
        '''
        play_datas = DoMySql().select(cnn=self.cnn, sql=play_sql, env_flag=self.env_flag)
        print(len(play_datas))
        play_level_id_set = set()
        for i in play_datas:
            play_level_id_set.add(i['level_id'])
        ex_id_list = list(ex_id_set)
        for i in play_level_id_set:
            if i in ex_id_list:
                ex_id_list.remove(i)
        if len(ex_id_list) > 0:
            err_str += f'雷竞技未删除系列赛无指数详情数据,雷竞技系列赛ID为：{ex_id_list}'
        print(err_str)
        if len(err_str) > 0:
            return err_str
        else:
            return ''


if __name__ == '__main__':
    ss = SeriesStatausFive(0)
    ss.series_status_market_status()
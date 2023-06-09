from common.do_mysql import DoMySql
from common.deal_with_data import count_time


class LeiJingJi(object):

    def __init__(self, env_flag):
        self.do_mysql = DoMySql()
        self.cnn = self.do_mysql.connect(env_flag=env_flag)
        self.env_flag = env_flag

    @count_time
    def series_6_hours(self):
        ex_series_sql = '''
            SELECT * FROM `data-center`.ex_series where deleted=1 and status=3 and source=1 and start_time > unix_timestamp() - 3600*24*30 and start_time< unix_timestamp() and game_id in (1,2,3,4) order by ex_id desc;
        '''
        ex_series_datas = self.do_mysql.select(cnn=self.cnn, sql=ex_series_sql, env_flag=self.env_flag)
        ex_id_set = set()
        lists = []
        for i in ex_series_datas:
            ex_id_time = {}
            ex_id_set.add(i['ex_id'])
            ex_id = i['ex_id']
            ex_time = i['end_time']
            ex_id_time['ex_id'] = ex_id
            ex_id_time['ex_time'] = ex_time
            lists.append(ex_id_time)
        # print(ex_id_set)
        # print(lists)
        rate_sql = f'''
            SELECT market_id,level_id,market_status,option_status,o.ex_id,o.update_time FROM `data-rate-center`.market_type as mt 
            left join `data-rate-center`.option as o on mt.id = o.market_type_id where level_id in {tuple(ex_id_set)} 
            and o.option_status in (3,4) order by level_id desc;

        '''
        rate_datas = self.do_mysql.select(cnn=self.cnn, sql=rate_sql, env_flag=self.env_flag)
        option_ex_id = []
        # for i in lists:
        #     # print(i)
        #     end_time = i.get('ex_time')
        #     level_id = i.get('ex_id')
        #     # print(end_time)
        #     # print(level_id)
        #     for y in rate_datas:
        #         if level_id == y['level_id']:
        #             if end_time + 3600*15 <= y['update_time']:
        #                 option_ex_id.append(y['ex_id'])
        print("选项总数", len(rate_datas))
        print("8小时后：", len(option_ex_id))
        print(option_ex_id)


if __name__ == '__main__':
    a = LeiJingJi(1)
    a.series_6_hours()

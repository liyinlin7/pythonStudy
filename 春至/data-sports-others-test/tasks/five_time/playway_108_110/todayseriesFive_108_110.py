from common.do_mysql import DoMySql
from common.deal_with_data import count_time


class TodaySeries_108_110(object):
    '''
        雷竞技的系列赛
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_basketball = self.do_mysql.connect_mysql_basketball(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn_rate = self.do_mysql.connect_mysql_rate(env_flag=env_flag)  # 0是测试，1是线上

    @count_time
    def today_series_id_1_108_110(self):
        '''
            当天系列赛所有玩法
        :param env_flag:
        :return:
        '''
        sql = '''
                 SELECT * FROM `sports-others`.ex_series  where source=2  and p_id != 0 and  sport_id in (108,109,110) and match_start_time >= (UNIX_TIMESTAMP() - 3600*24)
                 and match_start_time < (UNIX_TIMESTAMP() + 3600*24);
             '''
        datas = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        series_ex_id_list = set()
        series_status_3_list = set()  # 已经结束的系列赛ex_id
        for data in datas:
            series_ex_id_list.add(data.get('ex_id'))
            if data.get('status') == 8:
                series_status_3_list.add(data.get('ex_id'))
        series_ex_id_tuple = tuple(series_ex_id_list)
        series_ex_id_str = None
        if len(series_ex_id_tuple) == 1:
            series_ex_id_str = str(series_ex_id_tuple).replace(',', '')
        else:
            series_ex_id_str = series_ex_id_tuple
        if len(series_ex_id_str) != 0:
            mark_sql = f'''
                                SELECT * FROM `sports-rate-center`.market_type where level_id in {series_ex_id_str};
                            '''
            if self.env_flag == 0:
                market_res = self.do_mysql.select(cnn=self.cnn, sql=mark_sql, env_flag=self.env_flag)
            else:
                market_res = self.do_mysql.select_rate(cnn=self.cnn_rate, sql=mark_sql, env_flag=self.env_flag)
            err1 = self.today_option_108_110(market_res)
            err3 = self.today_market_type_option_status_108_110(market_res)
            # err4 = self.todya_match_id()
            if err3 is None : err3 = ''
            err = err1 + '\n' + err3 + '\n'
            print("错误数据:", err)
            if len(err) != 0:
                print(err)
                return err
            else:
                return ''
        else:
            return ''

    def today_option_108_110(self, market_res):
        '''
            当天所有系列赛的option 表
        :param datas:
        :return:
        '''
        try:
            # ID 关联 option 中的 market_type_id
            market_id_list = set()
            for data in market_res:
                # -- 指数详情玩法ID为null
                market_id_list.add(data.get('id'))
            sql = '''
                    SELECT * FROM `sports-rate-center`.option WHERE market_type_id in {};
                '''.format(tuple(market_id_list))
            if self.env_flag == 0:
                option_res = self.do_mysql.select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
            else:
                option_res = self.do_mysql.select_rate(cnn=self.cnn_rate, sql=sql, env_flag=self.env_flag)
            option_option_option_status_5_null = set()
            option_option_option_is_winner_1_2_null = set()
            err_str = '排台棒：当天所有系列赛的option表中(market_type_id)，'
            old_err_str_len = len(err_str)
            for data in option_res:
                # 指数详情同选项id，option_status为5，is_winner不等于（3, 2）
                if data.get('option_status') == 5:
                    if data.get('is_winner') not in (3, 2,4,5,6):
                        option_option_option_status_5_null.add(data.get('market_type_id'))
                # 指数详情同选项id，is_winner为1或2，option_status不等于5
                if data.get('is_winner') in (3, 2,4,5,6):
                    if data.get('option_status') != 5:
                        option_option_option_is_winner_1_2_null.add(data.get('market_type_id'))
            if len(option_option_option_status_5_null) != 0:
                err_str += f'指数详情同选项id，option_status为5，is_winner不等于（3, 2,4,5,6）的数据为：{str(option_option_option_status_5_null)}；\n'
            if len(option_option_option_is_winner_1_2_null) != 0:
                err_str += f'指数详情同选项id，is_winner为3或2，option_status不等于5的数据为：{str(option_option_option_is_winner_1_2_null)}；\n'
            if len(err_str) > old_err_str_len:
                return err_str + '\n'
            else:
                return ''
        except Exception:
            print("today_option:tuple的方法就一个值")

    def today_market_type_option_status_108_110(self, datas):
        '''
            market_type表的market_status和option表的optuion_status
        :param datas:
        :return:
        '''
        try:
            market_option_list = []
            market_type_id = set()
            err_str = '排台棒：当天所有赛程，'
            old_err_str_len = len(err_str)
            for data in datas:
                market_type = {}
                market_type_id.add(data.get('id'))
                market_type['id'] = data.get('id')
                market_type['market_status'] = data.get('market_status')
                market_option_list.append(market_type)
            option_sql = '''
                    select * FROM `sports-rate-center`.option where market_type_id in {};
                '''.format(tuple(market_type_id))
            if self.env_flag == 0:
                option_res = self.do_mysql.select(cnn=self.cnn, sql=option_sql, env_flag=self.env_flag)
            else:
                option_res = self.do_mysql.select_rate(cnn=self.cnn_rate, sql=option_sql, env_flag=self.env_flag)
            option_err_list_1 = set()  # 指数详情 同玩法id，任一option_status为1，market_status等于1
            option_err_list_2 = set()  # 指数详情 同玩法id，任一option_status为1，market_status等于1
            option_err_list_3 = set()  # 指数详情 同玩法id，market_status为3，任一option_status不是3
            option_err_list_4 = set()  # 指数详情 同玩法id，market_status为4，任一option_status不是4
            option_err_list_5 = set()  # 指数详情 同玩法id，market_status为5，任一option_status不是5
            for i in market_option_list:
                option_status_list_1 = set()
                option_status_list_2 = set()
                option_status_list_3 = set()
                option_status_list_4 = set()
                option_status_list_5 = set()
                market_type_num1 = 0
                market_type_num2 = 0
                market_type_num3 = 0
                market_type_num4 = 0
                market_type_num5 = 0
                for y in option_res:
                    if i.get('id') == y.get('market_type_id'):
                        # 指数详情 同玩法id，market_status等于1,任一option_status为1,2，
                        if i.get('market_status') == 1:
                            market_type_num1 = i.get('id')
                            option_status_list_1.add(y.get('option_status'))
                        # 指数详情 同玩法id，market_status等于1,任一option_status为1,2，
                        if i.get('market_status') == 2:
                            market_type_num2 = i.get('id')
                            option_status_list_2.add(y.get('option_status'))
                        # 指数详情 同玩法id，market_status为3，任一option_status不是3
                        if i.get('market_status') == 3:
                            market_type_num3 = i.get('id')
                            option_status_list_3.add(y.get('option_status'))
                        # 指数详情 同玩法id，market_status为4，任一option_status不是4
                        if i.get('market_status') == 4:
                            market_type_num4 = i.get('id')
                            option_status_list_4.add(y.get('option_status'))
                        # 指数详情 同玩法id，market_status为5，全部option_status均不是5
                        if i.get('market_status') == 5:
                            market_type_num5 = i.get('id')
                            option_status_list_5.add(y.get('option_status'))
                if i.get('market_status') not in option_status_list_1 and market_type_num1 != 0:
                    option_err_list_1.add(market_type_num1)
                if i.get('market_status') not in option_status_list_2 and market_type_num2 != 0 and len(option_status_list_2) != 1:
                    option_err_list_2.add(market_type_num2)
                if i.get('market_status') not in option_status_list_3 and market_type_num3 != 0 and len(option_status_list_3) != 1:
                    option_err_list_3.add(market_type_num3)
                if i.get('market_status') not in option_status_list_4 and market_type_num4 != 0 and len(option_status_list_4) != 1:
                    option_err_list_4.add(market_type_num4)
                if i.get('market_status') not in option_status_list_5 and market_type_num5 != 0 and len(option_status_list_5) != 1:
                    option_err_list_5.add(market_type_num5)
            if len(option_err_list_1) != 0:
                err_str += f'指数详情 option表中（market_type_id）同玩法market_status等于1，任一option_status不为1的数据为：{str(option_err_list_1)}\n；'
            if len(option_err_list_2) != 0:
                err_str += f'指数详情 option表中（market_type_id）同玩法market_status等于2，全部option_status不为2的数据为：{str(option_err_list_2)}\n；'
            if len(option_err_list_3) != 0:
                err_str += f'指数详情 option表中（market_type_id）同玩法id，market_status为3，全部一option_status不是3的数据为：{str(option_err_list_3)}； \n'
            if len(option_err_list_4) != 0:
                err_str += f'指数详情 option表中（market_type_id）同玩法id，market_status为4，全部option_status不是4的数据为：{str(option_err_list_4)}； \n'
            if len(option_err_list_5) != 0:
                err_str += f'指数详情 option表中（market_type_id）同玩法id，market_status为5，全部option_status均不是5的数据为：{str(option_err_list_5)}； \n'
            market_status_4_err = set()  # 全部option_status为4，market_status不是4的ID
            market_status_5_err = set()  # option_status为5，market_status不是5的ID
            for i in option_res:
                market_status_4_1 = set()  # option status为4的时候，market_status 的状态
                market_status_4_2 = set()  # option status不为4的时候，market_status 的状态
                # 指数详情 同玩法id，全部option_status为4，market_status不是4
                if i.get('option_status') == 4:
                    i.get('market_type_id')
                    for data in datas:
                        if data.get('id') == i.get('market_type_id'):
                            market_status_4_1.add(data.get('market_status'))
                else:
                    i.get('market_type_id')
                    for data in datas:
                        if data.get('id') == i.get('market_type_id'):
                            market_status_4_2.add(data.get('market_status'))
                # 指数详情同玩法id，任一option_status为5，market_status不是5
                if i.get('option_status') == 5:
                    i.get('market_type_id')
                    for data in datas:
                        if data.get('id') == i.get('market_type_id'):
                            if data.get('market_status') != 5:
                                market_status_5_err.add(i.get('market_type_id'))
                for m_2 in market_status_4_2:
                    for m_1 in market_status_4_1:
                        if m_2 == m_1:
                            market_status_4_err.add(m_1)
            if len(market_status_4_err) != 0:
                err_str += f'指数详情 option表中（market_type_id）同玩法id，全部option_status为4，market_status不是4的数据为：{str(market_status_4_err)}； \n'
            if len(market_status_5_err) != 0:
                err_str += f'指数详情 option表中（market_type_id）同玩法id，任一option_status为5，market_status不是5的数据为：{str(market_status_5_err)}； \n'
            if len(err_str) > old_err_str_len:
                print(err_str)
                return err_str + '\n'
            else:
                return ''
        except Exception:
            print("today_market_type_option_status:tuple方法就一个值")


if __name__ == '__main__':
    t = TodaySeries_108_110(env_flag=1).today_series_id_1_108_110()
    # t = TodaySeries(env_flag=1).today_series_id_1()

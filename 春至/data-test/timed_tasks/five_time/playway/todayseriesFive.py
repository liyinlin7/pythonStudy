from common.do_mysql import DoMySql
from common.deal_with_data import count_time


class TodaySeries(object):
    '''
        雷竞技的系列赛
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.cnn = DoMySql().connect(env_flag=env_flag)  # 0是测试，1是线上

    @count_time
    def today_series_id_1(self):
        '''
            当天系列赛所有玩法
        :param env_flag:
        :return:
        '''
        sql = '''
                 SELECT * FROM `data-center`.ex_series where deleted=1 and p_id != 0 and source =1 and start_time >= (UNIX_TIMESTAMP() - 3600*24)
                 and start_time < (UNIX_TIMESTAMP() + 3600*24);
             '''
        # sql = '''
        #                 SELECT * FROM `data-center`.ex_series where deleted=1 and p_id != 0 and source =1 and start_time> 1614079200;
        #             '''
        # sql =  '''
        #     SELECT ex_id FROM `data-center`.ex_series where create_time > 1614425100 and p_id != 0 and source=1
        # '''
        datas = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        series_ex_id_list = set()
        series_status_3_list = set()  # 已经结束的系列赛ex_id
        for data in datas:
            series_ex_id_list.add(data.get('ex_id'))
            if data.get('status') == 3:
                series_status_3_list.add(data.get('ex_id'))
        series_ex_id_tuple = tuple(series_ex_id_list)
        series_ex_id_str = None
        if len(series_ex_id_tuple) == 1:
            series_ex_id_str = str(series_ex_id_tuple).replace(',', '')
        else:
            series_ex_id_str = series_ex_id_tuple
        mark_sql = f'''
                            SELECT * FROM `data-rate-center`.market_type where level_id in {series_ex_id_str};
                        '''
        market_res = DoMySql().select(cnn=self.cnn, sql=mark_sql, env_flag=self.env_flag)
        err1 = self.today_option(market_res)
        err3 = self.today_market_type_option_status(market_res)
        err4 = self.todya_match_id()
        if err3 is None : err3 = ''
        err = err1 + '\n' + err3 + '\n' + err4
        print("错误数据:", err)
        if len(err) != 0:
            print(err)
            return err
        else:
            return ''

    def today_option(self, market_res):
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
                    SELECT * FROM `data-rate-center`.option WHERE market_type_id in {};
                '''.format(tuple(market_id_list))
            option_res = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
            option_option_option_status_5_null = set()
            option_option_option_is_winner_1_2_null = set()
            err_str = '当天所有系列赛的option表中(market_type_id)，'
            old_err_str_len = len(err_str)
            for data in option_res:
                # 指数详情同选项id，option_status为5，is_winner不等于（3, 2）
                if data.get('option_status') == 5:
                    if data.get('is_winner') not in (3, 2):
                        option_option_option_status_5_null.add(data.get('market_type_id'))
                # 指数详情同选项id，is_winner为1或2，option_status不等于5
                if data.get('is_winner') in (3, 2):
                    if data.get('option_status') != 5:
                        option_option_option_is_winner_1_2_null.add(data.get('market_type_id'))
            if len(option_option_option_status_5_null) != 0:
                err_str += f'指数详情同选项id，option_status为5，is_winner不等于（3, 2）的数据为：{str(option_option_option_status_5_null)}；\n'
            if len(option_option_option_is_winner_1_2_null) != 0:
                err_str += f'指数详情同选项id，is_winner为3或2，option_status不等于5的数据为：{str(option_option_option_is_winner_1_2_null)}；\n'
            if len(err_str) > old_err_str_len:
                return err_str + '\n'
            else:
                return ''
        except Exception:
            print("today_option:tuple的方法就一个值")

    def today_market_type_option_status(self, datas):
        '''
            market_type表的market_status和option表的optuion_status
        :param datas:
        :return:
        '''
        try:
            market_option_list = []
            market_type_id = set()
            err_str = '当天所有系列赛，'
            old_err_str_len = len(err_str)
            for data in datas:
                market_type = {}
                market_type_id.add(data.get('id'))
                market_type['id'] = data.get('id')
                market_type['market_status'] = data.get('market_status')
                market_option_list.append(market_type)
            option_sql = '''
                    select * FROM `data-rate-center`.option where market_type_id in {};
                '''.format(tuple(market_type_id))
            option_res = DoMySql().select(cnn=self.cnn, sql=option_sql, env_flag=self.env_flag)
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

    def todya_match_id(self):
        '''
            当天已结束小局
        :return:
        '''
        try:
            lol_sql = '''
                              select * FROM `data-center`.lol_match where series_id in (
                              select p_id FROM `data-center`.ex_series where source=1 and status=3 and game_id=1 and source=1 and deleted=1 and audit in (2,4)
                              and start_time >= (UNIX_TIMESTAMP() - 3600*24)
                              and start_time < (UNIX_TIMESTAMP() + 3600*24)
                            ) and deleted=1 and status=3;
                            '''
            dota_sql = '''
                              select * FROM `data-center`.dota_match where series_id in (
                              select p_id FROM `data-center`.ex_series where source=1 and status=3 and game_id=2 and source=1 and deleted=1 and audit in (2,4)
                              and start_time >= (UNIX_TIMESTAMP() - 3600*24)
                              and start_time < (UNIX_TIMESTAMP() + 3600*24)
                            ) and deleted=1 and status=3;
                            '''
            csgo_sql = '''
                              select * FROM `data-center`.match where series_id in (
                              select p_id FROM `data-center`.ex_series where source=1 and status=3 and game_id=3 and source=1 and deleted=1 and audit in (2,4)
                              and start_time >= (UNIX_TIMESTAMP() - 3600*24)
                              and start_time < (UNIX_TIMESTAMP() + 3600*24)
                            ) and deleted=1 and status=3;
                            '''
            kog_sql = '''
                      select * FROM `data-center`.kog_match where series_id in (
                      select p_id FROM `data-center`.ex_series where source=1 and status=3 and game_id=4 and source=1 and deleted=1 and audit in (2,4)
                      and start_time >= (UNIX_TIMESTAMP() - 3600*24)
                      and start_time < (UNIX_TIMESTAMP() + 3600*24)
                    ) and deleted=1 and status=3;
                    '''
            lol_datas = DoMySql().select(cnn=self.cnn, sql=lol_sql, env_flag=self.env_flag)
            dota_datas = DoMySql().select(cnn=self.cnn, sql=dota_sql, env_flag=self.env_flag)
            csgo_datas = DoMySql().select(cnn=self.cnn, sql=csgo_sql, env_flag=self.env_flag)
            kog_datas = DoMySql().select(cnn=self.cnn, sql=kog_sql, env_flag=self.env_flag)
            lol_match_id_list = set()
            dota_match_id_list = set()
            csgo_match_id_list = set()
            kog_match_id_list = set()
            for data in lol_datas:
                lol_match_id_list.add(data.get('id'))
            for data in dota_datas:
                dota_match_id_list.add(data.get('id'))
            for data in csgo_datas:
                csgo_match_id_list.add(data.get('id'))
            for data in kog_datas:
                kog_match_id_list.add(data.get('id'))
            lol_option_err = set()
            dota_option_err = set()
            csgo_option_err = set()
            kog_option_err = set()
            err_str = '当天所有已结束的小局option中(id)，'
            old_err_str_len = len(err_str)
            if len(lol_match_id_list) != 0:
                lol_market_sql = '''
                        SELECT * FROM `data-rate-center`.market where inside_level_id in {} and game_id=1;
                    '''.format(tuple(lol_match_id_list))
                # print(lol_market_sql)
                lol_market_res = DoMySql().select(cnn=self.cnn, sql=lol_market_sql, env_flag=self.env_flag)
                lol_market_id_list = set()
                for data in lol_market_res:
                    lol_market_id_list.add(data.get('id'))
                if len(lol_market_id_list) != 0:
                    lol_market_type_sql = '''
                                SELECT * FROM `data-rate-center`.market_type where market_id in {};
                            '''.format(tuple(lol_market_id_list))
                    # print(lol_market_type_sql)
                    lol_market_type_res = DoMySql().select(cnn=self.cnn, sql=lol_market_type_sql, env_flag=self.env_flag)
                    lol_market_type_id_list = set()
                    for data in lol_market_type_res:
                        lol_market_type_id_list.add(data.get('id'))
                    if len(lol_market_type_id_list) != 0:
                        lol_option_sql = '''
                                        SELECT * FROM `data-rate-center`.option where market_type_id in {};
                                    '''.format(tuple(lol_market_type_id_list))
                        # print(lol_option_sql)
                        lol_option_res = DoMySql().select(cnn=self.cnn, sql=lol_option_sql, env_flag=self.env_flag)
                    # 指数详情lol小局状态为已结束，option_status为1或2, is_winner为1
                        for data in lol_option_res:
                            if data.get('option_status') in (1,):
                                lol_option_err.add(data.get('id'))
            if len(dota_match_id_list) != 0:
                dota_market_sql = '''
                                SELECT * FROM `data-rate-center`.market where inside_level_id in {} and game_id=2;
                            '''.format(tuple(dota_match_id_list))
                dota_market_res = DoMySql().select(cnn=self.cnn, sql=dota_market_sql, env_flag=self.env_flag)
                dota_market_id_list = set()
                for data in dota_market_res:
                    dota_market_id_list.add(data.get('id'))
                if len(dota_market_id_list) != 0:
                    dota_market_type_sql = '''
                                        SELECT * FROM `data-rate-center`.market_type where market_id in {};
                                    '''.format(tuple(dota_market_id_list))
                    dota_market_type_res = DoMySql().select(cnn=self.cnn, sql=dota_market_type_sql, env_flag=self.env_flag)
                    dota_market_type_id_list = set()
                    for data in dota_market_type_res:
                        dota_market_type_id_list.add(data.get('id'))
                    dota_option_sql = '''
                                            SELECT * FROM `data-rate-center`.option where market_type_id in {};
                                        '''.format(tuple(dota_market_type_id_list))
                    dota_option_res = DoMySql().select(cnn=self.cnn, sql=dota_option_sql, env_flag=self.env_flag)
                    # 指数详情dota小局状态为已结束，option_status为1或2, is_winner为1
                    for data in dota_option_err:
                        if data.get('option_status') in (1,):
                            dota_option_res.add(data.get('id'))
            if len(csgo_match_id_list) != 0:
                csgo_market_sql = '''
                                SELECT * FROM `data-rate-center`.market where inside_level_id in {} and game_id=3;
                            '''.format(tuple(csgo_match_id_list))
                csgo_market_res = DoMySql().select(cnn=self.cnn, sql=csgo_market_sql, env_flag=self.env_flag)
                csgo_market_id_list = set()
                for data in csgo_market_res:
                    csgo_market_id_list.add(data.get('id'))
                if len(csgo_market_id_list) != 0:
                    csgo_market_type_sql = '''
                                        SELECT * FROM `data-rate-center`.market_type where market_id in {};
                                    '''.format(tuple(csgo_market_id_list))
                    csgo_market_type_res = DoMySql().select(cnn=self.cnn, sql=csgo_market_type_sql, env_flag=self.env_flag)
                    csgo_market_type_id_list = set()
                    for data in csgo_market_type_res:
                        csgo_market_type_id_list.add(data.get('id'))
                    csgo_option_sql = '''
                                            SELECT * FROM `data-rate-center`.option where market_type_id in {};
                                        '''.format(tuple(csgo_market_type_id_list))
                    csgo_option_res = DoMySql().select(cnn=self.cnn, sql=csgo_option_sql, env_flag=self.env_flag)
                    # 指数详情csgo小局状态为已结束，option_status为1或2, is_winner为1
                    for data in csgo_option_err:
                        if data.get('option_status') in (1,):
                            csgo_option_res.add(data.get('id'))
            if len(kog_match_id_list) != 0:
                kog_market_sql = '''
                                SELECT * FROM `data-rate-center`.market where inside_level_id in {} and game_id=4;
                            '''.format(tuple(kog_match_id_list))
                kog_market_res = DoMySql().select(cnn=self.cnn, sql=kog_market_sql, env_flag=self.env_flag)
                kog_market_id_llist = set()
                for data in kog_market_res:
                    kog_market_id_llist.add(data.get('id'))
                kog_market_type_sql = '''
                            SELECT * FROM `data-rate-center`.market_type where market_id in {};
                        '''.format(tuple(kog_market_id_llist))
                kog_market_type_res = DoMySql().select(cnn=self.cnn, sql=kog_market_type_sql, env_flag=self.env_flag)
                kog_market_type_id_list = set()
                for data in kog_market_type_res:
                    kog_market_type_id_list.add(data.get('id'))
                kog_option_sql = '''
                                SELECT * FROM `data-rate-center`.option where market_type_id in {};
                            '''.format(tuple(kog_market_type_id_list))
                kog_option_res = DoMySql().select(cnn=self.cnn, sql=kog_option_sql, env_flag=self.env_flag)
                # 指数详情kog小局状态为已结束，option_status为1或2, is_winner为1
                for data in kog_option_err:
                    if data.get('option_status') in (1,):
                        kog_option_res.add(data.get('id'))
            if len(lol_option_err) != 0:
                err_str += f'指数详情lol小局状态为已结束，option_status为1的数据为：{str(lol_option_err)}；\n'
            if len(dota_option_err) != 0:
                err_str += f'指数详情dota小局状态为已结束，option_status为1的数据为：{str(dota_option_err)}；\n'
            if len(csgo_option_err) != 0:
                err_str += f'指数详情csgo小局状态为已结束，option_status为1的数据为：{str(csgo_option_err)}；\n'
            if len(kog_option_err) != 0:
                err_str += f'指数详情kog小局状态为已结束，option_status为1的数据为：{str(kog_option_err)}；\n'
            if len(err_str) > old_err_str_len:
                print(err_str)
                return err_str + '\n'
            else:
                return ''
        except Exception:
            print("todya_match_id:方法tuple只有一个值")


if __name__ == '__main__':
    t = TodaySeries(env_flag=1).todya_match_id()
    # t = TodaySeries(env_flag=1).today_series_id_1()

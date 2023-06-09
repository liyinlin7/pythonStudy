from common.do_mysql import DoMySql


class TodaySeriesTen(object):
    '''
        雷竞技的系列赛
    '''

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.doMysql = mysql_cnn

    def today_series_id(self):
        '''
            当天系列赛所有玩法
        :param env_flag:
        :return:
        '''
        sql = '''
                 SELECT * FROM `data-center`.ex_series where deleted=1 and p_id != 0 and source =1 and start_time >= (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE)) - 3600*8)
                 and start_time < (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE) + INTERVAL 1 DAY) - 3600*8) ;
             '''
        datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        series_ex_id_list = set()
        series_status_3_list = set()  # 已经结束的系列赛ex_id
        for data in datas:
            series_ex_id_list.add(data.get('ex_id'))
            if data.get('status') == 3:
                series_status_3_list.add(data.get('ex_id'))
        series_ex_id_tuple = tuple(series_ex_id_list)
        # series_status_3_tuple = tuple(series_status_3_list)
        series_ex_id_str = None
        # series_status_3_str = None
        if len(series_ex_id_tuple) == 1:
            series_ex_id_str = str(series_ex_id_tuple).replace(',', '')
        else:
            series_ex_id_str = series_ex_id_tuple
        # if len(series_status_3_tuple) == 1:
        #     series_status_3_str = str(series_status_3_tuple).replace(',', '')
        # else:
        #     series_status_3_str = series_status_3_tuple
        # if len(series_status_3_tuple) != 0:
        #     status_3_sql = f'''
        #             SELECT * FROM `data-rate-center`.market_type where level_id in {series_status_3_str};
        #         '''
        #     # series_status_3_res = DoMySql().select(cnn=self.cnn, sql=status_3_sql, env_flag=self.env_flag)
        #     # err2 = self.today_option_series_end(series_status_3_res)
        # else:
        #     err2 = ''
        mark_sql = f'''
                            SELECT * FROM `data-rate-center`.market_type where level_id in {series_ex_id_str};
                        '''
        if self.env_flag == 'release':
            market_res = self.doMysql.select_basic(cnn=self.cnn_basic, sql=mark_sql)
        elif self.env_flag == 'develop':
            market_res = self.doMysql.select_centon(cnn=self.cnn_centon, sql=mark_sql)
        err1 = self.today_market_type(market_res)
        # err4 = self.todya_match_id()
        if err1 is None : err1 = ''
        # if err2 is None : err2 = ''
        # if err4 is None : err4 = ''
        # err = err1 + '\n' + err2 + '\n' + err3 + '\n' + err4
        err = err1
        print("错误数据:", err)
        if len(err) != 0:
            print(err)
            return err
        else:
            pass

    def today_market_type(self, market_res):
        '''
            当天所有系列赛的market_type表
        :return:
        '''
        try:
            market_type_market_id_null = set()
            market_type_level_null = set()
            market_type_source_null = set()
            matket_type_market_status_null = set()
            market_type_is_inplay_null = set()
            # market_id 关联 market_name中的market_id
            market_market_id_list = set()
            # ID 关联 option 中的 market_type_id
            market_id_list = set()
            err_str = '当天所有系列赛的market_type表中(level_id)，'
            old_err_str_len = len(err_str)
            for data in market_res:
                # -- 指数详情玩法ID为null
                market_id_list.add(data.get('id'))
                if data.get('market_id') is None or data.get('market_id') == '':
                    market_type_market_id_null.add(data.get('level_id'))
                else:
                    market_market_id_list.add(data.get('market_id'))
                # 指数详情level = NULL或不等于（101, 100, 1, 2, 3, 4, 5, 6, 7）
                if data.get('level') is None or data.get('level') == '' or data.get('level') not in (1, 2, 3, 4, 5, 6, 7, 100, 101):
                    market_type_level_null.add(data.get('level_id'))
                # 指数详情market_type的source的来源为null
                if data.get('source') is None or data.get('source') == '':
                    market_type_source_null.add(data.get('level_id'))
                # 指数详情market中market_status不等于（1, 2, 3, 4, 5）
                if data.get('market_status') is None or data.get('market_status') == '' or data.get('market_status') not in (1, 2, 3, 4, 5):
                    matket_type_market_status_null.add(data.get('level_id'))
                # 指数详情 market中is_inplay不等于（1, 2）
                if data.get('is_inplay') is None or data.get('is_inplay') == '' or data.get('is_inplay') not in (1, 2):
                    market_type_is_inplay_null.add(data.get('level_id'))
            if len(market_type_market_id_null) != 0:
                err_str += f'存在指数详情玩法ID为null的数据为：{str(market_type_market_id_null)}；\n'
            if len(market_type_level_null) != 0:
                err_str += f'指数详情level = NULL或不等于(101, 100, 1, 2, 3, 4, 5, 6, 7)的数据为：{str(market_type_level_null)}；\n'
            if len(market_type_source_null) != 0:
                err_str += f'指数详情market_type的source的来源为null的数据为：{str(market_type_source_null)}；\n'
            if len(matket_type_market_status_null) != 0:
                err_str += f'指数详情market中market_status不等于(1, 2, 3, 4, 5)的数据为：{str(matket_type_market_status_null)}；\n'
            if len(market_type_is_inplay_null) != 0:
                err_str += f'指数详情 market中is_inplay不等于(1, 2)的数据为：{str(market_type_is_inplay_null)}；\n'
            market_name_err_str = self.today_market_name(market_market_id_list)
            option_err_str = self.today_option(market_id_list)
            err = ''
            if len(err_str) > old_err_str_len:
                err += err_str + '\n'
                if market_name_err_str is not None:
                    err += market_name_err_str + '\n'
                if option_err_str is not None:
                    err += option_err_str + '\n'
            else:
                if market_name_err_str is not None:
                    err += market_name_err_str + '\n'
                if option_err_str is not None:
                    err += option_err_str + '\n'
            return err + '\n'
        except Exception:
            print("today_market_type:tuple的方法就一个值")

    def today_market_name(self, datas):
        '''
            当天所有系列赛的market_name表
        :param datas:
        :return:
        '''
        try:
            market_name_sql = '''
                    SELECT * FROM `data-rate-center`.market_name where market_id in {};
                '''.format(tuple(datas))
            if self.env_flag == 'release':
                market_name_res = self.doMysql.select_basic(cnn=self.cnn_basic, sql=market_name_sql)
            elif self.env_flag == 'develop':
                market_name_res = self.doMysql.select_centon(cnn=self.cnn_centon, sql=market_name_sql)
            market_name_name_type_null = set()
            market_name_name_zh_en_null = set()
            market_name_name_value_null = set()
            market_name_name_id_null = set()
            err_str = '当天所有系列赛的market_name表中(market_id)，'
            old_err_str_len = len(err_str)
            for data in market_name_res:
                # 指数详情 market_name中 name_type 没有值,name_type不等于（1,2,3,4,5,6）
                if data.get('name_type') is None or data.get('name_type') not in (1, 2, 3, 4, 5, 6):
                    market_name_name_type_null.add(data.get('market_id'))
                # 指数详情market_name中name_type = 1，name_en = NULL并name_zh = NULL
                elif data.get('name_type') == 1:
                    if (data.get('name_zh') is None and data.get('name_en') is None) or (data.get('name_zh') == '' and data.get('name_en') == ''):
                        market_name_name_zh_en_null.add(data.get('market_id'))
                # 指数详情market_name中name_type = 2，name_value没有值
                elif data.get('name_type') == 2:
                    if data.get('name_value') is None or data.get('name_value') == '':
                        market_name_name_value_null.add(data.get('market_id'))
                # 指数详情market_name中name_type = 3, 4, 5, 6，name_id不是ID
                elif data.get('name_type') in (3, 4, 5, 6):
                    if data.get('name_id') == 0 or data.get('name_id') is None or data.get('name_id') == '':
                        market_name_name_id_null.add(data.get('market_id'))
            if len(market_name_name_type_null) != 0:
                err_str += f'指数详情 market_name中 name_type 没有值,name_type不等于(1,2,3,4,5,6)的数据为：{str(market_name_name_type_null)}；\n'
            if len(market_name_name_zh_en_null) != 0:
                err_str += f'指数详情market_name中name_type = 1，name_en = NULL并name_zh = NULL的数据为：{str(market_name_name_zh_en_null)}；\n'
            if len(market_name_name_value_null) != 0:
                err_str += f'指数详情market_name中name_type = 2，name_value没有值的数据为：{str(market_name_name_value_null)}；\n'
            if len(market_name_name_id_null) != 0:
                err_str += f'指数详情market_name中name_type = 3, 4, 5, 6，name_id不是ID的数据为：{str(market_name_name_id_null)}；\n'
            if len(err_str) > old_err_str_len:
                return err_str + '\n'
            else:
                pass
        except Exception:
            print("today_market_name:tuple的方法就一个值")

    def today_option(self, datas):
        '''
            当天所有系列赛的option 表
        :param datas:
        :return:
        '''
        try:
            sql = '''
                    SELECT * FROM `data-rate-center`.option WHERE market_type_id in {};
                '''.format(tuple(datas))
            if self.env_flag == 'release':
                option_res = self.doMysql.select_basic(cnn=self.cnn_basic, sql=sql)
            elif self.env_flag == 'develop':
                option_res = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
            option_id_null = set()
            option_rate_null = set()
            option_option_status_null = set()
            option_option_is_winner_null = set()
            # option_option_option_status_5_null = set()
            # option_option_option_is_winner_1_2_null = set()
            # 关联 option_name 中的 option_id
            option_id_list = set()
            err_str = '当天所有系列赛的option表中(market_type_id)，'
            old_err_str_len = len(err_str)
            for data in option_res:
                # 指数详情option中ID为null
                if data.get('id') is None or data.get('id') == '':
                    option_id_null.add(data.get('market_type_id'))
                else:
                    option_id_list.add(data.get('id'))
                # 指数详情option中rate为null
                if data.get('rate') is None or data.get('rate') == '':
                    option_rate_null.add(data.get('market_type_id'))
                # 指数详情 option 中option_status不等于（1,2,3,4,5）
                if data.get('option_status') is None or data.get('option_status') == '' or data.get('option_status') not in (1, 2, 3, 4, 5):
                    option_option_status_null.add(data.get('market_type_id'))
                # 指数详情option中is_winner不等于（3, 1, 2）
                if data.get('is_winner') is None or data.get('is_winner') == '' or data.get('is_winner') not in (1, 2, 3):
                    option_option_is_winner_null.add(data.get('market_type_id'))
                # 指数详情同选项id，option_status为5，is_winner不等于（3, 2）
                # if data.get('option_status') == 5:
                #     if data.get('is_winner') not in (3, 2):
                #         option_option_option_status_5_null.add(data.get('market_type_id'))
                # # 指数详情同选项id，is_winner为1或2，option_status不等于5
                # if data.get('is_winner') in (3, 2):
                #     if data.get('option_status') != 5:
                #         option_option_option_is_winner_1_2_null.add(data.get('market_type_id'))
            if len(option_id_null) != 0:
                err_str += f'指数详情option中ID为null的数据为：{str(option_id_null)}；\n'
            if len(option_rate_null) != 0:
                err_str += f'指数详情option中rate为null的数据为：{str(option_rate_null)}；\n'
            if len(option_option_status_null) != 0:
                err_str += f'指数详情 option 中option_status不等于(1,2,3,4,5)的数据为：{str(option_option_status_null)}；\n'
            if len(option_option_is_winner_null) != 0:
                err_str += f'指数详情option中is_winner不等于(3, 1, 2)的数据为：{str(option_option_is_winner_null)}；\n'
            # if len(option_option_option_status_5_null) != 0:
            #     err_str += f'指数详情同选项id，option_status为5，is_winner不等于（3, 2）的数据为：{str(option_option_option_status_5_null)}；\n'
            # if len(option_option_option_is_winner_1_2_null) != 0:
            #     err_str += f'指数详情同选项id，is_winner为3或2，option_status不等于5的数据为：{str(option_option_option_is_winner_1_2_null)}；\n'
            option_name_err = self.today_option_name(option_id_list)
            if len(err_str) > old_err_str_len:
                if option_name_err is None:
                    return err_str + '\n'
                else:
                    return err_str + '\n' + option_name_err + '\n'
            else:
                if option_name_err is None:
                    pass
                else:
                    return option_name_err + '\n'
        except Exception:
            print("today_option:tuple的方法就一个值")

    def today_option_name(self, datas):
        '''
            option_name 表
        :param datas:
        :return:
        '''
        try:
            sql = '''
                            SELECT * FROM `data-rate-center`.option_name WHERE option_id in {};
                        '''.format(tuple(datas))
            if self.env_flag == 'release':
                option_name_res = self.doMysql.select_basic(cnn=self.cnn_basic, sql=sql)
            elif self.env_flag == 'develop':
                option_name_res = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
            option_option_name_type_null = set()
            option_option_name_zh_en_null = set()
            option_option_name_value_null = set()
            option_option_name_id_null = set()
            err_str = '当天所有系列赛的option_name表中(id)，'
            old_err_str_len = len(err_str)
            for data in option_name_res:
                # 指数详情 option_name 中name_type不等于（1,2,3,4,5,6）
                if data.get('name_type') is None or data.get('name_type') == '' or data.get('name_type') not in (1, 2, 3, 4, 5, 6):
                    option_option_name_type_null.add('id')
                # 指数详情option中name_type = 1 时，name_en和name_zh都为null
                elif data.get('name_type') == 1:
                    if (data.get('name_zh') is None and data.get('name_en') is None) or (data.get('name_zh') == '' and data.get('name_en') == ''):
                        option_option_name_zh_en_null.add(data.get('id'))
                # 指数详情option中name_type = 2时，name_value为null
                elif data.get('name_type') == 2:
                    if data.get('name_value') is None or data.get('name_value') == '':
                        option_option_name_value_null.add(data.get('id'))
                # 指数详情option中name_type = 3, 4, 5, 6时，name_id为null
                elif data.get('name_type') in (3, 4, 5, 6):
                    if data.get('name_id') == 0 or data.get('name_id') is None or data.get('name_id') == '':
                        option_option_name_id_null.add(data.get('id'))
            if len(option_option_name_type_null) != 0:
                err_str += f'指数详情 option_name 中name_type不等于(1,2,3,4,5,6)的数据为：{str(option_option_name_type_null)}；\n'
            if len(option_option_name_zh_en_null) != 0:
                err_str += f'指数详情option_name中name_type = 1 时，name_en和name_zh都为null的数据为：{str(option_option_name_zh_en_null)}；\n'
            if len(option_option_name_value_null) != 0:
                err_str += f'指数详情option_name中name_type = 2时，name_value为null的数据为：{str(option_option_name_value_null)}；\n'
            if len(option_option_name_id_null) != 0:
                err_str += f'指数详情option_name中name_type = 3, 4, 5, 6时，name_id为null的数据为：{str(option_option_name_id_null)}；\n'
            if len(err_str) > old_err_str_len:
                return err_str + '\n'
            else:
                pass
        except Exception:
            print("today_option_name:tuple的方法就一个值")

    # def today_market_type_option_status(self, datas):
    #     '''
    #         market_type表的market_status和option表的optuion_status
    #     :param datas:
    #     :return:
    #     '''
    #     try:
    #         market_option_list = []
    #         market_type_id = set()
    #         err_str = '当天所有系列赛，'
    #         old_err_str_len = len(err_str)
    #         for data in datas:
    #             market_type = {}
    #             market_type_id.add(data.get('id'))
    #             market_type['id'] = data.get('id')
    #             market_type['market_status'] = data.get('market_status')
    #             market_option_list.append(market_type)
    #         option_sql = '''
    #                 select * FROM `data-rate-center`.option where market_type_id in {};
    #             '''.format(tuple(market_type_id))
    #         option_res = DoMySql().select(cnn=self.cnn, sql=option_sql, env_flag=self.env_flag)
    #         option_err_list_1 = set()  # 指数详情 同玩法id，任一option_status为1,2，market_status等于1
    #         option_err_list_2 = set()  # 指数详情 同玩法id，market_status为3，任一option_status不是3
    #         option_err_list_3 = set()  # 指数详情 同玩法id，market_status为4，任一option_status不是4
    #         option_err_list_4 = set()  # 指数详情 同玩法id，market_status为5，任一option_status不是5
    #         for i in market_option_list:
    #             option_status_list_1 = set()
    #             option_status_list_2 = set()
    #             option_status_list_3 = set()
    #             option_status_list_4 = set()
    #             market_type_num1 = 0
    #             market_type_num2 = 0
    #             market_type_num3 = 0
    #             market_type_num4 = 0
    #             for y in option_res:
    #                 if i.get('id') == y.get('market_type_id'):
    #                     # 指数详情 同玩法id，market_status等于1,任一option_status为1,2，
    #                     if i.get('market_status') == 1:
    #                         market_type_num1 = i.get('id')
    #                         option_status_list_1.add(y.get('option_status'))
    #                     # 指数详情 同玩法id，market_status为3，任一option_status不是3
    #                     if i.get('market_status') == 3:
    #                         market_type_num2 = i.get('id')
    #                         option_status_list_2.add(y.get('option_status'))
    #                     # 指数详情 同玩法id，market_status为4，任一option_status不是4
    #                     if i.get('market_status') == 4:
    #                         market_type_num3 = i.get('id')
    #                         option_status_list_3.add(y.get('option_status'))
    #                     # 指数详情 同玩法id，market_status为5，全部option_status均不是5
    #                     if i.get('market_status') == 5:
    #                         market_type_num4 = i.get('id')
    #                         option_status_list_4.add(y.get('option_status'))
    #             if i.get('market_status') not in option_status_list_1 and market_type_num1 != 0:
    #                 option_err_list_1.add(market_type_num1)
    #             if i.get('market_status') not in option_status_list_2 and market_type_num2 != 0:
    #                 option_err_list_2.add(market_type_num2)
    #             if i.get('market_status') not in option_status_list_3 and market_type_num3 != 0:
    #                 option_err_list_3.add(market_type_num3)
    #             if i.get('market_status') not in option_status_list_4 and market_type_num4 != 0:
    #                 option_err_list_4.add(market_type_num4)
    #         if len(option_err_list_2) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，market_status为3，任一option_status不是3的数据为：{str(option_err_list_2)}； \n'
    #         if len(option_err_list_3) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，market_status为4，任一option_status不是4的数据为：{str(option_err_list_3)}； \n'
    #         if len(option_err_list_4) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，market_status为5，全部option_status均不是5的数据为：{str(option_err_list_4)}； \n'
    #         if len(option_err_list_1) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法market_status等于1，任一option_status不为1,2的数据为：{str(option_err_list_1)}\n；'
    #         for i in option_res:
    #             market_status_4_1 = set()  # option status为4的时候，market_status 的状态
    #             market_status_4_2 = set()  # option status不为4的时候，market_status 的状态
    #             market_status_4_err = set()  # 全部option_status为4，market_status不是4的ID
    #             market_status_5_err = set()  # option_status为5，market_status不是5的ID
    #             # 指数详情 同玩法id，全部option_status为4，market_status不是4
    #             if i.get('option_status') == 4:
    #                 i.get('market_type_id')
    #                 for data in datas:
    #                     if data.get('id') == i.get('market_type_id'):
    #                         market_status_4_1.add(data.get('market_status'))
    #             else:
    #                 i.get('market_type_id')
    #                 for data in datas:
    #                     if data.get('id') == i.get('market_type_id'):
    #                         market_status_4_2.add(data.get('market_status'))
    #             # 指数详情同玩法id，任一option_status为5，market_status不是5
    #             if i.get('option_status') == 5:
    #                 i.get('market_type_id')
    #                 for data in datas:
    #                     if data.get('id') == i.get('market_type_id'):
    #                         if data.get('market_status') != 5:
    #                             market_status_5_err.add(i.get('market_type_id'))
    #             for m_2 in market_status_4_2:
    #                 for m_1 in market_status_4_1:
    #                     if m_2 == m_1:
    #                         market_status_4_err.add(m_1)
    #         if len(market_status_4_err) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，全部option_status为4，market_status不是4的数据为：{str(market_status_4_err)}； \n'
    #         if len(market_status_5_err) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，任一option_status为5，market_status不是5的数据为：{str(market_status_5_err)}； \n'
    #         if len(err_str) > old_err_str_len:
    #             return err_str + '\n'
    #         else:
    #             pass
    #     except Exception:
    #         print("today_market_type_option_status:tuple方法就一个值")

    # def today_market_type_option_status(self, datas):
    #     '''
    #         market_type表的market_status和option表的optuion_status
    #     :param datas:
    #     :return:
    #     '''
    #     try:
    #         market_option_list = []
    #         market_type_id = set()
    #         err_str = '当天所有系列赛，'
    #         old_err_str_len = len(err_str)
    #         for data in datas:
    #             market_type = {}
    #             market_type_id.add(data.get('id'))
    #             market_type['id'] = data.get('id')
    #             market_type['market_status'] = data.get('market_status')
    #             market_option_list.append(market_type)
    #         option_sql = '''
    #                 select * FROM `data-rate-center`.option where market_type_id in {};
    #             '''.format(tuple(market_type_id))
    #         option_res = DoMySql().select(cnn=self.cnn, sql=option_sql, env_flag=self.env_flag)
    #         option_err_list_1 = set()  # 指数详情 同玩法id，任一option_status为1,2，market_status等于1
    #         option_err_list_2 = set()  # 指数详情 同玩法id，market_status为3，任一option_status不是3
    #         option_err_list_3 = set()  # 指数详情 同玩法id，market_status为4，任一option_status不是4
    #         option_err_list_4 = set()  # 指数详情 同玩法id，market_status为5，任一option_status不是5
    #         for i in market_option_list:
    #             option_status_list_1 = set()
    #             option_status_list_2 = set()
    #             option_status_list_3 = set()
    #             option_status_list_4 = set()
    #             market_type_num1 = 0
    #             market_type_num2 = 0
    #             market_type_num3 = 0
    #             market_type_num4 = 0
    #             for y in option_res:
    #                 if i.get('id') == y.get('market_type_id'):
    #                     # 指数详情 同玩法id，market_status等于1,任一option_status为1,2，
    #                     if i.get('market_status') == 1:
    #                         market_type_num1 = i.get('id')
    #                         option_status_list_1.add(y.get('option_status'))
    #                     # 指数详情 同玩法id，market_status为3，任一option_status不是3
    #                     if i.get('market_status') == 3:
    #                         market_type_num2 = i.get('id')
    #                         option_status_list_2.add(y.get('option_status'))
    #                     # 指数详情 同玩法id，market_status为4，任一option_status不是4
    #                     if i.get('market_status') == 4:
    #                         market_type_num3 = i.get('id')
    #                         option_status_list_3.add(y.get('option_status'))
    #                     # 指数详情 同玩法id，market_status为5，全部option_status均不是5
    #                     if i.get('market_status') == 5:
    #                         market_type_num4 = i.get('id')
    #                         option_status_list_4.add(y.get('option_status'))
    #             if i.get('market_status') not in option_status_list_1 and market_type_num1 != 0:
    #                 option_err_list_1.add(market_type_num1)
    #             if i.get('market_status') not in option_status_list_2 and market_type_num2 != 0:
    #                 option_err_list_2.add(market_type_num2)
    #             if i.get('market_status') not in option_status_list_3 and market_type_num3 != 0:
    #                 option_err_list_3.add(market_type_num3)
    #             if i.get('market_status') not in option_status_list_4 and market_type_num4 != 0:
    #                 option_err_list_4.add(market_type_num4)
    #         if len(option_err_list_2) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，market_status为3，任一option_status不是3的数据为：{str(option_err_list_2)}； \n'
    #         if len(option_err_list_3) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，market_status为4，任一option_status不是4的数据为：{str(option_err_list_3)}； \n'
    #         if len(option_err_list_4) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，market_status为5，全部option_status均不是5的数据为：{str(option_err_list_4)}； \n'
    #         if len(option_err_list_1) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法market_status等于1，任一option_status不为1,2的数据为：{str(option_err_list_1)}\n；'
    #         for i in option_res:
    #             market_status_4_1 = set()  # option status为4的时候，market_status 的状态
    #             market_status_4_2 = set()  # option status不为4的时候，market_status 的状态
    #             market_status_4_err = set()  # 全部option_status为4，market_status不是4的ID
    #             market_status_5_err = set()  # option_status为5，market_status不是5的ID
    #             # 指数详情 同玩法id，全部option_status为4，market_status不是4
    #             if i.get('option_status') == 4:
    #                 i.get('market_type_id')
    #                 for data in datas:
    #                     if data.get('id') == i.get('market_type_id'):
    #                         market_status_4_1.add(data.get('market_status'))
    #             else:
    #                 i.get('market_type_id')
    #                 for data in datas:
    #                     if data.get('id') == i.get('market_type_id'):
    #                         market_status_4_2.add(data.get('market_status'))
    #             # 指数详情同玩法id，任一option_status为5，market_status不是5
    #             if i.get('option_status') == 5:
    #                 i.get('market_type_id')
    #                 for data in datas:
    #                     if data.get('id') == i.get('market_type_id'):
    #                         if data.get('market_status') != 5:
    #                             market_status_5_err.add(i.get('market_type_id'))
    #             for m_2 in market_status_4_2:
    #                 for m_1 in market_status_4_1:
    #                     if m_2 == m_1:
    #                         market_status_4_err.add(m_1)
    #         if len(market_status_4_err) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，全部option_status为4，market_status不是4的数据为：{str(market_status_4_err)}； \n'
    #         if len(market_status_5_err) != 0:
    #             err_str += f'指数详情 option表中（market_type_id）同玩法id，任一option_status为5，market_status不是5的数据为：{str(market_status_5_err)}； \n'
    #         if len(err_str) > old_err_str_len:
    #             return err_str + '\n'
    #         else:
    #             pass
    #     except Exception:
    #         print("today_market_type_option_status:tuple方法就一个值")
    #

    # def todya_match_id(self):
    #     '''
    #         当天已结束小局
    #     :return:
    #     '''
    #     try:
    #         lol_sql = '''
    #                           select * FROM `data-center`.lol_match where series_id in (
    #                           select p_id FROM `data-center`.ex_series where source=1 and status=3 and game_id={} and source=1 and deleted=1 and audit in (2,4)
    #                           and start_time >= (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE)) - 3600*8)
    #                           and start_time < (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE) + INTERVAL 1 DAY) - 3600*8)
    #                         ) and deleted=1 and status=3;
    #                         '''.format(1)
    #         dota_sql = '''
    #                           select * FROM `data-center`.dota_match where series_id in (
    #                           select p_id FROM `data-center`.ex_series where source=1 and status=3 and game_id={} and source=1 and deleted=1 and audit in (2,4)
    #                           and start_time >= (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE)) - 3600*8)
    #                           and start_time < (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE) + INTERVAL 1 DAY) - 3600*8)
    #                         ) and deleted=1 and status=3;
    #                         '''.format(2)
    #         csgo_sql = '''
    #                           select * FROM `data-center`.match where series_id in (
    #                           select p_id FROM `data-center`.ex_series where source=1 and status=3 and game_id={} and source=1 and deleted=1 and audit in (2,4)
    #                           and start_time >= (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE)) - 3600*8)
    #                           and start_time < (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE) + INTERVAL 1 DAY) - 3600*8)
    #                         ) and deleted=1 and status=3;
    #                         '''.format(3)
    #         kog_sql = '''
    #                   select * FROM `data-center`.kog_match where series_id in (
    #                   select p_id FROM `data-center`.ex_series where source=1 and status=3 and game_id={} and source=1 and deleted=1 and audit in (2,4)
    #                   and start_time >= (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE)) - 3600*8)
    #                   and start_time < (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE) + INTERVAL 1 DAY) - 3600*8)
    #                 ) and deleted=1 and status=3;
    #                 '''.format(3)
    #         lol_datas = DoMySql().select(cnn=self.cnn, sql=lol_sql, env_flag=self.env_flag)
    #         dota_datas = DoMySql().select(cnn=self.cnn, sql=dota_sql, env_flag=self.env_flag)
    #         csgo_datas = DoMySql().select(cnn=self.cnn, sql=csgo_sql, env_flag=self.env_flag)
    #         kog_datas = DoMySql().select(cnn=self.cnn, sql=kog_sql, env_flag=self.env_flag)
    #         lol_match_id_list = set()
    #         dota_match_id_list = set()
    #         csgo_match_id_list = set()
    #         kog_match_id_list = set()
    #         for data in lol_datas:
    #             lol_match_id_list.add(data.get('id'))
    #         for data in dota_datas:
    #             dota_match_id_list.add(data.get('id'))
    #         for data in csgo_datas:
    #             csgo_match_id_list.add(data.get('id'))
    #         for data in kog_datas:
    #             kog_match_id_list.add(data.get('id'))
    #         lol_option_err = set()
    #         dota_option_err = set()
    #         csgo_option_err = set()
    #         kog_option_err = set()
    #         err_str = '当天所有已结束的小局option中(id)，'
    #         old_err_str_len = len(err_str)
    #         if len(lol_match_id_list) != 0:
    #             lol_market_sql = '''
    #                     SELECT * FROM `data-rate-center`.market where inside_level_id in {};
    #                 '''.format(tuple(lol_match_id_list))
    #             lol_market_res = DoMySql().select(cnn=self.cnn, sql=lol_market_sql, env_flag=self.env_flag)
    #             lol_market_id_list = set()
    #             for data in lol_market_res:
    #                 lol_market_id_list.add(data.get('id'))
    #             if len(lol_market_id_list) != 0:
    #                 lol_market_type_sql = '''
    #                             SELECT * FROM `data-rate-center`.market_type where market_id in {};
    #                         '''.format(tuple(lol_market_id_list))
    #                 lol_market_type_res = DoMySql().select(cnn=self.cnn, sql=lol_market_type_sql, env_flag=self.env_flag)
    #                 lol_market_type_id_list = set()
    #                 for data in lol_market_type_res:
    #                     lol_market_type_id_list.add(data.get('id'))
    #                 if len(lol_market_type_id_list) != 0:
    #                     lol_option_sql = '''
    #                                     SELECT * FROM `data-rate-center`.option where market_type_id in {};
    #                                 '''.format(tuple(lol_market_type_id_list))
    #                     lol_option_res = DoMySql().select(cnn=self.cnn, sql=lol_option_sql, env_flag=self.env_flag)
    #                 # 指数详情lol小局状态为已结束，option_status为1或2, is_winner为1
    #                     for data in lol_option_res:
    #                         if data.get('option_status') in (1, 2):
    #                             if data.get('is_winner') == 1:
    #                                 lol_option_err.add(data.get('id'))
    #         if len(dota_match_id_list) != 0:
    #             dota_market_sql = '''
    #                             SELECT * FROM `data-rate-center`.market where inside_level_id in {};
    #                         '''.format(tuple(dota_match_id_list))
    #             dota_market_res = DoMySql().select(cnn=self.cnn, sql=dota_market_sql, env_flag=self.env_flag)
    #             dota_market_id_list = set()
    #             for data in dota_market_res:
    #                 dota_market_id_list.add(data.get('id'))
    #             if len(dota_market_id_list) != 0:
    #                 dota_market_type_sql = '''
    #                                     SELECT * FROM `data-rate-center`.market_type where market_id in {};
    #                                 '''.format(tuple(dota_market_id_list))
    #                 dota_market_type_res = DoMySql().select(cnn=self.cnn, sql=dota_market_type_sql, env_flag=self.env_flag)
    #                 dota_market_type_id_list = set()
    #                 for data in dota_market_type_res:
    #                     dota_market_type_id_list.add(data.get('id'))
    #                 dota_option_sql = '''
    #                                         SELECT * FROM `data-rate-center`.option where market_type_id in {};
    #                                     '''.format(tuple(dota_market_type_id_list))
    #                 dota_option_res = DoMySql().select(cnn=self.cnn, sql=dota_option_sql, env_flag=self.env_flag)
    #                 # 指数详情dota小局状态为已结束，option_status为1或2, is_winner为1
    #                 for data in dota_option_err:
    #                     if data.get('option_status') in (1, 2):
    #                         if data.get('is_winner') == 1:
    #                             dota_option_res.add(data.get('id'))
    #         if len(csgo_match_id_list) != 0:
    #             csgo_market_sql = '''
    #                             SELECT * FROM `data-rate-center`.market where inside_level_id in {};
    #                         '''.format(tuple(csgo_match_id_list))
    #             csgo_market_res = DoMySql().select(cnn=self.cnn, sql=csgo_market_sql, env_flag=self.env_flag)
    #             csgo_market_id_list = set()
    #             for data in csgo_market_res:
    #                 csgo_market_id_list.add(data.get('id'))
    #             if len(csgo_market_id_list) != 0:
    #                 csgo_market_type_sql = '''
    #                                     SELECT * FROM `data-rate-center`.market_type where market_id in {};
    #                                 '''.format(tuple(csgo_market_id_list))
    #                 csgo_market_type_res = DoMySql().select(cnn=self.cnn, sql=csgo_market_type_sql, env_flag=self.env_flag)
    #                 csgo_market_type_id_list = set()
    #                 for data in csgo_market_type_res:
    #                     csgo_market_type_id_list.add(data.get('id'))
    #                 csgo_option_sql = '''
    #                                         SELECT * FROM `data-rate-center`.option where market_type_id in {};
    #                                     '''.format(tuple(csgo_market_type_id_list))
    #                 csgo_option_res = DoMySql().select(cnn=self.cnn, sql=csgo_option_sql, env_flag=self.env_flag)
    #                 # 指数详情csgo小局状态为已结束，option_status为1或2, is_winner为1
    #                 for data in csgo_option_err:
    #                     if data.get('option_status') in (1, 2):
    #                         if data.get('is_winner') == 1:
    #                             csgo_option_res.add(data.get('id'))
    #         if len(kog_match_id_list) != 0:
    #             kog_market_sql = '''
    #                             SELECT * FROM `data-rate-center`.market where inside_level_id in {};
    #                         '''.format(tuple(kog_match_id_list))
    #             kog_market_res = DoMySql().select(cnn=self.cnn, sql=kog_market_sql, env_flag=self.env_flag)
    #             kog_market_id_llist = set()
    #             for data in kog_market_res:
    #                 kog_market_id_llist.add(data.get('id'))
    #             kog_market_type_sql = '''
    #                         SELECT * FROM `data-rate-center`.market_type where market_id in {};
    #                     '''.format(tuple(kog_market_id_llist))
    #             kog_market_type_res = DoMySql().select(cnn=self.cnn, sql=kog_market_type_sql, env_flag=self.env_flag)
    #             kog_market_type_id_list = set()
    #             for data in kog_market_type_res:
    #                 kog_market_type_id_list.add(data.get('id'))
    #             kog_option_sql = '''
    #                             SELECT * FROM `data-rate-center`.option where market_type_id in {};
    #                         '''.format(tuple(kog_market_type_id_list))
    #             kog_option_res = DoMySql().select(cnn=self.cnn, sql=kog_option_sql, env_flag=self.env_flag)
    #             # 指数详情kog小局状态为已结束，option_status为1或2, is_winner为1
    #             for data in kog_option_err:
    #                 if data.get('option_status') in (1, 2):
    #                     if data.get('is_winner') == 1:
    #                         kog_option_res.add(data.get('id'))
    #         if len(lol_option_err) != 0:
    #             err_str += f'指数详情lol小局状态为已结束，option_status为1或2, is_winner为0的数据为：{str(lol_option_err)}；\n'
    #         if len(dota_option_err) != 0:
    #             err_str += f'指数详情dota小局状态为已结束，option_status为1或2, is_winner为0的数据为：{str(dota_option_err)}；\n'
    #         if len(csgo_option_err) != 0:
    #             err_str += f'指数详情csgo小局状态为已结束，option_status为1或2, is_winner为0的数据为：{str(csgo_option_err)}；\n'
    #         if len(kog_option_err) != 0:
    #             err_str += f'指数详情kog小局状态为已结束，option_status为1或2, is_winner为0的数据为：{str(kog_option_err)}；\n'
    #         if len(err_str) > old_err_str_len:
    #             return err_str + '\n'
    #         else:
    #             pass
    #     except Exception:
    #         print("todya_match_id:方法tuple只有一个值")


if __name__ == '__main__':
    cnn_centon = DoMySql().cnn_centon_def()
    cnn_basic = DoMySql().cnn_basic_def()
    ss = TodaySeriesTen('develop', cnn_centon, cnn_basic)
    ss.today_series_id()

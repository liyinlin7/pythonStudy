from common.do_mysql import DoMySql
import logging


class TodaySeriesTen_football(object):
    '''
        雷竞技的系列赛
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_basketball = self.do_mysql.connect_mysql_basketball(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.cnn_rate = self.do_mysql.connect_mysql_rate(env_flag=env_flag)  # 0是测试，1是线上

    def today_series_id(self):
        '''
            当天赛程所有玩法
        :param env_flag:
        :return:
        '''
        sql = '''
                 SELECT * FROM `sports-soccer-match`.ex_match  where source=2  and p_id != 0 and match_start_time >= (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE)))
                 and match_start_time < (UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE) + INTERVAL 1 DAY)) ;
             '''
        datas = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
        series_ex_id_list = set()
        series_status_3_list = set()  # 已经结束的系列赛ex_id
        if len(datas) != 0:
            for data in datas:
                series_ex_id_list.add(data.get('ex_id'))
                if data.get('status') == 7:
                    series_status_3_list.add(data.get('ex_id'))
            series_ex_id_tuple = tuple(series_ex_id_list)
            series_ex_id_str = None
            if len(series_ex_id_tuple) == 1:
                series_ex_id_str = str(series_ex_id_tuple).replace(',', '')
            else:
                series_ex_id_str = series_ex_id_tuple
            mark_sql = f'''
                                SELECT * FROM `sports-rate-center`.market_type where level_id in {series_ex_id_str};
                            '''
            if self.env_flag == 0:
                market_res = self.do_mysql.select(cnn=self.cnn, sql=mark_sql, env_flag=self.env_flag)
            else:
                market_res = self.do_mysql.select_rate(cnn=self.cnn_rate, sql=mark_sql, env_flag=self.env_flag)
            err1 = self.today_market_type(market_res)
            if err1 is None : err1 = ''
            err = err1
            print("足球错误数据:", err)
            if len(err) != 0:
                print(err)
                return err
            else:
                return ''
        else:
            return ''


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
            err_str = '足球：当天所有赛程的market_type表中(level_id)，'
            old_err_str_len = len(err_str)
            for data in market_res:
                # print(data)
                # -- 指数详情玩法ID为null
                market_id_list.add(data.get('id'))
                if data.get('market_id') is None or data.get('market_id') == '':
                    market_type_market_id_null.add(data.get('level_id'))
                else:
                    market_market_id_list.add(data.get('market_id'))
                # 指数详情level = NULL或不等于（100）
                if data.get('level') is None or data.get('level') == '' or data.get('level') not in (100,):
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
                err_str += f'指数详情level = NULL或不等于(100)的数据为：{str(market_type_level_null)}；\n'
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
            return err
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
                    SELECT * FROM `sports-rate-center`.market_name where market_id in {};
                '''.format(tuple(datas))
            if self.env_flag == 0:
                market_name_res = self.do_mysql.select(cnn=self.cnn, sql=market_name_sql, env_flag=self.env_flag)
            else:
                market_name_res = self.do_mysql.select_rate(cnn=self.cnn_rate, sql=market_name_sql, env_flag=self.env_flag)
            market_name_name_type_null = set()
            market_name_name_zh_en_null = set()
            market_name_name_value_null = set()
            market_name_name_id_null = set()
            err_str = '足球：当天所有赛程的market_name表中(market_id)，'
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
                return ''
        except Exception:
            print("today_market_name:tuple的方法就一个值")

    def today_option(self, datas):
        '''
            当天所有赛程的option 表
        :param datas:
        :return:
        '''
        try:
            sql = '''
                    SELECT * FROM `sports-rate-center`.option WHERE market_type_id in {};
                '''.format(tuple(datas))
            if self.env_flag == 0:
                option_res = self.do_mysql.select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
            else:
                option_res = self.do_mysql.select_rate(cnn=self.cnn_rate, sql=sql, env_flag=self.env_flag)
            option_id_null = set()
            option_rate_null = set()
            option_option_status_null = set()
            option_option_is_winner_null = set()
            # option_option_option_status_5_null = set()
            # option_option_option_is_winner_1_2_null = set()
            # 关联 option_name 中的 option_id
            option_id_list = set()
            err_str = '足球：当天所有赛程的option表中(market_type_id)，'
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
                # 指数详情option中is_winner不等于（1, 2, 3, 4, 5, 6）
                if data.get('is_winner') is None or data.get('is_winner') == '' or data.get('is_winner') not in (1, 2, 3, 4, 5, 6):
                    option_option_is_winner_null.add(data.get('market_type_id'))

            if len(option_id_null) != 0:
                err_str += f'指数详情option中ID为null的数据为：{str(option_id_null)}；\n'
            if len(option_rate_null) != 0:
                err_str += f'指数详情option中rate为null的数据为：{str(option_rate_null)}；\n'
            if len(option_option_status_null) != 0:
                err_str += f'指数详情 option 中option_status不等于(1,2,3,4,5)的数据为：{str(option_option_status_null)}；\n'
            if len(option_option_is_winner_null) != 0:
                err_str += f'指数详情option中is_winner不等于(1, 2, 3, 4, 5, 6)的数据为：{str(option_option_is_winner_null)}；\n'
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
                    return option_name_err
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
                            SELECT * FROM `sports-rate-center`.option_name WHERE option_id in {};
                        '''.format(tuple(datas))
            if self.env_flag == 0:
                option_name_res = self.do_mysql.select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
            else:
                option_name_res = self.do_mysql.select_rate(cnn=self.cnn_rate, sql=sql, env_flag=self.env_flag)
            option_option_name_type_null = set()
            option_option_name_zh_en_null = set()
            option_option_name_value_null = set()
            option_option_name_id_null = set()
            err_str = '足球：当天所有系列赛的option_name表中(id)，'
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
                return ''
        except Exception:
            print("today_option_name:tuple的方法就一个值")


if __name__ == '__main__':
    t = TodaySeriesTen(env_flag=0).today_series_id()

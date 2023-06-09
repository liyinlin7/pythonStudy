import json
import time
import mysql.connector
from common.read_config import ReadConfig
from common import read_path
import logging
from common.send_alarm import SendAlarm
import os
import datetime
import time
from common import my_logger

sql = 'SELECT sqlString,sql_describe,status,id FROM `api-mega`.`auto_sql`'
sql_list = [['SELECT id,source,game_id,start_time,ex_id from `data-center`.ex_series WHERE `status` = 1 and '
             'start_time < unix_timestamp(now())-900;', '比赛开始时间是15分钟前，但是当前比赛状态是未开始']]
topic = eval(ReadConfig().read_config(read_path.conf_path, 'TOPIC', 'topic_dic'))


class DoMySql:
    def connect(self, env_flag=0):
        """连接数据库"""
        # env_flag = ReadConfig().read_config(read_path.conf_path, 'MODE', 'env_flag')
        if env_flag == 0:  # 如果是0，表示测试环境
            config = eval(ReadConfig().read_config(read_path.conf_path, 'TEST', 'config'))  # 测试环境数据库
        else:  # 如果是1，表示生产环境
            config = eval(ReadConfig().read_config(read_path.conf_path, 'PRODUCTION', 'config'))  # 生产环境数据库
        cnn_flag = True
        retry_count = 0
        while cnn_flag:
            try:
                logging.info('开始连接数据库---------')
                cnn = mysql.connector.connect(**config)  # 建立连接
                logging.info('数据库连接成功')
                cnn_flag = False
                return cnn
            except Exception as e:
                retry_count += 1
                logging.error('第{}次连接数据库失败：{}'.format(retry_count, e))

    def test_connection(self, cnn):
        """测试数据库是否正常连接"""
        try:
            cnn.ping()
            logging.info('ping成功')
            result = True
        except Exception as e:
            logging.info('ping失败：{}'.format(e))
            result = False
        return result

    def select(self, cnn, sql, env_flag, state=0):
        """
        查询数据库
        :param cnn: 数据库连接对象
        :param sql: 执行的sql
        :param state: 如果只查询一条数据，传1；查询多条数据，传0
        :return:返回查询结果，嵌套字典列表形式，key为对应的字段名，如：[{'team_id': 1107}, {'team_id': 1108}]
        """
        # 判断数据库能否正常连接，如果不能连接，则重新建立连接
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect(env_flag=env_flag)
        cursor = db.cursor()  # 创建一个游标
        # logging.info('开始执行sql：{}'.format(sql))
        cursor.execute(sql)  # 执行SQL语句
        desc = cursor.description
        if state == 1:
            res = cursor.fetchone()  # 返回的数据类型是元组
        else:
            res = cursor.fetchall()  # 返回的数据类型是列表,里面的元素是元组
        data_dic = [dict(zip([col[0] for col in desc], row)) for row in res]
        cursor.close()
        return data_dic

    def insert(self, cnn, sql):
        """插入数据库"""
        # 判断数据库能否正常连接，如果不能连接，则重新建立连接
        if self.test_connection(cnn):
            db = cnn
        else:
            db = self.connect(env_flag=0)
        cursor = db.cursor()  # 创建一个游标
        try:
            cursor.execute(sql)  # 执行SQL语句
            print(cursor.rowcount, "记录插入成功。")
        except Exception as e:
            logging.error('记录插入失败:{}'.format(e))
            logging.error('出错SQL是：{}'.format(sql))
        cnn.commit()
        return cursor.lastrowid

    def insert_data(self, cnn, data, type):
        """
        插入数据
        :param cnn: 数据库连接对象
        :param data: 需要插入的源数据
        :param type: 数据类型，csgo_live_data,csgo_live_event,csgo_live_special_event
        :return: 插入成功，返回success，失败返回fail
        """
        create_time = time.strftime('%Y-%m-%d %T', time.localtime(time.time()))
        if type == topic['CSGO_LIVE_DATA']:  # 实时数据

            # 插入系列赛表信息
            series_insert_sql = self.insert_sql('k_series', data, extra_key=['teams'], add_dic={'json_data': data})
            # 获取新增的系列赛id
            s_id = self.insert(cnn, series_insert_sql)

            # 插入战队表信息
            team_data = eval(str(data).strip('"').replace('\\', '').replace('null', 'None'))['teams']
            for i in team_data:
                team_insert_sql = self.insert_sql(db_name='k_series_team', data=i, extra_key=['player'],
                                                  add_dic={'s_id': s_id},
                                                  replace_key=[{'old_key': 'kill', 'new_key': '`kill`'}])
                # print(team_insert_sql)
                self.insert(cnn, team_insert_sql.replace('None', 'null'))
                team_id = i['team_id']

                # 插入队员表信息
                player_data = i['player']
                for n in player_data:
                    player_insert_sql = self.insert_sql(db_name='k_series_player', data=n,
                                                        add_dic={'s_id': s_id, 'team_id': team_id},
                                                        replace_key=[{'old_key': 'kill', 'new_key': '`kill`'}],
                                                        str_key=['item'])
                    # print(player_insert_sql)
                    self.insert(cnn, player_insert_sql.replace('None', 'null'))

        elif type == topic['CSGO_LIVE_EVENT']:  # csgo实时赛事事件
            # 处理data格式
            data_0 = eval(str(data).strip('"').replace('\\', '').replace('null', 'None'))
            # 取出event_data的值
            data_1 = data_0['event_data']
            if 'assist' in data_1:
                data_1['assist'] = str(data_1['assist'])
            # 删除event_data
            del data_0['event_data']
            # 修改stage键名
            data_0['s_stage'] = data_0['stage']
            del data_0['stage']
            # 组装event_data
            try:
                final_data = {**data_0, **data_1}
            except Exception as e:
                logging.error('出错数据是：{}，\n出错原因是：{}'.format(data, e))
                final_data = data_0
                pass
            # 插入事件表信息
            live_event_insert_sql = self.insert_sql('k_live_event', final_data,
                                                    add_dic={'json_data': data, 'create_time': create_time})
            self.insert(cnn, live_event_insert_sql)

        elif type == topic['CSGO_LIVE_EVENT_SPECIAL']:  # 实时特殊事件
            # 处理data格式
            data_0 = eval(str(data).strip('"').replace('\\', '').replace('null', 'None'))
            # 取出event_data的值
            data_1 = data_0['event_data']
            # 删除event_data
            del data_0['event_data']
            # 组装event_data
            final_data = {**data_0, **data_1}

            # 插入事件表信息
            live_event_insert_sql = self.insert_sql('k_live_event_special', final_data, add_dic={'json_data': data})
            self.insert(cnn, live_event_insert_sql)

        elif type == topic['LOL_LIVE_DATA']:  # lol实时数据
            # 插入系列赛表信息
            series_insert_sql = self.insert_sql('k_lol_series', data, extra_key=['team'])
            # 获取新增的系列赛id
            s_id = self.insert(cnn, series_insert_sql)

            # 插入战队表信息
            team_data = json.loads(str(data).strip('"').replace('\\', ''))['team']
            for i in team_data:
                team_insert_sql = self.insert_sql(db_name='k_lol_team', data=i, extra_key=['player'],
                                                  add_dic={'s_id': s_id},
                                                  replace_key=[{'old_key': 'kill', 'new_key': '`kill`'}])
                # print(team_insert_sql)
                self.insert(cnn, team_insert_sql)
                team_id = i['team_id']

                # 插入队员表信息
                player_data = i['player']
                for n in player_data:
                    player_insert_sql = self.insert_sql(db_name='k_lol_player', data=n,
                                                        add_dic={'s_id': s_id, 'team_id': team_id},
                                                        replace_key=[{'old_key': 'kill', 'new_key': '`kill`'}],
                                                        str_key=['item', 'spell'])
                    # print(player_insert_sql)
                    self.insert(cnn, player_insert_sql)

        elif type == topic['LOL_LIVE_EVENT']:
            # 插入实时事件表信息
            live_event_insert_sql = self.insert_sql('k_lol_event', data, str_key=['event_data'],
                                                    add_dic={'json_data': data})
            self.insert(cnn, live_event_insert_sql)

        elif type == topic['LOL_LIVE_EVENT_SPECIAL']:
            # 处理data格式
            data_0 = json.loads(str(data).strip('"').replace('\\', ''))
            # 取出event_data的值
            data_1 = data_0['event_data']
            # 删除event_data
            del data_0['event_data']
            # 组装event_data
            final_data = {**data_0, **data_1}

            # 插入事件表信息
            live_event_insert_sql = self.insert_sql('k_lol_special_event', final_data, add_dic={'json_data': data})
            self.insert(cnn, live_event_insert_sql)

        # elif type == topic['DOTA_LIVE_DATA']:  # 实时数据
        #     # 插入系列赛表信息
        #     series_insert_sql = self.insert_sql('k_dota_series', data, extra_key=['team'])
        #     # 获取新增的系列赛id
        #     s_id = self.insert(cnn, series_insert_sql)
        #
        #     # 插入战队表信息
        #     team_data = json.loads(str(data).strip('"').replace('\\', ''))['team']
        #     for i in team_data:
        #         team_insert_sql = self.insert_sql(db_name='k_dota_team', data=i, extra_key=['player'],
        #                                           add_dic={'s_id': s_id},
        #                                           replace_key=[{'old_key': 'kill', 'new_key': '`kill`'}])
        #         # print(team_insert_sql)
        #         self.insert(cnn, team_insert_sql)
        #         team_id = i['team_id']
        #
        #         # 插入队员表信息
        #         player_data = i['player']
        #         for n in player_data:
        #             player_insert_sql = self.insert_sql(db_name='k_dota_player', data=n,
        #                                                 add_dic={'s_id': s_id, 'team_id': team_id},
        #                                                 replace_key=[{'old_key': 'kill', 'new_key': '`kill`'}],
        #                                                 str_key=['item'])
        #             # print(player_insert_sql)
        #             self.insert(cnn, player_insert_sql)
        #
        # elif type == topic['DOTA_LIVE_EVENT']:  # 实时事件
        #     # 插入实时事件表信息
        #     live_event_insert_sql = self.insert_sql('k_dota_event', data, str_key=['event_data'],
        #                                             add_dic={'json_data': data})
        #     self.insert(cnn, live_event_insert_sql)
        #
        # elif type == topic['DOTA_LIVE_EVENT_SPECIAL']:  # 实时特殊事件
        #     # 处理data格式
        #     data_0 = json.loads(str(data).strip('"').replace('\\', ''))
        #     # 取出event_data的值
        #     data_1 = data_0['event_data']
        #     # 删除event_data
        #     del data_0['event_data']
        #     # 组装event_data
        #     final_data = {**data_0, **data_1}
        #     # 插入事件表信息
        #     live_event_insert_sql = self.insert_sql('k_dota_special_event', final_data, add_dic={'json_data': data})
        #     self.insert(cnn, live_event_insert_sql)

    def insert_sql(self, db_name, data, extra_key=None, add_dic=None, replace_key=None, str_key=None):
        """
        处理数据新增的数据
        :param db_name: 表名称
        :param data: 待处理的json数据
        :param extra_key: 去除的字段名，type为list
        :param add_dic: 添加的字典
        :param replace_key: 需要替换的key名称，嵌套字典列表形式：[{'old_key': XXX, 'new_key': XXX}]
        :param str_key: 需要转换成字符串的键，type为list
        :return: 返回处理后的SQL
        """
        deal_data = eval(str(data).replace('null', 'None'))
        # 删除不需要的键值对
        if extra_key:
            for i in extra_key:
                del deal_data[i]
        # 添加需要的键值对
        if add_dic:
            deal_data = {**deal_data, **add_dic}

        # 替换key值
        if replace_key:
            for i in replace_key:
                deal_data[i['new_key']] = deal_data[i['old_key']]
                del deal_data[i['old_key']]

        # 转换字符串
        if str_key:
            for i in str_key:
                if i in deal_data:
                    deal_data[i] = str(deal_data[i])

        keys = tuple(deal_data.keys())
        val = tuple(deal_data.values())
        # str_s = ','.join(['%s' for i in keys])
        sql = "INSERT INTO `api-mega`.{} {} VALUES {}".format(db_name, str(keys).replace("'", ''), val).replace('None',
                                                                                                                'null')

        return sql

    def do_my_sql(self, sql, state=0, env_flag=1):
        # env_flag = ReadConfig().read_config(read_path.conf_path, 'MODE', 'env_flag')
        if env_flag == '0':  # 如果是0，表示测试环境
            config = eval(ReadConfig().read_config(read_path.conf_path, 'TEST', 'config'))  # 测试环境数据库
        else:  # 如果是1，表示生产环境
            config = eval(ReadConfig().read_config(read_path.conf_path, 'PRODUCTION', 'config'))  # 生产环境数据库
        cnn_flag = True
        retry_count = 0
        while cnn_flag:
            try:
                # logging.info('开始连接数据库---------')
                cnn = mysql.connector.connect(**config)  # 建立连接
                cursor = cnn.cursor()  # 创建一个游标
                # logging.info('开始执行sql：{}'.format(sql))
                cursor.execute(sql)  # 执行SQL语句
                desc = cursor.description
                if state == 1:
                    res = cursor.fetchone()  # 返回的数据类型是元组
                else:
                    res = cursor.fetchall()  # 返回的数据类型是列表,里面的元素是元组
                data_dic = [dict(zip([col[0] for col in desc], row)) for row in res]
                cursor.close()
                cnn.close()
                cnn_flag = False
                return data_dic
            except Exception as e:
                retry_count += 1
                logging.error('第{}次连接数据库失败：{}'.format(retry_count, e))

    def link_testsql(self):
        config = eval(ReadConfig().read_config(read_path.conf_path, 'TEST', 'config'))
        cnn = mysql.connector.connect(**config)
        return cnn

    def getSql(sql):
        # 配置测试站数据库 读取要跑auto的sql
        config = eval(ReadConfig().read_config(read_path.conf_path, 'TEST', 'config'))
        # 连接数据库
        cnn = mysql.connector.connect(**config)
        cursor = cnn.cursor()
        # 查询sql 取出要跑的sql语句
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        cnn.close()
        return res

    # status = 1 bug   status = 2 人工
    def do_sql(res):
        b_res_list = []
        r_res_list = []
        for i in res:
            sql_list = list(i)
            if sql_list[2] == '1':
                r_res_list.append(sql_list)
            else:
                b_res_list.append(sql_list)
        return b_res_list, r_res_list

    def auto_sql(res, type):
        try:
            config = eval(ReadConfig().read_config(read_path.conf_path, 'PRODUCTION', 'config'))
            # 连接数据库
            cnn = mysql.connector.connect(**config)
            cursor = cnn.cursor()
            count = 0
            errorCount = 0
            re_str = ''
            for i in res:
                print(i[3])
                count += 1
                cursor.execute(i[0])
                data = cursor.fetchall()
                if type == 1:
                    # DoMySql.sql_log(data)
                    pass
                # print(data)
                if len(data) == 0:
                    pass
                else:
                    errorCount += 1
                    print(data)
                    mystr = '数据id:' + str(i[3]) + ' 注释:' + i[1]
                    make_str = mystr + '----'
                    re_str = re_str + make_str
            cursor.close()
            cnn.close()
            return (count, errorCount, re_str)
        except Exception:
            print('数据库操作失败')

    def autoRunSql_b(sql, type):
        res = DoMySql.getSql(sql)
        result = DoMySql.do_sql(res)
        data = list(result)
        item = data[0]
        b_data = DoMySql.auto_sql(item, type)
        b_data = list(b_data)
        # print(b_data)
        SendAlarm.send_dingtalk_sql_b(b_data)

    def autoRunSql_r(sql, type):
        res = DoMySql.getSql(sql)
        result = DoMySql.do_sql(res)
        data = list(result)
        item = data[1]
        r_data = DoMySql.auto_sql(item, type)
        r_data = list(r_data)
        # print(r_data)
        SendAlarm.send_dingtalk_sql_r(r_data)

    # 特殊处理的sql执行
    def specialSql(sql_list, type):
        data = DoMySql.auto_sql(sql_list, type)
        mylist = list(data)
        print(mylist)
        SendAlarm.send_dingtalk_sql(mylist)

    def sql_log(data):
        time = datetime.datetime.now().strftime('%Y-%m-%d- %H:%M:%S')
        sql_log = time + str(data) + '\n'
        fp = open('mysql.txt', 'w')
        fp.write(sql_log)

    def notReview(self):
        s_id = []
        msg = '线上存在1小时内未审核的比赛系列赛id为：'
        mystr = ''
        config = eval(ReadConfig().read_config(read_path.conf_path, 'PRODUCTION', 'config'))
        cnn = mysql.connector.connect(**config)
        cursor = cnn.cursor()
        sql = 'SELECT * FROM `data-center`.ex_series WHERE audit = 1 AND source = 3 AND game_id in (1,3) AND start_time - unix_timestamp(now()) <= 3600 AND start_time >= unix_timestamp(now()) - 86400 ;'
        cursor.execute(sql)
        result = cursor.fetchall()
        try:
            state = len(result)
            if state != 0:
                desc = cursor.description
                res = result
                data_dic = [dict(zip([col[0] for col in desc], row)) for row in res]
                for data in data_dic:
                    print(data)
                    s_id.append(data['id'])
                for i in s_id:
                    mystr = mystr + str(i) + '/'
                msg = msg + mystr
                # print(msg)
                SendAlarm().send_dingtalk_review(msg)
            else:
                msg = '暂无匹配数据'
                # print(msg)
                SendAlarm().send_dingtalk_review(msg)
        except Exception as e:
            msg = '暂无匹配数据'
            # print(e)
            SendAlarm().send_dingtalk_review(msg)

    def lol_match(self):
        sql = 'SELECT id, bo FROM `data-center`.series WHERE game_id = 1 AND deleted = 1;'
        re_str = ''
        config = eval(ReadConfig().read_config(read_path.conf_path, 'PRODUCTION', 'config'))
        cnn = mysql.connector.connect(**config)
        # cnn = DoMySql().link_testsql()
        cursor = cnn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        desc = cursor.description
        data_dic = [dict(zip([col[0] for col in desc], row)) for row in result]
        for item in data_dic:
            sql = 'SELECT count(*) FROM `data-center`.lol_match WHERE series_id = {} AND deleted = 1;'.format(
                item['id'])
            cursor.execute(sql)
            match_count = cursor.fetchone()
            if item['bo'] != match_count[0]:
                re_str = re_str + str(item['id']) + '/'
        print(re_str)
        cursor.close()
        cnn.close()
        SendAlarm().send_dingtalk_match(re_str)

    def dota_match(self):
        sql = 'SELECT id, bo FROM `data-center`.series WHERE game_id = 2 AND deleted = 1;'
        re_str = ''
        config = eval(ReadConfig().read_config(read_path.conf_path, 'PRODUCTION', 'config'))
        cnn = mysql.connector.connect(**config)
        # cnn = DoMySql().link_testsql()
        cursor = cnn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        desc = cursor.description
        data_dic = [dict(zip([col[0] for col in desc], row)) for row in result]
        for item in data_dic:
            sql = 'SELECT count(*) FROM `data-center`.dota_match WHERE series_id = {} AND deleted = 1;'.format(
                item['id'])
            cursor.execute(sql)
            match_count = cursor.fetchone()
            if item['bo'] != match_count[0]:
                re_str = re_str + str(item['id']) + '/'
        print(re_str)
        cursor.close()
        cnn.close()
        SendAlarm().send_dingtalk_match(re_str)

    def match(self):
        DoMySql().lol_match()
        DoMySql().dota_match()


if __name__ == '__main__':
    # sql = "select team_id from `data-center`.league_team where deleted = 1 and league_id = 171;"
    # cnn = DoMySql().connect(env_flag=0)
    # a = r'"{\"stage\": 1,\"series_id\": \"125632\",\"type\": 6,\"source\": 3,\"event_data\": {\"stage\": 1,\"round_num\": 1,\"win_type\":2,\"win_team_id\":\"21\",\"alive_player_t\":3,\"alive_player_ct\":0}}"'
    # DoMySql().insert_data(cnn, a, 'csgo_live_event')
    # cnn.close()
    # a = DoMySql().insert_sql('k_series_team', data2, extra_key=['player'], replace_key=[{'old_key': 'kill', 'new_key': "`kill`"}])
    # print(a)
    # while True:
    # while True:
    # DoMySql().notReview()
    #     time.sleep(0.5)
    # time.sleep(5)
    # while True:
    # DoMySql.autoRunSql_b(sql, 0)
    # DoMySql.autoRunSql_r(sql, 0)
    #     time.sleep(120)
    # DoMySql().lol_match()
    DoMySql().connect()

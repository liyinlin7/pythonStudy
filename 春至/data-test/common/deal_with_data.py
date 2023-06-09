import operator
import time
import logging
from common import my_logger
from common.do_mysql import DoMySql
from common.do_excel import DoExcel
from common import read_path


def count_time(func):
    """
    :param func: 接收被装饰的函数
    """

    def wrapper(*args, **kwargs):
        # 函数调用之前获取一下当前的实际：start_time
        start_time = time.time()
        # 调用原功能函数
        res = func(*args, **kwargs)
        # 函数调用之后：再获取一下当前时间 end_time
        end_time = time.time()
        logging.info('{}函数运行的时间为：{}'.format(func.__name__, end_time - start_time))
        return res
    return wrapper


class DealWithData:
    """处理数据"""

    @staticmethod
    def sort_li(li, *key):
        """给嵌套字典的列表按字典某个键排序"""
        sorted_li = sorted(li, key=operator.itemgetter(*key))
        return sorted_li

    def trans_list(self, dic_list, key):
        """把嵌套字典列表转换成某个value组成的列表"""
        return [i[key] for i in dic_list]

    @count_time
    def package_dic(self, main_dic_sql, key_dic: list, cnn, sql_key='id'):
        """
        对于字典值类型为list的参数进行组装处理
        :param main_dic_sql: 主字典列表查询sql
        :param key_dic: 嵌套的关键字字典列表，形式：[{'name': 'XXX', 'type': 'XXX', 'sql': 'XXX'},……]
                        name:对应字段名。
                        type:返回类型，目前三种，int_list、dic_list、str_list。
                        sql:查询name的sql语句。
        :param cnn: 数据库连接对象
        :param sql_key:主字典列表的键名，用于key_dic中sql查询用
        :return:返回组装后的字典
        """
        # 数据库查询列表
        res_main_dic = DoMySql().select(cnn, main_dic_sql)
        for i in res_main_dic:
            sql_value = i[sql_key]
            logging.info('正在处理id为{}的数据---------'.format(sql_value))
            for j in key_dic:
                if j['type'] == 'int_list':
                    j['result'] = self.trans_list(DoMySql().select(cnn, j['sql'].format(sql_value)), j['key'])
                elif j['type'] == 'str_list':
                    res_0 = DoMySql().select(cnn, j['sql'].format(sql_value))
                    final_res = []
                    for item in res_0:
                        values = item.values()
                        string = ''
                        for s in values:
                            string += str(s) + ','
                        final_res.append(string.strip(','))
                    j['result'] = final_res
                else:
                    j['result'] = DoMySql().select(cnn, j['sql'].format(sql_value))
                # 当字段返回结果为空，返回null
                if j['allow_null']:
                    if not j['result']:
                        j['result'] = None
                i[j['name']] = j['result']
        return res_main_dic

    @count_time
    def sort_dic(self, dic_list, key_dic):
        """
        对嵌套字典值为list类型的数据进行排序处理
        :param dic_list: 待处理的嵌套字典列表
        :param key_dic: 形式：[{'name': 'XXX', 'type': 'XXX', 'key': 'XXX', 'allow_null': True, 'sql': 'XXX'},……]
                        name:对应字段名。
                        type:返回类型，目前两种，int_list和dic_list。
                        key：type为int_list时用于转化为列表的字段名；type为dic_list时为排序字段名。
                        sql:查询name的sql语句。
        :return:返回各嵌套字段排序处理后的数据
        """
        for i in dic_list:
            for j in key_dic:
                if j['type'] == 'int_list':
                    i[j['name']] = sorted(i[j['name']])
                elif j['type'] == 'dic_list' and j['key'] != '':
                    i[j['name']] = self.sort_li(i[j['name']], j['key'])
        return dic_list

    @count_time
    def trans_name(self, dic_list, trans_dic):
        """
        替换字段为对应代码
        :param dic_list: 待处理的嵌套字典列表
        :param trans_dic: 形式：[{'name': 'country', 'type': 'str_country'}, {'name': 'area', 'type': 'str_area'}, ...]
                          name:待替换的字段名
                          type:字段类型，目前类型：str_country,str_area,list_country,list_area...(str开头代表纯字符串替换，
                               list开头代表列表字符串替换)
        :return:返回替换名称后的嵌套字典列表
        """
        file_path = read_path.test_data_path
        country_code = DoExcel(file_path).get_base_data('country_code')
        area_code = DoExcel(file_path).get_base_data('area_code')
        for i in dic_list:
            for j in trans_dic:
                if j['type'] == 'str_country':
                    for item in country_code:
                        if i[j['name']] == item['name']:
                            i[j['name']] = item['code']
                        if i[j['name']] == ' ':
                            i[j['name']] = ''
                elif j['type'] == 'str_area':
                    for item in area_code:
                        if i[j['name']] == item['name']:
                            i[j['name']] = item['code']
                        if i[j['name']] == ' ':
                            i[j['name']] = ''
                elif j['type'] == 'list_country':
                    li = []
                    for m in i[j['name']]:
                        for item in country_code:
                            if m == item['name']:
                                li.append(item['code'])
                    i[j['name']] = li
        return dic_list


if __name__ == '__main__':
    # sql = "select id,game_id,league_id,start_time,end_time,`status`,bo,has_odds,has_inplay,'' as match_id,'' as live_id,'' as series_team from `data-center`.series where deleted = 1"
    # aa = [{'id': 61, 'game_id': 1, 'league_id': 2, 'start_time': 1594289700, 'end_time': 0, 'status': 2, 'bo': 1, 'has_odds': 0, 'has_inplay': 0, 'match_id': [495, 494, 493], 'live_id': [32, 30], 'series_team': [{'team_id': 4, 'score': 1, 'is_home': 1, 'is_winner': 1}, {'team_id': 2, 'score': 2, 'is_home': 1, 'is_winner': 1}]}]
    # dic = [{"name": "match_id", "type": "int_list", "key": "id", "allow_null": False,
    #         "sql": "select id from `data-center`.`match` where deleted = 1 and series_id = {}"},
    #        {"name": "live_id", "type": "int_list", "key": "id", "allow_null": False,
    #         "sql": "select id from `data-tools`.live_video where deleted = 1 and format = 'stream' and series_id = {}"},
    #        {"name": "series_team", "type": "dic_list", "key": "team_id", "allow_null": False,
    #         "sql": "select team_id,score,is_home,is_winner from `data-center`.series_team where series_id={}"}]
    # cnn = DoMySql().connect()
    # res = DealWithData().package_dic(main_dic_sql=sql, key_dic=dic, cnn=cnn)
    # cnn.close()
    # # res = DealWithData().sort_dic(aa, dic)
    # print(res)

    a = [{'id': 1, 'country': '中国大陆', 'area': '亚洲', 'location': ['中国大陆', '日本', '美国']},
         {'id': 2, 'country': '日本', 'area': '亚洲', 'location': ['美国', '韩国']}]
    trans_dic = [{'name': 'country', 'type': 'str_country'}, {'name': 'area', 'type': 'str_area'},
                 {'name': 'location', 'type': 'list_country'}]
    b = DealWithData().trans_name(a, trans_dic)
    print(b)

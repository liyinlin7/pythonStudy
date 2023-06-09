from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
from common.read_config import ReadConfig
from common import read_path
import requests


dataBase = 'sports-soccer'
mogonDB_collection_result = 'test_result'

class RequestErr(object):
    '''
        赛果错误
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.request_dataBase = ReadConfig().read_config(read_path.conf_path, 'sports_soccer', 'dataBase_basket')
        self.request_dataBase_result = ReadConfig().read_config(read_path.conf_path, 'sports_soccer', 'mogonDB_collection_result_basket')

    def requestdata_null_status_7(self):
        '''
            比赛结束10分钟后赛果为空
        :return:
        '''
        sql = '''
           SELECT *  FROM `sports-basketball`.ex_series WHERE status = 10 and match_start_time > unix_timestamp() - 3600*24*7 and  source=4 and  `delete` = 1  and p_id !=0;
        '''
        cnn = DoMySql().connect_mysql_basketball(self.env_flag)
        match_datas = DoMySql().select_basketball(cnn=cnn, sql=sql, env_flag=self.env_flag)
        match_id_set = set()
        for i in match_datas:
            match_id_set.add(i['p_id'])
        match_id_list = list(match_id_set)
        dcnn = MongoDB(self.env_flag).sport_connect_basketball(dataBase=self.request_dataBase, collection=self.request_dataBase_result)
        result_datas = MongoDB(self.env_flag).get_data_list_basketball(dcnn=dcnn, list=match_id_list)
        result_datas_list_matich_id = []
        for y in result_datas:
            # print(y)
            result_datas_list_matich_id.append(y['matchId'])
        for i in result_datas_list_matich_id:
            if i in match_id_list:
                match_id_list.remove(i)
        if len(match_id_list) != 0:
            msg = '篮球：比赛状态为已结束，没有赛果的比赛ID' + str(match_id_list) + "------"
            print(msg)
            return msg
        else:
            return ''

    # def result_basket_match_id(self, match_ids):


if __name__ == '__main__':
    rr = RequestErr(1)
    rr.requestdata_null_status_7()
    # rr.requestdata_null_status_7_test()
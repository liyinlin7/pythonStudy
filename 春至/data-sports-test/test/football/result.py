from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
from common.read_config import ReadConfig
from common import read_path


dataBase = 'sports-soccer'
mogonDB_collection_result = 'test_result'

class Result(object):

    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.request_dataBase = ReadConfig().read_config(read_path.conf_path, 'sports_soccer', 'dataBase')
        self.request_dataBase_result = ReadConfig().read_config(read_path.conf_path, 'sports_soccer', 'mogonDB_collection_result')

    def requestdata(self):
        sql = '''
            SELECT *  FROM `sports-soccer-match`.match WHERE status = 7 and match_start_time > unix_timestamp() - 3600*24*30;
        '''
        cnn = DoMySql().connect_mysql(self.env_flag)
        match_datas = DoMySql().select(cnn=cnn, sql=sql, env_flag=self.env_flag)
        match_id_set = set()
        for i in match_datas:
            match_id_set.add(i['id'])
        match_id_list = list(match_id_set)
        dcnn = MongoDB(self.env_flag).sport_connect(dataBase=self.request_dataBase, collection=self.request_dataBase_result)
        result_datas = MongoDB(self.env_flag).get_data_list(dcnn=dcnn, list=match_id_list)
        result_datas_list_matich_id = []
        for y in result_datas:
            for i in y['data']:
                # if i['pass_success'] is None and i['pass_success_rate'] != '':
                #     result_datas_list_matich_id.append(y['match_id'])
                if i['penalty_kick'] is not None and i['penalty_goal'] is not None:
                    # print(i['penalty_kick'])
                    # print(i['penalty_goal'])
                    if int(i['penalty_kick']) < int(i['penalty_goal']):
                        result_datas_list_matich_id.append(y['match_id'])
        print(result_datas_list_matich_id)

    def requestdata_team_player_id_null(self):
        '''
            1.赛果数据-有team_id=0
            2.赛果数据-有player_id=0
        :return:
        '''
        sql = '''
            SELECT *  FROM `sports-soccer-match`.match WHERE status = 7 ;
        '''
        cnn = DoMySql().connect_mysql(self.env_flag)
        match_datas = DoMySql().select(cnn=cnn, sql=sql, env_flag=self.env_flag)
        match_id_set = set()
        for i in match_datas:
            match_id_set.add(i['id'])
        match_id_list = list(match_id_set)
        dcnn = MongoDB(self.env_flag).sport_connect(dataBase=self.request_dataBase, collection=self.request_dataBase_result)
        result_datas = MongoDB(self.env_flag).get_data_list(dcnn=dcnn, list=match_id_list)
        team_id_null_list = set()
        player_id_null_list = set()
        for y in result_datas:
            # print(y)
            for i in y['data']:
                try:
                    i['team_id']
                except:
                    pass
                else:
                    if i['team_id'] == 0:
                        team_id_null_list.add(y['match_id'])
                    # for player in i['player']:
                    #     if player['player_id'] == 0:
                    #         player_id_null_list.add(y['match_id'])
        print("队伍team_id为0的小局：", team_id_null_list)
        print("队员player_id为0的小局：", player_id_null_list)


if __name__ == '__main__':
    r = Result(1)
    r.requestdata_team_player_id_null()
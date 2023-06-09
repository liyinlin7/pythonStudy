from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
import requests
import json
import time

class ResultErr(object):

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn, monGon_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        # self.mogonDB_dataBase = 'data-centen'
        self.mogonDB_dataBase = 'data-result'
        self.mogonDB_collection_lol = 'lol_result'
        self.mogonDB_collection_dota = 'dota_result'
        self.mogonDB_collection_csgo = 'csgo_result'
        self.mogonDB_collection_kog = 'kog_result'
        self.monGon = monGon_cnn
        self.doMysql = mysql_cnn

    '''
        赛果错误
    '''
    def get_data(self, match_id, dataBase, collection):
        myDb = self.monGon
        collect1 = myDb.connect(dataBase, collection)  # status=0 是测试MongoDB，非1都是线上MongoDB
        sen = '{"match_id":' + str(match_id) + '}'
        result = myDb.select_data_one(collect1, sen)
        return result

    def get_data_all_list(self, match_id, dataBase, collection):
        myDb = self.monGon
        collect1 = myDb.connect(dataBase, collection)  # status=0 是测试MongoDB，非1都是线上MongoDB
        # sen = '{"match_id":' + str(match_id) + '}'
        sen = '{"match_id": { "$in":' + str(match_id) + '}}'
        result = myDb.select_data_all(collect1, sen)
        return result

    def result_null(self):
        lol_msg = self.result_null_lol()
        dota_msg = self.result_null_dota()
        csgo_msg = self.result_null_csgo()
        kog_msg = self.result_null_kog()
        msg = lol_msg + csgo_msg + kog_msg + dota_msg
        print(msg)
        # msg = str(lol_msg) + str(dota_msg) + str(csgo_msg) + str(kog_msg)
        if msg != '':
            return msg
        else:
            return ""

    def result_null_dota(self):
        '''
            DOTA已入库小局状态更新已结束，超过10分钟仍未有赛果数据
        :return:
        '''
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.dota_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.status != 4 and s.start_time >= (unix_timestamp()-3600*24*7) 
                and (m.end_time+600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source = 6 and game_id = 2);
            '''
        datas = self.doMysql.select_centon(self.cnn_centon, sql)
        match_list = []
        for i in datas:
            match_list.append(i['id'])
        # for i in match_list:
        #     data = self.get_data(i, mogonDB_dataBase, mogonDB_collection_dota, mongon_status)
        #     if data is None:
        #         err_match.add(i)
        data = self.get_data_all_list(match_list, self.mogonDB_dataBase, self.mogonDB_collection_dota)
        data_request_list_matich_id = []
        for i in data:
            data_request_list_matich_id.append(i['match_id'])
        for i in data_request_list_matich_id:
            if i in match_list:
                match_list.remove(i)
        if len(match_list) != 0:
            msg = f'DOTA已入库小局状态更新已结束，超过10分钟仍未有赛果数据(条数{len(match_list)})' + str(match_list)
            print(msg)
            return msg
        else:
            return ""

    def result_null_csgo(self):
        '''
            CSGO已入库小局状态更新已结束，超过10分钟仍未有赛果数据
        :return:
        '''
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.match as m on s.id=m.series_id  
                left join `data-center`.match_team as mt  on m.id= mt.match_id where s.deleted=1 and m.deleted=1 and m.status=3  and s.status != 4
                and s.start_time >= (unix_timestamp()-3600*24*7) and (m.end_time+600)<=unix_timestamp() and mt.is_winner not in (6,7) 
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source = 3 and game_id = 3);
            '''
        datas = self.doMysql.select_centon(self.cnn_centon, sql)
        match_set = set()
        for i in datas:
            match_set.add(i['id'])
        match_list = list(match_set)
        data = self.get_data_all_list(match_list, self.mogonDB_dataBase, self.mogonDB_collection_csgo)
        data_request_list_matich_id = []
        for i in data:
            data_request_list_matich_id.append(i['match_id'])
        for i in data_request_list_matich_id:
            if i in match_list:
                match_list.remove(i)
        if len(match_list) != 0:
            msg = f'CSGO已入库小局状态更新已结束，超过10分钟仍未有赛果数据(条数{len(match_list)})' + str(match_list)
            print(msg)
            return msg
        else:
            return ""

    def result_null_kog(self):
        '''
            KOG已入库小局状态更新已结束，超过10分钟仍未有赛果数据
        :return:
        '''
        sql = '''
                SELECT m.id, m.league_id FROM `data-center`.series as s left join `data-center`.kog_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.status != 4 and s.start_time >= (unix_timestamp()-3600*24*7) and (m.end_time+600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source = 7 and game_id = 4);
            '''
        datas = self.doMysql.select_centon(self.cnn_centon, sql)
        match_list = []
        for i in datas:
            if i['league_id'] not in [781, 5559]:
                match_list.append(i['id'])
        # err_match = set()
        # for i in match_list:
        #     data = self.get_data(i, mogonDB_dataBase, mogonDB_collection_kog, mongon_status)
        #     if data is None:
        #         err_match.add(i)
        data = self.get_data_all_list(match_list, self.mogonDB_dataBase, self.mogonDB_collection_kog)
        data_request_list_matich_id = []
        for i in data:
            data_request_list_matich_id.append(i['match_id'])
        for i in data_request_list_matich_id:
            if i in match_list:
                match_list.remove(i)
        if len(match_list) != 0:
            msg = f'KOG已入库小局状态更新已结束，超过10分钟仍未有赛果数据(条数{len(match_list)}):' + str(match_list)
            # print(msg)
            return msg
        else:
            return ""

    def result_null_lol(self):
        '''
            LOL已入库小局状态更新已结束，超过10分钟仍未有赛果数据
        :return:
        '''

        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.lol_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.status != 4 and s.start_time >= (unix_timestamp()-3600*24*7) and (m.end_time+600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source = 2 and game_id = 1);
            '''
        datas = self.doMysql.select_centon(self.cnn_centon, sql)
        match_list = []
        for i in datas:
            match_list.append(i['id'])
        data = self.get_data_all_list(match_list, self.mogonDB_dataBase, self.mogonDB_collection_lol)
        data_request_list_matich_id = []
        for i in data:
            data_request_list_matich_id.append(i['match_id'])
        for i in data_request_list_matich_id:
            if i in match_list:
                match_list.remove(i)
        match_null, err_match_pandan = self.pandanscore_teams(match_list)
        if len(match_null) != 0 or len(err_match_pandan) != 0:
            msg = f'''
            LOL已入库小局状态更新已结束，超过10分钟仍未有赛果数据(条数{len(match_list)}){str(match_list)}(pandascore有数据)；pandascore没数据的小局{str(err_match_pandan)}
            '''
            print(msg)
            return msg
        else:
            return ""

    def pandanscore_teams(self, match_list):
        tuple_match_id = tuple(match_list)
        if len(tuple_match_id) != 1:
            match_list_str = str(tuple_match_id)
        else:
            match_list_str = str(tuple_match_id).replace(',', '')
        print(match_list_str)
        if len(match_list_str) > 2:
            sql_match = f'''
                SELECT * FROM `data-center`.lol_match where id in {match_list_str} order by series_id;
            '''
            match_data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql_match)
            map_stage_list = []
            series_set = set()
            for i in match_data:
                series_set.add(i['series_id'])
            for i in series_set:
                match_map_list = []
                map_2 = {}
                for y in match_data:
                    if i == y['series_id']:
                        map_3 = {}
                        map_3['match_id'] = y['id']
                        map_3['stage'] = y['stage']
                        match_map_list.append(map_3)
                map_2['series_id'] = i
                map_2['match_id_list'] = match_map_list
                map_stage_list.append(map_2)
            tuple_series_set = tuple(series_set)
            if len(tuple_series_set) != 1:
                tuple_series_str = str(tuple_series_set)
            else:
                tuple_series_str = str(tuple_series_set).replace(',', '')
            # print(tuple_series_str)
            ex_series_sql = f'''
                SELECT * FROM `data-center`.ex_series where p_id  in {tuple_series_str} and  source = 2;
            '''
            ex_series_data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=ex_series_sql)
            ex_p_id_series = []
            for i in ex_series_data:
                map_ = {}
                map_['ex_id'] = i['ex_id']
                map_['p_id'] = i['p_id']
                ex_p_id_series.append(map_)
            pandascore_series_url = 'https://api.pandascore.co/lol/matches?token=_k-j4mYNOpgtGwwa19ndPyU0CKjgUm17N06aiDDOnIXaxDDndJI&filter[id]={}'
            pandascore_match_url = 'https://api.pandascore.co/lol/games/{}?token=_k-j4mYNOpgtGwwa19ndPyU0CKjgUm17N06aiDDOnIXaxDDndJI'
            pandan_mathch_map_list = []
            for i in ex_p_id_series:
                series_url = pandascore_series_url.format(i.get('ex_id'))
                time.sleep(1)
                res_data = requests.get(url=series_url)
                games_list = res_data.json()[0].get('games')
                pandan_mathch_list = []
                for y in games_list:
                    pandan_mathch_list.append(y['id'])
                map_1 = {}
                map_1['series_id'] = i
                map_1['mathch_list'] = pandan_mathch_list
                pandan_mathch_map_list.append(map_1)
            err_match_pandan = []
            for i in map_stage_list:
                match_lists = i.get('match_id_list')
                for y in pandan_mathch_map_list:
                    series_id_e_p = y.get('series_id')
                    p_id = series_id_e_p.get('p_id')
                    match_pandan_list = y.get('mathch_list')
                    if i.get('series_id') == p_id:
                        for z in match_lists:
                            stage = z.get('stage')
                            match_id_pan = match_pandan_list[stage-1]
                            p_match_url = pandascore_match_url.format(match_id_pan)
                            time.sleep(1)
                            match_res = requests.get(url=p_match_url)
                            json_match_res = match_res.json()
                            if len(json_match_res['teams']) == 0 or len(json_match_res['teams'][0]['player_ids']) == 0 or len(json_match_res['teams'][1]['player_ids']) == 0:
                                err_match_pandan.append(z.get('match_id'))
                                match_list.remove(z.get('match_id'))
            print(err_match_pandan)
            return match_list, err_match_pandan
        else:
            return [], []



if __name__ == '__main__':
    cnn_centon = DoMySql().cnn_centon_def()
    cnn_basic = DoMySql().cnn_basic_def()
    a = ResultErr('release', cnn_centon, cnn_basic, DoMySql(), MongoDB())  # release   # develop
    a.result_null_lol()


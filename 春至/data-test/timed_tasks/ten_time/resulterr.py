from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB

# mogonDB_dataBase = 'data-center'
mogonDB_dataBase = 'data-result'
mogonDB_collection_lol = 'lol_result'
mogonDB_collection_dota = 'dota_result'
mogonDB_collection_csgo = 'csgo_result'
mogonDB_collection_kog = 'kog_result'


class ResultErr(object):
    '''
        赛果错误
    '''
    def get_data(self, match_id, dataBase, collection, status):
        myDb = MongoDB()
        collect1 = myDb.connect(dataBase, collection, status=status)  # status=0 是测试MongoDB，非1都是线上MongoDB
        sen = '{"match_id":' + str(match_id) + '}'
        result = myDb.select_data_one(collect1, sen)
        return result

    def get_data_all_list(self, match_id, dataBase, collection, status):
        myDb = MongoDB()
        collect1 = myDb.connect(dataBase, collection, status=status)  # status=0 是测试MongoDB，非1都是线上MongoDB
        # sen = '{"match_id":' + str(match_id) + '}'
        sen = '{"match_id": { "$in":' + str(match_id) + '}}'
        result = myDb.select_data_all(collect1, sen)
        return result

    def result_null(self, env_flag=0, mongon_status=0):
        lol_msg = self.result_null_lol(env_flag, mongon_status)
        dota_msg = self.result_null_dota(env_flag, mongon_status)
        csgo_msg = self.result_null_csgo(env_flag, mongon_status)
        kog_msg = self.result_null_kog(env_flag, mongon_status)
        msg = lol_msg + csgo_msg + kog_msg + dota_msg
        print(msg)
        # msg = str(lol_msg) + str(dota_msg) + str(csgo_msg) + str(kog_msg)

        if msg != '':
            return msg
        else:
            return ""

    def result_null_lol(self, env_flag=0, mongon_status=0):
        '''
            LOL已入库小局状态更新已结束，超过10分钟仍未有赛果数据
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.lol_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.status != 4 and s.start_time >= (unix_timestamp()-3600*24*7) and (m.end_time+600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source != 1 and game_id = 1);
            '''
        datas = DoMySql().select(cnn, sql, env_flag)
        match_list = []
        for i in datas:
            match_list.append(i['id'])
        # err_match = set()
        # for i in match_list:
        #     data = self.get_data(i, mogonDB_dataBase, mogonDB_collection_lol, mongon_status)
        #     if data is None:
        #         err_match.add(i)
        data = self.get_data_all_list(match_list, mogonDB_dataBase, mogonDB_collection_lol, mongon_status)
        data_request_list_matich_id = []
        for i in data:
            data_request_list_matich_id.append(i['match_id'])
        for i in data_request_list_matich_id:
            if i in match_list:
                match_list.remove(i)
        if len(match_list) != 0:
            msg = 'LOL已入库小局状态更新已结束，超过10分钟仍未有赛果数据' + str(match_list)
            # print(msg)
            return msg
        else:
            return ""

    def result_null_dota(self, env_flag=0, mongon_status=0):
        '''
            DOTA已入库小局状态更新已结束，超过10分钟仍未有赛果数据
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.dota_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.status != 4 and s.start_time >= (unix_timestamp()-3600*24*7) 
                and (m.end_time+600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source != 1 and game_id = 2);
            '''
        datas = DoMySql().select(cnn, sql, env_flag)
        match_list = []
        for i in datas:
            match_list.append(i['id'])
        # for i in match_list:
        #     data = self.get_data(i, mogonDB_dataBase, mogonDB_collection_dota, mongon_status)
        #     if data is None:
        #         err_match.add(i)
        data = self.get_data_all_list(match_list, mogonDB_dataBase, mogonDB_collection_dota, mongon_status)
        data_request_list_matich_id = []
        for i in data:
            data_request_list_matich_id.append(i['match_id'])
        for i in data_request_list_matich_id:
            if i in match_list:
                match_list.remove(i)
        if len(match_list) != 0:
            msg = 'DOTA已入库小局状态更新已结束，超过10分钟仍未有赛果数据' + str(match_list)
            print(msg)
            return msg
        else:
            return ""

    def result_null_csgo(self, env_flag=0, mongon_status=0):
        '''
            CSGO已入库小局状态更新已结束，超过10分钟仍未有赛果数据
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.match as m on s.id=m.series_id  
                left join `data-center`.match_team as mt  on m.id= mt.match_id where s.deleted=1 and m.deleted=1 and m.status=3  and s.status != 4
                and s.start_time >= (unix_timestamp()-3600*24*7) and (m.end_time+600)<=unix_timestamp() and mt.is_winner not in (6,7) 
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source != 1 and game_id = 3);
            '''
        datas = DoMySql().select(cnn, sql, env_flag)
        match_set = set()
        for i in datas:
            match_set.add(i['id'])
        match_list = list(match_set)
        data = self.get_data_all_list(match_list, mogonDB_dataBase, mogonDB_collection_csgo, mongon_status)
        data_request_list_matich_id = []
        for i in data:
            data_request_list_matich_id.append(i['match_id'])
        for i in data_request_list_matich_id:
            if i in match_list:
                match_list.remove(i)
        if len(match_list) != 0:
            msg = 'CSGO已入库小局状态更新已结束，超过10分钟仍未有赛果数据' + str(match_list)
            print(msg)
            return msg
        else:
            return ""

    def result_null_kog(self, env_flag=0, mongon_status=0):
        '''
            KOG已入库小局状态更新已结束，超过10分钟仍未有赛果数据
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = '''
                SELECT m.id, m.league_id FROM `data-center`.series as s left join `data-center`.kog_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.status != 4 and s.start_time >= (unix_timestamp()-3600*24*7) and (m.end_time+600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source != 1 and game_id = 4);
            '''
        datas = DoMySql().select(cnn, sql, env_flag)
        match_list = []
        for i in datas:
            if i['league_id'] not in [781, 5559, 5879]:
                match_list.append(i['id'])
        # err_match = set()
        # for i in match_list:
        #     data = self.get_data(i, mogonDB_dataBase, mogonDB_collection_kog, mongon_status)
        #     if data is None:
        #         err_match.add(i)
        data = self.get_data_all_list(match_list, mogonDB_dataBase, mogonDB_collection_kog, mongon_status)
        data_request_list_matich_id = []
        for i in data:
            data_request_list_matich_id.append(i['match_id'])
        for i in data_request_list_matich_id:
            if i in match_list:
                match_list.remove(i)
        if len(match_list) != 0:
            msg = 'KOG已入库小局状态更新已结束，超过10分钟仍未有赛果数据' + str(match_list)
            # print(msg)
            return msg
        else:
            return ""


if __name__ == '__main__':
    ResultErr = ResultErr()
    # ResultErr.result_null(env_flag=1, mongon_status=1)
    ResultErr.result_null_lol(env_flag=0, mongon_status=0)
    # ResultErr.result_null_dota(env_flag=1, mongon_status=1)
    # ResultErr.result_null_csgo(env_flag=1, mongon_status=1)


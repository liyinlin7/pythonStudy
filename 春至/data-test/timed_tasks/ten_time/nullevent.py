from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB

# mogonDB_dataBase = 'data-center'
mogonDB_dataBase = 'data-result'
mogonDB_collection_lol = 'lol_result'
mogonDB_collection_lol_event = 'lol_event'
mogonDB_collection_dota_event = 'dota_result_event'
mogonDB_collection_dota = 'dota_result'


class NullEvent(object):

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
        print(sen)
        result = myDb.select_data_all(collect1, sen)
        return result

    def result_null_all(self, env_flag=0, mongon_status=0):
        lol_msg = self.result_null_lol(env_flag=env_flag, mongon_status=env_flag)
        dota_msg = self.result_null_dota(env_flag=mongon_status, mongon_status=mongon_status)
        if len(lol_msg+dota_msg) != 0:
            return lol_msg+dota_msg
        else:
            return ""

    def result_null_lol(self, env_flag=0, mongon_status=0):
        '''
            LOL有赛果没有赛果事件
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.lol_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.start_time >= (unix_timestamp()-3600*24*3) and (m.end_time-600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source != 1 and game_id = 1);
            '''
        datas = DoMySql().select(cnn, sql, env_flag)
        match_list = []
        for i in datas:
            match_list.append(i['id'])
        request_data = self.get_data_all_list(match_list, mogonDB_dataBase, mogonDB_collection_lol, mongon_status)
        data_request_list_matich_id = []
        for i in request_data:
            data_request_list_matich_id.append(i['match_id'])
        event_data = self.get_data_all_list(data_request_list_matich_id, mogonDB_dataBase, mogonDB_collection_lol_event, mongon_status)
        event_match_list = set()
        for i in event_data:
            event_match_list.add(i['match_id'])
        for i in event_match_list:
            if i in data_request_list_matich_id:
                data_request_list_matich_id.remove(i)
        if len(data_request_list_matich_id) != 0:
            msg = 'LOL有赛果但是没有赛果事件' + str(data_request_list_matich_id)
            print(msg)
            return msg
        else:
            return ""

    def result_null_dota(self, env_flag=0, mongon_status=0):
        '''
            DOTA有赛果没有赛果事件
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.dota_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.start_time >= (unix_timestamp()-3600*24*3) and (m.end_time-600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source != 1 and game_id = 2);
            '''
        datas = DoMySql().select(cnn, sql, env_flag)
        print(len(datas))
        match_list = []
        for i in datas:
            match_list.append(i['id'])
        request_data = self.get_data_all_list(match_list, mogonDB_dataBase, mogonDB_collection_dota, mongon_status)
        data_request_list_matich_id = []
        for i in request_data:
            data_request_list_matich_id.append(i['match_id'])
        event_data = self.get_data_all_list(data_request_list_matich_id, mogonDB_dataBase, mogonDB_collection_dota_event,
                                            mongon_status)
        event_match_list = set()
        for i in event_data:
            event_match_list.add(i['match_id'])
        print(data_request_list_matich_id)
        print(event_match_list)
        for i in event_match_list:
            if i in data_request_list_matich_id:
                data_request_list_matich_id.remove(i)
        if len(data_request_list_matich_id) != 0:
            msg = 'DOTA有赛果但是没有赛果事件' + str(data_request_list_matich_id)
            print(msg)
            return msg
        else:
            return ""


if __name__ == '__main__':
    Null = NullEvent()
    # Null.result_null_lol(env_flag=1, mongon_status=1)
    Null.result_null_dota(env_flag=1, mongon_status=1)
    # Null.result_null_dota()

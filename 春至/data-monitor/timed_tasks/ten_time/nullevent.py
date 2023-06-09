from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB


class NullEvent(object):

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn, monGon_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        # self.mogonDB_dataBase = 'data-centen'
        self.mogonDB_dataBase = 'data-result'
        self.mogonDB_collection_lol = 'lol_result'
        self.mogonDB_collection_lol_event = 'lol_event'
        self.mogonDB_collection_dota_event = 'dota_result_event'
        self.mogonDB_collection_dota = 'dota_result'
        self.monGon = monGon_cnn
        self.doMysql = mysql_cnn

    def get_data(self, match_id, dataBase, collection):
        myDb = self.monGon
        collect1 = myDb.connect(dataBase, collection)
        sen = '{"match_id":' + str(match_id) + '}'
        result = myDb.select_data_one(collect1, sen)
        return result

    def get_data_all_list(self, match_id, dataBase, collection):
        myDb = self.monGon
        collect1 = myDb.connect(dataBase, collection)
        # sen = '{"match_id":' + str(match_id) + '}'
        sen = '{"match_id": { "$in":' + str(match_id) + '}}'
        result = myDb.select_data_all(collect1, sen)
        return result

    def result_null_all(self):
        lol_msg = self.result_null_lol()
        dota_msg = self.result_null_dota()
        if len(lol_msg+dota_msg) != 0:
            return lol_msg+dota_msg
        else:
            return ""

    def result_null_lol(self, env_flag=0, mongon_status=0):
        '''
            LOL有赛果没有赛果事件
        :return:
        '''
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.lol_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.start_time >= (unix_timestamp()-3600*24*3) and (m.end_time-600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source != 1 and game_id = 1);
            '''
        datas = self.doMysql.select_centon(self.cnn_centon, sql)
        match_list = []
        for i in datas:
            match_list.append(i['id'])
        request_data = self.get_data_all_list(match_list, self.mogonDB_dataBase, self.mogonDB_collection_lol)
        data_request_list_matich_id = []
        for i in request_data:
            data_request_list_matich_id.append(i['match_id'])
        event_data = self.get_data_all_list(data_request_list_matich_id, self.mogonDB_dataBase, self.mogonDB_collection_lol_event)
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

    def result_null_dota(self):
        '''
            DOTA有赛果没有赛果事件
        :return:
        '''
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.dota_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.start_time >= (unix_timestamp()-3600*24*3) and (m.end_time-600)<=unix_timestamp()
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source != 1 and game_id = 2);
            '''
        datas = self.doMysql.select_centon(self.cnn_centon, sql)
        match_list = []
        for i in datas:
            match_list.append(i['id'])
        request_data = self.get_data_all_list(match_list, self.mogonDB_dataBase, self.mogonDB_collection_dota)
        data_request_list_matich_id = []
        for i in request_data:
            data_request_list_matich_id.append(i['match_id'])
        event_data = self.get_data_all_list(data_request_list_matich_id, self.mogonDB_dataBase, self.mogonDB_collection_dota_event)
        event_match_list = set()
        for i in event_data:
            event_match_list.add(i['match_id'])
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
    cnn_centon = DoMySql().cnn_centon_def()
    cnn_basic = DoMySql().cnn_basic_def()
    a = NullEvent('develop', cnn_centon, cnn_basic)
    # a.result_null_lol()
    # a.result_null_dota()
    a.result_null_all()

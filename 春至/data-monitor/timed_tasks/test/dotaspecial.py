from common.do_mongoDB import MongoDB
from common.do_mysql import DoMySql
import logging

mogonDB_dataBase = 'data-center'
mogonDB_collection_dota_special = 'dota_result_special_event'
mogonDB_collection_dota_live_special = 'dota_special_event'


class DotaSpecial(object):

    def __init__(self, env_flag=0):
        self.env_flag = env_flag

    def get_data_all(self, match_id, dataBase, collection, status):
        myDb = MongoDB()
        collect1 = myDb.connect(dataBase, collection, status=status)  # status=0 是测试MongoDB，非1都是线上MongoDB
        # sen = '{"match_id":' + str(match_id) + '}'
        sen = '{"match_id": { "$in":' + str(match_id) + '}}'
        result = myDb.select_data_all(collect1, sen)
        return result

    def dota_special(self):
        cnn = DoMySql().connect(env_flag=self.env_flag)
        sql = '''
            SELECT m.id FROM `data-center`.series as s left join `data-center`.dota_match as m on s.id=m.series_id 
            where s.deleted=1 and m.deleted=1 and m.status=3 and s.start_time >= (unix_timestamp()-3600*24*3)  and s.start_time > 1612344600;
        '''
        data = DoMySql().select(cnn=cnn, sql=sql, env_flag=self.env_flag)
        match_set = set()
        for i in data:
            match_set.add(i['id'])
        match_list = list(match_set)
        dota_live_special_datas = self.get_data_all(match_id=match_list, dataBase=mogonDB_dataBase,collection=mogonDB_collection_dota_live_special,status=self.env_flag)
        dota_resquest_special_datas = list(self.get_data_all(match_id=match_list, dataBase=mogonDB_dataBase,collection=mogonDB_collection_dota_special,status=self.env_flag))
        for i in dota_live_special_datas:
            for y in dota_resquest_special_datas:
                if i['match_id'] == y['match_id']:
                    if i['type'] == y['type'] and (i['event']['value'] == y['event']['value']) and \
                            (i['event']['related_type'] == y['event']['related_type']) and \
                            y['event']['related_id'] != 0:
                        if i['event']['related_id'] != y['event']['related_id']:
                            print("NO")
                            logging.info(f"match_id:{i['match_id']},type:{i['type']},value:{i['event']['value']}")
                        else:
                            pass


if __name__ == '__main__':
    DotaSpecial = DotaSpecial(env_flag=0)
    DotaSpecial.dota_special()
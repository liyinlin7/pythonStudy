from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
from common.read_config import ReadConfig
from common import read_path


dataBase = 'sports-soccer'
mogonDB_collection_result = 'test_result'

class mysql_shuju(object):

    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.request_dataBase = ReadConfig().read_config(read_path.conf_path, 'sports_soccer', 'dataBase')
        self.request_dataBase_result = ReadConfig().read_config(read_path.conf_path, 'sports_soccer', 'mogonDB_collection_result')

    def players(self):
        sql = '''
          SELECT * FROM `sports-rate-center`.market where inside_level_id  in (
            SELECT p_id FROM `sports-soccer-match`.ex_match where source  = 2 and p_id != 0  and  status = 1 and match_start_time > 1630382400
            );'''
        cnn = DoMySql().connect_mysql(self.env_flag)
        players = DoMySql().select(cnn=cnn, sql=sql, env_flag=self.env_flag)
        p_id = []
        ex_id = []
        for i in players:
            p_id.append(i['id'])
            # ex_id.append(i['ex_id'])
        print("队员p_id", p_id)
        print("len", len(p_id))
        print("队员ex_id", ex_id)

    def rate_play(self):
        sql = '''
        '''
        cnn = DoMySql().connect_mysql_basketball(self.env_flag)
        players = DoMySql().select_basketball(cnn=cnn, sql=sql, env_flag=self.env_flag)
        ex_id = []
        for i in players:
            ex_id.append(i['ex_id'])
        print("选项ex_id", ex_id)

if __name__ == '__main__':
    mysql_shuju(1).players()
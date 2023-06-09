from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB


class ResultErr(object):

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn, monGon_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.mogonDB_dataBase = 'data-result'
        self.mogonDB_collection_dota = 'dota_result'
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

    def result_dota_score(self):
        '''
            DOTA已入库小局状态更新已结束，超过10分钟仍未有赛果数据
        :return:
        '''
        sql = '''
                SELECT m.id FROM `data-center`.series as s left join `data-center`.dota_match as m on s.id=m.series_id 
                where s.deleted=1 and m.deleted=1 and m.status=3 and s.status != 4  
                and m.series_id in (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source != 1 and game_id = 2)
                and s.league_id  in (SELECT id FROM `data-center`.league where level>=2);
            '''
        datas = self.doMysql.select_centon(self.cnn_centon, sql)
        match_list = []
        for i in datas:
            match_list.append(i['id'])
        datas = self.get_data_all_list(match_list, self.mogonDB_dataBase, self.mogonDB_collection_dota)
        match_score_small = []
        match_score_big = []
        for i in datas:
            data = i['data']
            team_score = 0
            try:
                for team in data:
                    team_score += team['score']
                if team_score <= 5:
                    match_score_small.append(i['match_id'])
                elif team_score > 10:
                    match_score_big.append(i['match_id'])
            except Exception:
                pass
        print('赛果队伍比分之和小于10', match_score_small)
        print('赛果队伍比分之和大于10', match_score_big)


if __name__ == '__main__':
    cnn_centon = DoMySql().cnn_centon_def()
    cnn_basic = DoMySql().cnn_basic_def()
    a = ResultErr('release', cnn_centon, cnn_basic, DoMySql(), MongoDB())   # release,develop
    a.result_dota_score()

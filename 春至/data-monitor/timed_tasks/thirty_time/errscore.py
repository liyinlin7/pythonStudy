from common.do_mongoDB import MongoDB
from common.do_mysql import DoMySql


class ErrScore(object):

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn, monGon_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.mogonDB_dataBase = 'data-result'
        self.mogonDB_collection_csgo = 'csgo_result'
        self.monGon = monGon_cnn
        self.doMysql = mysql_cnn

    def get_data_all_list(self, match_id, dataBase, collection):
        myDb = self.monGon
        collect1 = myDb.connect(dataBase, collection)
        # sen = '{"match_id":' + str(match_id) + '}'
        sen = '{"match_id": { "$in":' + str(match_id) + '}}'
        result = myDb.select_data_all(collect1, sen)
        return result

    def csgo_score(self):
        series_sql = '''
            SELECT * FROM `data-center`.ex_series where game_id =3 and source =3 and deleted=1 and status=3 and p_id !=0  
            and start_time > unix_timestamp()-3600*24*7 and start_time<unix_timestamp();
        '''
        # series_sql = '''
        #             SELECT * FROM `data-center`.ex_series where game_id =3 and source =3 and deleted=1 and status=3
        #             and p_id !=0;
        #         '''
        series_id_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=series_sql)
        series_p_ex_id_list = []
        p_id_set = set()
        for i in series_id_datas:
            id_ = {}
            id_['p_id'] = i['p_id']
            id_['ex_id'] = i['ex_id']
            p_id_set.add(i['p_id'])
            series_p_ex_id_list.append(id_)
        # print(series_p_ex_id_list)
        # print(p_id_set)
        match_sql = f'''
            SELECT * FROM `data-center`.match where series_id in {tuple(p_id_set)} and deleted=1 and status=3;
        '''
        match_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=match_sql)
        match_map_list = []
        match_set = set()
        for y in match_datas:
            match_ = {}
            match_['match_id'] = y['id']
            match_['series_id'] = y['series_id']
            match_['stage'] = y['stage']
            match_set.add(y['id'])
            match_map_list.append(match_)
        # print(match_map_list)
        # print(match_set)
        csgo_results = self.get_data_all_list(list(match_set), self.mogonDB_dataBase, self.mogonDB_collection_csgo)
        err_score_match_id = []
        for i in csgo_results:
            datas = i['data']
            team_score_1_all = datas[0]['team_score'][0]
            team_score_2_all = datas[1]['team_score'][0]
            if team_score_1_all == team_score_2_all:
                err_score_match_id.append(i['match_id'])
        # print(err_score_match_id)
        err_mathc_id__map_list = []
        for i in err_score_match_id:
            for y in match_map_list:
                if i == y.get('match_id'):
                    err_mathc_id__map_list.append(y)
        # print(err_mathc_id__map_list)
        err_match = []
        for i in err_mathc_id__map_list:
            for y in series_p_ex_id_list:
                if i.get('series_id') == y.get('p_id'):
                    err_ex_id_map_ = {}
                    err_ex_id_map_['ex_id'] = y.get('ex_id')
                    err_ex_id_map_['stage'] = i.get('stage')
                    err_ex_id_map_['match_id'] = i.get('match_id')
                    err_match.append(err_ex_id_map_)
        print(err_match)
        if len(err_match) > 0:
            return "CSOG小局赛果2支队伍的总比分相同的小局数据：", err_match
        else:
            return ''


if __name__ == '__main__':
    domysql = DoMySql()
    domongon = MongoDB()
    center_cnn = domysql.cnn_centon_def()
    basic_cnn = domysql.cnn_basic_def()
    a = ErrScore('release', center_cnn, basic_cnn, domysql, domongon)
    a.csgo_score()

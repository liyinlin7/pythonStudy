from common.do_mongoDB import MongoDB
from common.do_mysql import DoMySql


class MatchTeam_Is_Winner(object):
    '''
        小局is_winner状态不对
    '''
    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn, monGon_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        # self.mogonDB_dataBase = 'data-centen'
        self.mogonDB_dataBase = 'data-result'
        self.dota_event_collection = 'dota_event'
        self.monGon = monGon_cnn
        self.doMysql = mysql_cnn


    def dota_martchteam_is_winner(self):
        '''
            通过SQL查询没有is_weinner的小局，然后反向查询MongoDB有没有是实时数据
            如果有实时数据，就报警；没有就不报警。
        :return:
        '''
        m_cnn = self.monGon.connect(dataBase=self.mogonDB_dataBase, collection=self.dota_event_collection)
        sql = '''
            SELECT * FROM `data-center`.dota_match as m left join `data-center`.dota_match_team as mt on m.id=mt.match_id where 
            m.start_time >= (unix_timestamp() - 3600*24*7) and m.deleted=1 and m.status=3 and mt.is_winner=1 and m.series_id in 
            (SELECT p_id FROM `data-center`.ex_series where  deleted =1 and source = 1 and game_id = 2 and  status = 3); 
            '''
        match_id_res = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        match_id_list = set()
        match_id_is_winner_err = set()
        err_str = ''
        for i in match_id_res:
            match_id_list.add(i.get('match_id'))
        if len(match_id_list) != 0:
            for i in match_id_list:
                sen = '{"match_id":' + str(i) + '}'
                dota_event = self.monGon.select_data_all(m_cnn, sen)
                if dota_event is None:
                    pass
                else:
                    match_id_is_winner_err.add(i)
        if len(match_id_is_winner_err) != 0:
            err_str += f'dota已入库已结束小局is_winner字段没有胜负有问题的match_id：{str(match_id_is_winner_err)}；'
        print(err_str)
        if err_str != '':
            return err_str
        else:
            return ''


if __name__ == '__main__':
    cnn_centon = DoMySql().cnn_centon_def()
    cnn_basic = DoMySql().cnn_basic_def()
    a = MatchTeam_Is_Winner('develop', cnn_centon, cnn_basic)
    a.dota_martchteam_is_winner()


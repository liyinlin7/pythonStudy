from common.do_mysql import DoMySql


class TeamID_err(object):

    '''
        队伍的问题
    '''

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.doMysql = mysql_cnn

    def play_team_series_team(self):
        '''
            雷竞技的队伍和系列赛的队伍 内部ID不一致
        :return:
        '''
        sql = '''
             SELECT * FROM `data-center`.ex_series where game_id in (1,2,3,4) and start_time > unix_timestamp() - 3600*24*1 and p_id !=0 and source=1 and audit in (2,4)
             and ex_id not in ('37446368', '37446383', '37451175');
        '''
        p_id_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        series_list = []
        for i in p_id_datas:
            series_dis = {}
            p_id = i['p_id']
            ex_id = i['ex_id']
            series_dis['p_id'] = p_id
            series_dis['ex_id'] = ex_id
            series_list.append(series_dis)
        null_level_id = []
        err_team_id_ex_id = []
        for i in series_list:
            # print("------------------------------------------------")
            play_team_id_sql = f'''
                SELECT
                mt.level_id,opn.name_id
                FROM `data-rate-center`.market_type as mt 
                inner join `data-rate-center`.market_name as mn on mt.market_id=mn.market_id 
                join `data-rate-center`.option as o on mt.id=o.market_type_id 
                join `data-rate-center`.option_name as opn on o.id=opn.option_id where mt.level_id={i.get('ex_id')}
                and mn.name_zh = '获胜队伍' group by opn.name_id;
            '''
            if self.env_flag == 'release':
                play_team_id_data = self.doMysql.select_basic(cnn=self.cnn_basic, sql=play_team_id_sql)
            elif self.env_flag == 'develop':
                play_team_id_data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=play_team_id_sql)
            series_team_id_sql = f'''
                SELECT * FROM `data-center`.series_team where series_id = {i.get('p_id')};
            '''
            series_team_id_data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=series_team_id_sql)
            play_team_id_list = []
            series_team_id_list = []
            for y in play_team_id_data:
                play_team_id_list.append(y['name_id'])
            # print(play_team_id_list)
            # try:
            if None in play_team_id_list:
                play_team_id_list.remove(None)
            # print(play_team_id_list)
            if play_team_id_list:
                play_team_id_list.sort()
            for c in series_team_id_data:
                series_team_id_list.append(c['team_id'])
            series_team_id_list.sort()
            if len(play_team_id_list) != 0:
                if play_team_id_list == series_team_id_list:
                    pass
                else:
                    err_team_id_ex_id.append(i.get('ex_id'))
            else:
                null_level_id.append(i.get('ex_id'))
            # except:
            #     pass
        print(str(err_team_id_ex_id))
        if len(err_team_id_ex_id) != 0:
            return str(err_team_id_ex_id)
        else:
            return ''


if __name__ == '__main__':
    cnn_centon = DoMySql().cnn_centon_def()
    cnn_basic = DoMySql().cnn_basic_def()
    c = TeamID_err('release', cnn_centon, cnn_basic, DoMySql())
    c.play_team_series_team()


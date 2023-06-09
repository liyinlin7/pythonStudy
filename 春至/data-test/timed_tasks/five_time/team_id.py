from common.do_mysql import DoMySql


class TeamID_err(object):

    '''
        队伍的问题
    '''
    def __init__(self, env_flag):
        self.cnn = DoMySql().connect(env_flag=env_flag)
        self.env_flag = env_flag


    def play_team_series_team(self):
        '''
            雷竞技的队伍和系列赛的队伍 内部ID不一致
        :return:
        '''
        sql = '''
             SELECT * FROM `data-center`.ex_series where game_id in (1,2,3,4) and start_time > unix_timestamp() - 3600*24*1 and p_id !=0 and source=1 and audit in (2,4);
        '''
        p_id_datas = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.env_flag)
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
            play_team_id_data = DoMySql().select(cnn=self.cnn, sql=play_team_id_sql, env_flag=self.env_flag)
            series_team_id_sql = f'''
                SELECT * FROM `data-center`.series_team where series_id = {i.get('p_id')};
            '''
            series_team_id_data = DoMySql().select(cnn=self.cnn, sql=series_team_id_sql, env_flag=self.env_flag)
            play_team_id_list = []
            series_team_id_list = []
            for y in play_team_id_data:
                play_team_id_list.append(y['name_id'])
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
        if len(err_team_id_ex_id) != 0:
            return str(err_team_id_ex_id)
        else:
            return ''


if __name__ == '__main__':
    c = TeamID_err(0)
    c.play_team_series_team()


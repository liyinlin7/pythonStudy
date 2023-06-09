from common.do_mysql import DoMySql

class SeriesTeam(object):

    def __init__(self, env_flag):
        self.domysql = DoMySql()
        self.cnn = self.domysql.connect_mysql_basketball(env_flag)
        self.env_flag = env_flag

    def ex_series_team(self):
        '''
            纳米 外部的队伍ID 对应的p_id 。 跟纳米内部比赛队伍的ID 不一致
        :return:
        '''
        ex_series_team_sql = '''
         SELECT ex_s.p_id, ex_s.ex_id as series_ex_id,ex_s_t.ex_id FROM `sports-basketball`.ex_series_team as ex_s_t 
        left join `sports-basketball`.ex_series as ex_s on ex_s.ex_id = ex_s_t.series_id 
        where
        ex_s.p_id != 0 and ex_s.source = 4 and ex_s.match_start_time >UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE)) and ex_s.match_start_time < UNIX_TIMESTAMP(CAST(SYSDATE()AS DATE) + INTERVAL 7 DAY) order by  ex_s.match_start_time;
        '''
        ex_series_team_datas = self.domysql.select_basketball(cnn=self.cnn, sql=ex_series_team_sql, env_flag=self.env_flag)
        ex_series_p_id_set = set()
        for i in ex_series_team_datas:
            ex_series_p_id_set.add(i['p_id'])
        out_series_p_id = []
        ex_p_id = []
        for i in ex_series_p_id_set:
            team = []
            for y in ex_series_team_datas:
                map_ = {}
                if i == y['p_id'] and i not in out_series_p_id:
                    team.append(int(y['ex_id']))
                    out_series_p_id.append(i)
                elif i == y['p_id'] and i in out_series_p_id:
                    map_['p_id'] = y['p_id']
                    map_['ex_id'] = y['series_ex_id']
                    team.append(int(y['ex_id']))
                    team.sort()
                    map_['ex_team'] = team
                    ex_p_id.append(map_)
        in_series_p_id_tuple = tuple(ex_series_p_id_set)
        in_series_id_sql = f'''
            SELECT s.id, s_t.team_id FROM `sports-basketball`.series_team as s_t 
            left join `sports-basketball`.series as s on s.id = s_t.series_id 
            where s.id in {str(in_series_p_id_tuple)} order by  s.match_start_time ;
                    '''
        in_series_id_data = self.domysql.select_basketball(cnn=self.cnn, sql=in_series_id_sql, env_flag=self.env_flag)
        in_series_id = []
        id_teamid = []
        for i in ex_series_p_id_set:
            team = []
            for y in in_series_id_data:
                map_ = {}
                if i == y['id'] and i not in in_series_id:
                    team.append(int(y['team_id']))
                    in_series_id.append(i)
                elif i == y['id'] and i in in_series_id:
                    map_['id'] = y['id']
                    team.append(int(y['team_id']))
                    team.sort()
                    map_['team_id'] = team
                    id_teamid.append(map_)
        print(ex_p_id)
        print(id_teamid)
        true_list = []
        err_list = []
        for i in ex_p_id:
            ex_p_id = i['p_id']
            ex_ex_id = i['ex_id']
            ex_team = i['ex_team']
            for y in id_teamid:
                id = y['id']
                team = y['team_id']
                if ex_p_id == id:
                    ex_team_tuple = tuple(ex_team)
                    ex_team_sql = f'''
                        SELECT * FROM `sports-basketball`.ex_team where ex_id in {str(ex_team_tuple)} and source = 4 ;
                    '''
                    ex_team_datas = self.domysql.select_basketball(cnn=self.cnn, sql=ex_team_sql, env_flag=self.env_flag)
                    teams_list = []
                    for c in ex_team_datas:
                        teams_list.append(int(c['p_id']))
                    teams_list.sort()
                    if teams_list == team:
                        true_list.append(i)
                    else:
                        err_list.append(i)

        print("没有问题的数据：", true_list)
        print("有问题的数据：", err_list)
        if len(err_list) != 0:
            return f'纳米过审的比赛,外部比赛和内部比赛的队伍p_id不一致：{str(err_list)}'
        else:
            return ''






if __name__ == '__main__':
    rr = SeriesTeam(1)
    rr.ex_series_team()



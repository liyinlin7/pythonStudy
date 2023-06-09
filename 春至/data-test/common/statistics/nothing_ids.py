from common.do_mysql import DoMySql


class nothing_ids(object):
    '''
        获取不重复的 ID 数据
    '''

    def series_ids(self, game_id, league, status=0):
        '''
            获取不重复的 series ID
        :param game_id:
        :param league:
        :param status:
        :return:
        '''
        if status == 0:
            cnn = DoMySql().connect(env_flag=0)  # env_flag,0为测试环境数据库，1为生产环境数据库
        else:
            cnn = DoMySql().connect(env_flag=1)
        sql = "select distinct id  from `data-center`.series " \
              "where game_id = {} and league_id = {};".format(game_id, league)
        datas = DoMySql().select(cnn, sql)
        series_ids = list()
        for i in datas:
            series_ids.append(i["id"])
        return tuple(series_ids)

    def team_ids(self, series_list, status=0):
        '''
            获取 不重复的队伍ID
        :param series_list:
        :param status:
        :return:
        '''
        if status == 0:
            cnn = DoMySql().connect(env_flag=0)  # env_flag,0为测试环境数据库，1为生产环境数据库
        else:
            cnn = DoMySql().connect(env_flag=1)
        sql = "SELECT distinct team_id FROM `data-center`.series_team where series_id in {};".format(series_list)
        datas = DoMySql().select(cnn, sql)
        team_ids = list()
        for i in datas:
            team_ids.append(i["team_id"])
        return tuple(team_ids)

    def match_ids(self, game_id, league, status=0):
        if status == 0:
            cnn = DoMySql().connect(env_flag=0)  # env_flag,0为测试环境数据库，1为生产环境数据库
        else:
            cnn = DoMySql().connect(env_flag=1)
        sql = "SELECT * FROM `data-center`.kog_match where game_id={} and league_id = {};".format(game_id, league)
        datas = DoMySql().select(cnn, sql)
        match_ids = list()
        for i in datas:
            match_ids.append(i['id'])
        # print(match_ids)
        return tuple(match_ids)


if __name__ == '__main__':
    nothing_ids().match_ids(game_id=4, league=685)


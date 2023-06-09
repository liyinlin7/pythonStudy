from common.do_mongoDB import MongoDB
from common.do_mysql import DoMySql


class League_TeamId_Err(object):
    '''
        各个游戏联赛的队伍ID对应的游戏ID 不一致
    '''
    def __init__(self):
        self.doMysql = DoMySql()
        self.cnn_basic = self.doMysql.cnn_basic
        self.cnn_centon = self.doMysql.cnn_centon

    def lol_league_team(self):
        sql = '''
            SELECT * FROM `data-center`.ex_league where source = 8 and p_id != 0 and game_id = 1;
        '''
        datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        league_p_id = []
        for i in datas:
            league_p_id.append(i['p_id'])
        # print(league_p_id)
        for i in league_p_id:
            league_team_sql = f'''
                SELECT * FROM `data-center`.league_team where league_id = {i} and deleted = 1;
            '''
            league_team_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=league_team_sql)
            league_team_list = []
            for y in league_team_datas:
                league_team_list.append(y['team_id'])
            # print(i)
            # print(league_team_list)
            league_team_tuple_str = ''
            if len(league_team_list) != 0:
                if len(league_team_list) == 1:
                    league_team_tuple = tuple(league_team_list)
                    league_team_tuple_str = str(league_team_tuple).replace(',', '')
                    # print(league_team_tuple)
                    # print(league_team_tuple_str)
                else:
                    league_team_tuple = tuple(league_team_list)
                    league_team_tuple_str = str(league_team_tuple)
                    # print(league_team_tuple)
                    # print(league_team_tuple_str)
            if league_team_tuple_str != '':
                basic_team_sql = f'''
                    SELECT * FROM `data-basic`.team where id in {league_team_tuple_str} and game_id != 1;
                '''
                # print(basic_team_sql)
                err_team_game_id_datas = self.doMysql.select_basic(cnn=self.cnn_basic, sql=basic_team_sql)
                err_team_game_id_list = []
                for z in err_team_game_id_datas:
                    err_team_game_id_list.append(z['id'])
                if err_team_game_id_list:
                    print('LOL联赛ID：', i, '错误的队伍ID：', err_team_game_id_list)

    def dota_league_team(self):
        sql = '''
            SELECT * FROM `data-center`.ex_league where source = 8 and p_id != 0 and game_id = 2;
        '''
        datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        league_p_id = []
        for i in datas:
            league_p_id.append(i['p_id'])
        # print(league_p_id)
        for i in league_p_id:
            league_team_sql = f'''
                SELECT * FROM `data-center`.league_team where league_id = {i} and deleted = 1;
            '''
            league_team_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=league_team_sql)
            league_team_list = []
            for y in league_team_datas:
                league_team_list.append(y['team_id'])
            # print(i)
            # print(league_team_list)
            league_team_tuple_str = ''
            if len(league_team_list) != 0:
                if len(league_team_list) == 1:
                    league_team_tuple = tuple(league_team_list)
                    league_team_tuple_str = str(league_team_tuple).replace(',', '')
                    # print(league_team_tuple)
                    # print(league_team_tuple_str)
                else:
                    league_team_tuple = tuple(league_team_list)
                    league_team_tuple_str = str(league_team_tuple)
                    # print(league_team_tuple)
                    # print(league_team_tuple_str)
            if league_team_tuple_str != '':
                basic_team_sql = f'''
                    SELECT * FROM `data-basic`.team where id in {league_team_tuple_str} and game_id != 2;
                '''
                # print(basic_team_sql)
                err_team_game_id_datas = self.doMysql.select_basic(cnn=self.cnn_basic, sql=basic_team_sql)
                err_team_game_id_list = []
                for z in err_team_game_id_datas:
                    err_team_game_id_list.append(z['id'])
                if err_team_game_id_list:
                    print('DOTA联赛ID：', i, '错误的队伍ID：', err_team_game_id_list)

    def csgo_league_team(self):
        sql = '''
            SELECT * FROM `data-center`.ex_league where source = 8 and p_id != 0 and game_id = 3;
        '''
        datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        league_p_id = []
        for i in datas:
            league_p_id.append(i['p_id'])
        # print(league_p_id)
        for i in league_p_id:
            league_team_sql = f'''
                SELECT * FROM `data-center`.league_team where league_id = {i} and deleted = 1;
            '''
            league_team_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=league_team_sql)
            league_team_list = []
            for y in league_team_datas:
                league_team_list.append(y['team_id'])
            # print(i)
            # print(league_team_list)
            league_team_tuple_str = ''
            if len(league_team_list) != 0:
                if len(league_team_list) == 1:
                    league_team_tuple = tuple(league_team_list)
                    league_team_tuple_str = str(league_team_tuple).replace(',', '')
                    # print(league_team_tuple)
                    # print(league_team_tuple_str)
                else:
                    league_team_tuple = tuple(league_team_list)
                    league_team_tuple_str = str(league_team_tuple)
                    # print(league_team_tuple)
                    # print(league_team_tuple_str)
            if league_team_tuple_str != '':
                basic_team_sql = f'''
                    SELECT * FROM `data-basic`.team where id in {league_team_tuple_str} and game_id != 3;
                '''
                # print(basic_team_sql)
                err_team_game_id_datas = self.doMysql.select_basic(cnn=self.cnn_basic, sql=basic_team_sql)
                err_team_game_id_list = []
                for z in err_team_game_id_datas:
                    err_team_game_id_list.append(z['id'])
                if err_team_game_id_list:
                    print('CSGO联赛ID：', i, '错误的队伍ID：', err_team_game_id_list)

    def kog_league_team(self):
        sql = '''
            SELECT * FROM `data-center`.ex_league where source = 8 and p_id != 0 and game_id = 4;
        '''
        datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        league_p_id = []
        for i in datas:
            league_p_id.append(i['p_id'])
        # print(league_p_id)
        for i in league_p_id:
            league_team_sql = f'''
                SELECT * FROM `data-center`.league_team where league_id = {i} and deleted = 1;
            '''
            league_team_datas = self.doMysql.select_centon(cnn=self.cnn_centon, sql=league_team_sql)
            league_team_list = []
            for y in league_team_datas:
                league_team_list.append(y['team_id'])
            # print(i)
            # print(league_team_list)
            league_team_tuple_str = ''
            if len(league_team_list) != 0:
                if len(league_team_list) == 1:
                    league_team_tuple = tuple(league_team_list)
                    league_team_tuple_str = str(league_team_tuple).replace(',', '')
                    # print(league_team_tuple)
                    # print(league_team_tuple_str)
                else:
                    league_team_tuple = tuple(league_team_list)
                    league_team_tuple_str = str(league_team_tuple)
                    # print(league_team_tuple)
                    # print(league_team_tuple_str)
            if league_team_tuple_str != '':
                basic_team_sql = f'''
                    SELECT * FROM `data-basic`.team where id in {league_team_tuple_str} and game_id != 4;
                '''
                # print(basic_team_sql)
                err_team_game_id_datas = self.doMysql.select_basic(cnn=self.cnn_basic, sql=basic_team_sql)
                err_team_game_id_list = []
                for z in err_team_game_id_datas:
                    err_team_game_id_list.append(z['id'])
                if err_team_game_id_list:
                    print('KOG联赛ID：', i, '错误的队伍ID：', err_team_game_id_list)


if __name__ == '__main__':
    l = League_TeamId_Err()
    l.lol_league_team()
    l.dota_league_team()
    l.csgo_league_team()
    l.kog_league_team()
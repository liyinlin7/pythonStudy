import time
import json
from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
import datetime
from common import my_logger
from common.read_config import ReadConfig
from common import read_path


class BasketBallResult(object):

    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_basketball = self.do_mysql.connect_mysql_basketball(env_flag=env_flag)  # 0是测试，1是线上
        self.team = self.basket_ball_team()
        self.player = self.basket_ball_player()
        self.request_dataBase = ReadConfig().read_config(read_path.conf_path, 'sports_soccer', 'dataBase_basket')
        self.request_dataBase_result = ReadConfig().read_config(read_path.conf_path, 'sports_soccer',
                                                                'mogonDB_collection_result_basket')

    def basket_ball_team(self):
        sql = '''
            SELECT * FROM `sports-basketball`.team ;
        '''
        basket_team_datas = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        team_list = []
        for i in basket_team_datas:
            team_map = {}
            team_map[i['id']] = i['name_zh']
            team_list.append(team_map)
        return team_list

    def basket_ball_player(self):
        sql = '''
            SELECT * FROM `sports-basketball`.player ;
        '''
        basket_player_datas = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        player_list = []
        for i in basket_player_datas:
            player_map = {}
            player_map[i['id']] = i['name_zh']
            player_list.append(player_map)
        return player_list

    def requestdata_team_player_id_null(self, match_id, team_id):
        '''
            1.赛果数据-有team_id=0
            2.赛果数据-有player_id=0
        :return:
        '''
        player_maps = self.basket_ball_player()
        team_maps = self.basket_ball_team()
        print(self.request_dataBase_result)
        print(self.request_dataBase)
        dcnn = MongoDB(self.env_flag).sport_connect_basketball(dataBase=self.request_dataBase, collection=self.request_dataBase_result)
        result_datas = MongoDB(self.env_flag).get_data_list_basketball(dcnn=dcnn, list=match_id)
        for i in result_datas:
            # print(i)
            tems_data = i['data']
            for team in team_id:
                team_value = ''
                for y in tems_data:
                    if team == y['teamId']:
                        for j in team_maps:
                            if team in j.keys():
                                team_value = j.get(team)
                        if team_value != '':
                            print("队伍是：", team_value)
                        player_datas = y['player']
                        for player in player_datas:
                            player_value = ''
                            player_id = player['playerId']
                            for k in player_maps:
                                if player_id in k.keys():
                                    player_value = k.get(player_id)
                            print("队员名称:", player_value)
                            print('出场时间', player['playingTime'])
                            print('是否出场（1、未出场，2、出场）', player['isplaying'])
                            print('是否首发（1、非首发，2、首发）', player['isstarting'])
                            print('得分', player['point'])
                            print('投篮次数', player['fieldshotattempt'])
                            print('命中次数', player['fieldgoal'])
                            if player['fieldgoal'] != 0:
                                print('投篮命中率:', player['fieldshotsuccessrate'],
                                      '[计算得出的结果]:', format(player['fieldgoal'] / player['fieldshotattempt'], '.2f'))
                            else:
                                print('投篮命中率:', player['fieldshotsuccessrate'])
                            print('三分投篮次数', player['threepointshotattempt'])
                            print('三分球投篮命中次数', player['threepointgoal'])
                            if player['threepointgoal'] != 0:
                                print('三分球命中率:', player['threepointshotsuccessrate'],
                                      '[计算得出的结果]:', format(player['threepointgoal'] / player['threepointshotattempt'], '.2f'))
                            else:
                                print('三分球命中率:', player['threepointshotsuccessrate'])

                            print('两分球投篮命中次数', player['twopointgoal'], '计算结果：', player['fieldgoal'] - player['threepointgoal'])
                            print('两分球投篮次数', player['twopointshotattempt'], '计算结果：', player['fieldshotattempt'] - player['threepointshotattempt'])
                            if player['fieldgoal'] - player['threepointgoal'] != 0:
                                print('两分球命中率:', player['twopointshotsuccessrate'],
                                      '[计算得出的结果]:', format((player['fieldgoal'] - player['threepointgoal']) / (player['fieldshotattempt'] - player['threepointshotattempt']), '.2f'))
                            else:
                                print('两分球命中率:', player['twopointshotsuccessrate'])
                            print('罚球投篮次数', player['freethrowattempt'])
                            print('罚球命中次数', player['freethrowgoal'])
                            if player['freethrowgoal'] != 0:
                                print('罚球命中率:', player['freethrowsuccessrate'],
                                      '[计算得出的结果]:', format(player['freethrowgoal'] / player['freethrowattempt'], '.2f'))
                            else:
                                print('罚球命中率:', player['freethrowsuccessrate'])
                            print('进攻篮板', player['offensiverebound'])
                            print('防守篮板', player['defensiverebound'])
                            print('总篮板', player['rebound'])
                            print('助攻数', player['assist'])
                            print('抢断数', player['steal'])
                            print('盖帽数', player['block'])
                            print('失误次数', player['turnover'])
                            print('个人犯规次数', player['foul'])
                            print('--------------------------------')


if __name__ == '__main__':
    b = BasketBallResult(env_flag=0)
    b.requestdata_team_player_id_null([2620], [5951, 5950])
    # con = DoMySql().link_testsql()
    # storage_data(data, con)
    # storage_statistics(data, con)
    # storage_special_event(data, con)






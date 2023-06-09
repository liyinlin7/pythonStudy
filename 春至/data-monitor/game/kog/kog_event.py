from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
import time
import datetime
import json

class Kog_Event(object):
    '''
        王者赛果事件 数据显示
    '''

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn, monGon_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.mogonDB_dataBase = 'data-result'
        self.mogonDB_collection_kog_event = 'kog_event'
        self.monGon = monGon_cnn
        self.doMysql = mysql_cnn

    def get_data_all(self, match_id, dataBase, collection):
        myDb = self.monGon
        collect1 = myDb.connect(dataBase, collection)
        sen = '{"match_id":' + str(match_id) + '}'
        result = myDb.select_data_all(collect1, sen)
        return result

    def kog_result_event(self, match_id):
        hero_list = self.kog_hero()
        team_list = self.kog_team()
        player_list = self.kog_player()
        event_datas = self.get_data_all(match_id=match_id, dataBase=self.mogonDB_dataBase, collection=self.mogonDB_collection_kog_event)
        for i in event_datas:
            print(i)
            play_time = i["time"]
            event = i['event']
            event_type = i['type']
            if event_type == 1:  # BP英雄
                self.event_type_1(event, hero_list, team_list, player_list)
            elif event_type == 2:  # 小局开始事件
                self.event_type_2(event)
            elif event_type == 3:  # 小局结束事件
                self.event_type_3(event)
            elif event_type == 4:  # 击杀事件
                self.event_type_4(event, hero_list, team_list, player_list, play_time)
            elif event_type == 5:  # 中立怪击杀事件
                self.event_type_5(event, team_list, player_list, play_time)
            elif event_type == 6:  # 推塔事件
                self.event_type_6(event, team_list, player_list, play_time)

    def kog_player(self):
        sql = '''
                SELECT * FROM `data-basic`.player where game_id=4 and deleted =1;
            '''
        if self.env_flag == 'release':
            player_data = self.doMysql.select_basic(cnn=self.cnn_basic, sql=sql)
        elif self.env_flag == 'develop':
            player_data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        player_list = []
        for i in player_data:
            player_map = {}
            player_map[i['id']] = i['name_full']
            # player_map['name_full'] =
            player_list.append(player_map)
        # print(player_list)
        return player_list

    def kog_hero(self):
        sql = '''
                SELECT * FROM `data-basic`.hero where game_id=4 and deleted =1;
            '''
        if self.env_flag == 'release':
            hero_data = self.doMysql.select_basic(cnn=self.cnn_basic, sql=sql)
        elif self.env_flag == 'develop':
            hero_data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        hero_list = []
        for i in hero_data:
            hero_map = {}
            hero_map[i['id']] = i['name_zh']
            hero_list.append(hero_map)
        # print(hero_list)
        return hero_list

    def kog_team(self):
        sql = '''
                SELECT * FROM `data-basic`.team where game_id=4 and deleted =1;
            '''
        if self.env_flag == 'release':
            team_data = self.doMysql.select_basic(cnn=self.cnn_basic, sql=sql)
        elif self.env_flag == 'develop':
            team_data = self.doMysql.select_centon(cnn=self.cnn_centon, sql=sql)
        team_list = []
        for i in team_data:
            team_map = {}
            team_map[i['id']] = i['name_full']
            # team_map['name_full'] =
            team_list.append(team_map)
        # print(team_list)
        return team_list

    def event_type_1(self, event, hero_list, team_list, player_list):
        event_ = event
        team_value = ''
        bp_str = ''
        hero_value = ''
        plyaer_value = None
        if event_['bp_type'] == 2:
            bp_str = 'pick的英雄'
        elif event_['bp_type'] == 1:
            bp_str = 'ban的英雄'
        for i in team_list:
            if event_['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in hero_list:
            if event_['hero_id'] in i.keys():
                hero_value = i.get(event['hero_id'])
        for i in player_list:
            if event_['player_id'] in i.keys():
                plyaer_value = i.get(event['player_id'])
        print(team_value + '  ' + str(plyaer_value) + ' ' + bp_str + ' ' + hero_value)

    def event_type_2(self, event):
        timestamp = event['start_time']
        time_local = time.localtime(timestamp)
        star_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        print(f'小局开始时间：{star_time}')

    def event_type_3(self, event):
        timestamp = event['end_time']
        time_local = time.localtime(timestamp)
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        print(f'小局结束时间{end_time}')

    def event_type_4(self, event, hero_list, team_list, player_list, play_time):
        kill_time = str(datetime.timedelta(seconds=play_time))
        kill_team_value = ''
        kill_player_value = ''
        kill_hero_value = ''
        killed_team_value = ''
        killed_player_value = ''
        killed_hero_value = ''
        for i in team_list:
            if event['kill_team_id'] in i.keys():
                kill_team_value = i.get(event['kill_team_id'])
            if event['killed_team_id'] in i.keys():
                killed_team_value = i.get(event['killed_team_id'])
        for i in hero_list:
            if event['kill_hero_id'] in i.keys():
                kill_hero_value = i.get(event['kill_hero_id'])
            if event['killed_hero_id'] in i.keys():
                killed_hero_value = i.get(event['killed_hero_id'])
        for i in player_list:
            if event['kill_player_id'] in i.keys():
                kill_player_value = i.get(event['kill_player_id'])
            if event['killed_player_id'] in i.keys():
                killed_player_value = i.get(event['killed_player_id'])
        print(f"比赛开始{kill_time}：{kill_team_value}的{kill_player_value}_{kill_hero_value} 击杀了 {killed_team_value}的{killed_player_value}_{killed_hero_value}")

    def event_type_5(self, event, team_list, player_list, play_time):
        kill_time = str(datetime.timedelta(seconds=play_time))
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                kill_player_value = i.get(event['player_id'])
        if event['neutral_type'] == 1:
            monster_value = '主宰'
        elif event['neutral_type'] == 2:
            monster_value = '先知主宰'
        elif event['neutral_type'] == 3:
            monster_value = '暴君'
        elif event['neutral_type'] == 4:
            monster_value = '黑暗暴君'
        elif event['neutral_type'] == 5:
            monster_value = '风暴龙王'
        elif event['neutral_type'] == 6:
            monster_value = '未知龙'
            kill_player_value = '未知队员'
        print(f'比赛开始{kill_time}：{team_value}的{kill_player_value}击杀了{monster_value}')

    def event_type_6(self, event, team_list, player_list, play_time):
        kill_time = str(datetime.timedelta(seconds=play_time))
        team_value = ''
        player_value = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        if event['killer_type'] == 1:
            print(f'比赛开始{kill_time}：{team_value}的{player_value}推了一座塔')
        elif event['killer_type'] == 2:
            print(f'比赛开始{kill_time}：{team_value}的 小兵 推了一座塔')


if __name__ == '__main__':
    mysql_cnn = DoMySql()
    monGon_cnn = MongoDB()
    cnn_centon = mysql_cnn.cnn_centon_def()
    cnn_basic = mysql_cnn.cnn_basic_def()
    a = Kog_Event('release', cnn_centon, cnn_basic, mysql_cnn, monGon_cnn)   # release  , develop
    a.kog_result_event(4195)





import time
import websocket
import threading
import json
from common.do_mysql import DoMySql
import ssl
import datetime
from common import my_logger
import logging


illegal_str = ['Pong', 'Ping']


class BasketBallWS(object):

    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_basketball = self.do_mysql.connect_mysql_basketball(env_flag=env_flag)  # 0是测试，1是线上
        self.team = self.basket_ball_team()
        self.player = self.basket_ball_player()

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


    def result_event(self, match_id):
        sql = f'''
                    SELECT * FROM `sports-basketball-match`.event where match_id = {match_id};
                '''
        result_event = self.do_mysql.select_basketball(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        for event in result_event:
            event_type = event['type']
            # print(event_type)
            data1 = event['data']
            data = json.loads(data1)
            self.basket_result_event(event_type, data)


    def basket_result_event(self, event_type, data):
        player_list = self.player
        team_list = self.team
        event_type = event_type
        play_time = data["time"]
        event_data = data['event_data']
        section = play_time[0]
        # time = str(datetime.timedelta(milliseconds=play_time[1]))
        time_1 = datetime.datetime.fromtimestamp(play_time[1]/1000)
        str1 = time_1.strftime("%M:%S.%f")
        print(f'第  {section}  小节，时间:{str1}')
        if event_type == 1:  # 阶段开始
            self.event_type_1(event_data)
        elif event_type == 2:  # 阶段结束
            self.event_type_2(event_data)
        elif event_type == 3:  # 球员出场
            self.event_type_3(event_data, team_list, player_list)
        elif event_type == 4:  # 投篮事件
            self.event_type_4(event_data, team_list, player_list)
        elif event_type == 5:  # 罚篮事件
            self.event_type_5(event_data, team_list, player_list)
        elif event_type == 6:  # 篮板事件
            self.event_type_6(event_data, team_list, player_list)
        elif event_type == 7:  # 失误事件
            self.event_type_7(event_data, team_list, player_list)
        elif event_type == 8:  # 换人事件
            self.event_type_8(event_data, team_list, player_list)
        elif event_type == 9:  # 犯规事件
            self.event_type_9(event_data, team_list, player_list)
        elif event_type == 10:  # 暂停事件
            self.event_type_10(event_data, team_list)
        elif event_type == 11:  # 争球事件
            self.event_type_11(event_data, team_list, player_list)
        else:
            print('错误事件', data)

    def event_type_1(self, event):
        if event['stage'] == 1:
            print('比赛开始')
        elif event['stage'] == 2:
            print('第一节开始')
        elif event['stage'] == 3:
            print('第二节开始')
        elif event['stage'] == 4:
            print('第三节开始')
        elif event['stage'] == 5:
            print('第四节开始')
        elif event['stage'] == 6:
            print('第一节加时赛开始')
        elif event['stage'] == 7:
            print('第二节加时赛开始')
        elif event['stage'] == 100:
            print('比赛结束')
        else:
            print('更多加时赛开始')

    def event_type_2(self, event):
        if event['stage'] == 2:
            print('第一节结束')
        elif event['stage'] == 3:
            print('第二节结束')
        elif event['stage'] == 4:
            print('第三节结束')
        elif event['stage'] == 5:
            print('第四节结束')
        elif event['stage'] == 6:
            print('第一节加时赛结束')
        elif event['stage'] == 7:
            print('第二节加时赛结束')
        else:
            print('更多加时赛结束')

    def event_type_3(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        is_starting = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        if event['is_starting'] == 1:
            is_starting = '不是首发'
        elif event['is_starting'] == 2:
            is_starting = '是首发'
        print(f'球员出场事件： {team_value} 出场球员 {player_value}， {is_starting}')

    def event_type_4(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        assist_player_id = event['assist_player_id']
        assist_player_value = ''
        x, y = event['x'], event['y']
        score_value = ''
        value = event['value']
        is_target_value = ''
        is_target = event['is_target']
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
            if assist_player_id is not None:
                if assist_player_id in i.keys():
                    assist_player_value = i.get(assist_player_id)
        if value == 1:
            score_value = '两分球'
        elif value == 2:
            score_value = '三分球'
        if is_target == 1:
            is_target_value = '未命中'
        elif is_target == 2:
            is_target_value = '命中'
        if assist_player_id is not None:
            print(f'投篮事件： {team_value} 的 {player_value} 投 {score_value} {is_target_value} 助攻队员 {assist_player_value}，X轴{x} y轴{y}')
        else:
            print(f'投篮事件： {team_value} 的 {player_value} 投 {score_value} {is_target_value} 没有助攻队员，X轴{x} y轴{y}')

    def event_type_5(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        score_value = ''
        value = event['value']
        is_target_value = ''
        is_target = event['is_target']
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        if value == 1:
            score_value = '2罚的第一罚'
        elif value == 2:
            score_value = '2罚的第二罚'
        elif value == 3:
            score_value = '3罚的第一罚'
        elif value == 4:
            score_value = '3罚的第二罚'
        elif value == 5:
            score_value = '3罚的第三罚'
        elif value == 6:
            score_value = '1罚的第1罚'
        if is_target == 1:
            is_target_value = '未命中'
        elif is_target == 2:
            is_target_value = '命中'
        print(f'罚篮事件： {team_value} 的 {player_value}  {score_value} {is_target_value}')

    def event_type_6(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        player_id = event['player_id']
        x, y = event['x'], event['y']
        score_value = ''
        value = event['value']
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if player_id is not None:
                if event['player_id'] in i.keys():
                    player_value = i.get(event['player_id'])
        if value == 1:
            score_value = '防守篮板'
        elif value == 2:
            score_value = '进攻篮板'
        elif value == 3:
            score_value = '全队防守篮板'
        elif value == 4:
            score_value = '全队进攻篮板'
        if value in (1, 2):
            print(f'篮板事件： {team_value} 的 {player_value} 抢到  {score_value} ， X轴{x} y轴{y}')
        else:
            print(f'篮板事件： {team_value} 的 {str(player_value)} 抢到  {score_value} ， X轴{x} y轴{y}')

    def event_type_7(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        x, y = event['x'], event['y']
        block_team_id = event['block_team_id']
        block_team_value = ''
        block_player_id = event['block_player_id']
        block_player_value = ''
        score_value = ''
        value = event['value']
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
            if block_team_id is not None:
                if block_team_id in i.keys():
                    block_team_value = i.get(block_team_id)
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
            if block_player_id is not None:
                if block_player_id in i.keys():
                    block_player_value = i.get(block_player_id)
        if value == 1:
            score_value = '传球失误'
        elif value == 2:
            score_value = '丢球失误'
        elif value == 3:
            score_value = '出界失误'
        elif value == 4:
            score_value = '运球失误'
        elif value == 6:
            score_value = '进攻事件超时失误'
        elif value == 7:
            score_value = '其他'
        print(f'失误事件： {team_value} 的 {player_value} 失误是 {score_value} ，抢断的是 {str(block_team_value)} 的 {str(block_player_value)}')

    def event_type_8(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        score_value = ''
        value = event['value']
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        if value == 1:
            score_value = '下场'
        elif value == 2:
            score_value = '上场'
        print(f'换人事件： {team_value} 的 {player_value} {score_value}')

    def event_type_9(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        x, y = event['x'], event['y']
        score_value = ''
        value = event['value']
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        if value == 1:
            score_value = '个人犯规'
        elif value == 2:
            score_value = '投篮犯规'
        elif value == 3:
            score_value = '进攻犯规'
        elif value == 4:
            score_value = '技术犯规'
        elif value == 5:
            score_value = '无球犯规'
        print(f'犯规事件： {team_value} 的 {player_value}  {score_value} ， X轴{x} y轴{y}')

    def event_type_10(self, event, team_list):
        team_value = ''
        team_id = event['team_id']
        score_value = ''
        value = event['value']
        for i in team_list:
            if team_id is not None:
                if event['team_id'] in i.keys():
                    team_value = i.get(event['team_id'])
        if value == 1:
            score_value = '长暂停'
        elif value == 2:
            score_value = '短暂停'
        elif value == 3:
            score_value = '官方暂停'
        elif value == 4:
            score_value = '特殊暂停'
        print(f'暂停事件： {str(team_value)}  {str(score_value)}')

    def event_type_11(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        home_player_value = ''
        away_player_value = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
            if event['home_player_id'] in i.keys():
                home_player_value = i.get(event['home_player_id'])
            if event['away_player_id'] in i.keys():
                away_player_value = i.get(event['away_player_id'])
        print(f'争球事件： {home_player_value} 与 {away_player_value} 争球， {team_value} 的 {player_value} 得到球')


if __name__ == '__main__':
    b = BasketBallWS(env_flag=1)
    b.result_event(62623)
    # con = DoMySql().link_testsql()
    # storage_data(data, con)
    # storage_statistics(data, con)
    # storage_special_event(data, con)






import time
import websocket
import threading
import json
from common.do_mysql import DoMySql
import ssl
import datetime
from common import my_logger
import logging
from test_live.football_live_statistics import FootBallLiveStatistics


illegal_str = ['Pong', 'Ping']


class FootballEvent(object):

    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_football = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.team = self.football_team()
        self.player = self.football_player()
        # self.ex_team = self.football_ex_team()
        # self.ex_player = self.football_ex_player()

    def football_team(self):
        sql = '''
            SELECT * FROM `sports-soccer`.team ;
        '''
        football_team_datas = self.do_mysql.select(cnn=self.cnn_football, sql=sql, env_flag=self.env_flag)
        team_list = []
        for i in football_team_datas:
            team_map = {}
            team_map[i['id']] = i['name_zh']
            team_list.append(team_map)
        return team_list

    def football_ex_team(self):
        sql = '''
            SELECT * FROM `sports-soccer`.ex_team where source = 4;
        '''
        football_team_datas = self.do_mysql.select(cnn=self.cnn_football, sql=sql, env_flag=self.env_flag)
        team_list = []
        for i in football_team_datas:
            team_map = {}
            team_map[i['ex_id']] = i['p_id']
            team_map['name'] = i['name_zh']
            team_list.append(team_map)
        return team_list

    def football_player(self):
        sql = '''
            SELECT * FROM `sports-soccer`.player ;
        '''
        football_player_datas = self.do_mysql.select(cnn=self.cnn_football, sql=sql, env_flag=self.env_flag)
        player_list = []
        for i in football_player_datas:
            player_map = {}
            player_map[i['id']] = i['name_zh']
            player_list.append(player_map)
        return player_list

    def football_ex_player(self):
        sql = '''
            SELECT * FROM `sports-soccer`.ex_player where source =4 ;
        '''
        football_player_datas = self.do_mysql.select(cnn=self.cnn_football, sql=sql, env_flag=self.env_flag)
        player_list = []
        for i in football_player_datas:
            player_map = {}
            player_map[i['ex_id']] = i['p_id']
            player_map['name'] = i['name_zh']
            player_list.append(player_map)
        return player_list

    def get_heart(self, ws):
        try:
            while True:
                time.sleep(3)
                ws.send('2')
                # print("发送了心跳！")
        except:
            self.get_heart(ws)

    def my_data(self, data):
        if data not in illegal_str:
            data = data.replace('payload":"{', 'payload":\'{')
            data = data.replace('}"}', '}\'}')
        return data

    def message_handle(self,  match_id):
        url = "wss://soccer_stream.sportsapi.cn/ws"  # 测试
        # url = "wss://soccer_stream.dawnbyte.com/ws"   # 线上
        print(1111, url)
        ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
        ws.send('1')  # 以字符串发送消息
        t = threading.Thread(target=self.get_heart, name="心跳线程", args=(ws,))  # 心跳线程
        t.setDaemon(True)  # 设置线程守护
        t.start()
        try:
            while True:
                try:
                    mes = ws.recv()  # 接收消息，如果无消息将会堵塞,直到21s超时等待结束
                    # print("实时数据", mes)
                    if mes not in illegal_str:
                        try:
                            res = json.loads(mes)
                            payload = res['payload']
                            payload_a = json.loads(payload)
                            if res['type'] == 202 and payload_a['id'] == match_id:  # 2674 and payload_a['match_id'] == 2674
                                print("比赛数据202", str(mes))
                                self.football_series_live(payload_a)
                            elif res['type'] == 301 and payload_a['match_id'] == match_id:  # 2674 and payload_a['match_id'] == 2674
                                print("实时数据301", str(mes))
                                self.football_live_301(payload_a)
                            # if res['type'] == 303 and payload_a['match_id'] == match_id:  # match_id = 2674
                            #     print('--------------------------------------')
                            #     print("实时事件303:", mes)
                            #     self.football_live_303(payload_a)
                            # if res['type'] == 302:  # and payload_a['match_id'] == match_id:  # match_id = 2674
                            #     print("实时统计302:", mes)
                            #     self.football_live_302(payload_a)
                            # if res['type'] == 304:
                            #     print("视频推送304", str(mes))
                        except Exception as e:
                            print("数据存储操作出错：", e)
                            self.message_handle(match_id)
                except Exception as e:
                    print("出错！！！", e)
                    self.message_handle(match_id)
        except Exception as e:
            print("连接超时！！！！", e)
            self.message_handle(match_id)

    def football_series_live(self, data):
        status = {"1": "未开始", "2": "上半场", "3": "中场", "4": "下半场", "5": "加时赛", "6": "点球大战",
                  "7": "已结束", "8": "已取消", "9": "比赛中断", "10": "推迟", "11": "腰斩", "12": "待定", "13": "异常"}
        status_ = str(data['status'])
        status_value = ''
        if status_ in status.keys():
            status_value = status.get(status_)
        teams = data['team']
        team_list = self.team
        print(f'比赛阶段：{status_value}')
        for team in teams:
            team_value = ''
            team_id = team['team_id']
            for i in team_list:
                if team_id in i.keys():
                    team_value = i.get(team_id)
            print(f"{team_value} 的分数 {team['score']}")

    def football_live_301(self, data):
        status = {"1": "未开始", "2": "上半场", "3": "中场", "4": "下半场", "5": "加时赛", "6": "点球大战",
                  "7": "已结束", "8": "已取消", "9": "比赛中断", "10": "推迟", "11": "腰斩", "12": "待定", "13": "异常"}
        status_ = str(data['status'])
        status_value = ''
        if status_ in status.keys():
            status_value = status.get(status_)
        play_time = data["time"]
        time_ = str(datetime.timedelta(seconds=play_time))
        # time_1 = datetime.datetime.fromtimestamp(play_time/1000)
        # str1 = time_1.strftime("%M:%S.%f")
        # time_ = data['time'] / 60
        teams = data['team']
        team_list = self.team
        print(f'比赛阶段：{status_value}，比赛时间：{time_}')
        for team in teams:
            team_value = ''
            team_id = team['team_id']
            for i in team_list:
                if team_id in i.keys():
                    team_value = i.get(team_id)
            print(f"{team_value} 的分数：{team['score']},红牌数：{team['red']},  黄牌数：{team['yellow']},  角球数：{team['corner']},"
                  f"两黄一红：{team['yellow2red_cards']},  点球进球数：{team['penalty_goal']},  点球射失数：{team['penalty_missed']},  换人数：{team['substitute']},"
                  f"  乌龙球数：{team['own_goal']},  射门数：{team['shot']},  射正数：{team['target_shot']},  射偏数：{team['off_target_shot']},"
                  f"  进攻数：{team['attack']},  危险进攻数：{team['dangerous_attack']},  控球率：{team['possession']}")

    def football_live_303(self, data):
        player_list = self.player
        team_list = self.team
        event_list = data['event']
        for i in event_list:
            play_time = i["time"]
            event = i['event_data']
            event_type = i['type']
            # section = play_time[0]
            time_ = str(datetime.timedelta(seconds=play_time))
            # time_1 = datetime.datetime.fromtimestamp(play_time[1]/1000)
            # str1 = time_1.strftime("%M:%S.%f")
            print(f'比赛时长: {time_}')
            if event_type == 1:  # 阶段开始
                self.event_type_1(event)
            elif event_type == 2:  # 阶段结束
                self.event_type_2(event)
            elif event_type == 3:  # 进球事件
                self.event_type_3(event, team_list, player_list)
            elif event_type == 4:  # 点球事件
                self.event_type_4(event, team_list, player_list)
            elif event_type == 5:  # 乌龙球事件
                self.event_type_5(event, team_list, player_list)
            elif event_type == 6:  # 角球事件
                self.event_type_6(event, team_list, player_list)
            elif event_type == 7:  # 黄牌事件
                self.event_type_7(event, team_list, player_list)
            elif event_type == 8:  # 红牌事件
                self.event_type_8(event, team_list, player_list)
            elif event_type == 9:  # 换人事件
                self.event_type_9(event, team_list, player_list)
            elif event_type == 10:  # 视频助力裁判事件
                self.event_type_10(event, team_list, player_list)
            else:
                print('错误事件', data)

    def event_type_1(self, event):
        if event['stage'] == 1:
            print('开始：上半场')
        elif event['stage'] == 2:
            print('开始：下半场')
        elif event['stage'] == 3:
            print('开始：加时赛')
        elif event['stage'] == 4:
            print('开始：点球')
        elif event['stage'] == 5:
            print('开始：伤停补时')
        else:
            print('type=1，status错误状态')

    def event_type_2(self, event):
        if event['stage'] == 1:
            print('结束：上半场')
        elif event['stage'] == 2:
            print('结束：下半场')
        elif event['stage'] == 3:
            print('结束：加时赛')
        elif event['stage'] == 4:
            print('结束：点球')
        else:
            print('type=2，status错误状态')

    def event_type_3(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        assist_player_id = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
            if event['assist_player_id'] in i.keys():
                assist_player_id = i.get(event['assist_player_id'])
        print(f'进球队伍： {team_value}， 进球队员： {player_value}， 助攻队员：{assist_player_id}')

    def event_type_4(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        is_goal = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        if event['is_goal'] == 1:
            is_goal = '未进'
        elif event['is_goal'] == 2:
            is_goal = '进球'
        print(f'点球队伍： {team_value}， 点球队员： {player_value}， 是否进球：{is_goal}')

    def event_type_5(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        print(f'乌龙球队伍： {team_value}， 造成乌龙球队员： {player_value}')

    def event_type_6(self, event, team_list, player_list):
        team_value = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        print(f'角球队伍： {team_value}')

    def event_type_7(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        print(f'黄牌队伍： {team_value}，黄牌队员： {player_value}')

    def event_type_8(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        is_yellow = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        if event['is_yellow'] == 1:
            is_yellow = '不是 '
        elif event['is_yellow'] == 2:
            is_yellow = '是'
        print(f'红牌队伍： {team_value}， 红牌队员： {player_value}， 是否是“两黄一红”：{is_yellow}')

    def event_type_9(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        sub_player_value = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
            if event['sub_player_id'] in i.keys():
                sub_player_value = i.get(event['sub_player_id'])
        print(f'换人队伍：{team_value}，上场队员：{player_value}， 下场队员：{sub_player_value}')

    def event_type_10(self, event, team_list, player_list):
        team_value = ''
        player_value = ''
        reason_value = ''
        result_value = ''
        for i in team_list:
            if event['team_id'] in i.keys():
                team_value = i.get(event['team_id'])
        for i in player_list:
            if event['player_id'] in i.keys():
                player_value = i.get(event['player_id'])
        reason_value = event['reason']
        result_value = event['result']
        print(f'视频助力事件 队伍：{team_value}，队员：{player_value}， 原因：{reason_value}， 结果：{result_value}')

    def football_live_302(self, data):
        F = FootBallLiveStatistics()
        foot_nami = F.nami_resquest()
        print(foot_nami)
        ex_player_list = self.ex_player
        ex_team_list = self.ex_team
        teams = data['team']
        for ex_team in ex_team_list:  # 循环 内外部ID 队伍字典
            for i in teams:  # 循环 302 统计数据的 team
                i_team_pid = i['team_id']
                i_player_list = i['player']
                for nami_data in foot_nami:  # 循环  纳米接口 数据
                    nami_team_id = nami_data['team_id']
                    nami_player_id = nami_data['player_id']
                    # print("内部队伍字典", ex_team)
                    # print("内部ID", i_team_pid)
                    # print("外部ID", nami_team_id)
                    if i_team_pid in ex_team.values() and str(nami_team_id) in ex_team.keys():  # 统计的内部队伍ID 和 纳米的队伍 外部ID  同时对比 字段数据
                        for ex_player in ex_player_list:  # 循环 内外部ID 队员字典
                            for y in i_player_list:
                                if y['player_id'] in ex_player.values() and str(nami_player_id) in ex_player.keys():  # 统计的内部队员ID 和 纳米的 外部队员ID  同时对比 字段数据
                                    print("队伍名称是：", ex_team.get('name'))
                                    print("队员内部的ID，：", y['player_id'], "队员的名称是：",  ex_player.get('name'))
                                    print("是否首发：", "内部数据：", y['is_starting'], "外部数据：", nami_data['first'], "我们的1对应0,2对应1")
                                    print("上场时间，单位秒：", "内部数据：", y['playing_time'], "外部数据：", nami_data['minutes_played'])
                                    print("球员进球数：", "内部数据：", y['goal'], "外部数据：", nami_data['goals'])
                                    print("球员点球进球数：", "内部数据：", y['penalty_goal'], "外部数据：", nami_data['penalty'])
                                    print("球员助攻数：", "内部数据：", y['assist'], "外部数据：", nami_data['assists'])
                                    print("球员红牌数：", "内部数据：", y['red'], "外部数据：", nami_data['red_cards'])
                                    print("球员黄牌数：", "内部数据：", y['yellow'], "外部数据：", nami_data['yellow_cards'])
                                    print("球员两黄一红：", "内部数据：", y['yellow2red_cards'], "外部数据：", nami_data['yellow2red_cards'])
                                    print("球员射门数：", "内部数据：", y['shot'], "外部数据：", nami_data['shots'])
                                    print("球员射正数：", "内部数据：", y['target_shot'], "外部数据：", nami_data['shots_on_target'])
                                    print("带球过人：", "内部数据：", y['dribble'], "外部数据：", nami_data['dribble'])
                                    print("带球过人成功数：", "内部数据：", y['dribble_success'], "外部数据：", nami_data['dribble_succ'])
                                    if y['dribble_success'] != 0 and y['dribble'] != 0:
                                        dribble_success_rate = y['dribble_success']/y['dribble']
                                    else:
                                        dribble_success_rate = 0
                                    print("过人成功率：", "内部数据：", y['dribble_success_rate'], "计算结果：", dribble_success_rate)  # 计算的
                                    print("球员有效进攻阻挡数：", "内部数据：", y['block'], "外部数据：", nami_data['blocked_shots'])
                                    print("球员解除危险球：", "内部数据：", y['clearance'], "外部数据：", nami_data['clearances'])
                                    print("球员抢断数：", "内部数据：", y['tackle'], "外部数据：", nami_data['tackles'])
                                    print("球员拦截数：", "内部数据：", y['interception'], "外部数据：", nami_data['interceptions'])
                                    print("球员传球数：", "内部数据：", y['pass'], "外部数据：", nami_data['passes'])
                                    print("球员传球成功数：", "内部数据：", y['pass_success'], "外部数据：", nami_data['passes_accuracy'])
                                    if y['pass_success'] != 0 and y['pass'] != 0:
                                        pass_success_rate = y['pass_success']/y['pass']
                                    else:
                                        pass_success_rate = 0
                                    print("球员传球成功率：", "内部数据：", y['pass_success_rate'], "计算结果：", pass_success_rate)  # 计算
                                    print("球员长传数：", "内部数据：", y['long_pass'], "外部数据：", nami_data['long_balls'])
                                    print("球员长传成功数：", "内部数据：", y['long_pass_success'], "外部数据：", nami_data['long_balls_accuracy'])
                                    if y['long_pass_success'] != 0 and y['long_pass'] != 0:
                                        long_pass_success_rate = y['long_pass_success']/y['long_pass']
                                    else:
                                        long_pass_success_rate = 0
                                    print("球员长传成功率：", "内部数据：", y['long_pass_success_rate'], "计算结果：",long_pass_success_rate)  # 计算
                                    print("球员传中球数：", "内部数据：", y['cross_pass'], "外部数据：", nami_data['crosses'])
                                    print("球员传中球成功数：", "内部数据：", y['cross_pass_success'], "外部数据：", nami_data['crosses_accuracy'])
                                    if y['cross_pass_success'] != 0 and y['cross_pass'] != 0:
                                        cross_pass_success_rate = y['cross_pass_success']/y['cross_pass']
                                    else:
                                        cross_pass_success_rate = 0
                                    print("球员传中球成功率：", "内部数据：", y['cross_pass_success_rate'], "计算结果：", cross_pass_success_rate)  # 计算
                                    print("球员关键传球数：", "内部数据：", y['key_pass'], "外部数据：", nami_data['key_passes'])
                                    print("球员失去球权数：", "内部数据：", y['loss_possession'], "外部数据：", nami_data['dispossessed'])
                                    print("球员拼抢次数：", "内部数据：", y['challenge'], "外部数据：", nami_data['duels'])
                                    print("球员拼抢成功数：", "内部数据：", y['challenge_success'], "外部数据：", nami_data['duels_won'])
                                    if y['challenge_success'] != 0 and y['challenge'] != 0:
                                        challenge_success_rate = y['challenge_success']/y['challenge']
                                    else:
                                        challenge_success_rate = 0
                                    print("球员拼抢成功率：", "内部数据：", y['challenge_success_rate'], "计算结果：", challenge_success_rate)  # 计算
                                    print("球员犯规数：", "内部数据：", y['foul'], "外部数据：", nami_data['fouls'])
                                    print("球员被犯规数：", "内部数据：", y['fouled'], "外部数据：", nami_data['was_fouled'])
                                    print("球员越位数：", "内部数据：", y['offside'], "外部数据：", nami_data['offsides'])
                                    print("守门员扑救数：", "内部数据：", y['save'], "外部数据：", nami_data['saves'])
                                    print("守门员拳击球数：", "内部数据：", y['fist_ball'], "外部数据：", nami_data['punches'])
                                    print("守门员出击数：", "内部数据：", y['run_out'], "外部数据：", nami_data['runs_out'])
                                    print("守门员出击成功数：", "内部数据：", y['run_out_success'], "外部数据：", nami_data['runs_out_succ'])
                                    if y['run_out_success'] != 0 and y['run_out'] != 0:
                                        run_out_success_rate = y['run_out_success']/y['run_out']
                                    else:
                                        run_out_success_rate = 0
                                    print("守门员出击成功率：", "内部数据：", y['run_out_success_rate'], "计算结果：", run_out_success_rate)  # 计算
                                    print("守门员高空出击数：", "内部数据：", y['high_claim'], "外部数据：", nami_data['good_high_claim'])
                                    print("----------------------------------------------------------"
                                          "-----------------------------------------------------------")





if __name__ == '__main__':
    b = FootballEvent(env_flag=0)
    b.message_handle(64244)
    # con = DoMySql().link_testsql()
    # storage_data(data, con)
    # storage_statistics(data, con)
    # storage_special_event(data, con)






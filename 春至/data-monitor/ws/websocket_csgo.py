import websocket
import threading
from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
import json
import ssl
import time
import datetime
import logging
# from common import desired_caps
from common import my_logger

illegal_str = ['Pong', 'Ping']

data = '{"id":"5f4dbba7a10b8a0001c18559","type":301,"game_id":1,"action_type":1,"create_time":1598929831,"payload":"{\"match_id\":11,\"series_id\":362,\"stage\":1,\"time\":774,\"team\":[{\"team_id\":334,\"gold\":20500,\"gold_min\":\"1589.00\",\"gold_diff\":-200,\"cs\":459,\"cs_min\":\"35.58\",\"cs_diff\":-10,\"kill\":1,\"assist\":2,\"death\":1,\"kda\":\"3.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":1,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0,\"player\":[{\"player_id\":617,\"level\":8,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":38},{\"summon_spell_id\":31}],\"cs\":133,\"cs_min\":\"10.31\",\"cs_diff\":12,\"kill\":0,\"assist\":0,\"death\":0,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":1,\"inhibitor_kill\":0},{\"player_id\":619,\"level\":8,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":25},{\"summon_spell_id\":31}],\"cs\":80,\"cs_min\":\"6.20\",\"cs_diff\":-17,\"kill\":0,\"assist\":1,\"death\":1,\"kda\":\"1.00\",\"neutral_kill\":2,\"herald_kill\":1,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":1,\"infernal_drake_kill\":0,\"mountain_drake_kill\":1,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":1,\"inhibitor_kill\":1},{\"player_id\":615,\"level\":10,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":34},{\"summon_spell_id\":38}],\"cs\":128,\"cs_min\":\"9.92\",\"cs_diff\":0,\"kill\":1,\"assist\":0,\"death\":0,\"kda\":\"1.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":1,\"inhibitor_kill\":0},{\"player_id\":616,\"level\":7,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":31},{\"summon_spell_id\":39}],\"cs\":19,\"cs_min\":\"1.47\",\"cs_diff\":2,\"kill\":0,\"assist\":0,\"death\":0,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0},{\"player_id\":618,\"level\":10,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":27},{\"summon_spell_id\":31}],\"cs\":99,\"cs_min\":\"7.67\",\"cs_diff\":-7,\"kill\":0,\"assist\":1,\"death\":0,\"kda\":\"1.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0}]},{\"team_id\":397,\"gold\":20700,\"gold_min\":\"1604.00\",\"gold_diff\":200,\"cs\":469,\"cs_min\":\"36.36\",\"cs_diff\":10,\"kill\":1,\"assist\":1,\"death\":1,\"kda\":\"2.00\",\"neutral_kill\":2,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":2,\"infernal_drake_kill\":0,\"mountain_drake_kill\":1,\"cloud_drake_kill\":1,\"ocean_drake_kill\":1,\"tower_kill\":0,\"inhibitor_kill\":0,\"player\":[{\"player_id\":624,\"level\":8,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":31},{\"summon_spell_id\":38}],\"cs\":121,\"cs_min\":\"9.38\",\"cs_diff\":-12,\"kill\":0,\"assist\":0,\"death\":0,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":1,\"inhibitor_kill\":0},{\"player_id\":625,\"level\":9,\"hp\":67,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":25},{\"summon_spell_id\":31}],\"cs\":97,\"cs_min\":\"7.52\",\"cs_diff\":17,\"kill\":1,\"assist\":0,\"death\":0,\"kda\":\"1.00\",\"neutral_kill\":4,\"herald_kill\":1,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":3,\"infernal_drake_kill\":0,\"mountain_drake_kill\":1,\"cloud_drake_kill\":1,\"ocean_drake_kill\":1,\"tower_kill\":0,\"inhibitor_kill\":0},{\"player_id\":631,\"level\":10,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":27},{\"summon_spell_id\":31}],\"cs\":128,\"cs_min\":\"9.92\",\"cs_diff\":0,\"kill\":0,\"assist\":1,\"death\":0,\"kda\":\"1.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0},{\"player_id\":627,\"level\":7,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":31},{\"summon_spell_id\":35}],\"cs\":17,\"cs_min\":\"1.32\",\"cs_diff\":-2,\"kill\":0,\"assist\":0,\"death\":0,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0},{\"player_id\":630,\"level\":9,\"hp\":77,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":27},{\"summon_spell_id\":31}],\"cs\":106,\"cs_min\":\"8.22\",\"cs_diff\":7,\"kill\":0,\"assist\":0,\"death\":1,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0}]}]}"}'

class ws_kog(object):

    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn, monGon_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.monGon = monGon_cnn
        self.doMysql = mysql_cnn
        self.hero_list = self.kog_hero()
        self.team_list = self.kog_team()
        self.player_list = self.kog_player()

    def get_heart(self, ws):
        try:
            while True:
                time.sleep(3)
                ws.send('2')
                # print("发送了心跳！")
        except:
            self.get_heart(ws)

    def message_handle(self, match_id, url):
        print(1111, url)
        # ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE}, http_proxy_host='8.210.99.228',
        #                                  http_proxy_port=59073)
        ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
        ws.send('1')  # 以字符串发送消息
        t = threading.Thread(target=self.get_heart, name="心跳线程", args=(ws,))  # 心跳线程
        t.setDaemon(True)  # 设置线程守护
        t.start()
        # try:
        #     # con = DoMySql().link_testsql()
        #
        # except Exception as e:
        #     print("link出错！！！", e)
        #     self.message_handle()
        try:
            while True:
                try:
                    mes = ws.recv()  # 接收消息，如果无消息将会堵塞,直到21s超时等待结束
                    # print("实时数据", mes)
                    data = self.my_data(mes)
                    if data not in illegal_str:
                        try:
                            res = eval(data)
                            payload = res['payload']
                            payload_a = json.loads(payload)
                            # if res['type'] == 301 and res['game_id'] == 3 and payload_a['match_id'] == match_id:
                            #     # print("实时数据", res)
                            #     # timeArray = time.localtime(res['create_time'])
                            #     # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                            #     # print(otherStyleTime)
                            #     teams = payload_a['team']
                            #     kill_a = teams[0]['kill']
                            #     kill_b = teams[1]['kill']
                            #     print(f'比分{kill_a}:{kill_b}')
                            #     # storage_data(data, con)
                            if res['type'] == 302 and res['game_id'] == 3 and payload_a['match_id'] == match_id:
                                print("实时统计", mes)
                                timeArray = time.localtime(res['create_time'])
                                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                                print("创建时间：", otherStyleTime)
                                # logging.info("创建时间：", otherStyleTime)
                                teams = payload_a['team']
                                kill_a = teams[0]['team_score']
                                kill_b = teams[1]['team_score']
                                print(f'比分{kill_a}:{kill_b}')
                                # logging.info(f'比分{kill_a}:{kill_b}')
                                # storage_statistics(data, con)
                            # if res['type'] == 203 and res['id'] == match_id:
                            #     print("小局信息", mes)
                            #     # storage_statistics(data, con)
                            # if res['type'] == 303 and res['game_id'] == 3 and payload_a['match_id'] == match_id:
                            #     print("实时事件", res)
                            #     self.kog_live_event(res)
                                # storage_event(data, con)
                            # if res['type'] == 304 and res['game_id'] == 3 and payload_a['match_id'] == match_id:
                            #     print("实时特殊事件", mes)
                                # storage_special_event(data, con)
                            # if res['type'] == 401 and res['game_id'] == 3 and payload_a['match_id'] == match_id:
                            #     print("赛果数据", mes)
                            #     # storage_special_event(data, con)
                            # if res['type'] == 402 and res['game_id'] == 3 and payload_a['match_id'] == match_id:
                            #     print("赛果事件", mes)
                            #     # storage_special_event(data, con)
                            # if res['type'] == 403 and res['game_id'] == 3 and payload_a['match_id'] == match_id:
                            #     print("赛果特殊事件", mes)
                            #     # storage_special_event(data, con)
                        except Exception as e:
                            print("数据存储操作出错：", e)
                            self.message_handle(match_id, url)
                except Exception as e:
                    print("出错！！！", e)
                    self.message_handle(match_id, url)
        except Exception as e:
            print("连接超时！！！！", e)
            self.message_handle(match_id, url)

    def kog_live_event(self, res):
        # print(res)
        hero_list = self.hero_list
        team_list = self.team_list
        player_list = self.player_list
        # event_datas = self.get_data(match_id=match_id, dataBase=self.mogonDB_dataBase, collection=self.mogonDB_collection_kog_event)
        data = json.loads(res['payload'])
        play_time = data["time"]
        event = data['event_data']
        event_type = data['type']
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

    def my_data(self, data):
        if data not in illegal_str:
            data = data.replace('payload":"{', 'payload":\'{')
            data = data.replace('}"}', '}\'}')
        return data

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
        team_value = ''
        kill_player_value = ''
        monster_value = ''
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

    def get_data(self, match_id, dataBase, collection):
        myDb = self.monGon
        collect1 = myDb.connect(dataBase, collection)
        sen = '{"match_id":' + str(match_id) + '}'
        result = myDb.select_data_all(collect1, sen)
        return result


if __name__ == '__main__':
    url = "wss://stream.dawnbyte.com/ws"  #  线上
    # url = "wss://stream.sportsapi.cn/ws"   # 测试
    mysql_cnn = DoMySql()
    monGon_cnn = MongoDB()
    cnn_centon = mysql_cnn.cnn_centon_def()
    cnn_basic = mysql_cnn.cnn_basic_def()
    a = ws_kog('release', cnn_centon, cnn_basic, mysql_cnn, monGon_cnn)
    a.message_handle(match_id=47001, url=url)
    # a.message_handle_1()

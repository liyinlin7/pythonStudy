import time
import websocket
import threading
import json
from common.do_mysql import DoMySql
import ssl

game_id = 3
data_type = 301
event_type = 303
# event_data = '{"id":"5f30e97c9e71cc0001da4ab9","type":303,"game_id":3,"action_type":1,"create_time":1597041020,"payload":"{\"match_id\":1233,\"series_id\":287,\"type\":7,\"event_data\":{\"stage\":2,\"round_num\":15,\"kill_team_id\":180,\"kill_player_id\":168,\"weapon_id\":505,\"has_headshot\":2,\"assist\":[],\"killed_team_id\":550,\"killed_player_id\":205}}"}'
# special_data = '{"id": "5f2a6cc48e269a0001e4636e", "type": 304, "game_id": 3, "action_type": 1, "create_time": 1596615876,"payload": {"match_id": 1,"series_id": 125632,"type": 10,"event_data": {"value": 1,"related_type": 1,"related_id":2}}}'
# special = '{"id": "5f2e7af19e71cc0001dc5bd9", "type": 304, "game_id": 3, "action_type": 1, "create_time": 1596881649, "payload": "{\"match_id\":1214,\"series_id\":278,\"type\":1,\"event_data\":{\"value\":1,\"related_type\":1,\"related_id\":554}}"}'
# result = '{"id":"5f30e5809e71cc000120def8","type":301,"game_id":3,"action_type":1,"create_time":1597040000,"payload":"{\"match_id\":1233,\"series_id\":287,\"round_num\":3,\"round_time\":50,\"team\":[{\"team_id\":550,\"round_kill\":2,\"kill\":11,\"round_headshot\":1,\"headshot\":364,\"round_death\":5,\"death\":13,\"round_assist\":1,\"assist\":3,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":0,\"entry_death\":0,\"one_win_multi\":0,\"multi_kill_rounds\":0,\"player\":[{\"player_id\":204,\"gold\":1800,\"hp\":0,\"item\":[],\"round_kill\":1,\"kill\":4,\"round_headshot\":0,\"headshot\":45,\"round_death\":1,\"death\":2,\"round_assist\":0,\"assist\":1,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":1,\"entry_death\":0,\"one_win_multi\":0,\"multi_kill_rounds\":1},{\"player_id\":206,\"gold\":1400,\"hp\":0,\"item\":[],\"round_kill\":0,\"kill\":4,\"round_headshot\":0,\"headshot\":57,\"round_death\":1,\"death\":2,\"round_assist\":1,\"assist\":1,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":0,\"entry_death\":0,\"one_win_multi\":0,\"multi_kill_rounds\":1},{\"player_id\":203,\"gold\":2500,\"hp\":0,\"item\":[],\"round_kill\":1,\"kill\":2,\"round_headshot\":1,\"headshot\":135,\"round_death\":1,\"death\":3,\"round_assist\":0,\"assist\":1,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":0,\"entry_death\":0,\"one_win_multi\":0,\"multi_kill_rounds\":0},{\"player_id\":202,\"gold\":1650,\"hp\":0,\"item\":[],\"round_kill\":0,\"kill\":1,\"round_headshot\":0,\"headshot\":70,\"round_death\":1,\"death\":3,\"round_assist\":0,\"assist\":0,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":0,\"entry_death\":1,\"one_win_multi\":0,\"multi_kill_rounds\":0},{\"player_id\":205,\"gold\":1950,\"hp\":0,\"item\":[],\"round_kill\":0,\"kill\":0,\"round_headshot\":0,\"headshot\":57,\"round_death\":1,\"death\":3,\"round_assist\":0,\"assist\":0,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":0,\"entry_death\":1,\"one_win_multi\":0,\"multi_kill_rounds\":0}]},{\"team_id\":180,\"round_kill\":5,\"kill\":13,\"round_headshot\":3,\"headshot\":141,\"round_death\":2,\"death\":11,\"round_assist\":1,\"assist\":2,\"round_flash_assist\":1,\"flash_assist\":1,\"entry_kill\":0,\"entry_death\":0,\"one_win_multi\":0,\"multi_kill_rounds\":0,\"player\":[{\"player_id\":167,\"gold\":3250,\"hp\":0,\"item\":[],\"round_kill\":0,\"kill\":5,\"round_headshot\":0,\"headshot\":0,\"round_death\":1,\"death\":2,\"round_assist\":1,\"assist\":1,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":2,\"entry_death\":1,\"one_win_multi\":1,\"multi_kill_rounds\":2},{\"player_id\":165,\"gold\":2850,\"hp\":3,\"item\":[494,500],\"round_kill\":2,\"kill\":4,\"round_headshot\":0,\"headshot\":0,\"round_death\":0,\"death\":2,\"round_assist\":0,\"assist\":0,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":0,\"entry_death\":0,\"one_win_multi\":0,\"multi_kill_rounds\":2},{\"player_id\":168,\"gold\":4250,\"hp\":98,\"item\":[494,505],\"round_kill\":3,\"kill\":3,\"round_headshot\":3,\"headshot\":55,\"round_death\":0,\"death\":2,\"round_assist\":0,\"assist\":1,\"round_flash_assist\":1,\"flash_assist\":1,\"entry_kill\":0,\"entry_death\":0,\"one_win_multi\":0,\"multi_kill_rounds\":1},{\"player_id\":169,\"gold\":3300,\"hp\":14,\"item\":[493,494,505],\"round_kill\":0,\"kill\":1,\"round_headshot\":0,\"headshot\":36,\"round_death\":0,\"death\":2,\"round_assist\":0,\"assist\":0,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":0,\"entry_death\":0,\"one_win_multi\":0,\"multi_kill_rounds\":0},{\"player_id\":166,\"gold\":3850,\"hp\":0,\"item\":[],\"round_kill\":0,\"kill\":0,\"round_headshot\":0,\"headshot\":50,\"round_death\":1,\"death\":3,\"round_assist\":0,\"assist\":0,\"round_flash_assist\":0,\"flash_assist\":0,\"entry_kill\":0,\"entry_death\":0,\"one_win_multi\":0,\"multi_kill_rounds\":0}]}]}"}'
data = '{"id":"5f312cde9e71cc0001af1b78","type":302,"game_id":3,"action_type":1,"create_time":1597058270,"payload":"{\"match_id\":1245,\"series_id\":291,\"round_num\":8,\"team\":[{\"team_id\":572,\"team_score\":[0,0,0,0],\"kpr\":\"0.00\",\"dpr\":\"0.00\",\"fk_diff\":\"0.00\",\"kd_diff\":\"0.00\",\"kd_ratio\":\"NaN\",\"adr\":\"0\",\"kast\":\"0\",\"player\":[{\"player_id\":343,\"kpr\":\"1.62\",\"dpr\":\"1.62\",\"fk_diff\":\"1.62\",\"kd_diff\":\"1.62\",\"kd_ratio\":\"1.00\",\"adr\":\"0\",\"kast\":\"0\"},{\"player_id\":345,\"kpr\":\"0.00\",\"dpr\":\"0.00\",\"fk_diff\":\"0.00\",\"kd_diff\":\"0.00\",\"kd_ratio\":\"NaN\",\"adr\":\"0\",\"kast\":\"0\"},{\"player_id\":347,\"kpr\":\"0.00\",\"dpr\":\"0.00\",\"fk_diff\":\"0.00\",\"kd_diff\":\"0.00\",\"kd_ratio\":\"NaN\",\"adr\":\"0\",\"kast\":\"0\"},{\"player_id\":346,\"kpr\":\"0.38\",\"dpr\":\"0.38\",\"fk_diff\":\"0.38\",\"kd_diff\":\"0.38\",\"kd_ratio\":\"1.00\",\"adr\":\"0\",\"kast\":\"0\"},{\"player_id\":344,\"kpr\":\"0.62\",\"dpr\":\"0.62\",\"fk_diff\":\"0.62\",\"kd_diff\":\"0.62\",\"kd_ratio\":\"1.00\",\"adr\":\"0\",\"kast\":\"0\"}]},{\"team_id\":571,\"team_score\":[0,0,0,0],\"kpr\":\"0.00\",\"dpr\":\"0.00\",\"fk_diff\":\"0.00\",\"kd_diff\":\"0.00\",\"kd_ratio\":\"NaN\",\"adr\":\"0\",\"kast\":\"0\",\"player\":[{\"player_id\":352,\"kpr\":\"0.38\",\"dpr\":\"0.38\",\"fk_diff\":\"0.38\",\"kd_diff\":\"0.38\",\"kd_ratio\":\"1.00\",\"adr\":\"0\",\"kast\":\"0\"},{\"player_id\":350,\"kpr\":\"0.00\",\"dpr\":\"0.00\",\"fk_diff\":\"0.00\",\"kd_diff\":\"0.00\",\"kd_ratio\":\"NaN\",\"adr\":\"0\",\"kast\":\"0\"},{\"player_id\":351,\"kpr\":\"0.25\",\"dpr\":\"0.25\",\"fk_diff\":\"0.25\",\"kd_diff\":\"0.25\",\"kd_ratio\":\"1.00\",\"adr\":\"0\",\"kast\":\"0\"},{\"player_id\":349,\"kpr\":\"0.00\",\"dpr\":\"0.00\",\"fk_diff\":\"0.00\",\"kd_diff\":\"0.00\",\"kd_ratio\":\"NaN\",\"adr\":\"0\",\"kast\":\"0\"},{\"player_id\":348,\"kpr\":\"0.00\",\"dpr\":\"0.00\",\"fk_diff\":\"0.00\",\"kd_diff\":\"0.00\",\"kd_ratio\":\"NaN\",\"adr\":\"0\",\"kast\":\"0\"}]}]}"}'


def cs_data(data):
    con = DoMySql().link_testsql()
    # data = my_data(data)
    # data = eval(data)
    # m_statistics(data, con)
    # m_statistics(data, con, 302)
    # m_event(event_data, con, 303)
    # m_event_special(data, con, 304)
    # 存储主表数据
    # do_csgo_data(data, con)
    # 存储系列赛表数据
    # do_series(data, con)
    # 存储队伍数据
    # do_series_team(data, con)
    # 存储队员数据
    # do_series_player(data, con)
    # 存储实时事件数据
    # m_data(data, con, 301)


def get_heart(ws):
    try:
        while True:
            time.sleep(3)
            ws.send('2')
            print("发送了心跳！")
    except:
        get_heart(ws)


# 获取实时数据
def message_handle():
    # url = "wss://stream.dawnbyte.com/ws"
    url = "wss://stream.sportsapi.cn/ws"
    print(1111, url)
    # ws = websocket.WebSocket()
    # 'ws://47.114.175.98:1325/ws'  测试
    # , http_proxy_host = '8.210.99.228', http_proxy_port = 59073
    # ws.connect(url, http_proxy_host='8.210.99.228', http_proxy_port=59073)
    # ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE}, http_proxy_host='8.210.99.228', http_proxy_port=59073)
    ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.send('1')  # 以字符串发送消息
    t = threading.Thread(target=get_heart, name="心跳线程", args=(ws,))  # 心跳线程
    t.setDaemon(True)  # 设置线程守护
    t.start()
    con = DoMySql().link_testsql()
    try:
        while True:
            try:
                mes = ws.recv()  # 接收消息，如果无消息将会堵塞,直到21s超时等待结束
                # print("实时数据", mes)
                # 处理第一层数据
                data = my_data(mes)
                if data != 'Pong':
                    data = eval(data)
                    # if data['type'] == 301:
                    #     # pass
                    #     # 实时数据
                    #     m_data(data, con)
                    if data['type'] == 302:
                        # pass
                        # 实时统计
                        print("实时统计：", data)
                        m_statistics(data, con)
                    # if data['type'] == 303:
                    #     print("实时数据", mes)
                    #     # pass
                    #     # 实时事件
                    #     m_event(data, con)
                    if data['type'] == 304:
                        # pass
                        # 实时特殊事件
                        print("实时特殊事件：", data)
                        m_event_special(data, con)
                    if data['type'] == 401:
                        # pass
                        # 实时统计
                        print("赛果：", mes)
                    if data['type'] == 402:
                        # pass
                        # 实时统计
                        print("赛果事件：", mes)
                    if data['type'] == 403:
                        # pass
                        # 实时统计
                        print("赛果特殊事件：", mes)
            except Exception as e:
                print("出错！！！", e)
                message_handle()
    except Exception as e:
        print("连接超时！！！！", e)
        message_handle()


# 实时统计
def m_statistics(data, con):
    if data['game_id'] == game_id:
        pay_data = data['payload']
        pay_data = eval(pay_data)
        match_id = pay_data['match_id']
        series_id = pay_data['series_id']
        round_num = pay_data['round_num']
        data_json = str(data)
        sql = "insert into `api-mega`.w_statistics(match_id, series_id, round_num, data_json) value (%s, %s, %s, %s)"
        try:
            cursor = con.cursor()
            cursor.execute(sql, (match_id, series_id, round_num, data_json))
            con.commit()
        except Exception as e:
            print('执行w_csgo_data表出错', e)


# 实时数据处理
def m_data(data, con):
    if data['game_id'] == game_id:
        # 存储主表数据
        do_csgo_data(data, con)
        # 存储系列赛表数据
        s_id = do_series(data, con)
        # 存储队伍数据
        do_series_team(data, con, s_id)
        # 存储队员数据
        do_series_player(data, con, s_id)


def do_csgo_data(data, con):
    json_data = str(data)
    data_id = data['id']
    type = data['type']
    game_id = data['game_id']
    action_type = data['action_type']
    create_time = data['create_time']
    sql = "insert into `api-mega`.w_csgo_data(data_id, type, game_id, action_type, create_time, json_data) " \
          "value (%s, %s, %s, %s, %s, %s)"
    try:
        cursor = con.cursor()
        cursor.execute(sql, (data_id, type, game_id, action_type, create_time, json_data))
        con.commit()
    except Exception as e:
        print('执行w_csgo_data表出错', e)


def do_series(data, con):
    data = data["payload"]
    data = json.loads(data)
    csgo_data = str(data)
    match_id = data['match_id']
    series_id = data['series_id']
    round_num = data['round_num']
    round_time = data['round_time']
    sql = "insert into `api-mega`.w_series(match_id, series_id, round_num, round_time, csgo_data) " \
          "value (%s, %s, %s, %s, %s)"
    try:
        cursor = con.cursor()
        cursor.execute(sql, (match_id, series_id, round_num, round_time, csgo_data))
        con.commit()
        return cursor.lastrowid
    except Exception as e:
        print('执行w_series表出错', e)


def do_series_team(data, con, s_id):
    data = data["payload"]
    data1 = json.loads(data)
    data2 = data1["team"]
    s_id = s_id
    for i in data2:
        team_id = i['team_id']
        round_kill = i['round_kill']
        t_kill = i['kill']
        round_headshot = i['round_headshot']
        headshot = i['headshot']
        round_death = i['round_death']
        death = i['death']
        round_assist = i['round_assist']
        assist = i['assist']
        round_flash_assist = i['round_flash_assist']
        flash_assist = i['flash_assist']
        entry_kill = i['entry_kill']
        entry_death = i['entry_death']
        one_win_multi = i['one_win_multi']
        multi_kill = i['multi_kill']
        # list = [s_id, team_id, round_kill, t_kill, round_headshot, headshot, round_death, death, round_assist, assist, round_flash_assist, flash_assist, entry_kill, entry_death, one_win_multi, multi_kill_rounds]
        # print(list)
        sql = "insert into `api-mega`.w_series_team(s_id, team_id, round_kill, t_kill, round_headshot, " \
              "headshot, round_death, death, round_assist, assist, round_flash_assist, flash_assist, " \
              "entry_kill, entry_death, one_win_multi, multi_kill) " \
              "value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor = con.cursor()
            cursor.execute(sql, (s_id, team_id, round_kill, t_kill, round_headshot, headshot, round_death, death,
                                 round_assist, assist, round_flash_assist, flash_assist, entry_kill, entry_death,
                                 one_win_multi, multi_kill))
            con.commit()
        except Exception as e:
            print('执行w_series_team表出错', e)


def do_series_player(data, con, s_id):
    data = data["payload"]
    data1 = json.loads(data)
    data2 = data1["team"]
    s_id = s_id
    for team in data2:
        team_id = team['team_id']
        for player in team["player"]:
            player_id = player['player_id']
            gold = player['gold']
            hp = player['hp']
            item = str(player['item'])
            round_kill = player['round_kill']
            p_kill = player['kill']
            round_headshot = player['round_headshot']
            headshot = player['headshot']
            round_death = player['round_death']
            death = player['death']
            round_assist = player['round_assist']
            assist = player['assist']
            round_flash_assist = player['round_flash_assist']
            flash_assist = player['flash_assist']
            entry_kill = player['entry_kill']
            entry_death = player['entry_death']
            one_win_multi = player['one_win_multi']
            multi_kill = player['multi_kill']
            # list = [s_id, team_id, player_id, gold, hp, item, round_kill, p_kill, round_headshot, headshot,round_death, death, round_assist, assist, round_flash_assist, flash_assist, entry_kill, entry_death, one_win_multi, multi_kill]
            # print(list)
            sql = "insert into `api-mega`.w_series_player(s_id, team_id, player_id, gold, hp, item, round_kill, p_kill, round_headshot, headshot, round_death, death, round_assist, assist, round_flash_assist, flash_assist, entry_kill, entry_death, one_win_multi, multi_kill)" \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            try:
                cursor = con.cursor()
                cursor.execute(sql, (
                    s_id, team_id, player_id, gold, hp, item, round_kill, p_kill, round_headshot, headshot, round_death,
                    death, round_assist, assist, round_flash_assist, flash_assist, entry_kill, entry_death,
                    one_win_multi,
                    multi_kill))
                con.commit()
            except Exception as e:
                print('执行w_series_player表出错', e)


# 实时事件处理
def m_event(data, con):
    if data['game_id'] == game_id:
            # 获取第一层推送数据
            key_list = list(data.keys())
            value_list = list(data.values())
            key_list.pop()
            value_list.pop()
            # 获取比赛推送数据
            payload_data = data['payload']
            payload_data = eval(payload_data)
            pay_key_list = list(payload_data.keys())
            num = pay_key_list.index('type')
            pay_key_list[num] = 'e_type'
            pay_value_list = list(payload_data.values())
            pay_key_list.pop()
            pay_value_list.pop()
            all_list = insert_data(key_list, value_list, pay_key_list, pay_value_list)
            key_list = all_list[0]
            value_list = all_list[1]
            # 获取事件推送数据
            event_data = payload_data['event_data']
            event_key_list = list(event_data.keys())
            event_value_list = list(event_data.values())
            all_list = insert_data(key_list, value_list, event_key_list, event_value_list)
            key_list = all_list[0]
            value_list = all_list[1]
            if 'assist' in key_list:
                index = key_list.index('assist')
                value_list[index] = str(value_list[index])
            keys = tuple(key_list)
            val = tuple(value_list)
            sql = "INSERT INTO `api-mega`.{} {} VALUES {}".format('w_event', str(keys).replace("'", ''), val)
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()


# 实时特殊事件处理
def m_event_special(data, con):
    if data['game_id'] == game_id:
            # 获取第一层推送数据
            key_list = list(data.keys())
            value_list = list(data.values())
            key_list.pop()
            value_list.pop()
            # 获取比赛推送数据
            payload_data = data['payload']
            payload_data = eval(payload_data)
            pay_key_list = list(payload_data.keys())
            num = pay_key_list.index('type')
            pay_key_list[num] = 'e_type'
            pay_value_list = list(payload_data.values())
            pay_key_list.pop()
            pay_value_list.pop()
            all_list = insert_data(key_list, value_list, pay_key_list, pay_value_list)
            key_list = all_list[0]
            value_list = all_list[1]
            # 获取事件推送数据
            event_data = payload_data['event_data']
            event_key_list = list(event_data.keys())
            num = event_key_list.index('value')
            event_key_list[num] = 'e_value'
            event_value_list = list(event_data.values())
            all_list = insert_data(key_list, value_list, event_key_list, event_value_list)
            key_list = all_list[0]
            value_list = all_list[1]
            keys = tuple(key_list)
            val = tuple(value_list)
            sql = "INSERT INTO `api-mega`.{} {} VALUES {}".format('w_event_special', str(keys).replace("'", ''), val)
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()


# 列表处理数据
def insert_data(key_list, value_list, n_key_list, n_value_list):
    list = []
    for i in n_key_list:
        key_list.append(i)
    list.append(key_list)
    for i in n_value_list:
        value_list.append(i)
    list.append(value_list)
    return list


def my_data(data):
    if data != 'Pong':
        data = data.replace('payload":"{', 'payload":\'{')
        data = data.replace('}"}', '}\'}')
    return data


if __name__ == '__main__':
    message_handle()
    # cs_data(data)

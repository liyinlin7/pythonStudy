import time
import websocket
import threading
import json
from common.do_mysql import DoMySql
import ssl

illegal_str = ['Pong', 'Ping']

data = '{"id":"5f4dbba7a10b8a0001c18559","type":301,"game_id":1,"action_type":1,"create_time":1598929831,"payload":"{\"match_id\":11,\"series_id\":362,\"stage\":1,\"time\":774,\"team\":[{\"team_id\":334,\"gold\":20500,\"gold_min\":\"1589.00\",\"gold_diff\":-200,\"cs\":459,\"cs_min\":\"35.58\",\"cs_diff\":-10,\"kill\":1,\"assist\":2,\"death\":1,\"kda\":\"3.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":1,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0,\"player\":[{\"player_id\":617,\"level\":8,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":38},{\"summon_spell_id\":31}],\"cs\":133,\"cs_min\":\"10.31\",\"cs_diff\":12,\"kill\":0,\"assist\":0,\"death\":0,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":1,\"inhibitor_kill\":0},{\"player_id\":619,\"level\":8,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":25},{\"summon_spell_id\":31}],\"cs\":80,\"cs_min\":\"6.20\",\"cs_diff\":-17,\"kill\":0,\"assist\":1,\"death\":1,\"kda\":\"1.00\",\"neutral_kill\":2,\"herald_kill\":1,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":1,\"infernal_drake_kill\":0,\"mountain_drake_kill\":1,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":1,\"inhibitor_kill\":1},{\"player_id\":615,\"level\":10,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":34},{\"summon_spell_id\":38}],\"cs\":128,\"cs_min\":\"9.92\",\"cs_diff\":0,\"kill\":1,\"assist\":0,\"death\":0,\"kda\":\"1.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":1,\"inhibitor_kill\":0},{\"player_id\":616,\"level\":7,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":31},{\"summon_spell_id\":39}],\"cs\":19,\"cs_min\":\"1.47\",\"cs_diff\":2,\"kill\":0,\"assist\":0,\"death\":0,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0},{\"player_id\":618,\"level\":10,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":27},{\"summon_spell_id\":31}],\"cs\":99,\"cs_min\":\"7.67\",\"cs_diff\":-7,\"kill\":0,\"assist\":1,\"death\":0,\"kda\":\"1.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0}]},{\"team_id\":397,\"gold\":20700,\"gold_min\":\"1604.00\",\"gold_diff\":200,\"cs\":469,\"cs_min\":\"36.36\",\"cs_diff\":10,\"kill\":1,\"assist\":1,\"death\":1,\"kda\":\"2.00\",\"neutral_kill\":2,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":2,\"infernal_drake_kill\":0,\"mountain_drake_kill\":1,\"cloud_drake_kill\":1,\"ocean_drake_kill\":1,\"tower_kill\":0,\"inhibitor_kill\":0,\"player\":[{\"player_id\":624,\"level\":8,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":31},{\"summon_spell_id\":38}],\"cs\":121,\"cs_min\":\"9.38\",\"cs_diff\":-12,\"kill\":0,\"assist\":0,\"death\":0,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":1,\"inhibitor_kill\":0},{\"player_id\":625,\"level\":9,\"hp\":67,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":25},{\"summon_spell_id\":31}],\"cs\":97,\"cs_min\":\"7.52\",\"cs_diff\":17,\"kill\":1,\"assist\":0,\"death\":0,\"kda\":\"1.00\",\"neutral_kill\":4,\"herald_kill\":1,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":3,\"infernal_drake_kill\":0,\"mountain_drake_kill\":1,\"cloud_drake_kill\":1,\"ocean_drake_kill\":1,\"tower_kill\":0,\"inhibitor_kill\":0},{\"player_id\":631,\"level\":10,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":27},{\"summon_spell_id\":31}],\"cs\":128,\"cs_min\":\"9.92\",\"cs_diff\":0,\"kill\":0,\"assist\":1,\"death\":0,\"kda\":\"1.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0},{\"player_id\":627,\"level\":7,\"hp\":100,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":31},{\"summon_spell_id\":35}],\"cs\":17,\"cs_min\":\"1.32\",\"cs_diff\":-2,\"kill\":0,\"assist\":0,\"death\":0,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0},{\"player_id\":630,\"level\":9,\"hp\":77,\"status\":2,\"respawn_time\":0,\"item\":[],\"spell\":[{\"summon_spell_id\":27},{\"summon_spell_id\":31}],\"cs\":106,\"cs_min\":\"8.22\",\"cs_diff\":7,\"kill\":0,\"assist\":0,\"death\":1,\"kda\":\"0.00\",\"neutral_kill\":0,\"herald_kill\":0,\"nashor_kill\":0,\"elder_drake_kill\":0,\"drake_kill\":0,\"infernal_drake_kill\":0,\"mountain_drake_kill\":0,\"cloud_drake_kill\":0,\"ocean_drake_kill\":0,\"tower_kill\":0,\"inhibitor_kill\":0}]}]}"}'

def get_heart(ws):
    try:
        while True:
            time.sleep(3)
            ws.send('2')
            print("发送了心跳！")
    except:
        get_heart(ws)


def message_handle():
    # url = "wss://stream.dawnbyte.com/ws"
    url = "ws://47.114.175.98:1325/ws"
    print(1111, url)
    # ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE}, http_proxy_host='8.210.99.228',
    #                                  http_proxy_port=59073)
    ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.send('1')  # 以字符串发送消息
    t = threading.Thread(target=get_heart, name="心跳线程", args=(ws,))  # 心跳线程
    t.setDaemon(True)  # 设置线程守护
    t.start()
    try:
        con = DoMySql().link_testsql()
    except Exception as e:
        print("link出错！！！", e)
        message_handle()
    try:
        while True:
            try:
                mes = ws.recv()  # 接收消息，如果无消息将会堵塞,直到21s超时等待结束
                print("实时数据", mes)
                data = my_data(mes)
                if data not in illegal_str:
                    try:
                        res = eval(data)
                        if res['type'] == 301 and res['game_id'] == 1:
                            print("实时数据", mes)
                            storage_data(data, con)
                        if res['type'] == 302 and res['game_id'] == 1:
                            print("实时统计", mes)
                            storage_statistics(data, con)
                        if res['type'] == 303 and res['game_id'] == 1:
                            print("实时事件", mes)
                            storage_event(data, con)
                        if res['type'] == 304 and res['game_id'] == 1:
                            print("实时特殊事件", mes)
                            storage_special_event(data, con)
                    except Exception as e:
                        print("数据存储操作出错：", e)
                        message_handle()
            except Exception as e:
                print("出错！！！", e)
                message_handle()
    except Exception as e:
        print("连接超时！！！！", e)
        message_handle()


def my_data(data):
    if data not in illegal_str:
        data = data.replace('payload":"{', 'payload":\'{')
        data = data.replace('}"}', '}\'}')
    return data


def storage_data(data, con):
    data = my_data(data)
    data = eval(data)
    # data表
    sql = DoMySql().insert_sql('w_lol_data', data, replace_key=[{"old_key": "id", "new_key": "data_id"}],
                               extra_key=['payload'])
    # print('data表', sql)
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    # series
    s_data = data['payload']
    es_data = eval(s_data)
    match_id = es_data['match_id']
    series_id = es_data['series_id']
    sql = DoMySql().insert_sql('w_lol_series', s_data, extra_key=['team'])
    s_id = DoMySql().insert(con, sql)
    # cursor.execute(sql)
    # con.commit()

    # team
    s_data = eval(s_data)
    t_data = s_data['team']
    for item in t_data:
        sql = DoMySql().insert_sql('w_lol_team', item, extra_key=['player'],
                                   add_dic={"s_id": s_id, "match_id": match_id, "series_id": series_id},
                                   replace_key=[{'old_key': 'kill', 'new_key': 'team_kill'}])
        cursor.execute(sql)
        con.commit()

    # player
    for t_item in t_data:
        p_data = t_item['player']
        team_id = t_item['team_id']
        for p_item in p_data:
            sql = DoMySql().insert_sql('w_lol_player', p_item,
                                       str_key=['item', 'spell'],
                                       add_dic={"s_id": s_id, "team_id": team_id, "match_id": match_id,
                                                "series_id": series_id},
                                       replace_key=[{'old_key': 'kill', 'new_key': 'p_kill'},
                                                    {'old_key': 'level', 'new_key': 'p_level'}])
            cursor.execute(sql)
            con.commit()


def storage_statistics(data, con):
    data = my_data(data)
    data = eval(data)
    # data表
    sql = DoMySql().insert_sql('w_lol_statistics', data, replace_key=[{"old_key": "id", "new_key": "data_id"}],
                               extra_key=['payload'])
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    # series
    s_data = data['payload']
    es_data = eval(s_data)
    match_id = es_data['match_id']
    series_id = es_data['series_id']
    sql = DoMySql().insert_sql('w_lol_statistics_series', s_data, extra_key=['team'])
    s_id = DoMySql().insert(con, sql)
    cursor.execute(sql)
    con.commit()

    # team
    s_data = json.loads(s_data)
    t_data = s_data['team']
    for item in t_data:
        sql = DoMySql().insert_sql('w_lol_statistics_team', item, extra_key=['player'],
                                   replace_key=[{"old_key": "double", "new_key": "double_kill"}],
                                   add_dic={"s_id": s_id, "match_id": match_id, "series_id": series_id})
        cursor.execute(sql)
        con.commit()

    # player
    for t_item in t_data:
        p_data = t_item['player']
        team_id = t_item['team_id']
        for p_item in p_data:
            sql = DoMySql().insert_sql('w_lol_statistics_player', p_item,
                                       replace_key=[{"old_key": "double", "new_key": "double_kill"}],
                                       add_dic={"s_id": s_id, "team_id": team_id, "match_id": match_id,
                                                "series_id": series_id})
            cursor.execute(sql)
            con.commit()


def storage_event(data, con):
    data = my_data(data)
    data = eval(data)
    data = data['payload']
    sql = DoMySql().insert_sql('w_lol_event', data, str_key=['event_data'])
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()


def storage_special_event(data, con):
    data = my_data(data)
    data = eval(data)
    data = data['payload']
    data = eval(data)
    event_data = data['event_data']
    sql = DoMySql().insert_sql('w_lol_special_event', data, extra_key=['event_data'],
                               add_dic={"s_value": event_data['value'], "related_type": event_data['related_type'],
                                        "related_id": event_data['related_id']})
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()


if __name__ == '__main__':
    message_handle()
    # con = DoMySql().link_testsql()
    # storage_data(data, con)
    # storage_statistics(data, con)
    # storage_special_event(data, con)

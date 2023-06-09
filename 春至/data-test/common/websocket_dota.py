import time
import websocket
import threading
import json
from common.do_mysql import DoMySql
import ssl

illegal_str = ['Pong', 'Ping']


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
    ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE}, http_proxy_host='8.210.99.228',
                                     http_proxy_port=59073)
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
                # print("实时数据", mes)
                data = my_data(mes)
                if data not in illegal_str:
                    try:
                        res = eval(data)
                        if res['type'] == 301 and res['game_id'] == 2:
                            print("实时数据", mes)
                            storage_data(data, con)
                        if res['type'] == 302 and res['game_id'] == 2:
                            print("实时统计", mes)
                            storage_statistics(data, con)
                        if res['type'] == 303 and res['game_id'] == 2:
                            print("实时事件", mes)
                            storage_event(data, con)
                        if res['type'] == 304 and res['game_id'] == 2:
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
    sql = DoMySql().insert_sql('w_dota_data', data, replace_key=[{"old_key": "id", "new_key": "data_id"}],
                               extra_key=['payload'])
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    # series
    s_data = data['payload']
    es_data = eval(s_data)
    match_id = es_data['match_id']
    series_id = es_data['series_id']
    sql = DoMySql().insert_sql('w_dota_series', s_data, extra_key=['team'])
    s_id = DoMySql().insert(con, sql)
    # cursor.execute(sql)
    # con.commit()

    # team
    s_data = eval(s_data)
    t_data = s_data['team']
    for item in t_data:
        sql = DoMySql().insert_sql('w_dota_team', item, extra_key=['player'],
                                   add_dic={"s_id": s_id, "match_id": match_id, "series_id": series_id},
                                   replace_key=[{'old_key': 'kill', 'new_key': 't_kill'}],
                                   str_key=['tower_location', 'barrack_location'])
        cursor.execute(sql)
        con.commit()

    # player
    for t_item in t_data:
        p_data = t_item['player']
        team_id = t_item['team_id']
        for p_item in p_data:
            sql = DoMySql().insert_sql('w_dota_player', p_item,
                                       str_key=['item'],
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
    sql = DoMySql().insert_sql('w_dota_statistics', data, replace_key=[{"old_key": "id", "new_key": "data_id"}],
                               extra_key=['payload'])
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    # series
    s_data = data['payload']
    es_data = eval(s_data)
    match_id = es_data['match_id']
    series_id = es_data['series_id']
    sql = DoMySql().insert_sql('w_dota_statistics_series', s_data, extra_key=['team'])
    s_id = DoMySql().insert(con, sql)
    cursor.execute(sql)
    con.commit()

    # team
    s_data = json.loads(s_data)
    t_data = s_data['team']
    for item in t_data:
        sql = DoMySql().insert_sql('w_dota_statistics_team', item, extra_key=['player'],
                                   replace_key=[{"old_key": "double", "new_key": "double_kill"}],
                                   add_dic={"s_id": s_id, "match_id": match_id, "series_id": series_id})
        cursor.execute(sql)
        con.commit()

    # player
    for t_item in t_data:
        p_data = t_item['player']
        team_id = t_item['team_id']
        for p_item in p_data:
            sql = DoMySql().insert_sql('w_dota_statistics_player', p_item,
                                       replace_key=[{"old_key": "double", "new_key": "double_kill"}],
                                       add_dic={"s_id": s_id, "team_id": team_id, "match_id": match_id,
                                                "series_id": series_id})
            cursor.execute(sql)
            con.commit()


def storage_event(data, con):
    data = my_data(data)
    data = eval(data)
    data = data['payload']
    sql = DoMySql().insert_sql('w_dota_event', data, str_key=['event_data'])
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()


def storage_special_event(data, con):
    data = my_data(data)
    data = eval(data)
    data = data['payload']
    data = eval(data)
    event_data = data['event_data']
    sql = DoMySql().insert_sql('w_dota_special_event', data, extra_key=['event_data'],
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

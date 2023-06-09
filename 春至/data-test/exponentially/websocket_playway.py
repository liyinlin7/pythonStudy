import time
import websocket
import threading
import json
from common.do_mysql import DoMySql
import ssl
import logging

illegal_str = ['Pong', 'Ping']
data = '{"id":"5fb6140e95343100016b13b6","type":601,"create_time":1605768206,"payload":"{\"id\":1,\"market_status\":4,\"rate\":1,\"is_winner\":3,\"option\":[{\"option_id\":2338},{\"option_id\":2338}],\"value_data\":[{\"index\":2338,\"value\":2,\"is_winner\":4,\"player\":[]},{\"team_id\":2342,\"side\":1,\"is_winner\":2,\"player\":[]}]}"}'


def get_heart(ws):
    try:
        while True:
            time.sleep(3)
            ws.send('2')
            print("发送了心跳！")
    except:
        get_heart(ws)


def message_handle():
    url = "wss://stream.dawnbyte.com/ws"
    # url = "ws://47.114.175.98:1325/ws"
    # print(1111, url)
    # ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE}, http_proxy_host='8.210.99.228',
    #                                  http_proxy_port=59073)
    ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.send('1')  # 以字符串发送消息
    t = threading.Thread(target=get_heart, name="心跳线程", args=(ws,))  # 心跳线程
    t.setDaemon(True)  # 设置线程守护
    t.start()
    # cnn = DoMySql().connect(env_flag=0)
    try:
        while True:
            try:
                mes = ws.recv()  # 接收消息，如果无消息将会堵塞,直到21s超时等待结束
                # print("实时数据", mes)
                data = my_data(mes)
                if data not in illegal_str:
                    try:
                        res = eval(data)
                        if res['type'] == 602 and res['action_type'] == 2:
                            # print("实时指数数据：" + str(data))
                            # logging.info("实时指数数据：" + str(data))
                            # install_message_602(data, cnn)
                            print_message_602(data)
                        # if res['type'] == 601:
                        #     print("页面数据推送：", str(data))
                        #     # logging.info("实时指数数据：", str(data))
                        #     install_message_601(data, cnn)
                    except Exception as e:
                        print("数据存储操作出错：", e)
                        message_handle()
            except Exception as e:
                print("出错！！！", e)
                message_handle()
    except Exception as e:
        print("连接超时！！！！", e)
        message_handle()


def print_message_602(data):
    '''
        存储实时指数数据
    :param data:
    :param cnn:
    :return:
    '''
    data = my_data(data)
    data = eval(data)
    payload = json.loads(data['payload'])
    # print(payload)
    true_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['create_time']))
    for i in payload['option']:
        if i.get('option_id') in (972650,972652,972655,972656):
            print(data)
            print("收到的时间：：" + str(true_time))
            print("创建时间：：" + str(create_time))
            logging.info(data)
            logging.info("收到的时间：：" + str(true_time))
            logging.info("创建时间：：" + str(create_time))
            print("--------------------------------------------------------------------------------------------------")
    # cursor = cnn.cursor()
    # cursor.execute(sql)
    # cnn.commit()

def my_data(data):
    if data not in illegal_str:
        data = data.replace('payload":"{', 'payload":\'{')
        data = data.replace('}"}', '}\'}')
    return data

# def install_message_602(data, cnn):
#     '''
#         存储实时指数数据
#     :param data:
#     :param cnn:
#     :return:
#     '''
#     data = my_data(data)
#     data = eval(data)
#     payload = json.loads(data['payload'])
#     # print(data['create_time'])
#     true_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     # create_time = time.gmtime(data['create_time'])
#     create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['create_time']))
#     # print(true_time)
#     # print(create_time)
#     if data.get('type') is None:
#         type = 'Null'
#     else:
#         type = data['type']
#     if data.get('game_id') is None:
#         game_id = 'Null'
#     else:
#         game_id = data['game_id']
#     if data.get('action_type') is None:
#         action_type = 'Null'
#     else:
#         action_type = data['action_type']
#     if payload.get('id') is None:
#         id = 'Null'
#     else:
#         id = payload['id']
#     if payload.get('market_status') is None:
#         market_status = 'Null'
#     else:
#         market_status = payload['market_status']
#     if payload.get('value_data') is None:
#         value_data = 'Null'
#     else:
#         value_data = payload['value_data']
#     for i in payload['Option']:
#         if i.get('option_id') is None:
#             option_id = 'Null'
#         else:
#             option_id = i['option_id']
#         if i.get('rate') is None:
#             rate = 'Null'
#         else:
#             rate = i['rate']
#         if i.get('is_winner') is None:
#             is_winner = 'Null'
#         else:
#             is_winner = i['is_winner']
#         if i.get('option_status') is None:
#             option_status = 'Null'
#         else:
#             option_status = i['option_status']
#         # sql = 'INSERT INTO  `api-mega`.ws_playway values ({},\"{}\",\"{}\",{},{},{},{},\"{}\",{},{},\"{}\",{},{},{},{},{})'.format(type, true_time, create_time, action_type, game_id, id,
#         #                                                                                                             market_status, option_id, rate, is_winner, value_data, 'Null', 'Null', 'Null', 'Null', 'Null')
#         sql = 'INSERT INTO  `api-mega`.ws_playway values ({},{},\"{}\",\"{}\",{},{},{},{},\"{}\",{},{},{},\"{}\",{},{},{},\"{}\",{},{},{},{},\"{}\",\"{}\",\"{}\",{})'.format(0,
#             type, true_time, create_time, action_type, game_id, id,
#             market_status, option_id, rate, option_status, is_winner, value_data,  'Null', 'Null', 'Null', 'Null',
#             'Null', 'Null',
#             'Null', 'Null', 'Null', 'Null', 'Null', 'Null')
#         # data表
#         # print(sql)
#         sql.encode('utf8')
#         str = DoMySql().insert(cnn, sql)
#         print(str)
#     # cursor = cnn.cursor()
#     # cursor.execute(sql)
#     # cnn.commit()
#
# def install_message_601(data, cnn):
#     '''
#         存储实时指数数据
#     :param data:
#     :param cnn:
#     :return:
#     '''
#     data = my_data(data)
#     data = eval(data)
#     payload = json.loads(data['payload'])
#     # print(data['create_time'])
#     true_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     # create_time = time.gmtime(data['create_time'])
#     create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['create_time']))
#     # print(true_time)
#     # print(create_time)
#     if data.get('type') is None:
#         type = 'Null'
#     else:
#         type = data['type']
#     if data.get('game_id') is None:
#         game_id = 'Null'
#     else:
#         game_id = data['game_id']
#     if data.get('action_type') is None:
#         action_type = 'Null'
#     else:
#         action_type = data['action_type']
#     if payload.get('id') is None:
#         id = 'Null'
#     else:
#         id = payload['id']
#     if payload.get('market_status') is None:
#         market_status = 'Null'
#     else:
#         market_status = payload['market_status']
#     if payload.get('value_data') is None:
#         value_data = 'Null'
#     else:
#         value_data = payload['value_data']
#
#     if payload.get('market_type_id') is None:
#         market_type_id= 'Null'
#     else:
#         market_type_id = payload['market_type_id']
#     if payload.get('level') is None:
#         level= 'Null'
#     else:
#         level = payload['level']
#     if payload.get('level_id') is None:
#         level_id= 'Null'
#     else:
#         level_id = payload['level_id']
#     if payload.get('market_name') is None:
#         market_name= 'Null'
#     else:
#         market_name = payload['market_name']
#     if payload.get('game_id') is None:
#         market_game_id = 'Null'
#     else:
#         market_game_id = payload['game_id']
#     market_data = payload['market_data']
#     for k in market_data:
#         market_status_601 = k.get('market_status')
#         is_inplay = k.get('is_inplay')
#         for i in k.get('option_data'):
#             if i.get('option_id') is None:
#                 option_id = 'Null'
#             else:
#                 option_id = i['option_id']
#             if i.get('rate') is None:
#                 rate = 'Null'
#             else:
#                 rate = i['rate']
#             if i.get('is_winner') is None:
#                 is_winner = 'Null'
#             else:
#                 is_winner = i['is_winner']
#             if i.get('option_status') is None:
#                 option_status = 'Null'
#             else:
#                 option_status = i['option_status']
#             if i.get('option_name'):
#                 for y in i['option_name']:
#                     if y.get('name_type') is None:
#                         name_type = 'Null'
#                     else:
#                         name_type = y['name_type']
#                     if y.get('name_en') is None:
#                         name_en = 'Null'
#                     else:
#                         name_en = y['name_en']
#                     if y.get('name_zh') is None:
#                         name_zh = 'Null'
#                     else:
#                         name_zh = y['name_zh']
#                     if y.get('name_value') is None:
#                         name_value = 'Null'
#                     else:
#                         name_value = y['name_value']
#                     if y.get('name_id') is None:
#                         name_id = 'Null'
#                     else:
#                         name_id = y['name_id']
#                 sql = 'INSERT INTO  `api-mega`.ws_playway values ({},{},\"{}\",\"{}\",{},{},{},{},\"{}\",{},{},{},\"{}\",{},{},{},\"{}\",{},{},{},{},\"{}\",\"{}\",\"{}\",{})'.format(0,
#                     type, true_time, create_time, action_type, game_id, id,
#                     market_status, option_id, rate, option_status ,is_winner, value_data, market_type_id, level, level_id, market_name, market_game_id, is_inplay,
#                     market_status_601, name_type, name_en, name_zh, name_value, name_id)
#                 # data表
#                 # print(sql)
#                 sql.encode('utf8')
#                 str = DoMySql().insert(cnn, sql)
#                 print(str)
#     # cursor = cnn.cursor()
#     # cursor.execute(sql)
#     # cnn.commit()


if __name__ == '__main__':
    # cnn = DoMySql().connect(env_flag=0)
    message_handle()
    # data = '{"id":"5fc0e3bb99bdaf00014e3db2","type":601,"game_id":3,"action_type":1,"create_time":1606476731,"payload":"{\"id\":9304,\"market_type_id\":64,\"game_id\":3,\"level\":3,\"level_id\":652,\"market_name\":[{\"name_type\":1,\"name_en\":\"\",\"name_zh\":\"回合获胜总数单双\",\"name_value\":\"\",\"name_id\":0}],\"market_data\":[{\"bookmarker\":1,\"market_status\":1,\"is_inplay\":1,\"option_data\":[{\"option_id\":13852,\"rate\":\"1.80\",\"is_winner\":0,\"option_status\":1,\"option_name\":[{\"name_type\":1,\"name_en\":\"\",\"name_zh\":\"双数\",\"name_value\":\"\",\"name_id\":0}]},{\"option_id\":13853,\"rate\":\"2.01\",\"is_winner\":0,\"option_status\":1,\"option_name\":[{\"name_type\":1,\"name_en\":\"\",\"name_zh\":\"单数\",\"name_value\":\"\",\"name_id\":0}]}]}]}"}'
    # data = '''
    #     {"id":"601129b190762a00012f06d6","type":602,"game_id":1,"action_type":2,"create_time":1611737521,"payload":"{\"id\":565188,\"source\":1,\"market_status\":1,\"option\":[{\"option_id\":966779,\"rate\":\"2.11\",\"option_status\":1,\"is_winner\":1}]}"}
    # '''
    # print_message_602(data)
    # install_message_601(data, cnn)
    # my_data(data)
    # message_handle()
    # con = DoMySql().link_testsql()
    # storage_data(data, con)
    # storage_statistics(data, con)
    # storage_special_event(data, con)

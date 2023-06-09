import time
import websocket
import threading
import json
from common.do_mysql import DoMySql
import ssl
import logging

env_flag = 0
illegal_str = ['Pong', 'Ping']
data = ''


def get_heart(ws):
    try:
        while True:
            time.sleep(1)
            ws.send('5')
            print("发送了心跳！")
    except:
        get_heart(ws)


def message_handle():
    url = "wss://soccer_stream.dawnbyte.com/ws"
    # url = "wss://soccer_stream.sportsapi.cn/ws"   # 测试WS
    print(1111, url)
    # ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE}, http_proxy_host='8.210.99.228',
    #                                  http_proxy_port=59073)
    ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.send('1')  # 以字符串发送消息
    t = threading.Thread(target=get_heart, name="心跳线程", args=(ws,))  # 心跳线程
    t.setDaemon(True)  # 设置线程守护
    t.start()
    cnn = DoMySql().connect(env_flag=env_flag)
    try:
        while True:
            try:
                mes = ws.recv()  # 接收消息，如果无消息将会堵塞,直到21s超时等待结束
                # print("实时数据", mes)
                data = my_data(mes)
                if data not in illegal_str:
                    print(data)
                    logging.info(data)
                    try:
                        res = eval(data)
                        if res['type'] == 301 and res['game_id'] == 1:
                            # print("实时指数数据：" + str(data))
                            # logging.info("实时指数数据：" + str(data))
                            print("301")
                            install_message_301(data, cnn)
                        # elif res['type'] == 303 and res['game_id'] == 1:
                        #     print("实时指数数据：" + str(data))
                        #     # logging.info("实时指数数据：" + str(data))
                        #     print("303")
                            # install_message_303(data, cnn)
                        # elif res['type'] == 304 and res['game_id'] == 1:
                        #     # print("实时指数数据：" + str(data))
                        #     # logging.info("实时指数数据：" + str(data))
                        #     print("304")
                        #     # print(res)
                            # install_message_304(data, cnn)
                        # elif res['type'] == 401 and res['game_id'] == 1:
                        #     # print("实时指数数据：" + str(data))
                        #     # logging.info("实时指数数据：" + str(data))
                        #     print("401")
                        #     print(res)
                            # install_message_401(data, cnn)
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


def install_message_301(data, cnn):
    '''
        存储实时足球数据
    :param data:
    :param cnn:
    :return:
    '''
    data1 = my_data(data)
    data2 = eval(data1)
    payload = json.loads(data2['payload'])
    action_type = data2['action_type']
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(payload['create_time']))
    match_id = payload['match_id']
    time_ = payload['time']
    teams = payload['team']
    for i in teams:
        team_id = i['team_id']
        is_kick_off = i['is_kick_off']
        score = i['score']
        penalty_kick = i['penalty_kick']
        own_goal = i['own_goal']
        assist = i['assist']
        shot = i['shot']
        target_shot = i['target_shot']
        post_shot = i['post_shot']
        free_kick = i['free_kick']
        throw_in = i['throw_in']
        header = i['header']
        corner = i['corner']
        substitute = i['substitute']
        foul = i['foul']
        red = i['red']
        yellow = i['yellow']
        offside = i['offside']
        possession = i['possession']
        attack = i['attack']
        dangerous_attack = i['dangerous_attack']
        pass_ = i['pass']
        pass_success_rate = i['pass_success_rate']
        long_pass = i['long_pass']
        short_pass = i['short_pass']
        tackle = i['tackle']
        slide = i['slide']
        block = i['block']
        steal = i['steal']
        if i['player'] is None:
            sql = f'''
                      INSERT INTO  `api-mega`.w_football_data (action_type,create_time,match_id, `time`,team_id,
                      is_kick_off,score,penalty_kick,own_goal,assist,shot,target_shot,post_shot,free_kick,throw_in,
                     header,corner,substitute,foul,red,yellow,offside, possession, attack,dangerous_attack,pass,
                     pass_success_rate,long_pass,short_pass,tackle,slide,block,steal) values ({action_type}, '{create_time}', 
                        {match_id},{time_},{team_id}, {is_kick_off}, '{score}',
                        {penalty_kick}, {own_goal},{assist}, {shot}, {target_shot}, 
                        {post_shot}, {free_kick},{throw_in}, {header}, {corner}, 
                        {substitute}, {foul}, {red},{yellow}, {offside},'{possession}',{attack},{dangerous_attack},{pass_},
                        '{pass_success_rate}',{long_pass},{short_pass},{tackle},{slide},{block},{steal});
                        '''
            str = DoMySql().insert(cnn, sql)
            print(str)
        else:
            for i in i['player']:
                player_id = i['id']
                player_is_starting = i['is_starting']
                player_score = i['score']
                player_penalty_kick = i['penalty_kick']
                player_penalty_goal = i['penalty_goal']
                player_own_goal = i['own_goal']
                player_assist = i['assist']
                player_red = i['red']
                player_yellow = i['yellow']
                sql = f'''
                          INSERT INTO  `api-mega`.w_football_data (action_type,create_time,match_id, `time`,team_id,
                      is_kick_off,score,penalty_kick,own_goal,assist,shot,target_shot,post_shot,free_kick,throw_in,
                     header,corner,substitute,foul,red,yellow,offside, possession, attack,dangerous_attack,pass,
                     pass_success_rate,long_pass,short_pass,tackle,slide,block,steal,player_id,player_is_starting,
                     player_score,player_penalty_kick,player_penalty_goal,player_own_goal,player_assist,
                     player_red,player_yellow) values ({action_type}, '{create_time}', 
                        {match_id},{time_},{team_id}, {is_kick_off}, '{score}',
                        {penalty_kick}, {own_goal},{assist}, {shot}, {target_shot}, 
                        {post_shot}, {free_kick},{throw_in}, {header}, {corner}, 
                        {substitute}, {foul}, {red},{yellow}, {offside},'{possession}',{attack},{dangerous_attack},{pass_},
                        '{pass_success_rate}',{long_pass},{short_pass},{tackle},{slide},{block},{steal},{player_id}, 
                        {player_is_starting},'{player_score}', {player_penalty_kick}, {player_penalty_goal},
                        {player_own_goal}, {player_assist}, {player_red}, {player_yellow});
                                        '''
                str = DoMySql().insert(cnn, sql)
                print(str)

def install_message_303(data3, cnn):
    '''
        存储实时足球数据
    :param data:
    :param cnn:
    :return:
    '''
    data1 = my_data(data3)
    data2 = eval(data1)
    payload = json.loads(data2['payload'])
    action_type = data2['action_type']
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data2['create_time']))
    match_id = payload['match_id']
    event_id = payload['id']
    event_time = payload['time']
    event_type = payload['type']
    data = payload['data']
    sql = ''
    if event_type == 1 or event_type == 2:
        stage = data['stage']
        type_ = data['type']
        sql = f'''
              INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id ,match_id, event_type, event_time, stage, type) 
                  values ({action_type}, '{create_time}',{event_id}, {match_id}, {event_type}, {event_time},{int(stage)}, {int(type_)});
        '''
    elif event_type == 3:
        team_id = data['team_id']
        player_id = data['player_id']
        assist_player_id = data['assist_player_id']
        sql = f'''
                      INSERT INTO  `api-mega`.w_football_event (action_type, create_time,event_id,match_id, event_type, event_time, team_id, player_id, assist_player_id) 
                  values ({action_type}, '{create_time}', {event_id},{match_id}, {event_type}, {event_time},{team_id},{player_id}, {assist_player_id});
                '''
    elif event_type == 4:
        team_id = data['team_id']
        player_id = data['player_id']
        is_goal = data['is_goal']
        sql = f'''
                  INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id,match_id, event_type, event_time, team_id, player_id, is_goal) 
                  values ({action_type}, '{create_time}', {event_id},{match_id}, {event_type}, {event_time},{team_id},{player_id}, {is_goal});
                '''
    elif event_type == 5:
        team_id = data['team_id']
        player_id = data['player_id']
        sql = f'''
              INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id,match_id, event_type, event_time, team_id, player_id) 
                  values ({action_type}, '{create_time}',{event_id}, {match_id}, {event_type}, {event_time},{team_id},{player_id});
            '''
    elif event_type == 6:
        team_id = data['team_id']
        player_id = data['player_id']
        is_target = data['is_target']
        sql = f'''
                  INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id,match_id, event_type, event_time, team_id, player_id, is_target) 
                  values ({action_type}, '{create_time}',  {event_id},{match_id}, {event_type}, {event_time},{team_id},{player_id}, {is_target});
                '''
    elif event_type == 7:
        team_id = data['team_id']
        player_id = data['player_id']
        sql = f'''
              INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id,match_id, event_type, event_time, team_id, player_id, is_target) 
                  values ({action_type}, '{create_time}', {event_id},{match_id}, {event_type}, {event_time},{team_id},{player_id});
            '''
    elif event_type == 8:
        team_id = data['team_id']
        player_id = data['player_id']
        is_yellow = data['is_yellow']
        sql = f'''
              INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id,match_id, event_type, event_time, team_id, player_id, is_yellow) 
                  values ({action_type}, '{create_time}', {event_id},{match_id}, {event_type}, {event_time},{team_id},{player_id}, {is_yellow});
            '''
    elif event_type == 9:
        team_id = data['team_id']
        player_id = data['player_id']
        sql = f'''
              INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id,match_id, event_type, event_time, team_id, player_id) 
                  values ({action_type}, '{create_time}', {event_id},{match_id}, {event_type}, {event_time},{team_id},{player_id});
            '''
    elif event_type == 10:
        team_id = data['team_id']
        player_id = data['player_id']
        sql = f'''
             INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id,match_id, event_type, event_time, team_id, player_id) 
                  values ({action_type}, '{create_time}', {event_id},{match_id}, {event_type}, {event_time},{team_id},{player_id});
            '''
    elif event_type == 11:
        team_id = data['team_id']
        player_id = data['player_id']
        sql = f'''
              INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id,match_id, event_type, event_time, team_id, player_id) 
                  values ({action_type}, '{create_time}', {event_id},{match_id}, {event_type}, {event_time},{team_id},{player_id});
            '''
    elif event_type == 12:
        team_id = data['team_id']
        player_id = data['player_id']
        sub_player_id = data['sub_player_id']
        sql = f'''
              INSERT INTO  `api-mega`.w_football_event (action_type, create_time, event_id,match_id, event_type, event_time, team_id, player_id, sub_player_id) 
                  values ({action_type}, '{create_time}', {event_id},{match_id}, {event_type}, {event_time},{team_id},{player_id}, {sub_player_id});
            '''
    else:
        logging.info(f"实时事件错误：{data3}")
    if sql == '':
        pass
    else:
        print(sql)
        str = DoMySql().insert(cnn, sql)
        print(str)

def install_message_304(data3, cnn):
    '''
        存储实时足球数据
    :param data:
    :param cnn:
    :return:
    '''
    data1 = my_data(data3)
    data2 = eval(data1)
    payload = json.loads(data2['payload'])
    action_type = data2['action_type']
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data2['create_time']))
    id = payload['id']
    match_id = payload['match_id']
    time_ = payload['time']
    type_ = payload['type']
    data = payload['data']
    data_value = data['value']
    data_related_type = data['related_type']
    data_related_id = data['related_id']
    sql = f'''
              INSERT INTO  `api-mega`.w_football_event_special (action_type,create_time, id_, match_id,`time`,`type`, `value`,
              related_type,related_id) values ({action_type},'{create_time}',{id},{match_id}, {time_},{type_},  {data_value}, {data_related_type}, {data_related_id});
                '''
    str = DoMySql().insert(cnn, sql)
    print(str)

def install_message_401(data3, cnn):
    '''
        存储实时足球数据
    :param data:
    :param cnn:
    :return:
    '''
    data1 = my_data(data3)
    data2 = eval(data1)
    payload = json.loads(data2['payload'])
    try:
        action_type = data2['action_type']
    except Exception:
        action_type = -1
    # create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(payload['time']))
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    match_id = payload['match_id']
    data = payload['data']
    teams = data['team']
    for i in teams:
        team_id = i['team_id']
        is_kick_off = i['is_kick_off']
        score = i['score']
        penalty_kick = i['penalty_kick']
        penalty_goal = i['penalty_goal']
        own_goal = i['own_goal']
        assist = i['assist']
        shot = i['shot']
        target_shot = i['target_shot']
        post_shot = i['post_shot']
        free_kick = i['free_kick']
        throw_in = i['throw_in']
        header = i['header']
        corner = i['corner']
        substitute = i['substitute']
        foul = i['foul']
        red = i['red']
        yellow = i['yellow']
        offside = i['offside']
        possession = i['possession']
        attack = i['attack']
        dangerous_attack = i['dangerous_attack']
        pass_ = i['pass']
        square_pass = i['square_pass']
        long_pass = i['long_pass']
        turnover = i['turnover']
        short_pass = i['short_pass']
        through_pass = i['through_pass']
        key_pass = i['key_pass']
        pass_success = i['pass_success']
        pass_success_rate = i['pass_success_rate']
        break_ = i['break']
        tackle = i['tackle']
        slide = i['slide']
        block = i['block']
        clear = i['clear']
        team_turnover = i['turnover']
        team_sql = f'''
                  INSERT INTO  `api-mega`.w_football_result_team (action_type,create_time,match_id,team_id,
                  is_kick_off,score,penalty_kick,penalty_goal,own_goal,assist,shot,target_shot,post_shot,free_kick,throw_in,
                 header,corner,substitute,foul,red,yellow,offside, possession,attack,dangerous_attack,pass,square_pass,
                 long_pass,turnover,short_pass,through_pass,key_pass,pass_success,pass_success_rate,break,tackle,
                 slide,block,clear,team_turnover) values ({action_type}, '{create_time}', {match_id},{team_id}, 
                {is_kick_off}, '{score}',{penalty_kick}, {penalty_goal},{own_goal},{assist}, {shot}, {target_shot}, 
                    {post_shot}, {free_kick},{throw_in}, {header}, {corner}, 
                    {substitute}, {foul}, {red},{yellow}, {offside}, {possession}, {attack},{dangerous_attack},
                    {pass_},{square_pass},{long_pass},{turnover},{short_pass},{through_pass},{key_pass},{pass_success},
                    {pass_success_rate},{break_},{tackle},{slide},{block},{clear},{team_turnover});
                    '''
        team_str = DoMySql().insert(cnn, team_sql)
        print(team_str)
        players = i['player']
        if players is None:
            pass
        else:
            for k in players:
                player_id = k['id']
                player_is_kick_off = k['is_kick_off']
                player_score = k['score']
                player_penalty_kick = k['penalty_kick']
                player_penalty_goal = k['penalty_goal']
                player_own_goal = k['own_goal']
                player_assist = k['assist']
                player_shot = k['shot']
                player_target_shot = k['target_shot']
                player_post_shot = k['post_shot']
                player_foul = k['foul']
                player_offside = k['offside']
                player_offside_create = k['offside_create']
                player_fouled = k['fouled']
                player_red = k['red']
                player_yellow = k['yellow']
                player_duration = k['duration']
                player_pass = k['pass']
                player_square_pass = k['square_pass']
                player_long_pass = k['long_pass']
                player_through_pass = k['through_pass']
                player_key_pass = k['key_pass']
                player_pass_success = k['pass_success']
                player_pass_success_rate = k['pass_success_rate']
                player_break = k['break']
                player_dispossession = k['dispossession']
                player_turnover = k['turnover']
                player_tackle = k['tackle']
                player_slide = k['slide']
                player_block = k['block']
                player_clear = k['clear']
                player_sql = f'''
                  INSERT INTO  `api-mega`.w_football_result_player (action_type,create_time,match_id, team_id,player_id
                  is_kick_off,score,penalty_kick,penalty_goal,own_goal,assist,shot,target_shot,post_shot,free_kick,throw_in,
                 header,corner,substitute,foul,red,yellow,offside, possession,attack,dangerous_attack,pass,square_pass,
                 long_pass,turnover,short_pass,through_pass,key_pass,pass_success,pass_success_rate,break,tackle,
                 slide,block,clear,team_turnover) values ({action_type}, '{create_time}', {match_id},{team_id}, {player_id},
                {player_is_kick_off}, '{player_score}',{player_penalty_kick}, {player_penalty_goal},{player_own_goal},
                {player_assist}, {player_shot}, {player_target_shot}, {player_post_shot}, {free_kick},{player_foul}, 
                {player_offside}, {player_offside_create}, {player_fouled}, {player_red},{player_yellow},
                {player_duration}, {player_pass}, {player_square_pass},{player_long_pass},{player_through_pass},
                {player_key_pass},{player_pass_success},{player_pass_success_rate},{player_break},
                {player_dispossession},{player_turnover},{player_tackle},{player_slide},{player_block},{player_clear});
                    '''
                str_player = DoMySql().insert(cnn, player_sql)
                print(str_player)


if __name__ == '__main__':
    cnn = DoMySql().connect(env_flag=0)
    message_handle()


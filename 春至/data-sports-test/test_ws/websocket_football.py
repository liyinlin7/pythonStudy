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
            # print("发送了心跳！")
    except:
        get_heart(ws)

def my_data(data):
    if data not in illegal_str:
        data = data.replace('payload":"{', 'payload":\'{')
        data = data.replace('}"}', '}\'}')
    return data


def message_handle():
    url = "wss://sports.sportsapi.cn/soccer-stream/ws"   # 测试
    # url = "wss://sports.dawnbyte.com/soccer-stream/ws"   # 线上
    # url = "wss://sports.dawnbyte.com/rate-stream/ws"   # 指数线上
    # url = "wss://sports.sportsapi.cn/rate-stream/ws"   # 指数测试
    print(1111, url)
    ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.send('1')  # 以字符串发送消息
    t = threading.Thread(target=get_heart, name="心跳线程", args=(ws,))  # 心跳线程
    t.setDaemon(True)  # 设置线程守护
    t.start()
    # try:
    #     con = DoMySql().link_testsql()
    # except Exception as e:
    #     print("link出错！！！", e)
    #     message_handle()
    try:
        while True:
            try:
                mes = ws.recv()  # 接收消息，如果无消息将会堵塞,直到21s超时等待结束
                # print("实时数据", mes)
                data = my_data(mes)
                if data not in illegal_str:
                    try:
                        res = json.loads(mes)
                        payload = res['payload']
                        payload_a = json.loads(payload)
                        # print(res2)
                        # if res['type'] == 203:
                        #     print("赛季推送203", str(mes))
                        if res['type'] == 303 and payload_a['match_id'] == 400015998:
                        # if res['type'] == 303:
                            print("视频推送303", str(mes))
                        # if res['type'] == 304:
                        #     print("视频推送304", str(mes))
                        # if res['type'] == 402:
                        #     print("视频推送402", str(mes))
                        # if res['type'] == 501:
                        #     print("视频推送501", str(mes))
                        # if res['type'] == 502 and payload_a['match_id'] == 14625:
                        #     print("弹幕推流502", str(mes))
                        # if res['type'] == 601:
                        #     print("指数详情601", str(mes))
                        # if res['type'] == 602:
                        #     print("指数实时602", str(mes))
                        # if res['type'] == 701:
                        #     print("体彩701", str(mes))
                        # if res['type'] == 702:
                        #     print("体彩702", str(mes))
                        # if res['type'] == 801:
                        #     print("百家赔801", str(mes))
                        # if res['type'] == 802:
                        #     print("百家赔802", str(mes))
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


if __name__ == '__main__':
    message_handle()
    # con = DoMySql().link_testsql()
    # storage_data(data, con)
    # storage_statistics(data, con)
    # storage_special_event(data, con)

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
            # print("发送了心跳！")
    except:
        get_heart(ws)


def my_data(data):
    if data not in illegal_str:
        data = data.replace('payload":"{', 'payload":\'{')
        data = data.replace('}"}', '}\'}')
    return data


def message_handle():
    url = "wss://sports.sportsapi.cn/basketball-stream/ws"   # 测试
    # url = "wss://sports.dawnbyte.com/basketball-stream/ws"   # 正式
    print(1111, url)
    ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.send('1')  # 以字符串发送消息
    t = threading.Thread(target=get_heart, name="心跳线程", args=(ws,))  # 心跳线程
    t.setDaemon(True)  # 设置线程守护
    t.start()
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
                        # if res['type'] == 201:
                        #     print("联赛推送201", str(mes))
                        # if res['type'] == 202:
                        #     print("比赛推送202", str(mes))
                        # if res['type'] == 203:
                        #     print("联赛积分203", str(mes))
                        # if res['type'] == 301:
                        #     print("视频推送301", str(mes))
                        if res['type'] == 303 and payload_a['match_id'] == 6420:  # 2674 and payload_a['match_id'] == 2674
                            print("实时数据303", str(mes))
                        # if res['type'] == 304:
                        #     print("视频推送304", str(mes))
                        # if res['type'] == 402:
                        #     print("视频推送402", str(mes))
                        # if res['type'] == 501:
                        #     print("视频推送501", str(mes))
                        # if res['type'] == 502:
                        #     print("弹幕推流502", str(mes))
                        # if res['type'] == 601:
                        #     print("指数实时602", str(mes))
                        # if res['type'] == 602:
                        #     print("指数实时602", str(mes))
                    except Exception as e:
                        print("数据存储操作出错：", e)
                        message_handle()
            except Exception as e:
                print("出错！！！", e)
                message_handle()
    except Exception as e:
        print("连接超时！！！！", e)
        message_handle()


if __name__ == '__main__':
    message_handle()
    # con = DoMySql().link_testsql()
    # storage_data(data, con)
    # storage_statistics(data, con)
    # storage_special_event(data, con)






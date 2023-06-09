import time
import websocket
import threading
import json
import ssl
import datetime
from common import my_logger
import logging

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
    url = "wss://stream.dawnbyte.com/ws"  # 线上
    # url = "wss://stream.sportsapi.cn/ws"   # 测试
    print(1111, url)
    ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.send('1')  # 以字符串发送消息
    t = threading.Thread(target=get_heart, name="心跳线程", args=(ws,))  # 心跳线程
    t.setDaemon(True)  # 设置线程守护
    t.start()
    try:
        while True:
            try:
                mes = ws.recv()
                # print("实时数据", mes)
                data = my_data(mes)
                if data not in illegal_str:
                    try:
                        res = eval(data)
                        if res['type'] in (301, 302, 401, 402, 601, 602):
                            now_time = int(time.time())
                            su_time = res['create_time']
                            cha = now_time - int(su_time)
                            # logging.error(f"实时数据{mes}")
                            # logging.error(f'时间差-----：{cha}')
                            if cha > 1:
                                logging.error(f"实时数据{mes}")
                                logging.error(f'时间差-----：{cha}')
                                print("实时数据", mes)
                                print('时间差-----：', cha)
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

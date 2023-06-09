"""赛果事件"""

import time
import pymongo
from common.http_request import HttpRequest
from common.do_sign import DoSign
from common.deal_with_data import DealWithData


def get_event_data(match_id, db_name):
    """获取赛果事件"""
    # 生产环境
    # conn = pymongo.MongoClient(
    #     'mongodb://{}:{}@{}:{}/?authSource={}'.format("root", "123456", "47.56.193.4", "27017", "data-event"))

    # 测试环境
    conn = pymongo.MongoClient(
        'mongodb://{}:{}@{}:{}/?authSource={}'.format("root", "123456", "121.196.189.137", "27017", "data-event"))
    db = conn['data-live-center']
    collection = db[db_name]
    res1 = collection.find({"match_id": match_id})
    res_li = []
    for i in res1:
        del i['_id']
        res_li.append(i)
    return res_li


def deal_event(data):
    """处理赛事事件格式"""
    res = {
        'match_id': data[0]['match_id'],
        'series_id': data[0]['series_id'],
        'game_id': data[0]['game_id'],
        'event': []
    }
    for i in data:
        for n in i['event_data']:
            data1 = {
                'create_time': n['time_stamp'],
                'type': n['type'],
                'event_data': n['data']
            }
            res['event'].append(data1)
    res['event'] = DealWithData().sort_li(res['event'], 'create_time')
    return res


def deal_special_event(data):
    """处理特殊事件格式"""
    res = {
        'match_id': data[0]['match_id'] if data else 0,
        'series_id': data[0]['series_id'] if data else 0,
        'game_id': 3,
        'special_event': []
    }
    for i in data:
        for n in i['special_event']:
            data1 = {
                'create_time': i['create_time'],
                'type': n['type'],
                'event_data': n['data']
            }
            res['special_event'].append(data1)
    return res


def compare_data(url, param, data):
    """对比数据"""
    cookies = {}
    header = {'Sign': DoSign().get_sign(param)}
    http_data = HttpRequest().http_request(url, param, 'get', cookies, header).json()['result']
    http_data['event'] = DealWithData().sort_li(http_data['event'], 'create_time')
    for i in range(len(http_data['event'])):
        if http_data['event'][i]['event_data'] == data['event'][i]['event_data']:
            continue
        else:
            print('接口  数据：{}'.format(http_data['event'][i]))
            print('数据库数据：{}'.format(data['event'][i]))
            continue
    # return http_data['result'] == data


if __name__ == '__main__':

    # 赛事事件
    event_data = deal_event(get_event_data(1301, 'csgo_live_event'))
    # 特殊事件
    # event_data_special = deal_special_event(get_event_data(1211, 'csgo_live_event_special'))

    # 接口数据-赛事事件
    # cookies = {}
    url = 'http://47.114.175.98:8080/api/result/event/csgo'
    param = {'game_id': 3, 'match_id': 1301, 'event_type': 0, 'limit': 300, 'offset': 0, 'time_stamp': int(time.time())}
    # header = {'Sign': DoSign().get_sign(param)}
    # res = HttpRequest().http_request(url, param, 'get', cookies, header).json()
    print('赛事事件对比结果:', compare_data(url, param, event_data))
    # print(event_data)

    # 接口数据-特殊事件
    # cookies = {}
    url2 = 'http://47.114.175.98:8080/api/result/event/special/csgo'
    param2 = {'game_id': 3, 'match_id': 1211, 'event_type': 0, 'limit': 100, 'offset': 0, 'time_stamp': int(time.time())}
    # header = {'Sign': DoSign().get_sign(param)}
    # res = HttpRequest().http_request(url, param, 'get', cookies, header).json()
    # print('特殊事件对比结果:', compare_data(url2, param2, event_data_special))
    # print(event_data_special)

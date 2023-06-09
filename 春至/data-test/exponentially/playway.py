import requests
from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
import time, datetime
import logging,json


class PlayWay(object):
    '''
        玩法
    '''
    def data_unix(self, datatime):
        '''
            日期格式转换为Unix_time时间格式
        :return:
        '''
        # match_time = '2018-05-22 08:30:00'
        match_time = datatime
        ans_time_stamp = time.mktime(time.strptime(match_time, "%Y-%m-%d %H:%M:%S"))
        return int(ans_time_stamp)

    def unix_time(self):
        '''
        :return: 当前Unix_time时间
        '''
        unix_time = time.time()
        return int(unix_time)

    def play_way_details(self, status=0, game_id=None, level_id=None, level=None, begin_id=None, begin_time=None, limit=None):
        '''
            指数详情的数据
        :return:
        '''
        if status == 0:
            url = "http://47.114.175.98:8080"
            headers = {"token": "N75LPxLbvGQjnGvKvdCHUbkgSyP7u6FpfLu2mzfNyxfumxPfxd"}
        else:
            url = "https://openapi.dawnbyte.com"
            headers = {"token": "zCYIP4ADbtgZmmP04wQvMI9AKTJx5fPnHUQZtL7eIEjIBHzB76"}
        base_url = url+f'/api/markets/details?time_stamp={self.unix_time()}&game_id={game_id}'
        if level_id != None:
            base_url += f'&level_id={level_id}'
        if level != None:
            base_url += f'&level={level}'
        if begin_id != None:
            base_url += f'&begin_id={begin_id}'
        if begin_time != None:
            base_url += f'&begin_time={begin_time}'
        if limit != None:
            base_url += f'&limit={limit}'
        data = requests.get(base_url, headers=headers)
        result = data.json().get('result')
        # print(result)
        self.play_way_details_market_name(result)
        self.play_way_details_market_data(result)

    def play_way_details_market_name(self, data):
        '''
            数据拆分 market_name
        :return:
        '''
        # print(data)
        for i in data:
            logging.info('\n'*2)
            # print('id:', i['id'])
            # print('market_type_id:', i['market_type_id'])
            # print('level_id:', i['level_id'])
            # print('level:', i['level'])
            logging.info('\nid:' + str(i['id']) + '\n' + \
                         'market_type_id:' + str(i['market_type_id'])  + '\n' + \
                         'game_id:' + str(i['game_id']) + '\n' + \
                         'level_id:' + str(i['level_id']) + '\n' + \
                         'level:' + str(i['level']))
            en_str = ''
            zh_str = ''
            for y in i['market_name']:
                # print('y', y)
                if y['name_type'] == 1:
                    # if y['name_en'] != '':
                    #     en_str += y['name_en']
                    if y['name_zh'] != None:
                        zh_str += ' '*4 + y['name_zh']
                elif y['name_type'] == 2:
                    en_str += ' '*4 + y['name_value']
                    zh_str += ' '*4 + y['name_value']
                else:
                    if y['name_id'] is int:
                        en_str += ' '*4 + str(y['name_id'])
                        zh_str += ' '*4 + str(y['name_id'])
                    else:
                        print("name_type为3,4,5,6时，返回参数不为ID：", y['name_id'])
            # print(en_str + '\n' + zh_str)
            logging.info('\n' + "英文：" + en_str + '\n' + "中文：" + zh_str)



    def play_way_details_market_data(self, data):
        '''
            数据拆分 market_data
        :return:
        '''
        for i in data:
            # print(i)
            logging.info('\n'*2)
            for y in i['market_data']:
                # print(y)
                # print('bookmarker:', y['bookmarker'])
                # print('market_status:', y['market_status'])
                # print('is_inplay:', y['is_inplay'])
                logging.info('\nbookmarker:' +  str(y['bookmarker']) + '\n' + \
                            'market_status:' +  str(y['market_status']) + '\n' + \
                            'is_inplay:' + str(y['is_inplay']) + \
                            'level_id:' + str(y['level_id']) + '\n' + \
                            'level:' + str(y['level'])
                             )
                for z in y['option_data']:
                    # print('option_id:', z['option_id'])
                    # print('rate:', z['rate'])
                    # print('is_winner:', z['is_winner'])
                    logging.info('\noption_id:' +  str(z['option_id']) + '\n' + \
                                 'rate:' +  str(z['rate']) + '\n' + \
                                 'is_winner:' +  str(z['is_winner'])
                                 )
                    en_str = ''
                    zh_str = ''
                    for h in z['option_name']:
                        if h['name_type'] == 1:
                            if h['name_en'] != None:
                                en_str += h['name_en']
                            if h['name_zh'] != None:
                                zh_str += ' ' * 4 + h['name_zh']
                        elif h['name_type'] == 2:
                            en_str += ' ' * 4 + h['name_value']
                            zh_str += ' ' * 4 + h['name_value']
                        else:
                            if isinstance(h['name_id'],int):
                                en_str += ' ' * 4 + str(h['name_id'])
                                zh_str += ' ' * 4 + str(h['name_id'])
                            else:
                                print(type(h['name_id']))
                                print("name_type为3,4,5,6时，返回参数不为ID：", h['name_id'])
                    # print( '\n' + en_str + '\n' + zh_str)
                    logging.info('\n' + "英文：" + en_str + '\n' + "中文：" + zh_str)


if __name__ == '__main__':
    play = PlayWay()
    play.play_way_details(status=0, game_id=3, level_id=None, level=None, begin_id=None, begin_time=None, limit=10)

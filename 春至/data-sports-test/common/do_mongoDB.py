import pymongo
from common.read_config import ReadConfig
from common import read_path
import logging
import common.my_logger


class MongoDB(object):

    def __init__(self, env_flag):
        self.env_flag = env_flag

    def sport_connect(self, dataBase, collection):
        try:
            if self.env_flag == 0:
                # client = pymongo.MongoClient(host='47.110.84.47', port=13297,
                #                              username='soccer', password='UwJiAEuO9yB1YUoR',
                #                              authSource='sports-soccer')  # 连接测试mongo
                myclient = f"mongodb://root:cPjeplgWRGnoaYAD@172.16.0.16:13286/"      # 内网IP地址
                # myclient = f"mongodb://root:cPjeplgWRGnoaYAD@42.194.216.189:13286/"    # 公网IP地址
                print(myclient)
                client = pymongo.MongoClient(myclient)
            elif self.env_flag == 1:
                # myclient = f"mongodb://test:cPjeplgWRGnoaYAD@47.242.128.177:13286/"
                # print(myclient)
                # client = pymongo.MongoClient(host='47.242.128.177', port=13286,
                #                              username='test', password='cPjeplgWRGnoaYAD',
                #                              authSource='admin')  # 连接生产mongo
                # myclient = f"mongodb://test:cPjeplgWRGnoaYAD@47.57.231.50:13238/"       # 公网IP地址
                myclient = f"mongodb://test:cPjeplgWRGnoaYAD@172.16.0.119:13286/"       # 内网IP地址
                print(myclient)
                client = pymongo.MongoClient(myclient)
            db = client[dataBase]  # 连接数据库
            collection = db[collection]  # 连接集合
            return collection
        except Exception as e:
            print(f"体育MongoDB链接失败：{e}")

    def sport_connect_basketball(self, dataBase, collection):
        try:
            if self.env_flag == 0:
                # client = pymongo.MongoClient(host='47.110.84.47', port=13297,
                #                              username='soccer', password='UwJiAEuO9yB1YUoR',
                #                              authSource='sports-soccer')  # 连接测试mongo
                myclient = f"mongodb://test:cPjeplgWRGnoaYAD@47.57.231.50:13238/"  # 公网IP地址
                # myclient = f"mongodb://test:cPjeplgWRGnoaYAD@172.16.0.119:13286/"       # 内网IP地址
                print(myclient)
                client = pymongo.MongoClient(myclient)
            elif self.env_flag == 1:
                # myclient = f"mongodb://test:cPjeplgWRGnoaYAD@47.242.128.177:13286/"
                # print(myclient)
                # client = pymongo.MongoClient(host='47.242.128.177', port=13286,
                #                              username='test', password='cPjeplgWRGnoaYAD',
                #                              authSource='admin')  # 连接生产mongo
                # myclient = f"mongodb://test:cPjeplgWRGnoaYAD@47.57.231.50:13221/"       # 公网IP地址
                myclient = f"mongodb://test:cPjeplgWRGnoaYAD@172.16.0.126:13286/"       # 内网IP地址
                print(myclient)
                client = pymongo.MongoClient(myclient)
            db = client[dataBase]  # 连接数据库
            collection = db[collection]  # 连接集合
            return collection
        except Exception as e:
            print(f"体育MongoDB链接失败：{e}")

    def select_data_one(self, collection, sen):
        try:
            sen = eval(sen)
            results = collection.find_one(sen)
            return results
        except Exception as e:
            logging.error(f'MongoDB查询单条数据错误：{e}')

    def select_data_all(self, collection, sen):
        try:
            sen = eval(sen)
            results = collection.find(sen)
            return results
        except Exception as e:
            logging.error(f'MongoDB查询多条数据错误：{e}')

    def get_data_list(self, list, dcnn):
        try:
            sen = '{"match_id": { "$in":' + str(list) + '}}'
            result = self.select_data_all(dcnn, sen)
            # print(test_result)
            return result
        except Exception as e:
            logging.error(f'MongoDB查询列表多条数据错误：{e}')

    def get_data_list_basketball(self, list, dcnn):
        try:
            sen = '{"matchId": { "$in":' + str(list) + '}}'
            result = self.select_data_all(dcnn, sen)
            # print(test_result)
            return result
        except Exception as e:
            logging.error(f'MongoDB查询列表多条数据错误：{e}')

    # def get_data_all_list(self, match_id, dataBase, collection, status):
    #     myDb = MongoDB()
    #     collect1 = myDb.connect(dataBase, collection, env_flag=status)  # status=0 是测试MongoDB，非1都是线上MongoDB
    #     # sen = '{"match_id":' + str(match_id) + '}'
    #     sen = '{"match_id": { "$in":' + str(match_id) + '}}'
    #     test_result = myDb.select_data_all(collect1, sen)
    #     return test_result


if __name__ == '__main__':
    # myclient = f"mongodb://soccer:UwJiAEuO9yB1YUoR@172.16.195.5:13297/"  # 内网IP地址
    myclient = f"mongodb://soccer:UwJiAEuO9yB1YUoR@47.110.84.47:13297/"    # 公网IP地址
    print(myclient)
    client = pymongo.MongoClient(myclient)


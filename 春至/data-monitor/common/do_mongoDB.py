import pymongo
from common.read_config import ReadConfig
from common import read_path
import logging
import common.my_logger


class MongoDB(object):

    def __init__(self):
        self.mongo_host = ReadConfig().read_config(read_path.conf_path, 'mongoDB', 'host')
        self.mongo_port = ReadConfig().read_config(read_path.conf_path, 'mongoDB', 'port')
        self.mongo_user = ReadConfig().read_config(read_path.conf_path, 'mongoDB', 'username')
        self.mongo_pwd = ReadConfig().read_config(read_path.conf_path, 'mongoDB', 'password')
        self.mongo_authSource = ReadConfig().read_config(read_path.conf_path, 'mongoDB', 'authSource')
        self.mongo_database = ReadConfig().read_config(read_path.conf_path, 'mongoDB', 'database')

    def connect(self, dataBase, collection):
        try:
            myclient = f"mongodb://{self.mongo_user}:{self.mongo_pwd}@{self.mongo_host}:{self.mongo_port}/"
            print(myclient)
            client = pymongo.MongoClient(myclient)
            # client = pymongo.MongoClient(host=self.mongo_host, port=int(self.mongo_port),
            #                              username=self.mongo_user, password=self.mongo_pwd,
            #                              authSource=self.mongo_authSource)
            # client = pymongo.MongoClient("mongodb://121.196.189.137:27017/")

            db = client[dataBase]  # 连接数据库
            collection = db[collection]  # 连接集合
            print(f"电竞MongoDB链接成功")
            return collection
        except Exception as e:
            print(f"电竞MongoDB链接失败：{e}")

    def select_data_one(self, collection, sen):
        try:
            sen = eval(sen)
            results = collection.find_one(sen)
            print("select_data_one查询成功：", results)
            return results
        except Exception as e:
            logging.error(f'MongoDB查询单条数据错误：{e}')

    def select_data_all(self, collection, sen):
        try:
            sen = eval(sen)
            results = collection.find(sen)
            print("select_data_all查询成功：", results)
            return results
        except Exception as e:
            logging.error(f'MongoDB查询多条数据错误：{e}')

    def get_data_list(self, list, dcnn):
        try:
            sen = '{"match_id": { "$in":' + str(list) + '}}'
            results = self.select_data_all(dcnn, sen)
            print("get_data_list查询成功：", results)
            return results
        except Exception as e:
            logging.error(f'MongoDB查询列表多条数据错误：{e}')

    # def get_data_all_list(self, match_id, dataBase, collection, status):
    #     myDb = MongoDB()
    #     collect1 = myDb.connect(dataBase, collection, env_flag=status)  # status=0 是测试MongoDB，非1都是线上MongoDB
    #     # sen = '{"match_id":' + str(match_id) + '}'
    #     sen = '{"match_id": { "$in":' + str(match_id) + '}}'
    #     game = myDb.select_data_all(collect1, sen)
    #     return game


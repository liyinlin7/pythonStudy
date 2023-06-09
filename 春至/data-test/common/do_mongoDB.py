import pymongo


class MongoDB(object):
    def connect(self, dataBase, collection, status=0):
        try:
            if status == 0:
                # client = pymongo.MongoClient("mongodb://121.196.189.137:27017/")  # 外网连接测试mongo
                client = pymongo.MongoClient("mongodb://172.16.195.16:27017/")  # 内网连接测试mongo
            else:
                client = pymongo.MongoClient("mongodb://47.56.193.4:27017/")  # 连接生产mongo
            db = client[dataBase]  # 连接数据库
            collection = db[collection]  # 连接集合
            return collection
        except Exception:
            print("链接MongoDB失败")

    def select_data_one(self, collection, sen):
        sen = eval(sen)
        results = collection.find_one(sen)
        return results

    def select_data_all(self, collection, sen):
        try:
            sen = eval(sen)
            results = collection.find(sen)
            return results
        except Exception:
            print("MongoDB——ALL查询失败")

    def sport_connect(self, dataBase, collection, status=0):
        try:
            if status == 0:
                client = pymongo.MongoClient(host='47.110.84.47', port=13297,
                                             username='soccer', password='UwJiAEuO9yB1YUoR',
                                             authSource='sports-soccer')  # 连接测试mongo
            else:
                client = pymongo.MongoClient("")  # 连接生产mongo
            db = client[dataBase]  # 连接数据库
            collection = db[collection]  # 连接集合
            return collection
        except Exception as e:
            print(f"体育MongoDB链接失败：{e}")


if __name__ == '__main__':
    mogonDB_dataBase = 'data-result'
    mogonDB_collection_lol = 'lol_result'
    mogonDB_collection_lol_event = 'lol_event'
    mogonDB_collection_lol_special = 'lol_special_event'
    mogonDB_collection_dota_special = 'dota_result_special_event'
    mogonDB_collection_dota_event = 'dota_result_event'
    mogonDB_collection_dota = 'dota_result'
    myDb = MongoDB()
    collect = myDb.connect(mogonDB_dataBase, mogonDB_collection_lol, 0)

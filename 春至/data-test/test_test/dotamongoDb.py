import pymongo

mogonDB_dataBase = 'data-center'
mogonDB_collection_lol = 'lol_result'
mogonDB_collection_dota = 'dota_result'
mogonDB_collection_csgo = 'csgo_result'
mogonDB_collection_kog = 'kog_result'


def connect(dataBase, collection, status=0):
    if status == 0:
        client = pymongo.MongoClient("mongodb://121.196.189.137:27017/")  # 连接测试mongo
    else:
        client = pymongo.MongoClient("mongodb://47.56.193.4:27017/")  # 连接生产mongo
    db = client[dataBase]  # 连接数据库
    collection = db[collection]  # 连接集合
    return collection

def select_data_one(collection):
    # sen = eval(sen)
    results = collection.find_one()
    return results


def select_data_all(collection):
    # sen = eval(sen)
    results = collection.find()
    return results


def get_data(dataBase, collection):
    myclient = pymongo.MongoClient("mongodb://121.196.189.137:27017/")
    mydb = myclient["data-center"]
    mycol = mydb["dota_result"]
    for x in mycol.find():
        for a in x['data']:
            if a['tower_kill'] == 0:
                print(x['match_id'])
                print(x['series_id'])
                print('*' * 100)
    # print(result)


if __name__ == '__main__':
    get_data(mogonDB_dataBase, mogonDB_collection_kog)


import pymongo


def get_mongo_data(db_name, name, query, query2={}):
    """
    获取赛果数据
    :param db_name: 数据库名
    :param name: 表名
    :param query: 查询语句
    :param query2: 字段筛选语句
    :return: 查询结果
    """
    # 生产环境
    # conn = pymongo.MongoClient(
    #     'mongodb://{}:{}@{}:{}/?authSource={}'.format("root", "123456", "47.56.193.4", "27017", "data-event"))

    # 测试环境
    conn = pymongo.MongoClient(
        'mongodb://{}:{}@{}:{}/?authSource={}'.format("root", "123456", "121.196.189.137", "27017", "data-event"))
    db = conn[db_name]  # 数据库名需要再修改下
    collection = db[name]
    res1 = collection.find(query, query2)
    res_li = []
    for i in res1:
        # del i['_id']
        res_li.append(i)
    return res_li


def add_list(data1, data2):
    """列表数据相加"""
    new_data = []
    for i in range(len(data1)):
        new_data.append(float(data1[i]) + float(data2[i]))
    return new_data


if __name__ == '__main__':
    # a = get_mongo_data('data-center', 'csgo_result', {"match_id": 1326}, {"_id": 0})
    # print(a)

    # a = [1, 2]
    # b = ','.join([str(i) for i in a])
    # print(b)

    a = ['1', '2']
    b = ['3', '4']
    c = add_list(a, b)
    d = [round(i/2, 2) for i in c]
    print(d)

from common.do_mysql import DoMySql
from common.requestApi.request_sg import request_SG
from common.do_mongoDB import MongoDB
import logging

'''
查询dota2是否有赛果
更改SQL

'''


def csgo_matchID(request_sg=0, flag=1):
    '''

    :param request_sg: 0是不请求补充赛果接口
    :return:
    '''
    cnn = DoMySql().connect(env_flag=flag)
    sql = "select * FROM `data-center`.dota_match where series_id in " \
          "(SELECT id FROM `data-center`.series where start_time < unix_timestamp()  and game_id=2 and status != 4 and deleted != 2) and status != 4 and deleted=1;"
    # sql = "select * FROM `data-center`.dota_match where series_id in " \
    #       "(SELECT id FROM `data-center`.series where (unix_timestamp()-3600*24*7) <= start_time and  start_time < unix_timestamp() and  status != 4 and deleted = 1);"
    mactch_id = DoMySql().select(cnn, sql)
    dataBase = 'data-center'
    collection = 'dota_result'
    ha = set()
    ids = list()
    no_serices_id = set()
    for i in mactch_id:
        rul = get_data(i["id"], dataBase, collection, flag)
        if rul is None:
            print('matchid:'+str(i["id"])+'没有赛果')
            ha.add(i["id"])
            # 查询 ex_id和p_id
            ex_sericesID_SQL = "select p_id, ex_id from `data-center`.ex_series where p_id in (SELECT series_id FROM `data-center`.match" \
                              " where id in (%s)) ;" % int(i["id"])
            ex_sericesID = DoMySql().select(cnn, ex_sericesID_SQL)
            if len(ex_sericesID):
                ids.append(ex_sericesID)
            else:
               no_serices_id.add(i["id"])
    # if request_sg != 0:
    #     for i in ids:
    #         num = 0
    #         ex_id = i[num]["ex_id"]
    #         num += 1
    #         bool = request_SG().csgo_reuqes_sg(ex_id, status=flag)
    #         if bool:
    #             logging.info("系列赛ID" + str(ex_id) + "请求dota补充赛果接口成功")
    print(mactch_id)
    print("没有赛果的matchID" + str(ha))
    print("没有系列赛的的matchID" + str(no_serices_id))
    print(ids)


def get_data(match_id, dataBase, collection, flag):
    myDb = MongoDB()
    collect1 = myDb.connect(dataBase, collection, status=flag)  # status=0 是测试MongoDB，非1都是线上MongoDB
    sen = '{"match_id":' + str(match_id) + '}'
    result = myDb.select_data_one(collect1, sen)
    return result


if __name__ == '__main__':
    csgo_matchID(request_sg=0, flag=1)  # flag 0是测试数据库  request_sg: 0是不请求补充赛果接口

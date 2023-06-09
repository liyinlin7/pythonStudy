'''
链接数据库，数据解析
'''
from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB


do_sql = DoMySql()
mysql_cnn_center = do_sql.cnn_centon_def()
mysql_cnn_basic = do_sql.cnn_basic_def()
env_flag = 1


def sql_():
    sql = '''
    SELECT * FROM `sports-soccer-league`.ex_league_cup where source = 2  and audit in (2,4) and p_id != 0
    '''
    data = do_sql.select_centon(cnn=mysql_cnn_center, sql=sql)
    # data = do_sql.select_basic(cnn=mysql_cnn_basic, sql=sql)
    team_id = []
    team_id = set()
    for i in data:
        team_id.add(i['ex_id'])
    print(team_id)


if __name__ == '__main__':
    sql_()
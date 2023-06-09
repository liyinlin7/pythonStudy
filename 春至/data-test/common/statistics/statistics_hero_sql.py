from common.do_mysql import DoMySql
import json


class statistics_hero_sql(object):

    def statistics_lengue_hero(self, game_id, league, status=0):
        if status == 0:
            cnn = DoMySql().connect(env_flag=0)  # env_flag,0为测试环境数据库，1为生产环境数据库
        else:
            cnn = DoMySql().connect(env_flag=1)

        sql = "SELECT * FROM `data-center`.statistics_kog_hero where " \
              "game_id= {} and league_id = {};".format(game_id, league)
        datas = DoMySql().select(cnn, sql)
        return datas

    def statistics_a_war_hero(self, game_id, league, status=0):
        if status == 0:
            cnn = DoMySql().connect(env_flag=0)  # env_flag,0为测试环境数据库，1为生产环境数据库
        else:
            cnn = DoMySql().connect(env_flag=1)
        if game_id == 1:
            sql = ""
        elif game_id == 2:
            sql = ""
        elif game_id == 3:
            sql = ""
        elif game_id == 4:
            sql = ""
        datas = DoMySql().select(cnn, sql)
        return datas



if __name__ == '__main__':
    statistics_sql().statistics_lengue_team(4, 685)


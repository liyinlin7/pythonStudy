from common.do_mysql import DoMySql
import json


class statistics_player_sql(object):

    def statistics_lengue_player(self, game_id, league, status=0):
        if status == 0:
            cnn = DoMySql().connect(env_flag=0)  # env_flag,0为测试环境数据库，1为生产环境数据库
        else:
            cnn = DoMySql().connect(env_flag=1)
        sql = "SELECT * FROM `data-center`.statistics_kog_player where " \
              "game_id = {} and league_id = {} order  by start_time desc;".format(game_id, league)
        datas = DoMySql().select(cnn, sql)
        return datas

    def statistics_a_war_player(self, game_id, league, status=0):
        if status == 0:
            cnn = DoMySql().connect(env_flag=0)  # env_flag,0为测试环境数据库，1为生产环境数据库
        else:
            cnn = DoMySql().connect(env_flag=1)

        sql = "SELECT * FROM `data-center`.statistics_kog_team where " \
              "game_id={} and league_id = {};".format(game_id, league)
        datas = DoMySql().select(cnn, sql)
        return datas



if __name__ == '__main__':
    statistics_player_sql().statistics_lengue_team(4, 685)


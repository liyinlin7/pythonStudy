from common.do_mysql import DoMySql
from common.requestApi.kog_statistics_league import league


class a_war_count(object):
    '''
        交战统计计算
    '''

    def mysql_a_war_count(self, team_id, series_id, stats_date, stats_count, special_stats, game_id=4, status=0, query_type=1, stats_type=1):
        '''
            :param game_id: 4为王者荣耀
            :param query_type: 1=按系列赛查询；2=按队伍ID查询
            :param stats_date: 统计截止时间，query_type= 2 时必填
            :param series_id: 系列赛ID, query_type= 1 时必填
            :param stats_type: 1=按系列赛场数统计；2=按天数统计
            :param stats_count: stats_type=1时为系列赛场数数量；stats_type=2是为天数
            :param status: 0=测试环境；1=生产环境
            :param special_stats: 特殊事件统计
            :param team_id: 队伍ID，query_type= 2 时必填
            :return:
        '''
        if status == 0:
            cnn = DoMySql.connect(env_flag=0)  # env_flag,0为测试环境数据库，1为生产环境数据库
        else:
            cnn = DoMySql.connect(env_flag=1)
        if query_type == 1:
            if stats_type == 1:
                sql = ""
            else:
                sql = ""
        else:
            if stats_type == 1:
                sql = ""
            else:
                sql = ""

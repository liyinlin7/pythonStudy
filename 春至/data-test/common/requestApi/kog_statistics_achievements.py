import requests
import datetime
import time


class achievements(object):
    '''
        近期战绩统计
    '''
    def unix_time(self):
        '''
        :return: 当前Unix_time时间
        '''
        unix_time = time.mktime(datetime.datetime.now().timetuple())
        return int(unix_time)

    def data_unix(self, datatime):
        '''
            日期格式转换为Unix_time时间格式
        :return:
        '''
        # match_time = '2018-05-22 08:30:00'
        match_time = datatime
        ans_time_stamp = time.mktime(time.strptime(match_time, "%Y-%m-%d %H:%M:%S"))
        return int(ans_time_stamp)

    def statistics_achievements(self, team_id, series_id, stats_date, stats_count, special_stats, game_id=4, status=0, query_type=1, stats_type=1):
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
        :return: 接口返回结果，json类型
        '''
        time_stamp = self.unix_time()
        if status == 0:
            url = "47.114.175.98:8080"
            base_url = "http://" + url + "/api/stats/recent/kog?game_id={}&time_stamp={}".format(game_id, time_stamp)
        else:
            url = "openapi.dawnbyte.com"
            base_url = "https://" + url + "/api/stats/recent/kog?game_id={}&time_stamp={}".format(game_id, time_stamp)
        headers = {"sign": "1234"}
        print(base_url)
        if query_type == 1:
            if stats_type == 1:
                print("按系列赛场数统计")
                data = {"query_type": query_type, "series_id": series_id, "stats_type": stats_type, "stats_count": stats_count,
                        "special_stats": special_stats}
            else:
                print("按系列赛天数统计")
                stats_type = 2
                data = {"query_type": query_type, "series_id": series_id, "stats_type": stats_type, "stats_count": stats_count,
                        "special_stats": special_stats}
        else:
            query_type = 2
            stats_date = self.data_unix(stats_date)
            if stats_type == 1:
                print("按team_id赛查询")
                data = {"query_type": query_type, "team_id": team_id, "stats_type": stats_type,
                        "stats_count": stats_count, "stats_date": stats_date, "special_stats": special_stats}
            else:
                stats_type = 2
                data = {"query_type": query_type, "team_id": team_id, "stats_type": stats_type, "stats_count": stats_count,
                        "stats_date": stats_date, "special_stats": special_stats}
        r = requests.post(url=base_url, headers=headers, json=data)
        print(r.json())
        return r.json()


if __name__ == '__main__':
    achievements = achievements()
    status = 0  # 0=测试环境；1=生产环境
    game_id = 4  # 游戏ID 1=LOL 2=DOTA2 3=CS:GO 4=王者荣耀
    query_type = 1  # 1=按系列赛查询；2=按队伍ID查询
    series_id = 6506  # query_type= 1 时必填
    team_id = 2220  # query_type= 2 时必填
    stats_date = '2020-10-09 12:10:10'  # 统计截止时间，query_type= 2 时必填
    stats_type = 1  # 1=按系列赛场数统计；2=按天数统计
    stats_count = 10  # stats_type=1时为系列赛场数数量；stats_type=2是为天数
    special_stats = [{"type": 1, "value": [1, 2]}, {"type": 2, "value": [5]}]
    achievements.statistics_achievements(status=status, team_id=team_id, series_id=series_id, stats_date=stats_date,
                                         stats_count=stats_count, game_id=game_id,
                                         query_type=query_type, stats_type=stats_type, special_stats=special_stats)

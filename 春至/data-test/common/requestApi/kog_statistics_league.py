import requests
import datetime
import time


class league(object):
    '''
        联赛统计
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

    def statistics_league(self, league_id, special_stats, game_id=4, status=0):
        '''
        :param game_id: 4为王者荣耀
        :param league_id: 联赛ID
        :param stats_date: 统计截止时间，query_type= 2 时必填
        :param special_stats: 特殊事件统计
        :return: 接口返回结果，json类型
        '''
        time_stamp = self.unix_time()
        if status == 0:
            url = "47.114.175.98:8080"
            base_url = "http://" + url + "/api/stats/league/kog?game_id={}&time_stamp={}".format(game_id, time_stamp)
            headers = {"token": "N75LPxLbvGQjnGvKvdCHUbkgSyP7u6FpfLu2mzfNyxfumxPfxd"}
        else:
            url = "openapi.dawnbyte.com"
            base_url = "https://" + url + "/api/stats/league/kog?game_id={}&time_stamp={}".format(game_id, time_stamp)
            headers = {"token": "zCYIP4ADbtgZmmP04wQvMI9AKTJx5fPnHUQZtL7eIEjIBHzB76"}
        print(base_url)
        data = {"league_id": league_id, "special_stats": special_stats}
        r = requests.post(url=base_url, headers=headers, json=data)
        print(r.json())
        return r.json()


if __name__ == '__main__':
    a_war = league()
    status = 0  # 0=测试环境；1=生产环境
    game_id = 4  # 游戏ID 1=LOL 2=DOTA2 3=CS:GO 4=王者荣耀
    league_id = 784  # 联赛ID
    special_stats = [{"type": 1, "value": [1, 2]}, {"type": 2, "value": [5]}]
    a_war.statistics_league(status=status, game_id=game_id, league_id=league_id, special_stats=special_stats)

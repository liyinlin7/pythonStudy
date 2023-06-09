from common.do_mysql import DoMySql
from tasks.sendalarm import SendAlarm
from common.deal_with_data import count_time



class RepeaData(object):
    '''
        重复数据
    '''
    def __init__(self, env_flag):
        self.env_flag = env_flag

    @count_time
    def repeatdata_team_hour(self):
        '''
            已入库两条系列比赛数据出现队伍一致并且开赛时间相隔在1小时内（系列赛状态为未开始及进行中，每5分钟轮询一次）
        :return:
        '''
        cnn = DoMySql().connect_mysql_basketball(env_flag=self.env_flag)
        sql = '''
            SELECT m.id,m.match_start_time,mt.team_id  FROM `sports-basketball`.series as m left join 
            `sports-basketball`.series_team as mt on m.id = mt.series_id WHERE m.create_time > unix_timestamp()-3600*24 and m.status in (1,2,3,4,5,6);
        '''
        datas = DoMySql().select_basketball(cnn, sql, self.env_flag)
        lists = []
        series_ids = []
        # 遍历保存series_id
        None_team_match = set()
        for i in datas:
            if i['team_id'] == None:
                None_team_match.add(i['id'])
            if i['id'] not in series_ids:
                series_ids.append(i['id'])
        # print(None_team_match)
        # 将 原数据格式转换成 map_s = {'series_id': 0, 'team_ids': 1+2 的字符串, "start_time": 0}
        for id in series_ids:
            series_id = 0
            team_ids = []
            start_time = 0
            map_ = {}
            for lis in datas:
                if id == lis['id'] and id not in None_team_match:
                    # print(id)
                    # print(None_team_match)
                    series_id = lis['id']
                    team_ids.append(str(lis['team_id']))
                    team_ids.sort()
                    team_ids_ = ''.join(team_ids)
                    start_time = lis['match_start_time']
            if series_id != 0:
                map_['series_id'] = series_id
                map_['team_id'] = team_ids_
                map_['start_time'] = start_time
                lists.append(map_)
            # print(lists)
        # print(lists)
        list_copy = lists.copy()
        bool = False

        err_map = []
        # 对比数据，看是否有一支的team
        for i in lists:
            del list_copy[0]
            err_list = set()
            for y in list_copy:
                if i['team_id'] == y['team_id']:
                    if i['start_time'] is not None and y['start_time'] is not None:
                        # print("-------------------------")
                        # print(i['start_time'])
                        # print(y['start_time'])
                        time = int(i['start_time'] - y['start_time'])
                        if 0 <= time <= 3600 or 0 >= time >= -3600:
                            err_list.add(i['series_id'])
                            err_list.add(y['series_id'])
                            bool = True
                            # print("存在")
                        else:
                            pass
            if len(err_list) != 0:
                err_map.append(err_list)
        # print(err_map)
        if bool:
            # title = "已入库两条系列赛数据出现队伍一致并且开赛时间相隔在9小时内"
            # people = '@15657880727'
            msg = "篮球：已入库两条系列赛数据出现队伍一致并且开赛时间相隔在1小时内,存在问题系列赛为:" + str(err_map) + "------"
            # SendAlarm().send_alarm_python(title, people, msg)
            print(msg)
            return msg
        else:
            return ""


if __name__ == '__main__':
    r = RepeaData(1)
    r.repeatdata_team_hour()

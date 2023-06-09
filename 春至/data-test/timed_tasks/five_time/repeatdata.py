from common.do_mysql import DoMySql
from timed_tasks.sendalarm_li import SendAlarm


class RepeaData(object):
    '''
        重复数据
    '''

    def repeatdata_team_hour(self, env_flag=0):
        '''
            同游戏下，已入库两条系列赛数据出现队伍一致并且开赛时间相隔在9小时内  5分钟轮询
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = '''
              SELECT s.id,s.game_id,s.start_time,st.team_id FROM `data-center`.series as s left join `data-center`.series_team as st 
              on s.id=st.series_id where s.deleted=1 and s.status in (1,2) and s.game_id in (1,2,3,4) and st.team_id!=0 order by start_time;
              '''
        datas = DoMySql().select(cnn, sql, env_flag)
        lists = []
        series_ids = []
        # 遍历保存series_id
        for i in datas:
            if i['id'] not in series_ids:
                series_ids.append(i['id'])
        # 将 原数据格式转换成 map_s = {'series_id': 0, 'team_ids': 1+2 的字符串, "start_time": 0}
        for id in series_ids:
            series_id = 0
            team_ids = []
            start_time = 0
            map_ = {}
            for lis in datas:
                if id == lis['id']:
                    series_id = lis['id']
                    team_ids.append(str(lis['team_id']))
                    team_ids.sort()
                    team_ids_ = ''.join(team_ids)
                    start_time = lis['start_time']
            map_['series_id'] = series_id
            map_['team_id'] = team_ids_
            map_['start_time'] = start_time
            lists.append(map_)
        # print(lists)
        list_copy = lists.copy()
        bool = False
        err_map = []
        # 对比数据，看是否有一支的team
        for i in lists:
            del list_copy[0]
            err_list = []
            for y in list_copy:
                if i['team_id'] == y['team_id']:
                    # print("-------------------------")
                    # print(i['series_id'])
                    # print(y['series_id'])
                    time = int(i['start_time'] - y['start_time'])
                    if 0 <= time < 3600*4 or 0 >= time > -3600*4:
                        err_list.append(i['series_id'])
                        err_list.append(y['series_id'])
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
            msg = "已入库两条系列赛数据出现队伍一致并且开赛时间相隔在4小时内,存在问题系列赛为:" + str(err_map)
            # SendAlarm().send_alarm_python(title, people, msg)
            print(msg)
            return msg
        else:
            return ""


# if __name__ == '__main__':
#     r = RepeaData()
#     r.repeatdata_team_hour()

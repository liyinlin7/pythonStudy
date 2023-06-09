from  common.do_mysql import DoMySql
from timed_tasks.sendalarm_li import SendAlarm

class CompetitionStatus(object):
    '''
        赛制错误
    '''
    def match_bo(self, env_flag=0):
        '''
            已入库系列赛下小局数超过BO数
            10分钟轮询
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = 'select  * from `data-center`.series where status=2 and deleted=1 and update_time < unix_timestamp() and update_time > (unix_timestamp()-3600*24*7);'
        datas = DoMySql().select(cnn, sql, env_flag)
        series_ids = []
        for data in datas:
            if data['game_id'] == 1:
                sql1 = 'select * from `data-center`.lol_match where deleted=1  and series_id= {}'.format(data['id'])
                match_datas = DoMySql().select(cnn, sql1, env_flag)
                if len(match_datas) != data['bo']:
                    series_ids.append(data['id'])
            elif data['game_id'] == 2:
                sql1 = 'select * from `data-center`.dota_match where deleted=1 and series_id= {}'.format(data['id'])
                match_datas = DoMySql().select(cnn, sql1, env_flag)
                if len(match_datas) != data['bo']:
                    series_ids.append(data['id'])
            elif data['game_id'] == 3:
                sql1 = 'select * from `data-center`.match where deleted=1 and series_id= {}'.format(data['id'])
                match_datas = DoMySql().select(cnn, sql1, env_flag)
                if len(match_datas) != data['bo']:
                    series_ids.append(data['id'])
            elif data['game_id'] == 4:
                sql1 = 'select * from `data-center`.kog_match where deleted=1 and series_id= {}'.format(data['id'])
                match_datas = DoMySql().select(cnn, sql1, env_flag)
                if len(match_datas) != data['bo']:
                    series_ids.append(data['id'])
        if len(series_ids) != 0:
            # title = "已入库系列赛下小局数和系列赛的BO数不符"
            # people = '@15657880727'
            msg = "已入库系列赛下小局数和系列赛的BO数不符,存在问题系列赛为:" + str(series_ids)
            # SendAlarm().send_alarm_python(title, people, msg)
            return msg
        else:
            return ""


# if __name__ == '__main__':
#     a = CompetitionStatus()
#     a.match_bo()

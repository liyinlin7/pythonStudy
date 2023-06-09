from common.do_mysql import DoMySql
from timed_tasks.sendalarm_li import SendAlarm


class Error_status(object):
    '''
        错误状态报警
    '''
    def match_status_1(self, env_flag=0):
        '''
            已入库进行中系列赛下全部是未开始小局  5分钟轮训一次
        :return:
        '''
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = '''
            select  * from `data-center`.series where id in (
            select p_id from `data-center`.ex_series where source !=1 and p_id != 0 and status=2 and deleted=1)
            and status=2 and deleted=1;
        '''
        datas = DoMySql().select(cnn, sql, env_flag)
        series_ids = []
        for data in datas:
            if data['game_id'] == 1:
                sql1 = 'select * from `data-center`.lol_match where deleted=1 and series_id= {}'.format(data['id'])
                match_datas = DoMySql().select(cnn, sql1, env_flag)
                num = 0
                for match_data in match_datas:
                    if match_data['status'] == 1:
                        num += 1
                if num == len(match_datas):
                    series_ids.append(data['id'])
            elif data['game_id'] == 2:
                sql1 = 'select * from `data-center`.dota_match where deleted=1 and series_id= {}'.format(data['id'])
                match_datas = DoMySql().select(cnn, sql1, env_flag)
                num = 0
                for match_data in match_datas:
                    if match_data['status'] == 1:
                        num += 1
                if num == len(match_datas):
                    series_ids.append(data['id'])
            elif data['game_id'] == 3:
                sql1 = 'select * from `data-center`.match where deleted=1  and series_id= {}'.format(data['id'])
                match_datas = DoMySql().select(cnn, sql1, env_flag)
                num = 0
                for match_data in match_datas:
                    if match_data['status'] == 1:
                        num += 1
                if num == len(match_datas):
                    series_ids.append(data['id'])
            # elif data['game_id'] == 4:
            #     sql1 = 'select * from `data-center`.kog_match where deleted=1 and series_id= {}'.format(data['p_id'])
            #     match_datas = DoMySql().select(cnn, sql1, env_flag)
            #     num = 0
            #     for match_data in match_datas:
            #         if match_data['status'] == 1:
            #             num += 1
            #     if num == len(match_datas):
            #         series_ids.append(data['p_id'])
        print(series_ids)
        if len(series_ids) != 0:
            # title = "已入库进行中系列赛下全部是未开始小局"
            # people = '@15657880727'
            msg = "已入库进行中系列赛下全部是未开始小局,存在问题系列赛为:" + str(series_ids)
            # SendAlarm().send_alarm_python(title, people, msg)
            print(msg)
            return msg
        else:
            return ""


if __name__ == '__main__':
    Error_status = Error_status()
    Error_status.match_status_1(env_flag=1)

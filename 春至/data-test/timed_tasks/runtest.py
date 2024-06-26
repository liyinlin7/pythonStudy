from timed_tasks.five_time.errstatus import Error_status
from timed_tasks.five_time.nulldata import NullData
from timed_tasks.five_time.repeatdata import RepeaData
from timed_tasks.ten_time.competitionstatus import CompetitionStatus
from timed_tasks.ten_time.resulterr import ResultErr
from timed_tasks.ten_time.wrongcompetition import Wrong_Competition
from timed_tasks.ten_time.matchteam_is_winner import MatchTeam_Is_Winner
from timed_tasks.sendalarm_li import SendAlarm
from timed_tasks.ten_time.nullevent import NullEvent
from timed_tasks.ten_time.nullspecial import NullSpecial
from timed_tasks.ten_time.sql.league import League
from common.do_mysql import DoMySql
from timed_tasks.five_time.team_id import TeamID_err
# 指数↓
from timed_tasks.ten_time.playway.todayseriesTen import TodaySeriesTen
from timed_tasks.two_time.playway.twohoursseries import TwoHoursSeries
from timed_tasks.five_time.playway.seriesrstatusFive import SeriesStatausFive
from timed_tasks.five_time.playway.todayseriesFive import TodaySeries
from timed_tasks.thirty_time.playway.seriesrstatusThirty import SeriesStataus

env_flag = 0  # 0是MySQL测试数据  1是线上
mongon_status = 0  # 0是MongoDB的测试库， 1是线上库
status_1 = 15657880727
status_2 = 18978840274
status_3 = 18640219161


class RunTest(object):

    def run_five(self):
        Error_status_msg = Error_status().match_status_1(env_flag)
        NullData_msg = NullData().series_Required(env_flag)
        RepeaData_msg = RepeaData().repeatdata_team_hour(env_flag)
        msg_status_1 = NullData_msg + RepeaData_msg
        msg_status_2 = Error_status_msg
        # print(msg_status_1)
        # print(msg_status_2)
        if msg_status_1 != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_3}'
            err_msg = msg_status_1
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)
        if msg_status_2 != '':
            title = "存在问题的数据"
            people = f'@{status_2}@{status_3}'
            err_msg = msg_status_2
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)

    def run_ten(self):
        CompetitionStatus_msg = CompetitionStatus().match_bo(env_flag)
        ResultErr_msg = ResultErr().result_null(env_flag, mongon_status)
        Wrong_Competition_msg = Wrong_Competition().MatchSocreBo(env_flag)
        MatchTeam_Is_Winner_msg = MatchTeam_Is_Winner(env_flag).dota_martchteam_is_winner()
        NullEvent_msg = NullEvent().result_null_all(env_flag, mongon_status)
        NullSpecial_msg = NullSpecial().result_null_all(env_flag, mongon_status)
        # League_msg = League(env_flag=env_flag).league_series()
        msg_status_1 = ResultErr_msg + NullEvent_msg + NullSpecial_msg  # + League_msg
        msg_status_2 = CompetitionStatus_msg + Wrong_Competition_msg + MatchTeam_Is_Winner_msg
        # print(msg_status_1)
        # print(msg_status_2)
        if msg_status_1 != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_3}'
            err_msg = msg_status_1
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)
        if msg_status_2 != '':
            title = "存在问题的数据"
            people = f'@{status_2}@{status_3}'
            err_msg = msg_status_2
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)

    def run_sql_test(self):
        cnn = DoMySql().connect(env_flag=env_flag)
        sql = 'SELECT * FROM `api-mega`.`auto_sql`;'
        datas = DoMySql().select(cnn, sql, env_flag)
        staus_1_5 = []
        staus_1_10 = []
        staus_2_5 = []
        staus_2_10 = []
        staus_1_1 = []
        staus_2_1 = []
        staus_every_day_9am_1 = []
        staus_every_day_9am_2 = []
        staus_4_5 = []
        for i in datas:
            if int(i['status']) == 1 and i['time'] == 5:
                staus_1_5.append(i)
            elif int(i['status']) == 1 and i['time'] == 10:
                staus_1_10.append(i)
            elif int(i['status']) == 1 and i['time'] == 1:
                staus_1_1.append(i)
            elif int(i['status']) == 1 and i['time'] == 100:
                staus_every_day_9am_1.append(i)
            elif int(i['status']) == 4 and i['time'] == 5:
                staus_4_5.append(i)
            elif int(i['status']) == 2 and i['time'] == 5:
                staus_2_5.append(i)
            elif int(i['status']) == 2 and i['time'] == 10:
                staus_2_10.append(i)
            elif int(i['status']) == 2 and i['time'] == 1:
                staus_2_1.append(i)
            elif int(i['status']) == 2 and i['time'] == 100:
                staus_every_day_9am_2.append(i)
        return staus_1_5, staus_1_10, staus_2_5, staus_2_10, staus_1_1, staus_2_1, staus_every_day_9am_1, staus_every_day_9am_2, staus_4_5

    def sql_run_five_now(self):
        staus_1_5, staus_1_10, staus_2_5, staus_2_10, staus_1_1, staus_2_1, staus_every_day_9am_1, staus_every_day_9am_2, staus_4_5 = self.run_sql_test()
        League_msg = League(env_flag=env_flag).league_series()
        msg_4_5 = League_msg
        msg_4_5_num = 0
        cnn = DoMySql().connect(env_flag=env_flag)
        for i in staus_4_5:
            data = DoMySql().select(cnn, i['sqlString'], env_flag)
            # print(type(data))
            if str(data) == '' or data is None or len(data) == 0:
                pass
            else:
                msg_4_5_num += 1
                msg_4_5 += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
        if msg_4_5 != '':
            title = "存在问题的数据"
            people = f'@{status_1} @{status_3}'
            err_msg = f"> ##### 本次总共执行{str(len(staus_4_5))}条sql语句，其中错误{str(msg_4_5_num)}条，错误sql为："+msg_4_5
            SendAlarm().send_alarm_python_(title, people, err_msg, env_flag)
            print(err_msg)

    def sql_run_five(self):
        staus_1_5, staus_1_10, staus_2_5, staus_2_10, staus_1_1, staus_2_1, staus_every_day_9am_1, staus_every_day_9am_2, staus_4_5 = self.run_sql_test()
        msg_1_5 = ''
        msg_2_5 = ''
        msg_1_5_num = 0
        msg_2_5_num = 0
        cnn = DoMySql().connect(env_flag=env_flag)
        for i in staus_1_5:
            data = DoMySql().select(cnn, i['sqlString'], env_flag)
            print(type(data))
            if str(data) == '' or data is None or len(data) == 0:
                pass
            else:
                msg_1_5_num += 1
                msg_1_5 += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
        for i in staus_2_5:
            data = DoMySql().select(cnn, i['sqlString'])
            if str(data) == '' or data is None or len(data) == 0:
                pass
            else:
                msg_2_5_num += 1
                msg_2_5 += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
        if msg_1_5 != '':
            title = "存在问题的数据"
            people = f'@{status_1} @{status_3}'
            err_msg = f"> ##### 本次总共执行{str(len(staus_1_5))}条sql语句，其中错误{str(msg_1_5_num)}条，错误sql为："+msg_1_5
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)
            # print(err_msg)
        if msg_2_5 != '':
            title = "存在问题的数据"
            people = f'@{status_2} @{status_3}'
            err_msg = f"> ##### 本次总共执行{str(len(staus_2_5))}条sql语句，其中错误{str(msg_2_5_num)}条，错误sql为："+msg_2_5
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)


    def sql_run_ten(self):
        staus_1_5, staus_1_10, staus_2_5, staus_2_10, staus_1_1, staus_2_1, staus_every_day_9am_1, staus_every_day_9am_2, staus_4_1 = self.run_sql_test()
        msg_1_10 = ''
        msg_2_10 = ''
        msg_1_10_num = 0
        msg_2_10_num = 0
        cnn = DoMySql().connect(env_flag=env_flag)
        print(str(staus_1_10))
        for i in staus_1_10:
            data = DoMySql().select(cnn, i['sqlString'], env_flag)
            if str(data) == ''or data is None or len(data) == 0:
                pass
            else:
                msg_1_10_num += 1
                msg_1_10 += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
        for i in staus_2_10:
            data = DoMySql().select(cnn, i['sqlString'], env_flag)
            if str(data) == ''or data is None or len(data) == 0:
                pass
            else:
                msg_2_10_num += 1
                msg_2_10 += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
        if msg_1_10 != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_3}'
            err_msg = f"> ##### 本次总共执行{str(len(staus_1_10))}条sql语句，其中错误{str(msg_1_10_num)}条，错误sql为："+msg_1_10
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)
            # print(err_msg)
        if msg_2_10 != '':
            title = "存在问题的数据"
            people = f'@{status_2}@{status_3}'
            err_msg = f"> ##### 本次总共执行{str(len(staus_2_10))}条sql语句，其中错误{str(msg_2_10_num)}条，错误sql为："+msg_2_10
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)
            # print(err_msg)

    def sql_run_one(self):
        staus_1_5, staus_1_10, staus_2_5, staus_2_10, staus_1_1, staus_2_1, staus_every_day_9am_1, staus_every_day_9am_2, staus_4_1 = self.run_sql_test()
        msg_1_1 = ''
        msg_2_1 = ''
        msg_1_1_num = 0
        msg_2_1_num = 0
        cnn = DoMySql().connect(env_flag=env_flag)
        for i in staus_1_1:
            data = DoMySql().select(cnn, i['sqlString'], env_flag)
            if str(data) == ''or data is None or len(data) == 0:
                pass
            else:
                msg_1_1_num += 1
                msg_1_1 += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
        for i in staus_2_1:
            data = DoMySql().select(cnn, i['sqlString'], env_flag)
            if str(data) == ''or data is None or len(data) == 0:
                pass
            else:
                msg_2_1_num += 1
                msg_2_1 += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
        if msg_1_1 != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_3}'
            err_msg = f"> ##### 本次总共执行{str(len(staus_1_1))}条sql语句，其中错误{str(msg_1_1_num)}条，错误sql为："+msg_1_1
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)
            # print(err_msg)
        if msg_2_1 != '':
            title = "存在问题的数据"
            people = f'@{status_2}@{status_3}'
            err_msg = f"> ##### 本次总共执行{str(len(staus_2_1))}条sql语句，其中错误{str(msg_2_1_num)}条，错误sql为："+msg_2_1
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)
            # print(err_msg)

    def sql_every_day_9_am(self):
        '''
            每天早上9点执行
        :return:
        '''
        staus_1_5, staus_1_10, staus_2_5, staus_2_10, staus_1_1, staus_2_1, staus_every_day_9am_1, staus_every_day_9am_2, staus_4_1 = self.run_sql_test()
        msg_every_day_9am_1 = ''
        msg_every_day_9am_2 = ''
        msg_every_day_9am_1_num = 0
        msg_every_day_9am_2_num = 0
        cnn = DoMySql().connect(env_flag=env_flag)
        for i in staus_every_day_9am_1:
            data = DoMySql().select(cnn, i['sqlString'], env_flag)
            if str(data) == ''or data is None or len(data) == 0:
                pass
            else:
                msg_every_day_9am_1_num += 1
                msg_every_day_9am_1 += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
        for i in staus_every_day_9am_2:
            data = DoMySql().select(cnn, i['sqlString'], env_flag)
            if str(data) == ''or data is None or len(data) == 0:
                pass
            else:
                msg_every_day_9am_2_num += 1
                msg_every_day_9am_2 += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
        if msg_every_day_9am_1 != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_3}'
            err_msg = f"> ##### 本次总共执行{str(len(staus_every_day_9am_1))}条sql语句，其中错误{str(msg_every_day_9am_1_num)}条，错误sql为："+msg_every_day_9am_1
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)
            # print(err_msg)
        if msg_every_day_9am_2 != '':
            title = "存在问题的数据"
            people = f'@{status_2}@{status_3}'
            err_msg = f"> ##### 本次总共执行{str(len(staus_every_day_9am_2))}条sql语句，其中错误{str(msg_every_day_9am_2_num)}条，错误sql为："+msg_every_day_9am_2
            SendAlarm().send_alarm_python(title, people, err_msg, env_flag)
            # print(err_msg)

    def playway_ten_run(self):
        today_err = TodaySeriesTen(env_flag).today_series_id()
        if today_err is None or today_err == '':
            pass
        else:
            title = "存在问题的数据"
            people = f'@{status_2}@{status_3}'
            err_msg = today_err
            SendAlarm().send_playway_dingtalk(title, people, err_msg, env_flag)

    def playway_five_run(self):
        series_status_market = SeriesStatausFive(env_flag).series_status_market_status()
        series_status_market_null = SeriesStatausFive(env_flag).series_status_market_null()
        five_todaySeries_option_market = TodaySeries(env_flag).today_series_id_1()
        five_match_option_market = TodaySeries(env_flag).todya_match_id()
        err_str = series_status_market + series_status_market_null + five_todaySeries_option_market + five_match_option_market
        if err_str == '':
            pass
        else:
            title = "存在问题的数据"
            people = f'@{status_2}@{status_3}'
            err_msg = err_str
            SendAlarm().send_playway_dingtalk(title, people, err_msg, env_flag)

    def playway_thirty_run(self):
        thirty_serieve_one = SeriesStataus(env_flag).series_status_market_status_onehours()
        thirty_serieve_24 = SeriesStataus(env_flag).series_status_market_status_24hours()
        err_str = thirty_serieve_one + thirty_serieve_24
        if err_str == '':
            pass
        else:
            title = "存在问题的数据"
            people = f'@{status_2}@{status_3}'
            err_msg = err_str
            SendAlarm().send_playway_dingtalk(title, people, err_msg, env_flag)

    def playway_two_run(self):
        today_err = TwoHoursSeries(env_flag).today_series_id()
        if today_err is None or today_err == '':
            pass
        else:
            title = "存在问题的数据"
            people = f'@{status_2}@{status_3}'
            err_msg = today_err
            SendAlarm().send_playway_dingtalk(title, people, err_msg, env_flag)

    def team_run_five(self):
        teamID = TeamID_err(env_flag)
        err_time = teamID.play_team_series_team()
        if err_time != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            err_msg = f"> 出现雷竞技的队伍ID和内部系列赛队伍ID不一致的ex_id：" + err_time
            SendAlarm().send_alarm_python_(title, people, err_msg, env_flag)
            # print(err_msg)


if __name__ == '__main__':
    # MatchTeam_Is_Winner_msg = MatchTeam_Is_Winner(env_flag).dota_martchteam_is_winner()
    r = RunTest()
    r.team_run_five()
    # r.run_sql_test()
#     r.run_ten()
#     r.sql_run_five()
#     r.sql_run_ten()
#     r.sql_run_one()


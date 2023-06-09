from tasks.five_time.sportdatas.run_sql_five import RunSqlFive
from tasks.ten_time.sportdatas.run_sql_ten import RunSqlTen
from tasks.thirty_time.sportdatas.run_sql_thirty import RunSqlThirty
from tasks.five_time.sportdatas.repeatdata import RepeaData
from tasks.five_time.sportdatas.requesterr import RequestErr
from tasks.sendalarm import SendAlarm
from tasks.fifteen_time.sportdatas.seriesteam import SeriesTeam

# ↓指数
# 足球
from tasks.five_time.playway_football.seriesrstatusFive_football import SeriesStatausFive_football
from tasks.five_time.playway_football.todayseriesFive_football import TodaySeries_football
from tasks.thirty_time.playway_football.seriesrstatusThirty_football import SeriesStatausThirty_football
from tasks.ten_time.playway_football.before_football import BeforeFootball
# 篮球
from tasks.five_time.playway_basketball.seriesrstatusFive_basketball import SeriesStatausFive_basketball
from tasks.five_time.playway_basketball.todayseriesFive_basketball import TodaySeries_basketball
from tasks.thirty_time.playway_basketball.seriesrstatusThirty_basketball import SeriesStatausThirth_basketball
from tasks.ten_time.playway_basketball.before_basketball import BeforeBasketball

status_1 = 17623899724
status_3 = 18640219161

class RunTasks(object):
    '''
        执行调用报警
    '''

    def __init__(self, env_flag):
        self.env_flag = env_flag

    def run_five(self):
        RunSqlFive(env_flag=self.env_flag).sql_five()
        RunSqlFive(env_flag=self.env_flag).sql_five_SH()

    def run_ten(self):
        RunSqlTen(env_flag=self.env_flag).sql_ten()

    def run_five_repeatdata(self):
        repeaData = RepeaData(self.env_flag).repeatdata_team_hour()
        print(repeaData)
        err_msg_ = repeaData
        if err_msg_ != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sport_test(env_flag=self.env_flag, title=title, people=people, msg=err_msg_)

    def run_five_resquest(self):
        request = RequestErr(self.env_flag).requestdata_null_status_7()
        print(request)
        err_msg_ = request
        if err_msg_ != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sport_test(env_flag=self.env_flag, title=title, people=people, msg=err_msg_)

    def run_fifteen(self):
        series_result = SeriesTeam(self.env_flag).ex_series_team()
        print(series_result)
        err_msg_ = series_result
        if err_msg_ != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sport_test(env_flag=self.env_flag, title=title, people=people, msg=err_msg_)

# 指数 北单和竞猜
    def run_before_playway_ten(self):
        basketball = BeforeBasketball(self.env_flag).before_option_status_basketball()
        football = BeforeFootball(self.env_flag).before_option_status_football()
        if True:
            title = "（竞彩/北单）指数存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=basketball)
        if True:
            title = "（竞彩/北单）指数存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=football)

    def run_playway_five(self):
        self.run_five_playway_SeriesStatausFive_football()
        self.run_five_playway_TodaySeries_football()
        self.run_five_playway_SeriesStatausFive_basketball()
        self.run_five_playway_TodaySeries_basketball()

    def run_playway_thirty(self):
        self.run_thirty_playway_SeriesStataus_football()
        self.run_thirty_playway_SeriesStataus_basketball()

    def run_five_playway_SeriesStatausFive_football(self):
        s = SeriesStatausFive_football(self.env_flag)
        ms = s.series_status_market_status()
        mn = s.series_status_market_null()
        err_msg = ms + mn
        if True:
            title = "（竞彩/北单）指数存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five_playway_TodaySeries_football(self):
        today = TodaySeries_football(self.env_flag)
        err_msg = today.today_series_id_1()
        if True:
            title = "（竞彩/北单）指数存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_thirty_playway_SeriesStataus_football(self):
        ss = SeriesStatausThirty_football(self.env_flag)
        m_status = ss.series_status_market_status_onehours()
        o_status = ss.series_status_option_status_onehours()
        err_msg = m_status + o_status
        if True:
            title = "（竞彩/北单）指数存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five_playway_SeriesStatausFive_basketball(self):
        s = SeriesStatausFive_basketball(self.env_flag)
        ms = s.series_status_market_status_basketball()
        mn = s.series_status_market_null_basketball()
        err_msg = ms + mn
        if True:
            title = "（竞彩/北单）指数存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five_playway_TodaySeries_basketball(self):
        today = TodaySeries_basketball(self.env_flag)
        err_msg = today.today_series_id_1_basketball()
        if True:
            title = "（竞彩/北单）指数存在问题的数据"
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_thirty_playway_SeriesStataus_basketball(self):
        ss = SeriesStatausThirth_basketball(self.env_flag)
        m_status = ss.series_status_market_status_onehours_basketball()
        o_status = ss.series_status_option_status_onehours_basketball()
        err_msg = m_status + o_status
        if True:
            print(111111)
            title = "（竞彩/北单）指数存在问题的数据："
            people = f'@{status_1}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)


if __name__ == '__main__':
    r = RunTasks(1)
    r.run_thirty_playway_SeriesStataus_basketball()
    # r.run_five_resquest()
    # r.run_five()
    # r.run_ten()

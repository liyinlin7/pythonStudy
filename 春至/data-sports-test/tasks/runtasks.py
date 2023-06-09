from tasks.five_time.sportdatas.run_sql_five import RunSqlFive
from tasks.ten_time.sportdatas.run_sql_ten import RunSqlTen
from tasks.thirty_time.sportdatas.run_sql_thirty import RunSqlThirty
from tasks.five_time.sportdatas.repeatdata import RepeaData
from tasks.five_time.sportdatas.requesterr import RequestErr
from tasks.sendalarm import SendAlarm
# ↓指数
# 足球
from tasks.five_time.playway_football.seriesrstatusFive_football import SeriesStatausFive_football
from tasks.five_time.playway_football.todayseriesFive_football import TodaySeries_football
from tasks.ten_time.playway_football.todayseriesTen_football import TodaySeriesTen_football
from tasks.thirty_time.playway_football.seriesrstatusThirty_football import SeriesStataus_football
from tasks.ten_time.playway_football.before_football import BeforeFootball
# 篮球
from tasks.five_time.playway_basketball.seriesrstatusFive_basketball import SeriesStatausFive_basketball
from tasks.five_time.playway_basketball.todayseriesFive_basketball import TodaySeries_basketball
from tasks.ten_time.playway_basketball.todayseriesTen_basketball import TodaySeriesTen_basketball
from tasks.thirty_time.playway_basketball.seriesrstatusThirty_basketball import SeriesStataus_basketball
from tasks.ten_time.playway_basketball.before_basketball import BeforeBasketball
# 卫视达
from tasks.ten_time.weishida import WeiShiDa
status_1 = 15657880727
status_2 = 18978840274
status_3 = 18640219161

class RunTasks(object):
    '''
        执行调用报警
    '''

    def __init__(self, env_flag):
        self.env_flag = env_flag

    def weishida_ten(self):
        err_msg = WeiShiDa(env_flag=self.env_flag).weishida_foot_basket_examine()
        if err_msg != '':
            title = "预警"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_weishenda_examine(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five(self):
        RunSqlFive(env_flag=self.env_flag).sql_five()
        RunSqlFive(env_flag=self.env_flag).sql_five_SH()

    def run_ten(self):
        RunSqlTen(env_flag=self.env_flag).sql_ten()

    def run_thirty(self):
        RunSqlThirty(env_flag=self.env_flag).sql_thirty_football()
        RunSqlThirty(env_flag=self.env_flag).sql_thirty_basketball()

    def run_five_repeatdata(self):
        repeaData = RepeaData(self.env_flag).repeatdata_team_hour()
        print(repeaData)
        err_msg_ = repeaData
        if err_msg_ != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_alarm_python_(env_flag=self.env_flag, title=title, people=people, msg=err_msg_)

    def run_five_resquest(self):
        request = RequestErr(self.env_flag).requestdata_null_status_7()
        print(request)
        err_msg_ = request
        if err_msg_ != '':
            title = "存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_alarm_python_(env_flag=self.env_flag, title=title, people=people, msg=err_msg_)

    def run_playway_five(self):
        self.run_five_playway_SeriesStatausFive_football()
        self.run_five_playway_TodaySeries_football()
        self.run_five_playway_SeriesStatausFive_basketball()
        self.run_five_playway_TodaySeries_basketball()

    # def run_playway_ten(self):
    #     self.run_ten_playway_TodaySeriesTen_football()
    #     self.run_ten_playway_TodaySeriesTen_basketball()

    def run_before_playway_ten(self):
        basketball = BeforeBasketball(self.env_flag).before_option_status_basketball()
        football = BeforeFootball(self.env_flag).before_option_status_football()
        if basketball != '':
            title = "（沙巴）指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=basketball)
        if football != '':
            title = "（沙巴）指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=football)

    def run_playway_thirty(self):
        self.run_thirty_playway_SeriesStataus_football()
        self.run_thirty_playway_SeriesStataus_basketball()

    def run_five_playway_SeriesStatausFive_football(self):
        s = SeriesStatausFive_football(self.env_flag)
        ms = s.series_status_market_status()
        mn = s.series_status_market_null()
        err_msg = ms + mn
        if err_msg != '':
            title = "（沙巴）指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five_playway_TodaySeries_football(self):
        today = TodaySeries_football(self.env_flag)
        err_msg = today.today_series_id_1()
        if err_msg != '':
            title = "（沙巴）指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    # def run_ten_playway_TodaySeriesTen_football(self):
    #     todayTen = TodaySeriesTen_football(self.env_flag)
    #     err_msg = todayTen.today_series_id()
    #     if err_msg != '':
    #         title = "指数存在问题的数据"
    #         people = f'@{status_1}@{status_2}@{status_3}'
    #         SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_thirty_playway_SeriesStataus_football(self):
        ss = SeriesStataus_football(self.env_flag)
        m_status = ss.series_status_market_status_onehours()
        o_status = ss.series_status_option_status_onehours()
        err_msg = m_status + o_status
        if err_msg != '':
            title = "（沙巴）指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five_playway_SeriesStatausFive_basketball(self):
        s = SeriesStatausFive_basketball(self.env_flag)
        ms = s.series_status_market_status_basketball()
        mn = s.series_status_market_null_basketball()
        err_msg = ms + mn
        if err_msg != '':
            title = "（沙巴）指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five_playway_TodaySeries_basketball(self):
        today = TodaySeries_basketball(self.env_flag)
        err_msg = today.today_series_id_1_basketball()
        if err_msg != '':
            title = "（沙巴）指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    # def run_ten_playway_TodaySeriesTen_basketball(self):
    #     todayTen = TodaySeriesTen_basketball(self.env_flag)
    #     err_msg = todayTen.today_series_id_basketball()
    #     if err_msg != '':
    #         title = "指数存在问题的数据"
    #         people = f'@{status_1}@{status_2}@{status_3}'
    #         SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_thirty_playway_SeriesStataus_basketball(self):
        ss = SeriesStataus_basketball(self.env_flag)
        m_status = ss.series_status_market_status_onehours_basketball()
        o_status = ss.series_status_option_status_onehours_basketball()
        err_msg = m_status + o_status
        if err_msg != '':
            title = "（沙巴）指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)


if __name__ == '__main__':
    r = RunTasks(1)
    r.weishida_ten()
    # r.run_five_resquest()
    # r.run_five()
    # r.run_ten()

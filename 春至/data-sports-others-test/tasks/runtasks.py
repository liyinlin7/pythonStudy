from tasks.sendalarm import SendAlarm
from tasks.five_time.playway_107.seriesrstatusFive_107 import SeriesStatausFive_107
from tasks.five_time.playway_107.todayseriesFive_107 import TodaySeries_107
from tasks.five_time.playway_108_110.seriesrstatusFive_108_110 import SeriesStatausFive_108_110
from tasks.five_time.playway_108_110.todayseriesFive_108_110 import TodaySeries_108_110
from tasks.ten_time.playway_107.before_107 import Before107
from tasks.ten_time.playway_108_110.before_108_110 import Before108_110
from tasks.thirty_time.playway_107.seriesrstatusThirty_107 import SeriesStataus_107
from tasks.thirty_time.playway_108_110.seriesrstatusThirty_108_110 import SeriesStataus_108_110
# ------
from tasks.five_time.sportdatas.run_sql_five import RunSqlFive
from tasks.ten_time.sportdatas.run_sql_ten import RunSqlTen
from tasks.thirty_time.sportdatas.run_sql_thirty import RunSqlThirty
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

    # def run_five(self):
    #     RunSqlFive(env_flag=self.env_flag).sql_five()
    #     RunSqlFive(env_flag=self.env_flag).sql_five_SH()

    def weishida_ten(self):
        err_msg = WeiShiDa(env_flag=self.env_flag).weishida_others_examine()
        if err_msg != '':
            title = "预警"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_weishenda_examine(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_ten(self):
        RunSqlTen(env_flag=self.env_flag).sql_ten()

    def run_thirty(self):
        RunSqlThirty(env_flag=self.env_flag).sql_thirty()

    def run_playway_five(self):
        self.run_five_playway_SeriesStatausFive_107()
        self.run_five_playway_TodaySeries_107()
        self.run_five_playway_SeriesStatausFive_108_110()
        self.run_five_playway_TodaySeries_108_110()

    def run_before_playway_ten(self):
        basketball = Before108_110(self.env_flag).before_option_status_108_110()
        football = Before107(self.env_flag).before_option_status_107()
        if basketball != '':
            title = "指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=basketball)
        if football != '':
            title = "指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=football)

    def run_playway_thirty(self):
        self.run_thirty_playway_SeriesStataus_107()
        self.run_thirty_playway_SeriesStataus_108_110()

    def run_five_playway_SeriesStatausFive_107(self):
        s = SeriesStatausFive_107(self.env_flag)
        ms = s.series_status_market_status_107()
        mn = s.series_status_market_null_107()
        err_msg = ms + mn
        if err_msg != '':
            title = "指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five_playway_TodaySeries_107(self):
        today = TodaySeries_107(self.env_flag)
        err_msg = today.today_series_id_1_107()
        if err_msg != '':
            title = "指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)


    def run_thirty_playway_SeriesStataus_107(self):
        ss = SeriesStataus_107(self.env_flag)
        m_status = ss.series_status_market_status_onehours_107()
        o_status = ss.series_status_option_status_onehours_107()
        err_msg = m_status + o_status
        if err_msg != '':
            title = "指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five_playway_SeriesStatausFive_108_110(self):
        s = SeriesStatausFive_108_110(self.env_flag)
        ms = s.series_status_market_status_108_110()
        mn = s.series_status_market_null_108_110()
        err_msg = ms + mn
        if err_msg != '':
            title = "指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)

    def run_five_playway_TodaySeries_108_110(self):
        today = TodaySeries_108_110(self.env_flag)
        err_msg = today.today_series_id_1_108_110()
        if err_msg != '':
            title = "指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)


    def run_thirty_playway_SeriesStataus_108_110(self):
        ss = SeriesStataus_108_110(self.env_flag)
        m_status = ss.series_status_market_status_onehours_108_110()
        o_status = ss.series_status_option_status_onehours_108_110()
        err_msg = m_status + o_status
        if err_msg != '':
            title = "指数存在问题的数据"
            people = f'@{status_1}@{status_2}@{status_3}'
            SendAlarm().send_sports_playway(env_flag=self.env_flag, title=title, people=people, msg=err_msg)


if __name__ == '__main__':
    r = RunTasks(1)
    r.run_thirty_playway_SeriesStataus_108_110()
    # r.run_five_resquest()
    # r.run_five()
    # r.run_ten()

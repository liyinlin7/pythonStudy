import time
import unittest
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from tasks.runtasks import RunTasks
from tasks.updatasql.footballupdate import FootballUpdate

env_flag = 1


if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # scheduler.add_job(RunTest().sql_every_day_9_am, 'cron', day='*',  hour=9, minute=50)
    scheduler.add_job(RunTasks(env_flag=env_flag).run_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_five_repeatdata, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_five_resquest, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_fifteen, 'interval', minutes=15, next_run_time=datetime.datetime.now())
    # 指数  竞猜/北单
    scheduler.add_job(RunTasks(env_flag=env_flag).run_playway_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_before_playway_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_playway_thirty, 'interval', minutes=30, next_run_time=datetime.datetime.now())

    scheduler.start()
    # RunTasks(env_flag).run_five()

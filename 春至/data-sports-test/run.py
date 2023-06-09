import time
import unittest
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from tasks.runtasks import RunTasks
from tasks.updatasql.footballupdate import FootballUpdate
from tasks.updatasql.basketballupdate import BasketBallUpdate

env_flag = 1


if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # scheduler.add_job(RunTest().sql_every_day_9_am, 'cron', day='*',  hour=9, minute=50)
    scheduler.add_job(RunTasks(env_flag=env_flag).run_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_five_repeatdata, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_five_resquest, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_thirty, 'interval', minutes=30, next_run_time=datetime.datetime.now())
    # 指数↓
    # scheduler.add_job(RunTest().playway_two_run, 'interval', minutes=2, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_playway_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    # scheduler.add_job(RunTasks(env_flag=env_flag).run_playway_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_before_playway_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_playway_thirty, 'interval', minutes=30, next_run_time=datetime.datetime.now())
    # 卫视达
    scheduler.add_job(RunTasks(env_flag=env_flag).weishida_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    # 定时修改数据的SQL
    scheduler.add_job(FootballUpdate(env_flag=env_flag).update_football_mathc, 'interval', hours=6, next_run_time=datetime.datetime.now())
    scheduler.add_job(BasketBallUpdate(env_flag=env_flag).update_basketball_mathc, 'interval', hours=6, next_run_time=datetime.datetime.now())
    scheduler.start()
    # RunTasks(env_flag).run_five()

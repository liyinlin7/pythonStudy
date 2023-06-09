import time
import unittest
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from tasks.runtasks import RunTasks

env_flag = 1
#  1是线上 0是测试

if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # scheduler.add_job(RunTest().sql_every_day_9_am, 'cron', day='*',  hour=9, minute=50)
    scheduler.add_job(RunTasks(env_flag=env_flag).run_playway_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_before_playway_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_thirty, 'interval', minutes=30, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTasks(env_flag=env_flag).run_playway_thirty, 'interval', minutes=30, next_run_time=datetime.datetime.now())
    # 卫视达
    scheduler.add_job(RunTasks(env_flag=env_flag).weishida_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.start()
    # RunTasks(env_flag).run_five()

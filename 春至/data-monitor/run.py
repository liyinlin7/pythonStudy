import time
import unittest
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from common import read_path
from timed_tasks.runtest import RunTest
from common.etcd_client import WriteConf


etcd = WriteConf()
etcd.write_cfg()


if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # scheduler.add_job(RunTest().sql_every_day_9_am, 'cron', day='*',  hour=9, minute=50)

    scheduler.add_job(RunTest().run_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().run_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_run_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_run_five_now, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_run_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_run_one, 'interval', minutes=1, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_every_day_9_am, 'cron', day='*', hour=9, minute=50)
    scheduler.add_job(RunTest().run_thirty, 'cron', day='*', hour=9, minute=50)
    scheduler.add_job(RunTest().run_onr_hours, 'interval', minutes=60, next_run_time=datetime.datetime.now())
    # 指数↓
    scheduler.add_job(RunTest().playway_ten_run, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().playway_five_run, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().playway_thirty_run, 'interval', minutes=30, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().team_run_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    # 卫视达
    scheduler.add_job(RunTest().run_ten_weishida, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.start()



    # scheduler.add_job(RunTest().playway_two_run, 'interval', minutes=2, next_run_time=datetime.datetime.now())

import time
import unittest
import HTMLTestRunnerNew
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from common.test_http_request import TestHttpRequest
from common import read_path
from common.send_email import SendEmail
from common.do_excel import DoExcel
from common.send_alarm import SendAlarm
from common.deal_with_data import count_time
from common.do_mysql import DoMySql, sql, sql_list
from timed_tasks.runtest import RunTest


@count_time
def run():
    # 收集测试用例
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
    run_time = time.strftime('%Y%m%d', time.localtime(time.time()))

    # 生成测试报告
    with open(read_path.test_report_path, 'wb+') as file:
        runner = HTMLTestRunnerNew.HTMLTestRunner(file, title=str(run_time) + '测试报告', description='对外接口测试',
                                                  tester='李胤霖')
        runner.run(suite)

    # 统计测试结果，钉钉发送结果
    test_result = DoExcel(read_path.test_data_path).get_test_data('test_data')
    run_count = len(test_result)
    pass_count = len([i for i in test_result if i['TestResult'] == 'PASS'])
    fail_count = len([i for i in test_result if i['TestResult'] == 'FAIL'])
    run_fail_count = run_count - pass_count - fail_count
    msg = '本次测试共执行{}条用例，测试通过{}条用例，测试不通过{}条用例， 运行失败{}条用例'.format(run_count, pass_count, fail_count, run_fail_count)
    SendAlarm().send_dingtalk_alarm(msg)

    # 发送邮件
    file_dic = {'test_report.html': read_path.test_report_path,
                'test_case.xlsx': read_path.test_data_path,
                str(run_time) + '.log': read_path.log_path}
    if fail_count > 0:  # 测试不通过发送邮件
        # SendEmail().send_email('nicy710@163.com', file_dic)
        SendEmail().send_email('julia@equinox365.com', file_dic)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    '''
    以前蔡蔡他们写的
    # scheduler.add_job(DoMySql.specialSql, 'interval', minutes=15, args=[sql_list, 1],
    #                   next_run_time=datetime.datetime.now())
    # scheduler.add_job(DoMySql().notReview, 'interval', minutes=15, next_run_time=datetime.datetime.now())
    # scheduler.add_job(DoMySql.autoRunSql_r, 'interval', minutes=30, args=[sql, 0],
    #                   next_run_time=datetime.datetime.now())
    # scheduler.add_job(DoMySql.autoRunSql_b, 'interval', hours=4, args=[sql, 0], next_run_time=datetime.datetime.now())
    # scheduler.add_job(DoMySql().match, 'interval', hours=4, next_run_time=datetime.datetime.now())
    # scheduler.add_job(run, 'interval', hours=4, next_run_time=datetime.datetime.now())
    # scheduler.add_job(message_handle, 'interval', next_run_time=datetime.datetime.now())
    '''
    scheduler.add_job(RunTest().run_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().run_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_run_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_run_five_now, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_run_ten, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_run_one, 'interval', minutes=1, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().sql_every_day_9_am, 'cron', day='*',  hour=9, minute=50)
    # 指数↓
    scheduler.add_job(RunTest().playway_ten_run, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().playway_five_run, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().playway_thirty_run, 'interval', minutes=30, next_run_time=datetime.datetime.now())
    scheduler.add_job(RunTest().team_run_five, 'interval', minutes=5, next_run_time=datetime.datetime.now())
    # scheduler.add_job(RunTest().playway_two_run, 'interval', minutes=2, next_run_time=datetime.datetime.now())
    scheduler.start()

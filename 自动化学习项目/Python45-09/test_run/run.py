import unittest
from HTMLTestRunnerCN import HTMLTestRunner
import time,logging
import sys

path=r"D:\PycharmProjects\kyb_project"
sys.path.append(path)

test_dir='../test_case'
report_dir='../report'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'

with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title='<考研帮>测试报告',description='针对考研帮3.1.0 Android app 测试报告')
    logging.info('start run test case...')
    runner.run(discover)
    f.close()

import unittest
from testrunner.HTMLTestRunnerCN import HTMLTestRunner
import time

testcase_dir = './testcase'
report_dir = './reports'

# 找到测试用例 text_dir是需要在哪个“目录”去找，pattern是找什么“文件”
discover = unittest.defaultTestLoader.discover(testcase_dir, pattern='weather_api_unittest.py')

# 定义测试报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir+'/'+now+'_test_report.html'

with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="天气预报测试报告", description="对天气API进行的接口测试")
    runner.run(discover)


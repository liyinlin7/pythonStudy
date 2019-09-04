import unittest
from HTMLTestRunnerCN import HTMLTestRunner
import time

testcase_dir = './test_case'
report_dir = './reports'

# 加载测试用例
discover = unittest.defaultTestLoader.discover(testcase_dir, pattern='weather_api_unittest.py')

# 定义测试报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir+'/'+now+'_test_report.html'

with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="天气预报测试报告", description="对天气API进行的接口测试")
    runner.run(discover)


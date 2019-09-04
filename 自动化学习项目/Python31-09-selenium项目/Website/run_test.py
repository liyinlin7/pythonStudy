import unittest
from HTMLTestRunnerCN import HTMLTestRunner
import time

report_dir = './test_report'
test_dir = './test_case'

print("开始进行测试用例")
# 创建一个批量执行文件的对象
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_login.py")

# 记录现在的时间
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir+'/'+now+'result.html'

print("开始写入报告")
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="测试报告", description="针对localhost进行的测试")
    runner.run(discover)
    f.close()

print("测试结束")

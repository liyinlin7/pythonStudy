import datetime
import os

# 项目文件路径
pro_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 配置文件路径
conf_path = os.path.join(pro_path, 'conf', 'pro.conf')

# etcd配置文件路径
etcd_conf_path = os.path.join(pro_path, 'conf', 'pro.conf')

# 测试数据路径
test_data_path = os.path.join(pro_path, 'test_data', 'test_case.xlsx')

# 测试报告路径
test_report_path = os.path.join(pro_path, 'test_result', 'test_report', 'test_report.html')

# 测试log路径
file_name = datetime.datetime.today().strftime("%Y%m%d") + '.log'
log_path = os.path.join(pro_path, 'logs', file_name)
# error_name = datetime.datetime.today().strftime("%Y%m%d") + '_error.log'
# error_log_path = os.path.join(pro_path, 'test_result', 'log', error_name)



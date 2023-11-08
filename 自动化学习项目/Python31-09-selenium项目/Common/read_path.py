import datetime
import os

# 获取上一级目录
up_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 根目录
case_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

# 项目文件路径
pro_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 配置文件路径
conf_path = os.path.join(pro_path, 'conf', 'pro.conf')

# etcd配置文件路径
etcd_conf_path = os.path.join(pro_path, 'conf', 'pro.conf')

# 测试数据路径
test_data_path = os.path.join(pro_path, 'test_data', 'city_code.xlsx')

# 测试报告路径
test_report_path = os.path.join(pro_path, 'test_result', 'test_report', 'test_report.html')

# 测试log路径
file_name = datetime.datetime.today().strftime("%Y%m%d") + '.log'
log_path = os.path.join(pro_path, 'Logs', file_name)
# error_name = datetime.datetime.today().strftime("%Y%m%d") + '_error.log'
# error_log_path = os.path.join(pro_path, 'test_result', 'log', error_name)



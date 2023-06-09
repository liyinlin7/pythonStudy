from common.do_mysql import DoMySql
from tasks.sendalarm import SendAlarm

status_1 = 15657880727
status_2 = 18978840274
status_3 = 18640219161


class RunSqlThirty(object):
    '''
        30分钟执行SQL
    '''
    def __init__(self, env_flag):
        self.cnn = DoMySql().connect_mysql(env_flag)
        self.cnn_basketball = DoMySql().connect_mysql_basketball(env_flag)
        self.env_flag = env_flag

    # def sql_thirty_basketball(self):
    #     sql = '''
    #         SELECT * FROM `test-sport`.auto_sql where type = 1 and time = 30 and status= 4;
    #     '''
    #     datas = DoMySql().select_basketball(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
    #     err_count = 0
    #     err_str = ''
    #     for i in datas:
    #         data = DoMySql().select_basketball(cnn=self.cnn_basketball, sql=i['sqlString'], env_flag=self.env_flag)
    #         if data is None or len(data) == 0:
    #             pass
    #         else:
    #             err_count += 1
    #             err_str += f"数据ID：{i['id']},注释：{i['sql_describe']}---"
    #             print(err_str)
    #     if err_str != '':
    #         title = "存在问题的数据"
    #         people = f'@{status_1}@{status_2}@{status_3}'
    #         err_msg = f"> ##### 本次总共执行{str(len(datas))}条sql语句，其中错误{str(err_count)}条，错误sql为：" + err_str
    #         SendAlarm().send_alarm_python_dianjing(env_flag=self.env_flag, title=title, people=people, msg=err_msg)


if __name__ == '__main__':
    r = RunSqlThirty(1)
    r.sql_thirty_basketball()

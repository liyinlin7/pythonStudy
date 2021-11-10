from tasks.sendalarm import SendAlarm
from common.deal_with_data import count_time

status_1 = 15657880727
status_2 = 18978840274
status_3 = 18640219161

class RunTasks(object):
    '''
        执行调用报警
    '''

    def __init__(self, env_flag):
        self.env_flag = env_flag

    # def run_five(self):
    #     RunSqlFive(env_flag=self.env_flag).sql_five()
    #     RunSqlFive(env_flag=self.env_flag).sql_five_SH()

    @count_time
    def weishida_ten(self):
        # err_msg = weishida_ten(env_flag=self.env_flag).weishida_others_examine()
        # if err_msg != '':
        #     title = "预警"
        #     people = f'@{status_1}@{status_2}@{status_3}'
        #     SendAlarm().send_weishenda_examine(env_flag=self.env_flag, title=title, people=people, msg=err_msg)
        haha = []
        for i in range(0, 1000):
            haha.append(i)


if __name__ == '__main__':
    r = RunTasks(1)
    r.weishida_ten()
    # r.run_five()
    # r.run_ten()

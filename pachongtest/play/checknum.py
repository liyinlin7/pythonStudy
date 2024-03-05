from common.do_mysql import DoMySql
import random


class CheckNum(object):

    def __init__(self):
        self.do = DoMySql()
        self.cnn = self.do.connect_mysql()

    def red_boll(self):
        num_list = []
        num_bool = True
        while num_bool:
            num = random.randint(1, 35)
            if num not in num_list:
                num_list.append(num)
            if len(num_list) == 5:
                num_bool = False
        num_list.sort()
        return num_list

    def blue_boll(self):
        num_list_blue = []
        num_bool_blue = True
        while num_bool_blue:
            num = random.randint(1, 12)
            if num not in num_list_blue:
                num_list_blue.append(num)
            if len(num_list_blue) == 2:
                num_bool_blue = False
        num_list_blue.sort()
        return num_list_blue

    def check_num(self):
        num_list = self.red_boll()
        sql = '''
                SELECT * FROM daletou.number where red_1 = {} and red_2={} and red_3 = {} and red_4 ={} and red_5= {};
            '''.format(num_list[0], num_list[1], num_list[2], num_list[3], num_list[4])
        datas = self.do.select(cnn=self.cnn, sql=sql)
        if len(datas) == 0:
            # print('红球：', num_list)
            num_list_blue = self.blue_boll()
            # print('篮球：', num_list_blue)
        print('红球：', num_list,  '篮球：', num_list_blue)

    def check_num_1(self):
        red_bool = True
        while red_bool:
            num_list = self.red_boll()
            num_list_blue = []
            sql = '''
                            SELECT * FROM daletou.number where red_1 = {} and red_2={} and red_3 = {} and red_4 ={} and red_5= {};
                        '''.format(num_list[0], num_list[1], num_list[2], num_list[3], num_list[4])
            datas = self.do.select(cnn=self.cnn, sql=sql)
            if len(datas) > 0:
                red_bool = True
            else:
                # print('红球：', num_list)
                num_list_blue = self.blue_boll()
                red_bool = False
                # print('篮球：', num_list_blue)
                # print('红球：', num_list,  '篮球：', num_list_blue)
            if num_list == [3, 5, 12, 17, 26] and num_list_blue == [1, 12]:
                print('红球：', num_list, '篮球：', num_list_blue)
                return False
            else:
                return True


if __name__ == '__main__':
    CheckNum = CheckNum()
    # for i in range(1, 6):
    #     CheckNum.check_num()
    #     # CheckNum.check_num_1()

    # 选中一个号码 看多少次能选中
    bool_ = True
    num = 0
    while bool_:
        num += 1
        bool_ = CheckNum.check_num_1()
        print(num)
    print("次数：", num)

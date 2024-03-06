from common.do_mysql import DoMySql
import random
import requests
import json


class CountQuest(object):
    '''
        计算
    '''
    def count_red_num(self):
        '''
            计算红球数字历史出现概率
        :return:
        '''
        sql = '''
            SELECT red_1,red_2,red_3,red_4,red_5 FROM daletou.number;
        '''
        cnn = DoMySql().connect_mysql()
        datas = DoMySql().select(cnn=cnn, sql=sql)
        count_num_1,count_num_2,count_num_3,count_num_4,count_num_5,count_num_6,count_num_7,count_num_8,count_num_9,\
        count_num_10, count_num_11 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        count_num_12,count_num_13,count_num_14,count_num_15,count_num_16,count_num_17,count_num_18,count_num_19,count_num_20,\
        count_num_21,count_num_22 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        count_num_23,count_num_24,count_num_25,count_num_26,count_num_27,count_num_28,count_num_29,count_num_30,count_num_31,\
        count_num_32,count_num_33 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        count_num_35,count_num_34 = 0, 0
        for i in datas:
            if i['red_1'] == 1 or i['red_2'] == 1 or i['red_3'] == 1 or i['red_4'] == 1 or i['red_5'] == 1:
                count_num_1 += 1
            if i['red_1'] == 2 or i['red_2'] == 2 or i['red_3'] == 2 or i['red_4'] == 2 or i['red_5'] == 2:
                count_num_2 += 1
            if i['red_1'] == 3 or i['red_2'] == 3 or i['red_3'] == 3 or i['red_4'] == 3 or i['red_5'] == 3:
                count_num_3 += 1
            if i['red_1'] == 4 or i['red_2'] == 4 or i['red_3'] == 4 or i['red_4'] == 4 or i['red_5'] == 4:
                count_num_4 += 1
            if i['red_1'] == 5 or i['red_2'] == 5 or i['red_3'] == 5 or i['red_4'] == 5 or i['red_5'] == 5:
                count_num_5 += 1
            if i['red_1'] == 6 or i['red_2'] == 6 or i['red_3'] == 6 or i['red_4'] == 6 or i['red_5'] == 6:
                count_num_6 += 1
            if i['red_1'] == 7 or i['red_2'] == 7 or i['red_3'] == 7 or i['red_4'] == 7 or i['red_5'] == 7:
                count_num_7 += 1
            if i['red_1'] == 8 or i['red_2'] == 8 or i['red_3'] == 8 or i['red_4'] == 8 or i['red_5'] == 8:
                count_num_8 += 1
            if i['red_1'] == 9 or i['red_2'] == 9 or i['red_3'] == 9 or i['red_4'] == 9 or i['red_5'] == 9:
                count_num_9 += 1
            if i['red_1'] == 10 or i['red_2'] == 10 or i['red_3'] == 10 or i['red_4'] == 10 or i['red_5'] == 10:
                count_num_10 += 1
            if i['red_1'] == 11 or i['red_2'] == 11 or i['red_3'] == 11 or i['red_4'] == 11 or i['red_5'] == 11:
                count_num_11 += 1
            if i['red_1'] == 12 or i['red_2'] == 12 or i['red_3'] == 12 or i['red_4'] == 12 or i['red_5'] == 12:
                count_num_12 += 1
            if i['red_1'] == 13 or i['red_2'] == 13 or i['red_3'] == 13 or i['red_4'] == 13 or i['red_5'] == 13:
                count_num_13 += 1
            if i['red_1'] == 14 or i['red_2'] == 14 or i['red_3'] == 14 or i['red_4'] == 14 or i['red_5'] == 14:
                count_num_14 += 1
            if i['red_1'] == 15 or i['red_2'] == 15 or i['red_3'] == 15 or i['red_4'] == 15 or i['red_5'] == 15:
                count_num_15 += 1
            if i['red_1'] == 16 or i['red_2'] == 16 or i['red_3'] == 16 or i['red_4'] == 16 or i['red_5'] == 16:
                count_num_16 += 1
            if i['red_1'] == 17 or i['red_2'] == 17 or i['red_3'] == 17 or i['red_4'] == 17 or i['red_5'] == 17:
                count_num_17 += 1
            if i['red_1'] == 18 or i['red_2'] == 18 or i['red_3'] == 18 or i['red_4'] == 18 or i['red_5'] == 18:
                count_num_18 += 1
            if i['red_1'] == 19 or i['red_2'] == 19 or i['red_3'] == 19 or i['red_4'] == 19 or i['red_5'] == 19:
                count_num_19 += 1
            if i['red_1'] == 20 or i['red_2'] == 20 or i['red_3'] == 20 or i['red_4'] == 20 or i['red_5'] == 20:
                count_num_20 += 1
            if i['red_1'] == 21 or i['red_2'] == 21 or i['red_3'] == 21 or i['red_4'] == 21 or i['red_5'] == 21:
                count_num_21 += 1
            if i['red_1'] == 22 or i['red_2'] == 22 or i['red_3'] == 22 or i['red_4'] == 22 or i['red_5'] == 22:
                count_num_22 += 1
            if i['red_1'] == 23 or i['red_2'] == 23 or i['red_3'] == 23 or i['red_4'] == 23 or i['red_5'] == 23:
                count_num_23 += 1
            if i['red_1'] == 24 or i['red_2'] == 24 or i['red_3'] == 24 or i['red_4'] == 24 or i['red_5'] == 24:
                count_num_24 += 1
            if i['red_1'] == 25 or i['red_2'] == 25 or i['red_3'] == 25 or i['red_4'] == 25 or i['red_5'] == 25:
                count_num_25 += 1
            if i['red_1'] == 26 or i['red_2'] == 26 or i['red_3'] == 26 or i['red_4'] == 26 or i['red_5'] == 26:
                count_num_26 += 1
            if i['red_1'] == 27 or i['red_2'] == 27 or i['red_3'] == 27 or i['red_4'] == 27 or i['red_5'] == 27:
                count_num_27 += 1
            if i['red_1'] == 28 or i['red_2'] == 28 or i['red_3'] == 28 or i['red_4'] == 28 or i['red_5'] == 28:
                count_num_28 += 1
            if i['red_1'] == 29 or i['red_2'] == 29 or i['red_3'] == 29 or i['red_4'] == 29 or i['red_5'] == 29:
                count_num_29 += 1
            if i['red_1'] == 30 or i['red_2'] == 30 or i['red_3'] == 30 or i['red_4'] == 30 or i['red_5'] == 30:
                count_num_30 += 1
            if i['red_1'] == 31 or i['red_2'] == 31 or i['red_3'] == 31 or i['red_4'] == 31 or i['red_5'] == 31:
                count_num_31 += 1
            if i['red_1'] == 32 or i['red_2'] == 32 or i['red_3'] == 32 or i['red_4'] == 32 or i['red_5'] == 32:
                count_num_32 += 1
            if i['red_1'] == 33 or i['red_2'] == 33 or i['red_3'] == 33 or i['red_4'] == 33 or i['red_5'] == 33:
                count_num_33 += 1
            if i['red_1'] == 34 or i['red_2'] == 34 or i['red_3'] == 34 or i['red_4'] == 34 or i['red_5'] == 34:
                count_num_34 += 1
            if i['red_1'] == 35 or i['red_2'] == 35 or i['red_3'] == 35 or i['red_4'] == 35 or i['red_5'] == 35:
                count_num_35 += 1
        print("数字1:", format(count_num_1/len(datas)*100, '.5f'))
        print("数字2:", format(count_num_2/len(datas)*100, '.5f'))
        print("数字3:", format(count_num_3/len(datas)*100, '.5f'))
        print("数字4:", format(count_num_4/len(datas)*100, '.5f'))
        print("数字5:", format(count_num_5/len(datas)*100, '.5f'))
        print("数字6:", format(count_num_6/len(datas)*100, '.5f'))
        print("数字7:", format(count_num_7/len(datas)*100, '.5f'))
        print("数字8:", format(count_num_8/len(datas)*100, '.5f'))
        print("数字9:", format(count_num_9/len(datas)*100, '.5f'))
        print("数字10:", format(count_num_10/len(datas)*100, '.5f'))
        print("数字11:", format(count_num_11/len(datas)*100, '.5f'))
        print("数字12:", format(count_num_12/len(datas)*100, '.5f'))
        print("数字13:", format(count_num_13/len(datas)*100, '.5f'))
        print("数字14:", format(count_num_14/len(datas)*100, '.5f'))
        print("数字15:", format(count_num_15/len(datas)*100, '.5f'))
        print("数字16:", format(count_num_16/len(datas)*100, '.5f'))
        print("数字17:", format(count_num_17/len(datas)*100, '.5f'))
        print("数字18:", format(count_num_18/len(datas)*100, '.5f'))
        print("数字19:", format(count_num_19/len(datas)*100, '.5f'))
        print("数字20:", format(count_num_20/len(datas)*100, '.5f'))
        print("数字21:", format(count_num_21/len(datas)*100, '.5f'))
        print("数字22:", format(count_num_22/len(datas)*100, '.5f'))
        print("数字23:", format(count_num_23/len(datas)*100, '.5f'))
        print("数字24:", format(count_num_24/len(datas)*100, '.5f'))
        print("数字25:", format(count_num_25/len(datas)*100, '.5f'))
        print("数字26:", format(count_num_26/len(datas)*100, '.5f'))
        print("数字27:", format(count_num_27/len(datas)*100, '.5f'))
        print("数字28:", format(count_num_28/len(datas)*100, '.5f'))
        print("数字29:", format(count_num_29/len(datas)*100, '.5f'))
        print("数字30:", format(count_num_30/len(datas)*100, '.5f'))
        print("数字31:", format(count_num_31/len(datas)*100, '.5f'))
        print("数字32:", format(count_num_32/len(datas)*100, '.5f'))
        print("数字33:", format(count_num_33/len(datas)*100, '.5f'))
        print("数字34:", format(count_num_34/len(datas)*100, '.5f'))
        print("数字35:", format(count_num_35/len(datas)*100, '.5f'))

    def count_blue_num(self):
        '''
            计算红球数字历史出现概率
        :return:
        '''
        sql = '''
            SELECT blue_1,blue_2 FROM daletou.number;
        '''
        cnn = DoMySql().connect_mysql()
        datas = DoMySql().select(cnn=cnn, sql=sql)
        count_num_1,count_num_2,count_num_3,count_num_4,count_num_5,count_num_6,count_num_7,count_num_8,count_num_9,\
        count_num_10, count_num_11, count_num_12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        for i in datas:
            if i['blue_1'] == 1 or i['blue_2'] == 1:
                count_num_1 += 1
            if i['blue_1'] == 2 or i['blue_2'] == 2:
                count_num_2 += 1
            if i['blue_1'] == 3 or i['blue_2'] == 3:
                count_num_3 += 1
            if i['blue_1'] == 4 or i['blue_2'] == 4:
                count_num_4 += 1
            if i['blue_1'] == 5 or i['blue_2'] == 5:
                count_num_5 += 1
            if i['blue_1'] == 6 or i['blue_2'] == 6:
                count_num_6 += 1
            if i['blue_1'] == 7 or i['blue_2'] == 7:
                count_num_7 += 1
            if i['blue_1'] == 8 or i['blue_2'] == 8:
                count_num_8 += 1
            if i['blue_1'] == 9 or i['blue_2'] == 9:
                count_num_9 += 1
            if i['blue_1'] == 10 or i['blue_2'] == 10:
                count_num_10 += 1
            if i['blue_1'] == 11 or i['blue_2'] == 11:
                count_num_11 += 1
            if i['blue_1'] == 12 or i['blue_2'] == 12:
                count_num_12 += 1
        print("蓝数字1:", format(count_num_1/len(datas)*100, '.5f'))
        print("蓝数字2:", format(count_num_2/len(datas)*100, '.5f'))
        print("蓝数字3:", format(count_num_3/len(datas)*100, '.5f'))
        print("蓝数字4:", format(count_num_4/len(datas)*100, '.5f'))
        print("蓝数字5:", format(count_num_5/len(datas)*100, '.5f'))
        print("蓝数字6:", format(count_num_6/len(datas)*100, '.5f'))
        print("蓝数字7:", format(count_num_7/len(datas)*100, '.5f'))
        print("蓝数字8:", format(count_num_8/len(datas)*100, '.5f'))
        print("蓝数字9:", format(count_num_9/len(datas)*100, '.5f'))
        print("蓝数字10:", format(count_num_10/len(datas)*100, '.5f'))
        print("蓝数字11:", format(count_num_11/len(datas)*100, '.5f'))
        print("蓝数字12:", format(count_num_12/len(datas)*100, '.5f'))

    def red_sum(self):
        sql = '''
            SELECT * FROM daletou.number;
        '''
        cnn = DoMySql().connect_mysql()
        datas = DoMySql().select(cnn=cnn, sql=sql)
        red_sum_set = set()
        for i in datas:
            red_sum_set.add(i['red_sum'])
        for y in red_sum_set:
            count = 0
            for b in datas:
                if y == b['red_sum']:
                    count += 1
            print(f"红色总和为{y}，占比为：{count/len(datas)}, 次数为{count}")

    def blue_sum(self):
        sql = '''
            SELECT * FROM daletou.number;
        '''
        cnn = DoMySql().connect_mysql()
        datas = DoMySql().select(cnn=cnn, sql=sql)
        blue_sum_set = set()
        for i in datas:
            blue_sum_set.add(i['blue_sum'])
        for y in blue_sum_set:
            count = 0
            for b in datas:
                if y == b['blue_sum']:
                    count += 1
            print(f"蓝色色总和为{y}，占比为：{count/len(datas)}, 次数为{count}")

    def red_blue_sum(self):
        sql = '''
            SELECT * FROM daletou.number;
        '''
        cnn = DoMySql().connect_mysql()
        datas = DoMySql().select(cnn=cnn, sql=sql)
        sum_set = set()
        for i in datas:
            sum_set.add(i['sum'])
        for y in sum_set:
            count = 0
            for b in datas:
                if y == b['sum']:
                    count += 1
            print(f"红色+蓝色总和为{y}，占比为：{count/len(datas)}, 次数为{count}")

    def suiji_num(self):
        num_list_bool = True
        red_set = set()
        blue_set = set()
        # while num_list_bool:
        for i in range(1, 11):
            if len(red_set) >= 5:
                break
            else:
                red_set.add(random.randint(1, 34))
        red_list = list(red_set)
        for i in range(1, 3):
            if len(blue_set) >= 2:
                break
            else:
                blue_set.add(random.randint(1, 12))
        blue_list = list(blue_set)
        red_list.sort()
        blue_list.sort()
        print(red_list)
        print(blue_list)

    # 查询是否有重复的数字
    def contrast(self):
        page_num = 100
        do_my_sql = DoMySql()
        cnn = do_my_sql.connect_mysql()
        for y in range(1, page_num+1):
            url = f'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo={y}'
            data = requests.get(url=url)
            a = json.loads(data.text)
            list_number = a['value']['list']
            for i in list_number:
                red_1 = 0
                red_2 = 0
                red_3 = 0
                red_4 = 0
                red_5 = 0
                blue_1 = 0
                blue_2 = 0
                lotteryDrawNum = int(i['lotteryDrawNum'])
                lotteryDrawResult_list = i['lotteryDrawResult'].split(' ')
                select_sql = f'SELECT * FROM daletou.number where id = {lotteryDrawNum};'
                data_dic = do_my_sql.select(cnn=cnn, sql=select_sql)
                if len(data_dic) == 0:
                    red_1 = int(lotteryDrawResult_list[0])
                    red_2 = int(lotteryDrawResult_list[1])
                    red_3 = int(lotteryDrawResult_list[2])
                    red_4 = int(lotteryDrawResult_list[3])
                    red_5 = int(lotteryDrawResult_list[4])
                    blue_1 = int(lotteryDrawResult_list[5])
                    blue_2 = int(lotteryDrawResult_list[6])
                    sql = f'''
                       SELECT * FROM daletou.number where red_1 ={red_1} and red_2 = {red_2} and red_3 = {red_3} and  red_4 = {red_4} and  red_5 = {red_5};
                    '''
                    data = do_my_sql.select(cnn=cnn, sql=sql)
                    if len(data) != 0:
                        print(f'red_1 ={red_1} and red_2 = {red_2} and red_3 = {red_3} and  red_4 = {red_4} and red_5 = {red_5}')


if __name__ == '__main__':
    cc = CountQuest()
    # cc.count_red_num()
    # cc.count_blue_num()
    # cc.red_sum()
    # cc.blue_sum()
    # cc.red_blue_sum()
    # cc.suiji_num()
    cc.contrast()

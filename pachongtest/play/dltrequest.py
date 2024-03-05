import requests
import json
from common.do_mysql import DoMySql


class DltRequest(object):



    def request_Dlt(self):
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
                red_sum = 0
                blue_sum = 0
                sum_num = 0
                lotteryDrawNum = int(i['lotteryDrawNum'])
                lotteryDrawResult_list = i['lotteryDrawResult'].split(' ')
                # for y in lotteryDrawResult_list:
                #     print(y)
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
                    red_sum = red_1 + red_2 + red_3 + red_4 + red_5
                    blue_sum = blue_1 + blue_2
                    sum_num = red_sum + blue_sum
                    sql = f'''
                        INSERT INTO `daletou`.`number` (`id`,`red_1`,`red_2`,`red_3`,`red_4`,`red_5`,`blue_1`,`blue_2`,`red_sum`,`blue_sum`,`sum`)
                        VALUES({lotteryDrawNum},{red_1},{red_2},{red_3},{red_4},{red_5},{blue_1},{blue_2},
                        {red_sum},{blue_sum},{sum_num});
                    '''
                    do_my_sql.insert(cnn=cnn, sql=sql)


if __name__ == '__main__':
    d = DltRequest()
    d.request_Dlt()

from common.do_mysql import DoMySql
from time import sleep
import time
from common.deal_with_data import count_time


class Rate_Run(object):
    '''
        测试某些 外部玩法的名称的指数时效性
    '''
    def __init__(self, env_flag, series_id):
        self.do_mysql = DoMySql()
        self.mysql_cnn = self.do_mysql.connect_mysql(env_flag)
        self.env_flag = env_flag
        self.s_id = series_id

    @count_time
    def basketball(self):
        ex_market_name = ('大小盘', '上半场大小盘', '最先得分球队', '最后得分球队', '让球')
        series_id = self.s_id
        # match_status_sql = f'''
        #             SELECT status FROM `sports-others`.ex_series where p_id = {series_id};
        #            '''
        match_status_sql = f'''
                            SELECT status FROM `sports-basketball`.series where id = {series_id};
                        '''
        series_status = self.do_mysql.select(cnn=self.mysql_cnn, sql=match_status_sql, env_flag=self.env_flag)
        msg = "当前比赛状态为："
        status = series_status[0]['status']
        # print(status)
        if status == 1:
            msg += '未开始'
        elif status == 2:
            msg += ' 第一节进行中'
        elif status == 3:
            msg += '第二节进行中'
        elif status == 4:
            msg += '中场'
        elif status == 5:
            msg += '第三节进行中'
        elif status == 6:
            msg += '第四节进行中'
        elif status == 7:
            msg += '加时赛'
        elif status == 8:
            msg += '已结束'
        print(msg)
        sql = f'''
            SELECT
            mt.market_id,mt.level_id,mn.name_type,mn.name_zh as 'market_name_zh',mn.name_value,mn.name_id as 'market_name_id',
            o.ex_id as 'option的ex_id',o.rate,o.option_status,o.is_winner,opn.name_type,opn.name_zh   ,opn.name_value ,opn.name_id
            FROM `sports-rate-center`.market_type as mt 
            inner join `sports-rate-center`.market_name as mn on mt.market_id=mn.market_id 
            join `sports-rate-center`.option as o on mt.id=o.market_type_id 
            join `sports-rate-center`.option_name as opn on o.id=opn.option_id  where o.market_type_id in (SELECT id FROM `sports-rate-center`.market_type where market_id in (
                SELECT id FROM `sports-rate-center`.market where market_name  in  {str(ex_market_name)} and  inside_level_id = {series_id}
                )) order by 'option的ex_id' desc;
        '''
        datas = self.do_mysql.select(cnn=self.mysql_cnn, sql=sql, env_flag=self.env_flag)
        ex_option_id = []
        for i in datas:
            if i['option的ex_id'] not in ex_option_id:
                ex_option_id.append(i['option的ex_id'])
        # print(ex_option_id)
        for i in ex_option_id:
            option_status = None
            option_name_1 = None
            option_name_value = None
            option_ex_id = None
            market_name_zh = None
            market_id = None
            market_name_id = None
            for y in datas:
                if i == y['option的ex_id'] and y['option_status'] == 1:
                    if y['name_type'] == 1:
                        option_name_1 = y['name_zh']
                    elif y['name_type'] == 2:
                        option_name_value = y['name_value']
                    option_status = y['option_status']
                    option_rate = y['rate']
                    option_ex_id = y['option的ex_id']
                    market_name_zh = y['market_name_zh']
                    market_id = y['market_id']
                    market_name_id = y['market_name_id']
            if option_status != None:
                market_str = f"玩法 ID: {str(market_id)}, {str(market_name_zh)}{str(market_name_id)}"
                option_str = f"  选项状态：{option_status},   {option_name_1} {option_name_value}     {option_rate}。 选项ex_id：{option_ex_id}"
                print(market_str+option_str)


if __name__ == '__main__':
    # a.basketball()
    while 1 == 1:
        true_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("执行时间：", true_time)
        a = Rate_Run(0, 803)
        a.basketball()
        sleep(3)

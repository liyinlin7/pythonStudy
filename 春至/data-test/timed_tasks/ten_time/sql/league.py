from common.do_mysql import DoMySql


class League(object):

    def __init__(self, env_flag):
        self.cnn = DoMySql().connect(env_flag=env_flag)    # 0是测试环境，1是线上环境
        self.centen_dataBase = 'data-centen'
        self.dota_event_collection = 'dota_event'
        self.flag = env_flag

    def league_series(self):
        '''
            已入库已结束联赛下出现未开始或者进行中系列赛
        :return:
        '''
        sql = '''
            SELECT * FROM `data-center`.series where deleted =1  and league_id in (SELECT id 
            FROM `data-center`.league where start_time >= (unix_timestamp() - 3600*24*7*8) and deleted=1 and status =3) 
            and status in (1,2) and deleted=1;
        '''
        data = DoMySql().select(cnn=self.cnn, sql=sql, env_flag=self.flag)
        lol_league_id_list = set()
        dota_league_id_list = set()
        csgo_league_id_list = set()
        kog_league_id_list = set()
        for i in data:
            if i['game_id'] == 1:
                lol_league_id_list.add(i['league_id'])
            elif i['game_id'] == 2:
                dota_league_id_list.add(i['league_id'])
            elif i['game_id'] == 3:
                csgo_league_id_list.add(i['league_id'])
            elif i['game_id'] == 4:
                kog_league_id_list.add(i['league_id'])
        err_str = ''
        if len(lol_league_id_list) > 0:
            lol_str = f'lol已入库已结束联赛下出现未开始或者进行中系列赛,league_id:{str(lol_league_id_list)};'
            err_str += lol_str
        if len(dota_league_id_list) > 0:
            dota_str = f'dota已入库已结束联赛下出现未开始或者进行中系列赛,league_id:{str(dota_league_id_list)};'
            err_str += dota_str
        if len(csgo_league_id_list) > 0:
            csgo_str = f'csgo已入库已结束联赛下出现未开始或者进行中系列赛,league_id:{str(csgo_league_id_list)};'
            err_str += csgo_str
        if len(kog_league_id_list) > 0:
            kog_str = f'kog已入库已结束联赛下出现未开始或者进行中系列赛,league_id:{str(kog_league_id_list)};'
            err_str += kog_str
        if len(err_str) != 0:
            return err_str
        else:
            return ""


if __name__ == '__main__':
    League(1).league_series()


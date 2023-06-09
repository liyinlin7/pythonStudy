"""交战统计"""
import pymongo

from common.csgo_data import handle_data
from common.do_mysql import DoMySql

ENV_FLAG = '0'


class BattleStats:
    def __init__(self, query_type, stats_type, stats_count, series_id='', team_id=[], stats_date=''):
        self.query_type = query_type  # 1=按系列赛查询，2=自定义查询
        self.stats_type = stats_type  # 1=按系列赛场数统计，2=按天数统计
        self.stats_count = stats_count  # stats_type=1时代表系列赛数量，stats_type=2时代表天数
        self.series_id = series_id  # query_type为1时必填
        self.team_id = team_id  # query_type为2时必填
        self.stats_date = stats_date  # query_type为2时必填，时间戳格式

    def get_res_data(self, db_name, name, query, query2={}):
        """
        获取赛果数据
        :param db_name: 数据库名
        :param name: 表名
        :param query: 查询语句
        :param query2: 字段筛选语句
        :return: 查询结果
        """
        # 生产环境
        # conn = pymongo.MongoClient(
        #     'mongodb://{}:{}@{}:{}/?authSource={}'.format("root", "123456", "47.56.193.4", "27017", "data-event"))

        # 测试环境
        conn = pymongo.MongoClient(
            'mongodb://{}:{}@{}:{}/?authSource={}'.format("root", "123456", "121.196.189.137", "27017", "data-event"))
        db = conn[db_name]  # 数据库名需要再修改下
        collection = db[name]
        res1 = collection.find(query, query2)
        res_li = []
        for i in res1:
            # del i['_id']
            res_li.append(i)
        return res_li

    def get_stats_data(self):
        """获取待统计数据"""
        if self.query_type == 1:
            # 获取对应系列赛数据：战队id，开始时间
            team_id_sql = 'SELECT team_id from `data-center`.series_team where series_id = {}'.format(self.series_id)
            start_time_sql = 'SELECT start_time from `data-center`.series where id = {}'.format(self.series_id)
            self.team_id = [i['team_id'] for i in DoMySql().do_my_sql(sql=team_id_sql, env_flag=ENV_FLAG)]
            self.stats_date = DoMySql().do_my_sql(sql=start_time_sql, env_flag=ENV_FLAG)[0]['start_time']

        # 1=按系列赛场数统计
        if self.stats_type == 1:
            series_ids_sql = 'SELECT id from `data-center`.series WHERE id in ' \
                             '(SELECT series_id from `data-center`.series_team where team_id in {} ' \
                             'GROUP BY series_id HAVING COUNT(series_id)>1) and deleted = 1 and (`status` = 3 or `status` = 2) ' \
                             'ORDER BY start_time DESC LIMIT {}'.format(tuple(self.team_id), self.stats_count)
        # 2=按天数统计
        else:
            series_ids_sql = 'SELECT id from `data-center`.series WHERE id in ' \
                             '(SELECT series_id from `data-center`.series_team where team_id in {} ' \
                             'GROUP BY series_id HAVING COUNT(series_id)>1) and deleted = 1 and `status` = 3 ' \
                             'and start_time BETWEEN DATE_SUB(DATE_ADD(FROM_UNIXTIME({}),INTERVAL 8 HOUR),' \
                             'INTERVAL 10 DAY) and DATE_ADD(FROM_UNIXTIME({}),INTERVAL 8 HOUR)' \
                .format(tuple(self.team_id), self.stats_date, self.stats_date)
        series_ids = [i['id'] for i in DoMySql().do_my_sql(sql=series_ids_sql, env_flag=ENV_FLAG)]

        # 小局id列表
        match_ids = []
        if series_ids:
            for i in series_ids:
                # mach_ids_sql = 'SELECT id from `data-center`.`match` WHERE series_id = {} AND deleted = 1'.format(i)
                mach_ids_sql = 'SELECT DISTINCT match_id from `data-center`.statistics_csgo_team WHERE series_id = {}'.format(i)
                mach_id = [i['match_id'] for i in DoMySql().do_my_sql(sql=mach_ids_sql, env_flag=ENV_FLAG)]
                match_ids.extend(mach_id)

        # 选手id列表
        player_ids = []
        if match_ids:
            for i in match_ids:
                player_ids_sql = 'SELECT player_id from `data-center`.match_player WHERE match_id = {}'.format(i)
                player_id = [i['player_id'] for i in DoMySql().do_my_sql(sql=player_ids_sql, env_flag=ENV_FLAG)]
                player_ids.extend(player_id)
        player_ids = list(set(player_ids))

        # 从MongoDB获取赛果数据
        res_data = []
        for i in match_ids:
            res_data += handle_data.get_mongo_data('data-center', 'csgo_result', {"match_id": i},
                                                   {"_id": 0})  # 表名需要再修改下
        return res_data, series_ids, match_ids, player_ids

    def calculate_data(self):
        """计算交战统计相关字段"""
        data = self.get_stats_data()
        res_data = data[0]
        series_ids = data[1]
        match_ids = data[2]
        player_ids = data[3]
        result = {
            'team': [],
            'player': []
        }
        match_count = len(match_ids)
        for i in self.team_id:
            team_stats = {
                'team_id': i,
                'match_count': match_count,
                'match_id': match_ids,
                'series_count': len(series_ids),
                'series_id': series_ids
            }
            # 小局获胜数
            if match_ids:
                match_win_count_sql = 'SELECT COUNT(1) as win_count from `data-center`.match_team WHERE is_winner = 4 ' \
                                      'and team_id = {} and match_id in ({})'.format(i, ','.join(
                    str(m) for m in match_ids))
                match_win_count = DoMySql().do_my_sql(sql=match_win_count_sql, env_flag=ENV_FLAG)[0]['win_count']
            else:
                match_win_count = 0
            team_stats['match_win_count'] = match_win_count

            # 系列赛获胜数
            if series_ids:
                series_win_count_sql = 'SELECT COUNT(1) as win_count from `data-center`.series_team WHERE is_winner = 4' \
                                       ' and team_id = {} and series_id in ({})'.format(i, ','.join(
                    str(m) for m in series_ids))
                series_win_count = DoMySql().do_my_sql(sql=series_win_count_sql, env_flag=ENV_FLAG)[0]['win_count']
            else:
                series_win_count = 0
            team_stats['series_win_count'] = series_win_count

            # 参与统计的回合数
            round_count = 0
            for n in match_ids:
                round_num_list = handle_data.get_mongo_data('data-live-center', 'csgo_live_data', {"match_id": n},
                                                            {"_id": 0, "round_num": 1})
                round_count += max([i['round_num'] for i in round_num_list]) if round_num_list else 0
            team_stats['round_count'] = round_count

            team_score = ['0', '0', '0']
            kill = 0
            headshot = 0
            death = 0
            assist = 0
            flash_assist = 0
            entry_kill = 0
            entry_death = 0
            one_win_multi = 0
            multi_kill = 0
            fk_diff = 0
            kd_diff = 0
            kd_ratio = 0
            adr = 0
            kast = 0
            impact = 0
            rating = 0
            for one_data in res_data:
                for one_team_data in one_data['data']:
                    if one_team_data['team_id'] == i:
                        team_score = handle_data.add_list(team_score, one_team_data['team_score'])
                        kill += one_team_data['kill']
                        headshot += one_team_data['headshot']
                        death += one_team_data['death']
                        assist += one_team_data['assist']
                        flash_assist += one_team_data['flash_assist']
                        entry_kill += one_team_data['entry_kill']
                        entry_death += one_team_data['entry_death']
                        one_win_multi += one_team_data['one_win_multi']
                        multi_kill += one_team_data['multi_kill']
                        fk_diff += eval(one_team_data['fk_diff'])
                        kd_diff += eval(one_team_data['kd_diff'])
                        kd_ratio += eval(one_team_data['kd_ratio'])
                        adr += eval(one_team_data['adr'])
                        kast += eval(one_team_data['kast'])
                        impact += eval(one_team_data['impact'])
                        rating += eval(one_team_data['rating'])
            # 队伍平均小局回合分数
            team_stats['team_score'] = [round(i/match_count, 2) for i in team_score] if match_count else 0
            # 队伍总击杀数
            team_stats['kill'] = kill
            # 队伍总爆头数
            team_stats['headshot'] = headshot
            # 队伍总死亡数
            team_stats['death'] = death
            # 队伍总助攻数
            team_stats['assist'] = assist
            # 队伍总闪光助攻数
            team_stats['flash_assist'] = flash_assist
            # 队伍总首次击杀次数
            team_stats['entry_kill'] = entry_kill
            # 队伍总被首次击杀次数
            team_stats['entry_death'] = entry_death
            # 队伍总一对多人取胜回合数
            team_stats['one_win_multi'] = one_win_multi
            # 队伍总多杀回合数
            team_stats['multi_kill'] = multi_kill
            # 队伍平均小局首次击杀和被首次击杀的差
            team_stats['avg_fk_diff'] = round(fk_diff / match_count, 2) if match_count else 0
            # 队伍平均小局击杀数和死亡数的差
            team_stats['avg_kd_diff'] = round(kd_diff / match_count, 2) if match_count else 0
            # 队伍平均小局击杀数和死亡数的比例
            team_stats['avg_kd_ratio'] = round(kd_ratio / match_count, 2) if match_count else 0
            # 队伍平均回合造成伤害
            team_stats['avg_adr'] = round(adr / match_count, 2) if match_count else 0
            # 队伍平均队员的kast数值
            team_stats['avg_kast'] = round(kast / match_count, 2) if match_count else 0
            # 队伍平均队员影响力评分
            team_stats['avg_impact'] = round(impact / match_count, 2) if match_count else 0
            # 队伍平均队员的rating2.0数值
            team_stats['avg_rating'] = round(rating / match_count, 2) if match_count else 0

            result['team'].append(team_stats)

        for i in player_ids:
            player_stats = {'player_id': i}
            player_team_sql = 'SELECT team_id from `data-basic`.player WHERE id = {}'.format(i)
            team_id = DoMySql().do_my_sql(sql=player_team_sql, env_flag=ENV_FLAG)[0]['team_id']
            player_stats['team_id'] = team_id

            # 参与统计的小局数
            match_count_sql = 'SELECT COUNT(1) as match_count from `data-center`.statistics_csgo_player WHERE player_id = {} ' \
                              'and series_id in ({})'.format(i, ','.join(str(m) for m in series_ids))
            player_match_count = DoMySql().do_my_sql(sql=match_count_sql, env_flag=ENV_FLAG)[0]['match_count']
            player_stats['match_count'] = player_match_count

            # 选手获胜的小局总数
            match_win_count_sql = 'SELECT COUNT(1) as match_count from `data-center`.statistics_csgo_player WHERE player_id = {} ' \
                              'and series_id in ({}) and is_winner = 1'.format(i, ','.join(str(m) for m in series_ids))
            player_match_win_count = DoMySql().do_my_sql(sql=match_win_count_sql, env_flag=ENV_FLAG)[0]['match_count']
            player_stats['match_win_count'] = player_match_win_count

        return result


if __name__ == '__main__':
    # a = handle_data.get_mongo_data('data-live-center', 'csgo_live_data', {"match_id": 1243}, {"_id": 0, "round_num": 1})
    # b = max([i['round_num'] for i in a])
    # print(b)

    a = BattleStats(query_type=1, stats_type=1, stats_count=1, series_id='341').calculate_data()

    print(a)

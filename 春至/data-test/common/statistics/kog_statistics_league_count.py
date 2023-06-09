from common.do_mysql import DoMySql
from common.requestApi.kog_statistics_league import league
from common.statistics.statistics_hero_sql import statistics_hero_sql
from common.statistics.statistics_player_sql import statistics_player_sql
from common.statistics.statistics_team_sql import statistics_team_sql
from common.statistics.nothing_ids import nothing_ids
from common.requestApi.kog_statistics_league import league
from common.do_mongoDB import MongoDB
from collections import Counter



class league_count(object):
    '''
        联赛统计计算
    '''

    # 获取数据
    def get_mogon_data(self, match_id, dataBase, collection):
        myDb = MongoDB()
        collect = myDb.connect(dataBase, collection, status=0)  # status=0 是测试环境数据库
        sen = '{"match_id":' + str(match_id) + '}'
        result = myDb.select_data_one(collect, sen)
        return result

    def mysql_league_count_series(self, league_id, game_id=4, status=0):
        '''
                通过league查询不重复的series ID
               :param game_id: 4为王者荣耀
               :param league_id: 联赛ID
               :param special_stats: 特殊事件统计
               :return: 通过league 返回不重复的系列赛ID
        '''
        data_series_ids = nothing_ids().series_ids(game_id=game_id, league=league_id, status=status)
        return data_series_ids

    def mysql_league_count_teams(self, league_id, special_stats, game_id=4, status=0):
        '''
            联赛统计，team 字段中的数据计算
        :param league_id:
        :param special_stats:
        :param game_id:
        :param status:
        :return:
        '''
        dats = statistics_team_sql().statistics_lengue_team(game_id=game_id, league=league_id, status=status)
        data_series_ids = self.mysql_league_count_series(game_id=game_id, league_id=league_id, status=status)
        data_team_ids = nothing_ids().team_ids(series_list=str(data_series_ids), status=status)
        team = []
        for i in list(data_team_ids):
            match_id = []
            series_id = set()
            series_is_winner = set()
            match_win_streak = 0  # 最近一场比赛开始的连胜小局
            match_lose_streak = 0  # 最近一场比赛开始算连输小局
            series_win_streak = 0  # 最近一场比赛开始的连胜系列赛
            series_lose_streak = 0  # 最近一场比赛开始算连输系列赛
            duration_count = 0  # 参与统计的比赛总时长，时间戳格式，单位分钟
            gold, kill, assist, death, kda, team_fight = 0, 0, 0, 0, 0, 0  # 总经济，击杀，助攻，死亡，kda，队伍平均队员参团率
            damage, damage_kill_ratio, damage_gold_ratio = 0, 0, 0  # 队伍总输出，队伍平均击杀输出，队伍输出经济比例
            damage_taken, damage_taken_death_ratio, damage_taken_gold_ratio = 0, 0, 0  # 队伍总承伤,队伍平均死亡承伤,队伍承伤经济比例
            team_fight, pharaoh_kill, master_kill, tower_kill =0, 0, 0, 0  # 队伍平均队员参团率，队伍暴君击杀数，队员主宰击杀数，队伍摧毁塔总数
            exp, double, triple, quadra, penta, kill_streak= 0, 0, 0, 0, 0, 0  # 没有数据的字段
            match_win_count = 0
            match_fast_winner = []
            series_fast_winner = []
            for j in dats:
                if i == j['team_id']:
                    match_id.append(j['match_id'])
                    series_id.add(j['series_id'])
                    gold += j['gold']
                    kill += j['kill']
                    assist += j['assist']
                    death += j['death']
                    damage += j['damage']
                    pharaoh_kill += j['pharaoh_kill']
                    master_kill += j['master_kill']
                    tower_kill += j['tower_kill']
                    team_fight += float(j['team_fight'])
                    damage_kill_ratio += float(j['damage_kill_ratio'])
                    damage_gold_ratio += float(j['damage_gold_ratio'])
                    damage_taken += float(j['damage_taken'])
                    damage_taken_death_ratio += float(j['damage_taken_death_ratio'])
                    damage_taken_gold_ratio += float(j['damage_taken_gold_ratio'])
                    if j['is_winner'] == 1:
                        match_win_count += 1
                    if j['series_is_winner'] == 1:
                        series_is_winner.add(j['series_id'])
                    if len(match_fast_winner) == 0:
                        match_fast_winner.append(j['is_winner'])
                    else:
                        if match_fast_winner[0] == 0:
                            match_win_streak = "最近一场小局没有胜负"
                            match_lose_streak = "最近一场小局没有胜负"
                        elif match_fast_winner[0] == 1 and match_win_streak == 0:
                            if j['is_winner'] == 1:
                                match_fast_winner.append(j['is_winner'])
                            else:
                                match_win_streak = len(match_fast_winner)
                        elif match_fast_winner[0] == 2 and match_lose_streak == 0:
                            if j['is_winner'] == 2:
                                match_fast_winner.append(j['is_winner'])
                            else:
                                match_lose_streak = len(match_fast_winner)
                    if len(series_fast_winner) == 0:
                        series_fast_winner.append({j['series_id']: j['series_is_winner']})
                    else:
                        if 0 in series_fast_winner[0].values():
                            series_win_streak = "最近一场系列赛没有胜负"
                            series_lose_streak = "最近一场系列赛没有胜负"
                        elif 1 in series_fast_winner[0].values() and series_win_streak == 0:
                            if j['series_is_winner'] == 1:
                                series_fast_winner.append({j['series_id']: j['series_is_winner']})
                            else:
                                series_win_streak1 = set(match_fast_winner)
                                series_win_streak = len(series_win_streak1)
                        elif 2 in series_fast_winner[0].values() and series_lose_streak == 0:
                            if j['series_is_winner'] == 2:
                                series_fast_winner.append({j['series_id']: j['series_is_winner']})
                            else:
                                series_lose_streak1 = set(match_fast_winner)
                                series_lose_streak = len(series_lose_streak1)
            kda = format(((kill+assist)/death), '.2f')
            team_ = {"team_id": i, "match_id": match_id, "match_count": len(match_id), "match_win_count": match_win_count,
                    "match_win_streak": match_win_streak, "match_lose_streak": match_lose_streak, "series_count": len(series_id),
                    "series_id": list(series_id), "series_win_count": len(series_is_winner), "series_win_streak": series_win_streak,
                    "series_lose_streak": series_lose_streak, "duration_count": duration_count, "gold": gold, "exp": exp,
                    "kill": kill, "death": death, "assist": assist, "double": double, "triple": triple, "quadra": quadra,
                    "penta": penta, "kill_streak": kill_streak, "damage": damage, "damage_taken": round(damage_taken, 2),
                    "pharaoh_kill": pharaoh_kill, "master_kill": master_kill, "tower_kill": tower_kill, "kda": kda,
                    "team_fight": round(team_fight, 2), "damage_kill_ratio": round(damage_kill_ratio, 2),
                    "damage_gold_ratio": round(damage_gold_ratio, 2), "damage_taken_death_ratio": round(damage_taken_death_ratio, 2),
                    "damage_taken_gold_ratio": round(damage_taken_gold_ratio, 2)}
            team.append(team_)
            for k in team_["match_id"]:
                if game_id == 4:
                    data = self.get_mogon_data(k, dataBase='data-center', collection='kog_result')
                    for team_data in data['data']:
                        if team_data['team_id'] == team_['team_id']:
                            pharaoh_kill += team_data['pharaoh_kill']
                            master_kill += team_data['master_kill']
            team_['pharaoh_kill'] = pharaoh_kill
            team_['master_kill'] = master_kill
        return team

    def mysql_league_count_player(self, league_id, special_stats, game_id=4, status=0):
        '''
            联赛统计，player 字段中的数据计算
        :param league_id:
        :param special_stats:
        :param game_id:
        :param status:
        :return:
        '''
        datas = statistics_player_sql().statistics_lengue_player(game_id=game_id, league=league_id, status=status)
        player_ids = set()
        player = []
        for players in datas:
            player_ids.add(players['player_id'])
        for player_ in player_ids:
            match_list = []
            team_id, macth_count, series_count = 0, 0, set()  # 队伍id，参与统计的小局数量， 参与统计的系列赛数量
            match_win_count, series_win_count = 0, set()  # 选手获胜的小局数量， 队员获胜的系列赛数量
            match_win_streak, match_lose_streak, series_win_streak, series_lose_streak = 0, 0, 0, 0  # 连胜连败
            true_damage, true_damage_taken, exp, exp_ratio = 0, 0, 0, 0  # （队员真实输出，队员真实承伤，队员经验，队员经验占队伍经验比例）暂时不做
            duration_count = 0  # 参与统计的比赛总时长
            gold, kill, assist, death = 0, 0, 0, 0  # 队员经济，队员英雄击杀数，队员英雄助攻数，队员英雄死亡数
            double, triple, quadra, penta, kill_streak = 0, 0, 0, 0, 0  # 队员双杀、三杀、四杀、五杀，队员最大连续击杀(没有数据)
            damage, hero_damage, damage_taken = 0, 0, 0  # 队员输出，队员英雄输出，队员承伤
            pharaoh_kill, master_kill, ifre_hero = 0, 0, []   # 队员暴君击杀数，队员主宰击杀数，常用英雄
            tower_kill, kda, team_fight = 0, 0, 0  # 队员摧毁塔数，队员kda，队员参团率
            gold_ratio = 0  # 队员经济占队伍经济比例
            damage_kill_ratio, damage_gold_ratio = 0, 0  # 队员平均击杀输出，队员输出经济比例，
            damage_taken_death_ratio, damage_taken_gold_ratio = 0, 0  #队员平均死亡承伤，队员承伤经济比例
            damage_taken_ratio, damage_ratio = 0, 0  #队员承伤占比，队员输出占比
            match_fast_winner = []
            series_fast_winner = []
            team_damage_taken = 0  # 团队总承伤
            team_damage = 0  # 团队总输出
            player_damage_taken = 0  # 个人总承伤
            team_gold = 0  # 团队总经济
            for data in datas:
                if player_ == data['player_id']:
                    match_list.append(data['match_id'])
                    team_id = data['team_id']
                    macth_count += 1
                    series_count.add(data['series_id'])
                    gold += data['gold']
                    kill += data['kill']
                    assist += data['assist']
                    death += data['death']
                    damage += data['damage']
                    hero_damage += data['hero_damage']
                    damage_taken += data['damage_taken']
                    ifre_hero.append(data['hero_id'])
                    tower_kill += data['tower_kill']
                    duration_count += data['duration_count']
                    if data['is_winner'] == 1:
                        match_win_count += 1
                    if data['series_is_winner'] == 1:
                        series_win_count.add(data['series_id'])
                    if len(match_fast_winner) == 0:
                        match_fast_winner.append(data['is_winner'])
                    else:
                        if match_fast_winner[0] == 0:
                            match_win_streak = "最近一场小局没有胜负"
                            match_lose_streak = "最近一场小局没有胜负"
                        elif match_fast_winner[0] == 1 and match_win_streak == 0:
                            if data['is_winner'] == 1:
                                match_fast_winner.append(data['is_winner'])
                            else:
                                match_win_streak = len(match_fast_winner)
                        elif match_fast_winner[0] == 2 and match_lose_streak == 0:
                            if data['is_winner'] == 2:
                                match_fast_winner.append(data['is_winner'])
                            else:
                                match_lose_streak = len(match_fast_winner)
                    if len(series_fast_winner) == 0:
                        series_fast_winner.append({data['series_id']: data['series_is_winner']})
                    else:
                        if 0 in series_fast_winner[0].values():
                            series_win_streak = "最近一场系列赛没有胜负"
                            series_lose_streak = "最近一场系列赛没有胜负"
                        elif 1 in series_fast_winner[0].values() and series_win_streak == 0:
                            if data['series_is_winner'] == 1:
                                series_fast_winner.append({data['series_id']: data['series_is_winner']})
                            else:
                                series_win_streak1 = set(match_fast_winner)
                                series_win_streak = len(series_win_streak1)
                        elif 2 in series_fast_winner[0].values() and series_lose_streak == 0:
                            if data['series_is_winner'] == 2:
                                series_fast_winner.append({data['series_id']: data['series_is_winner']})
                            else:
                                series_lose_streak1 = set(match_fast_winner)
                                series_lose_streak = len(series_lose_streak1)
            for k in match_list:
                if game_id == 4:
                    data = self.get_mogon_data(k, dataBase='data-center', collection='kog_result')
                    for team_data in data['data']:
                        if team_data['team_id'] == team_id:
                            team_damage_taken += team_data['damage_taken']
                            team_gold += team_data['gold']
                            team_damage += team_data['damage']
                            players_data = team_data['player']
                            for m in players_data:
                                if m['player_id'] == player_:
                                    player_damage_taken += m['damage_taken']
            gold_ratio = format(gold / team_gold, '.2f')
            kda = format((kill + assist) / death, '.2f')
            team_fight = format((kill + assist) / death / macth_count, '.2f')
            damage_taken_ratio = format(player_damage_taken / team_damage_taken, '.2f')
            damage_ratio = format(damage / team_damage, '.2f')
            if kill == 0:
                damage_kill_ratio = format(damage / 1, '.2f')
                damage_taken_death_ratio = format(damage_taken / 1, '.2f')
            else:
                damage_kill_ratio = format(damage / kill, '.2f')
                damage_taken_death_ratio = format(damage_taken / kill, '.2f')
            damage_gold_ratio = format(float(damage_ratio) / float(gold_ratio), '.2f')
            damage_taken_gold_ratio = format(float(damage_taken_ratio) / float(gold_ratio), '.2f')
            ifre_hero = list(Counter(ifre_hero))
            ifre_hero.sort(key=lambda x: (x[1], x[1]), reverse=True)
            ifre_hero = ifre_hero[0:5]
            player_ = {"player_id": player_, "team_id": team_id, "match_count": macth_count, "match_win_count": match_win_count,
                      "match_win_streak": match_win_streak, "match_lose_streak": match_lose_streak,
                      "series_win_count": len(series_win_count), "series_win_streak": series_win_streak,
                      "series_lose_streak": series_lose_streak, "series_count": len(series_count), "true_damage": true_damage,
                      "true_damage_taken": true_damage_taken, "duration_count": duration_count, "gold": gold, "exp": exp,
                      "kill": kill, "assist": assist, "death": death, "double": double, "triple": triple, "quadra": quadra,
                      "penta": penta, "kill_streak": kill_streak, "damage": damage, "hero_damage": hero_damage,
                      "damage_taken": damage_taken, "pharaoh_kill": pharaoh_kill, "master_kill": master_kill, "tower_kill": tower_kill,
                      "ifre_hero": ifre_hero, "gold_ratio": gold_ratio, "exp_ratio": exp_ratio, "kda": kda, "team_fight": team_fight,
                      "damage_kill_ratio": damage_kill_ratio, "damage_gold_ratio": damage_gold_ratio,
                      "damage_taken_death_ratio": damage_taken_death_ratio, "damage_taken_gold_ratio": damage_taken_gold_ratio,
                      "damage_taken_ratio": damage_taken_ratio, "damage_ratio": damage_ratio}
            player.append(player_)
        print(str(player))

    def mysql_league_count_hero(self, league_id, special_stats, game_id=4, status=0):
        '''
            联赛统计，hero 字段中的数据计算
        :param league_id:
        :param special_stats:
        :param game_id:
        :param status:
        :return:
        '''
        datas = statistics_hero_sql().statistics_lengue_hero(game_id=game_id, league=league_id, status=status)



if __name__ == '__main__':
    # league_count().mysql_league_count_teams(league_id=685, special_stats=[])
    # league_count().mysql_league_count_player(league_id=685, special_stats=[])
    league_count().mysql_league_count_hero(league_id=685, special_stats=[])




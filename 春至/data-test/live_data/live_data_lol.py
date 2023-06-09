import json


class Live_lol(object):

    def __init__(self):
        self.data = '''
           {"match_id":25091,"series_id":1606925175,"stage":1,"time":2302,"team":[{"team_id":334,"gold":69200,"gold_min":"1803.00","gold_diff":-5400,"cs":1252,"cs_min":"32.63","cs_diff":-26,"kill":14,"assist":38,"death":17,"kda":"3.06","neutral_kill":3,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":1,"drake_kill":2,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":1,"ocean_drake_kill":0,"tower_kill":7,"inhibitor_kill":0,"player":[{"player_id":1121,"level":18,"hp":93,"status":2,"respawn_time":0,"item":[{"item_id":16,"is_trinket":2},{"item_id":157,"is_trinket":1},{"item_id":307,"is_trinket":1},{"item_id":252,"is_trinket":1},{"item_id":235,"is_trinket":1},{"item_id":775,"is_trinket":1},{"item_id":238,"is_trinket":1}],"spell":[{"summon_spell_id":14},{"summon_spell_id":7}],"cs":371,"cs_min":"9.67","cs_diff":-85,"kill":7,"assist":7,"death":2,"kda":"7.00","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":2,"inhibitor_kill":0},{"player_id":2198,"level":16,"hp":20,"status":2,"respawn_time":0,"item":[{"item_id":203,"is_trinket":2},{"item_id":193,"is_trinket":1},{"item_id":185,"is_trinket":1},{"item_id":273,"is_trinket":1},{"item_id":779,"is_trinket":1}],"spell":[{"summon_spell_id":7},{"summon_spell_id":5}],"cs":206,"cs_min":"5.37","cs_diff":-46,"kill":1,"assist":9,"death":3,"kda":"3.33","neutral_kill":2,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":1,"drake_kill":1,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":1,"ocean_drake_kill":0,"tower_kill":1,"inhibitor_kill":0},{"player_id":1840,"level":18,"hp":64,"status":2,"respawn_time":0,"item":[{"item_id":203,"is_trinket":2},{"item_id":193,"is_trinket":1},{"item_id":273,"is_trinket":1},{"item_id":185,"is_trinket":1},{"item_id":146,"is_trinket":1},{"item_id":781,"is_trinket":1}],"spell":[{"summon_spell_id":7},{"summon_spell_id":10}],"cs":350,"cs_min":"9.12","cs_diff":79,"kill":6,"assist":3,"death":2,"kda":"4.50","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":3,"inhibitor_kill":0},{"player_id":8712,"level":15,"hp":94,"status":2,"respawn_time":0,"item":[{"item_id":203,"is_trinket":2},{"item_id":145,"is_trinket":1},{"item_id":287,"is_trinket":1},{"item_id":134,"is_trinket":1},{"item_id":186,"is_trinket":1},{"item_id":166,"is_trinket":1},{"item_id":212,"is_trinket":1}],"spell":[{"summon_spell_id":15},{"summon_spell_id":7}],"cs":33,"cs_min":"0.86","cs_diff":1,"kill":0,"assist":8,"death":6,"kda":"1.33","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":0,"inhibitor_kill":0},{"player_id":2199,"level":18,"hp":94,"status":2,"respawn_time":0,"item":[{"item_id":203,"is_trinket":2},{"item_id":186,"is_trinket":1},{"item_id":9,"is_trinket":1},{"item_id":756,"is_trinket":1},{"item_id":176,"is_trinket":1},{"item_id":202,"is_trinket":1},{"item_id":782,"is_trinket":1}],"spell":[{"summon_spell_id":6},{"summon_spell_id":7}],"cs":292,"cs_min":"7.61","cs_diff":25,"kill":0,"assist":11,"death":4,"kda":"2.75","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":0,"inhibitor_kill":0}]},{"team_id":126202,"gold":74600,"gold_min":"1944.00","gold_diff":5400,"cs":1278,"cs_min":"33.31","cs_diff":26,"kill":17,"assist":47,"death":14,"kda":"4.57","neutral_kill":10,"herald_kill":2,"nashor_kill":3,"elder_drake_kill":1,"drake_kill":4,"infernal_drake_kill":1,"mountain_drake_kill":0,"cloud_drake_kill":1,"ocean_drake_kill":1,"tower_kill":8,"inhibitor_kill":0,"player":[{"player_id":3275,"level":18,"hp":0,"status":1,"respawn_time":7,"item":[{"item_id":16,"is_trinket":2},{"item_id":157,"is_trinket":1},{"item_id":300,"is_trinket":1},{"item_id":235,"is_trinket":1},{"item_id":771,"is_trinket":1},{"item_id":238,"is_trinket":1},{"item_id":774,"is_trinket":1}],"spell":[{"summon_spell_id":14},{"summon_spell_id":7}],"cs":456,"cs_min":"11.89","cs_diff":85,"kill":6,"assist":7,"death":2,"kda":"6.50","neutral_kill":2,"herald_kill":0,"nashor_kill":2,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":2,"inhibitor_kill":0},{"player_id":3229,"level":18,"hp":100,"status":2,"respawn_time":0,"item":[{"item_id":203,"is_trinket":2},{"item_id":174,"is_trinket":1},{"item_id":796,"is_trinket":1},{"item_id":217,"is_trinket":1},{"item_id":247,"is_trinket":1},{"item_id":273,"is_trinket":1},{"item_id":781,"is_trinket":1}],"spell":[{"summon_spell_id":7},{"summon_spell_id":5}],"cs":252,"cs_min":"6.57","cs_diff":46,"kill":6,"assist":10,"death":1,"kda":"16.00","neutral_kill":6,"herald_kill":2,"nashor_kill":1,"elder_drake_kill":0,"drake_kill":3,"infernal_drake_kill":1,"mountain_drake_kill":0,"cloud_drake_kill":1,"ocean_drake_kill":1,"tower_kill":0,"inhibitor_kill":0},{"player_id":3244,"level":18,"hp":0,"status":1,"respawn_time":7,"item":[{"item_id":16,"is_trinket":2},{"item_id":141,"is_trinket":1},{"item_id":166,"is_trinket":1},{"item_id":265,"is_trinket":1},{"item_id":269,"is_trinket":1},{"item_id":202,"is_trinket":1},{"item_id":782,"is_trinket":1}],"spell":[{"summon_spell_id":7},{"summon_spell_id":6}],"cs":271,"cs_min":"7.06","cs_diff":-79,"kill":3,"assist":9,"death":3,"kda":"4.00","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":2,"inhibitor_kill":0},{"player_id":2266,"level":15,"hp":0,"status":1,"respawn_time":50,"item":[{"item_id":203,"is_trinket":2},{"item_id":274,"is_trinket":1},{"item_id":192,"is_trinket":1},{"item_id":174,"is_trinket":1},{"item_id":8,"is_trinket":1},{"item_id":163,"is_trinket":1},{"item_id":212,"is_trinket":1}],"spell":[{"summon_spell_id":15},{"summon_spell_id":7}],"cs":32,"cs_min":"0.83","cs_diff":-1,"kill":1,"assist":14,"death":5,"kda":"3.00","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":0,"inhibitor_kill":0},{"player_id":3245,"level":18,"hp":0,"status":1,"respawn_time":2,"item":[{"item_id":203,"is_trinket":2},{"item_id":145,"is_trinket":1},{"item_id":174,"is_trinket":1},{"item_id":165,"is_trinket":1},{"item_id":265,"is_trinket":1},{"item_id":176,"is_trinket":1},{"item_id":763,"is_trinket":1}],"spell":[{"summon_spell_id":7},{"summon_spell_id":6}],"cs":267,"cs_min":"6.96","cs_diff":-25,"kill":1,"assist":7,"death":3,"kda":"2.67","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":1,"inhibitor_kill":0}]}]}
        '''
        self.data_tj = '''
            {"match_id":25091,"series_id":1606925175,"time":2198,"team":[{"team_id":334,"double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":4,"team_fight":null,"player":[{"player_id":1121,"cs_ratio":"0.29","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":4,"team_fight":"1.00"},{"player_id":2198,"cs_ratio":"0.16","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":1,"team_fight":"0.50"},{"player_id":1840,"cs_ratio":"0.28","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":1,"team_fight":"0.38"},{"player_id":8712,"cs_ratio":"0.03","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":null,"team_fight":"0.50"},{"player_id":2199,"cs_ratio":"0.24","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":null,"team_fight":"0.75"}]},{"team_id":126202,"double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":4,"team_fight":null,"player":[{"player_id":3275,"cs_ratio":"0.35","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":3,"team_fight":"0.73"},{"player_id":3229,"cs_ratio":"0.20","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":4,"team_fight":"0.93"},{"player_id":3244,"cs_ratio":"0.21","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":1,"team_fight":"0.67"},{"player_id":2266,"cs_ratio":"0.03","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":1,"team_fight":"0.87"},{"player_id":3245,"cs_ratio":"0.21","double":null,"triple":null,"quadra":null,"penta":null,"kill_streak":1,"team_fight":"0.40"}]}]}
        '''

    def live_data(self):
        data = self.data
        json_data = json.loads(data)
        teams_data = json_data.get('team')
        print(teams_data)
        play_time = round((json_data['time'] / 60), 2)
        for i in teams_data:
            players_data = i.get('player')
            team_gold = i['gold']
            team_gold_min = float(i['gold_min'])
            team_gold_diff = i['gold_diff']
            team_cs = i['cs']
            team_cs_min = float(i['cs_min'])
            team_cs_diff = i['cs_diff']
            team_kill = i['kill']
            team_assist = i['assist']
            team_death = i['death']
            team_kda = i['kda']
            team_neutral_kill = i['neutral_kill']
            team_herald_kill = i['herald_kill']
            team_nashor_kill = i['nashor_kill']
            team_elder_drake_kill = i['elder_drake_kill']
            team_drake_kill = i['drake_kill']
            team_infernal_drake_kill = i['infernal_drake_kill']
            team_mountain_drake_kill = i['mountain_drake_kill']
            team_cloud_drake_kill = i['cloud_drake_kill']
            team_ocean_drake_kill = i['ocean_drake_kill']
            team_tower_kill = i['tower_kill']
            team_inhibitor_kill = i['inhibitor_kill']
            # ---------------------------------
            player_cs = 0
            player_cs_min = 0
            player_cs_diff = 0
            player_kill = 0
            player_assist = 0
            player_death = 0
            player_kda = 0
            player_neutral_kill = 0
            player_herald_kill = 0
            player_nashor_kill = 0
            player_elder_drake_kill = 0
            player_drake_kill = 0
            player_infernal_drake_kill = 0
            player_mountain_drake_kill = 0
            player_cloud_drake_kill = 0
            player_ocean_drake_kill = 0
            player_tower_kill = 0
            player_inhibitor_kill = 0
            for b in players_data:
                player_cs += b['cs']
                # player_gold_min += float(b['gold_min'])
                player_cs_diff += b['cs_diff']
                player_kill += b['kill']
                player_assist += b['assist']
                player_death += b['death']
                player_neutral_kill += b['neutral_kill']
                player_herald_kill += float(b['herald_kill'])
                player_nashor_kill += b['nashor_kill']
                player_elder_drake_kill += b['elder_drake_kill']
                player_drake_kill += float(b['drake_kill'])
                player_infernal_drake_kill += b['infernal_drake_kill']
                player_mountain_drake_kill += b['mountain_drake_kill']
                player_cloud_drake_kill += b['cloud_drake_kill']
                player_ocean_drake_kill += b['ocean_drake_kill']
                player_tower_kill += b['tower_kill']
                player_inhibitor_kill += b['inhibitor_kill']
                if b['death'] == 0:
                    player_kda = (b['kill']+b['assist']) / 1
                elif (b['kill']+b['assist']) == 0:
                    player_kda = None
                else:
                    player_kda = (b['kill']+b['assist']) / b['death']
                print('-----player_id--------', b['player_id'])
                print(f'队员KDA 推送数据：{b["kda"]},计算：{player_kda}')
            print(f"队伍 gold 推送数据：{team_gold}，计算{None}")
            print(f"队伍 gold_min 推送数据：{team_gold_min}，计算{team_gold/play_time}")
            print(f"队伍 gold_diff 推送数据：{team_gold_diff}，计算{None}")
            print(f"队伍 cs 推送数据：{team_cs}，计算{player_cs}")
            print(f"队伍 cs_min 推送数据：{team_cs_min}，计算{team_cs/play_time}")
            print(f"队伍 cs_diff 推送数据：{team_cs_diff}，计算{player_cs_diff}")
            print(f"队伍 kill 推送数据：{team_kill}，计算{player_kill}")
            print(f"队伍 assist 推送数据：{team_assist}，计算{player_assist}")
            print(f"队伍 death 推送数据：{team_death}，计算{player_death}")
            if player_death == 0:
                team_kda_ = (player_kill + player_assist) / 1
            elif (player_kill + player_assist) == 0:
                team_kda_ = None
            else:
                team_kda_ = (player_kill + player_assist) / player_death
            print(f"队伍 kda 推送数据：{team_kda}，计算{team_kda_}")
            print(f"队伍 neutral_kill 推送数据：{team_neutral_kill}，计算{player_neutral_kill}")
            print(f"队伍 herald_kill 推送数据：{team_herald_kill}，计算{player_herald_kill}")
            print(f"队伍 nashor_kill 推送数据：{team_nashor_kill}，计算{player_nashor_kill}")
            print(f"队伍 elder_drake_kill 推送数据：{team_elder_drake_kill}，计算{player_elder_drake_kill}")
            print(f"队伍 drake_kill 推送数据：{team_drake_kill}，计算{player_drake_kill}")
            print(f"队伍 infernal_drake_kill 推送数据：{team_infernal_drake_kill}，计算{player_infernal_drake_kill}")
            print(f"队伍 mountain_drake_kill 推送数据：{team_mountain_drake_kill}，计算{player_mountain_drake_kill}")
            print(f"队伍 cloud_drake_kill 推送数据：{team_cloud_drake_kill}，计算{player_cloud_drake_kill}")
            print(f"队伍 ocean_drake_kill 推送数据：{team_ocean_drake_kill}，计算{player_ocean_drake_kill}")
            print(f"队伍 tower_kill 推送数据：{team_tower_kill}，计算{player_tower_kill}")
            print(f"队伍 inhibitor_kill 推送数据：{team_inhibitor_kill}，计算{player_inhibitor_kill}")
            print(f"----------------------------{i['team_id']}--------------------------------------")

    def live_data_tj(self):
        '''
            统计数据和实时数据 计算对比
        :return:
        '''
        data_tj = self.data_tj
        data = self.data
        json_data_tj = json.loads(data_tj)
        teams_data_tj = json_data_tj.get('team')
        json_data = json.loads(data)
        teams_data = json_data.get('team')
        for i in teams_data:
            print("--------team_id------------", i['team_id'])
            players_data = i.get('player')
            team_kill = i['kill']
            team_cs = i['cs']
            for y in teams_data_tj:
                y_players = y['player']
                team_kill_streak = y['kill_streak']
                player_kill_streak_list = []
                if i['team_id'] == y['team_id']:
                    for b in players_data:
                        b_player_id = b['player_id']
                        cs_ratio = b['cs'] / team_cs
                        team_fight = (b['kill'] + b['assist']) / team_kill
                        for c in y_players:
                            if b_player_id == c['player_id']:
                                print("--------player_id------------", c['player_id'])
                                player_kill_streak_list.append(c['kill_streak'])
                                print(f"队员 cs_ratio 推送数据：{c['cs_ratio']}，计算{cs_ratio}")
                                print(f"队员 team_fight 推送数据：{c['team_fight']}，计算{team_fight}")

            print(f"队员 kill_streak 推送数据：{team_kill_streak}，计算{player_kill_streak_list}")


if __name__ == '__main__':
    li = Live_lol()
    li.live_data()
    # li.live_data_tj()

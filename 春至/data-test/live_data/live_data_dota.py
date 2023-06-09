import json


class Live_dota(object):

    def __init__(self):
        self.data = '''
            {"match_id":25091,"series_id":1606925175,"stage":1,"time":2300,"team":[{"team_id":334,"gold":69100,"gold_min":"1802.00","gold_diff":-5500,"cs":1252,"cs_min":"32.66","cs_diff":-26,"kill":14,"assist":38,"death":17,"kda":"3.06","neutral_kill":3,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":1,"drake_kill":2,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":1,"ocean_drake_kill":0,"tower_kill":7,"inhibitor_kill":0,"player":[{"player_id":1121,"level":18,"hp":91,"status":2,"respawn_time":0,"item":[{"item_id":16,"is_trinket":2},{"item_id":157,"is_trinket":1},{"item_id":307,"is_trinket":1},{"item_id":252,"is_trinket":1},{"item_id":235,"is_trinket":1},{"item_id":775,"is_trinket":1},{"item_id":238,"is_trinket":1}],"spell":[{"summon_spell_id":14},{"summon_spell_id":7}],"cs":371,"cs_min":"9.68","cs_diff":-85,"kill":7,"assist":7,"death":2,"kda":"7.00","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":2,"inhibitor_kill":0},{"player_id":2198,"level":16,"hp":20,"status":2,"respawn_time":0,"item":[{"item_id":203,"is_trinket":2},{"item_id":193,"is_trinket":1},{"item_id":185,"is_trinket":1},{"item_id":273,"is_trinket":1},{"item_id":779,"is_trinket":1}],"spell":[{"summon_spell_id":7},{"summon_spell_id":5}],"cs":206,"cs_min":"5.37","cs_diff":-46,"kill":1,"assist":9,"death":3,"kda":"3.33","neutral_kill":2,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":1,"drake_kill":1,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":1,"ocean_drake_kill":0,"tower_kill":1,"inhibitor_kill":0},{"player_id":1840,"level":18,"hp":63,"status":2,"respawn_time":0,"item":[{"item_id":203,"is_trinket":2},{"item_id":193,"is_trinket":1},{"item_id":273,"is_trinket":1},{"item_id":185,"is_trinket":1},{"item_id":146,"is_trinket":1},{"item_id":781,"is_trinket":1}],"spell":[{"summon_spell_id":7},{"summon_spell_id":10}],"cs":350,"cs_min":"9.13","cs_diff":79,"kill":6,"assist":3,"death":2,"kda":"4.50","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":3,"inhibitor_kill":0},{"player_id":8712,"level":15,"hp":94,"status":2,"respawn_time":0,"item":[{"item_id":203,"is_trinket":2},{"item_id":145,"is_trinket":1},{"item_id":287,"is_trinket":1},{"item_id":134,"is_trinket":1},{"item_id":186,"is_trinket":1},{"item_id":166,"is_trinket":1},{"item_id":212,"is_trinket":1}],"spell":[{"summon_spell_id":15},{"summon_spell_id":7}],"cs":33,"cs_min":"0.86","cs_diff":1,"kill":0,"assist":8,"death":6,"kda":"1.33","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":0,"inhibitor_kill":0},{"player_id":2199,"level":18,"hp":94,"status":2,"respawn_time":0,"item":[{"item_id":203,"is_trinket":2},{"item_id":186,"is_trinket":1},{"item_id":9,"is_trinket":1},{"item_id":756,"is_trinket":1},{"item_id":176,"is_trinket":1},{"item_id":202,"is_trinket":1},{"item_id":782,"is_trinket":1}],"spell":[{"summon_spell_id":6},{"summon_spell_id":7}],"cs":292,"cs_min":"7.62","cs_diff":25,"kill":0,"assist":11,"death":4,"kda":"2.75","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":0,"inhibitor_kill":0}]},{"team_id":126202,"gold":74600,"gold_min":"1946.00","gold_diff":5500,"cs":1278,"cs_min":"33.34","cs_diff":26,"kill":17,"assist":47,"death":14,"kda":"4.57","neutral_kill":10,"herald_kill":2,"nashor_kill":3,"elder_drake_kill":1,"drake_kill":4,"infernal_drake_kill":1,"mountain_drake_kill":0,"cloud_drake_kill":1,"ocean_drake_kill":1,"tower_kill":8,"inhibitor_kill":0,"player":[{"player_id":3275,"level":18,"hp":0,"status":1,"respawn_time":9,"item":[{"item_id":16,"is_trinket":2},{"item_id":157,"is_trinket":1},{"item_id":300,"is_trinket":1},{"item_id":235,"is_trinket":1},{"item_id":771,"is_trinket":1},{"item_id":238,"is_trinket":1},{"item_id":774,"is_trinket":1}],"spell":[{"summon_spell_id":14},{"summon_spell_id":7}],"cs":456,"cs_min":"11.90","cs_diff":85,"kill":6,"assist":7,"death":2,"kda":"6.50","neutral_kill":2,"herald_kill":0,"nashor_kill":2,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":2,"inhibitor_kill":0},{"player_id":3229,"level":18,"hp":0,"status":1,"respawn_time":4,"item":[{"item_id":203,"is_trinket":2},{"item_id":174,"is_trinket":1},{"item_id":796,"is_trinket":1},{"item_id":217,"is_trinket":1},{"item_id":247,"is_trinket":1},{"item_id":273,"is_trinket":1},{"item_id":781,"is_trinket":1}],"spell":[{"summon_spell_id":7},{"summon_spell_id":5}],"cs":252,"cs_min":"6.57","cs_diff":46,"kill":6,"assist":10,"death":1,"kda":"16.00","neutral_kill":6,"herald_kill":2,"nashor_kill":1,"elder_drake_kill":0,"drake_kill":3,"infernal_drake_kill":1,"mountain_drake_kill":0,"cloud_drake_kill":1,"ocean_drake_kill":1,"tower_kill":0,"inhibitor_kill":0},{"player_id":3244,"level":18,"hp":0,"status":1,"respawn_time":9,"item":[{"item_id":16,"is_trinket":2},{"item_id":141,"is_trinket":1},{"item_id":166,"is_trinket":1},{"item_id":265,"is_trinket":1},{"item_id":269,"is_trinket":1},{"item_id":202,"is_trinket":1},{"item_id":782,"is_trinket":1}],"spell":[{"summon_spell_id":7},{"summon_spell_id":6}],"cs":271,"cs_min":"7.07","cs_diff":-79,"kill":3,"assist":9,"death":3,"kda":"4.00","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":2,"inhibitor_kill":0},{"player_id":2266,"level":15,"hp":0,"status":1,"respawn_time":52,"item":[{"item_id":203,"is_trinket":2},{"item_id":274,"is_trinket":1},{"item_id":192,"is_trinket":1},{"item_id":174,"is_trinket":1},{"item_id":8,"is_trinket":1},{"item_id":163,"is_trinket":1},{"item_id":212,"is_trinket":1}],"spell":[{"summon_spell_id":15},{"summon_spell_id":7}],"cs":32,"cs_min":"0.83","cs_diff":-1,"kill":1,"assist":14,"death":5,"kda":"3.00","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":0,"inhibitor_kill":0},{"player_id":3245,"level":18,"hp":0,"status":1,"respawn_time":4,"item":[{"item_id":203,"is_trinket":2},{"item_id":145,"is_trinket":1},{"item_id":174,"is_trinket":1},{"item_id":165,"is_trinket":1},{"item_id":265,"is_trinket":1},{"item_id":176,"is_trinket":1},{"item_id":763,"is_trinket":1}],"spell":[{"summon_spell_id":8},{"summon_spell_id":6}],"cs":267,"cs_min":"6.97","cs_diff":-25,"kill":1,"assist":7,"death":3,"kda":"2.67","neutral_kill":0,"herald_kill":0,"nashor_kill":0,"elder_drake_kill":0,"drake_kill":0,"infernal_drake_kill":0,"mountain_drake_kill":0,"cloud_drake_kill":0,"ocean_drake_kill":0,"tower_kill":1,"inhibitor_kill":0}]}]}
        '''
        self.data_tj = '''
            {"match_id":15953,"series_id":1606914775,"time":1250,"team":[{"team_id":1551,"team_fight":null,"player":[{"player_id":9895,"gold_ratio":"0.26","exp_ratio":"0.23","lh_ratio":"0.26","team_fight":"0.33"},{"player_id":8009,"gold_ratio":"0.17","exp_ratio":"0.16","lh_ratio":"0.14","team_fight":"0.67"},{"player_id":8006,"gold_ratio":"0.22","exp_ratio":"0.18","lh_ratio":"0.29","team_fight":"0.33"},{"player_id":9896,"gold_ratio":"0.11","exp_ratio":"0.12","lh_ratio":"0.00","team_fight":"0.67"},{"player_id":8119,"gold_ratio":"0.25","exp_ratio":"0.31","lh_ratio":"0.31","team_fight":"0.33"}]},{"team_id":3369,"team_fight":null,"player":[{"player_id":6566,"gold_ratio":"0.24","exp_ratio":"0.18","lh_ratio":"0.26","team_fight":"0.43"},{"player_id":7729,"gold_ratio":"0.25","exp_ratio":"0.20","lh_ratio":"0.30","team_fight":"0.29"},{"player_id":7170,"gold_ratio":"0.17","exp_ratio":"0.15","lh_ratio":"0.06","team_fight":"0.57"},{"player_id":7782,"gold_ratio":"0.26","exp_ratio":"0.32","lh_ratio":"0.36","team_fight":"0.43"},{"player_id":7110,"gold_ratio":"0.09","exp_ratio":"0.15","lh_ratio":"0.03","team_fight":"0.71"}]}]}
        '''

    def live_data(self):
        data = self.data
        json_data = json.loads(data)
        teams_data = json_data.get('team')
        # print(teams_data)
        play_time = round((json_data['time'] / 60), 2)
        for i in teams_data:
            players_data = i.get('player')
            team_gold = i['gold']
            team_gold_min = float(i['gold_min'])
            team_gold_diff = i['gold_diff']
            team_exp = i['exp']
            team_exp_min = float(i['exp_min'])
            team_exp_diff = i['exp_diff']
            team_lh = i['lh']
            team_lh_min = float(i['lh_min'])
            team_lh_diff = i['lh_diff']
            team_deny = i['deny']
            team_deny_min = float(i['deny_min'])
            team_deny_diff = i['deny_diff']
            team_kill = i['kill']
            team_assist = i['assist']
            team_death = i['death']
            team_kda = i['kda']
            team_tower_kill = i['tower_kill']
            team_barrack_kill = i['barrack_kill']
            player_gold = 0
            player_gold_min = 0
            player_gold_diff = 0
            player_exp = 0
            player_exp_min = 0
            player_exp_diff = 0
            player_lh = 0
            player_lh_min = 0
            player_lh_diff = 0
            player_deny = 0
            player_deny_min = 0
            player_deny_diff = 0
            player_kill = 0
            player_assist = 0
            player_death = 0
            for b in players_data:
                player_gold += b['gold']
                player_gold_min += float(b['gold_min'])
                player_gold_diff += b['gold_diff']
                player_exp += b['exp']
                player_exp_min += float(b['exp_min'])
                player_exp_diff += b['exp_diff']
                player_lh += b['lh']
                player_lh_min += float(b['lh_min'])
                player_lh_diff += b['lh_diff']
                player_deny += b['deny']
                player_deny_min += float(b['deny_min'])
                player_deny_diff += b['deny_diff']
                player_kill += b['kill']
                player_assist += b['assist']
                player_death += b['death']
                if b['death'] == 0:
                    player_kda = (b['kill']+b['assist']) / 1
                elif (b['kill']+b['assist']) == 0:
                    player_kda = None
                else:
                    player_kda = (b['kill']+b['assist']) / b['death']
                print('-----player_id--------', b['player_id'])
                print(f'队员KDA 推送数据：{b["kda"]},计算：{player_kda}')
                print("--------exp_diff------------", b['exp_diff'])
                print("--------deny_diff------------", b['deny_diff'])
            print(f"队伍 gold 推送数据：{team_gold}，计算{player_gold}")
            print(f"队伍 gold_min 推送数据：{team_gold_min}，计算{None}")
            print(f"队伍 gold_diff 推送数据：{team_gold_diff}，计算{player_gold_diff}")
            print(f"队伍 exp 推送数据：{team_exp}，计算{player_exp}")
            print(f"队伍 exp_min 推送数据：{team_exp_min}，计算{None}")
            print(f"队伍 exp_diff 推送数据：{team_exp_diff}，计算{player_exp_diff}")
            print(f"队伍 lh 推送数据：{team_lh}，计算{player_lh}")
            print(f"队伍 lh_min 推送数据：{team_lh_min}，计算{None}")
            print(f"队伍 lh_diff 推送数据：{team_lh_diff}，计算{player_lh_diff}")
            print(f"队伍 deny 推送数据：{team_deny}，计算{player_deny}")
            print(f"队伍 deny_min 推送数据：{team_deny_min}，计算{None}")
            print(f"队伍 deny_diff 推送数据：{team_deny_diff}，计算{player_deny_diff}")
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
            print(f"队伍 tower_kill 推送数据：{team_tower_kill}，计算{None}")
            print(f"队伍 barrack_kill 推送数据：{team_barrack_kill}，计算{None}")
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
            team_gold = i['gold']
            team_exp = i['exp']
            team_lh = i['lh']
            for y in teams_data_tj:
                y_players = y['player']
                if i['team_id'] == y['team_id']:
                    for b in players_data:
                        b_player_id = b['player_id']
                        gold_ratio = b['gold'] / team_gold
                        exp_ratio = b['exp'] / team_exp
                        lh_ratio = b['lh'] / team_lh
                        team_fight = (b['kill'] + b['assist']) / team_kill
                        for c in y_players:
                            if b_player_id == c['player_id']:
                                print("--------player_id------------", c['player_id'])
                                print(f"队员 gold_ratio 推送数据：{c['gold_ratio']}，计算{gold_ratio}")
                                print(f"队员 exp_ratio 推送数据：{c['exp_ratio']}，计算{exp_ratio}")
                                print(f"队员 lh_ratio 推送数据：{c['lh_ratio']}，计算{lh_ratio}")
                                print(f"队员 team_fight 推送数据：{c['team_fight']}，计算{team_fight}")


if __name__ == '__main__':
    li = Live_dota()
    li.live_data()
    # li.live_data_tj()

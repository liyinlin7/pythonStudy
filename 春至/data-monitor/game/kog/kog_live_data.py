import json

live_data_301 = '''
    {"series_id":1607037502,"match_id":4073,"time":968,"teams":[{"team_id":1043,"gold":null,"gold_min":"3106.25","gold_diff":1800,"kill":7,"assist":16,"death":10,"kda":"2.30","neutral_kill":1,"tyrant_kill":0,"dark_tyrant_kill":1,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"tower_kill":4,"structure_status":[{"location":1,"status":2},{"location":2,"status":2},{"location":3,"status":1},{"location":4,"status":2},{"location":5,"status":1},{"location":6,"status":1},{"location":7,"status":2},{"location":8,"status":1},{"location":9,"status":1}],"player":[{"player_id":4331,"level":14,"gold":8200,"gold_min":"512.50","gold_diff":100,"kill":1,"assist":4,"death":4,"kda":"1.25","neutral_kill":0,"tyrant_kill":0,"dark_tyrant_kill":0,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.37","y":"0.66"},"item":[{"item_id":389,"slot":0},{"item_id":67,"slot":1},{"item_id":348,"slot":2},{"item_id":427,"slot":3}],"spell":[{"summon_spell_id":19}]},{"player_id":5937,"level":3,"gold":13300,"gold_min":"831.25","gold_diff":1900,"kill":1,"assist":2,"death":1,"kda":"3.00","neutral_kill":1,"tyrant_kill":0,"dark_tyrant_kill":1,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.87","y":"0.69"},"item":[{"item_id":60,"slot":0},{"item_id":67,"slot":1},{"item_id":348,"slot":2},{"item_id":389,"slot":3},{"item_id":74,"slot":4},{"item_id":379,"slot":5}],"spell":[{"summon_spell_id":27}]},{"player_id":249828,"level":4,"gold":9200,"gold_min":"575.00","gold_diff":100,"kill":1,"assist":3,"death":1,"kda":"4.00","neutral_kill":0,"tyrant_kill":0,"dark_tyrant_kill":0,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.87","y":"0.69"},"item":[{"item_id":63,"slot":0},{"item_id":381,"slot":1},{"item_id":62,"slot":2},{"item_id":393,"slot":3},{"item_id":411,"slot":4},{"item_id":410,"slot":5}],"spell":[{"summon_spell_id":19}]},{"player_id":249825,"level":15,"gold":12600,"gold_min":"787.50","gold_diff":500,"kill":4,"assist":2,"death":3,"kda":"2.00","neutral_kill":0,"tyrant_kill":0,"dark_tyrant_kill":0,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.27","y":"0.13"},"item":[{"item_id":70,"slot":0},{"item_id":67,"slot":1},{"item_id":71,"slot":2},{"item_id":72,"slot":3},{"item_id":403,"slot":4},{"item_id":385,"slot":5}],"spell":[{"summon_spell_id":24}]},{"player_id":249826,"level":14,"gold":6500,"gold_min":"406.25","gold_diff":-1000,"kill":0,"assist":5,"death":1,"kda":"5.00","neutral_kill":0,"tyrant_kill":0,"dark_tyrant_kill":0,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.24","y":"0.23"},"item":[{"item_id":349,"slot":0},{"item_id":67,"slot":1},{"item_id":421,"slot":2},{"item_id":419,"slot":4},{"item_id":416,"slot":5}],"spell":[{"summon_spell_id":22}]}]},{"team_id":2274,"gold":null,"gold_min":"2993.75","gold_diff":-1800,"kill":10,"assist":23,"death":7,"kda":"4.71","neutral_kill":1,"tyrant_kill":0,"dark_tyrant_kill":1,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"tower_kill":4,"structure_status":[{"location":1,"status":2},{"location":2,"status":1},{"location":3,"status":1},{"location":4,"status":2},{"location":5,"status":1},{"location":6,"status":1},{"location":7,"status":2},{"location":8,"status":2},{"location":9,"status":1}],"player":[{"player_id":249835,"level":8,"gold":8100,"gold_min":"506.25","gold_diff":-100,"kill":0,"assist":4,"death":1,"kda":"4.00","neutral_kill":0,"tyrant_kill":0,"dark_tyrant_kill":0,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.45","y":"0.10"},"item":[{"item_id":388,"slot":0},{"item_id":67,"slot":1},{"item_id":391,"slot":2},{"item_id":384,"slot":3},{"item_id":396,"slot":4},{"item_id":361,"slot":5}],"spell":[{"summon_spell_id":19}]},{"player_id":249837,"level":12,"gold":11400,"gold_min":"712.50","gold_diff":-1900,"kill":3,"assist":2,"death":2,"kda":"2.50","neutral_kill":0,"tyrant_kill":0,"dark_tyrant_kill":0,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.79","y":"0.28"},"item":[{"item_id":59,"slot":0},{"item_id":348,"slot":1},{"item_id":67,"slot":2},{"item_id":389,"slot":3},{"item_id":74,"slot":4},{"item_id":379,"slot":5}],"spell":[{"summon_spell_id":27}]},{"player_id":4768,"level":1,"gold":9100,"gold_min":"568.75","gold_diff":-100,"kill":3,"assist":5,"death":2,"kda":"4.00","neutral_kill":0,"tyrant_kill":0,"dark_tyrant_kill":0,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.67","y":"0.28"},"item":[{"item_id":63,"slot":0},{"item_id":381,"slot":1},{"item_id":62,"slot":2},{"item_id":402,"slot":3},{"item_id":385,"slot":4},{"item_id":395,"slot":5}],"spell":[{"summon_spell_id":19}]},{"player_id":256929,"level":8,"gold":12100,"gold_min":"756.25","gold_diff":-500,"kill":4,"assist":4,"death":1,"kda":"8.00","neutral_kill":0,"tyrant_kill":0,"dark_tyrant_kill":0,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.68","y":"0.59"},"item":[{"item_id":71,"slot":0},{"item_id":67,"slot":1},{"item_id":72,"slot":2},{"item_id":70,"slot":3},{"item_id":403,"slot":4}],"spell":[{"summon_spell_id":19}]},{"player_id":249838,"level":6,"gold":7500,"gold_min":"468.75","gold_diff":1000,"kill":0,"assist":8,"death":1,"kda":"8.00","neutral_kill":1,"tyrant_kill":0,"dark_tyrant_kill":1,"prophet_overlord_kill":0,"overlord_kill":0,"storm_dragon_kill":0,"location":{"x":"0.40","y":"0.04"},"item":[{"item_id":404,"slot":0},{"item_id":67,"slot":1},{"item_id":384,"slot":2},{"item_id":416,"slot":3},{"item_id":417,"slot":4},{"item_id":349,"slot":5}],"spell":[{"summon_spell_id":22}]}]}]}
'''

live_data_302 = '''
    {"match_id":4073,"series_id":1607037502,"time":968,"team":[{"team_id":1043,"multi_kill":0,"kill_streak":0,"team_fight":"3.29","player":[{"player_id":4331,"gold_ratio":"0.16","multi_kill":null,"kill_streak":null,"team_fight":"0.71"},{"player_id":5937,"gold_ratio":"0.27","multi_kill":null,"kill_streak":null,"team_fight":"0.43"},{"player_id":249828,"gold_ratio":"0.18","multi_kill":null,"kill_streak":null,"team_fight":"0.57"},{"player_id":249825,"gold_ratio":"0.25","multi_kill":null,"kill_streak":null,"team_fight":"0.86"},{"player_id":249826,"gold_ratio":"0.13","multi_kill":null,"kill_streak":null,"team_fight":"0.71"}]},{"team_id":2274,"multi_kill":0,"kill_streak":0,"team_fight":"3.30","player":[{"player_id":249835,"gold_ratio":"0.17","multi_kill":null,"kill_streak":null,"team_fight":"0.40"},{"player_id":249837,"gold_ratio":"0.24","multi_kill":null,"kill_streak":null,"team_fight":"0.50"},{"player_id":4768,"gold_ratio":"0.19","multi_kill":null,"kill_streak":null,"team_fight":"0.80"},{"player_id":256929,"gold_ratio":"0.25","multi_kill":null,"kill_streak":null,"team_fight":"0.80"},{"player_id":249838,"gold_ratio":"0.16","multi_kill":null,"kill_streak":null,"team_fight":"0.80"}]}]}
'''
data_301 = json.loads(live_data_301)
data_302 = json.loads(live_data_302)


def live_data_302():
    players_list = []
    team_list = data_302['team']
    playes_map_list = []
    for i in team_list:
        player_lists = i['player']
        for player in player_lists:
            map_ = {}
            players_list.append(player['player_id'])
            map_['player_id'] = player['player_id']
            map_['gold_ratio'] = player['gold_ratio']
            map_['team_fight'] = player['team_fight']
            playes_map_list.append(map_)
    print(playes_map_list)
    print(players_list)
    return players_list, playes_map_list


def live_data_301():
    players_list, playes_map_list = live_data_302()
    team_list = data_301['teams']
    time = data_301['time']
    for item in team_list:
        team_kill = item['kill']
        if item['gold'] is None:
            team_gold = 0
        else:
            team_gold = item['gold']
        player_lists = item['player']
        print('#################队伍数据，队伍id:', item['team_id'], '################')
        if item['gold'] == 0 or item['gold'] is None:
            print('[队伍经济/分钟]:', item['gold_min'], '[计算得出的结果]:', 0 / (time / 60))
        else:
            print('[队伍经济/分钟]:', item['gold_min'], '[计算得出的结果]:', format(team_gold / (time / 60), '.2f'))

        for player in player_lists:
            print('###############队员的id: ', player['player_id'], '########################')
            if item['death'] != 0:
                kda = (player['kill'] + player['assist']) / player['death']
            else:
                kda = (player['kill'] + player['assist']) / 1
            print('[队员的kda]:', player['kda'], "[计算得出的结果]:", format(kda, '.2f'))
            print('[队员的平均时间经济]:', player['gold_min'], '[计算得出的结果]:', format((player['gold']) / (time / 60), '.2f'))
            for i in players_list:
                if i == player['player_id']:
                    for y in playes_map_list:
                        if y.get('player_id') == i:
                            # print(y)
                            gold_ratio = y.get('gold_ratio')
                            team_fight = y.get('team_fight')
                            if team_gold == 0:
                                print("gold_ratio实时统计的数据是：", gold_ratio, '实时数据的队伍gold是0')
                            else:
                                print("gold_ratio实时统计的数据是：", gold_ratio, '根据实时计算的数据是：', format(player['gold'] / team_gold, '.2f'))
                            print("team_fight实时统计的数据是：", team_fight, '根据实时计算的数据是：', format((player['kill'] + player['assist']) / team_kill, '.2f'))


if __name__ == '__main__':
    live_data_301()
    # live_data_302()

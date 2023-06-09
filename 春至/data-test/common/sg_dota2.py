from common.do_mongoDB import MongoDB

# 计算数据前需要记录
match_id = 716  # 小局ID
dataBase = 'data-center'
collection = 'dota_result'
team_id_z = 2488  # 主队ID
team_id_k = 3361  # 客队ID
time = round((1571/60), 2)   # 比赛时长


# 获取数据
def get_data(match_id, dataBase, collection):
    myDb = MongoDB()
    collect = myDb.connect(dataBase, collection, status=0)  # status=0 是测试环境数据库
    sen = '{"match_id":' + str(match_id) + '}'
    result = myDb.select_data_one(collect, sen)
    return result


def team_cal(data, team_id):
    team_data = data['data']
    for item in team_data:
        if item['team_id'] == team_id:
            player_data = item['player']
            p_gold = 0
            p_exp = 0
            p_lh = 0
            p_deny = 0
            p_rune = []
            p_observer = 0
            p_sentry = 0
            p_observer_kill = 0
            p_sentry_kill = 0
            p_kill = 0
            p_assist = 0
            p_death = 0
            p_double = 0
            p_triple = 0
            p_ultra = 0
            p_rampage = 0
            p_kill_streak = []
            p_team_fight = 0
            p_damage = 0
            p_hero_damage = 0
            p_tower_damage = 0
            p_damage_taken = 0
            p_heal = 0
            p_courier_kill = 0
            p_neutral_kill = 0
            p_ancient_kill = 0
            p_rs_kill = 0
            p_tower_kill = 0
            p_barrack_kill = 0
            p_buyback_count = 0
            p_smoke_of_deceit_count = 0
            for player in player_data:
                p_gold = p_gold + player['gold']
                p_exp = p_exp + player['exp']
                p_lh = p_lh + player['lh']
                p_deny = p_deny + player['deny']
                p_observer = p_observer + player['observer']
                p_sentry = p_sentry + player['sentry']
                p_observer_kill = p_observer_kill + player['observer_kill']
                p_sentry_kill = p_sentry_kill + player['sentry_kill']
                p_kill = p_kill + player['kill']
                p_assist = p_assist + player['assist']
                p_death = p_death + player['death']
                p_double = p_double + player['double']
                p_triple = p_triple + player['triple']
                p_ultra = p_ultra + player['ultra']
                p_rampage = p_rampage + player['rampage']
                p_kill_streak.append(player['kill_streak'])
                p_team_fight = p_team_fight + float(player['team_fight'])
                p_damage = p_damage + player['damage']
                p_hero_damage = p_hero_damage + player['hero_damage']
                p_tower_damage = p_tower_damage + player['tower_damage']
                p_damage_taken = p_damage_taken + player['damage_taken']
                p_heal = p_heal + player['heal']
                p_courier_kill = p_courier_kill + player['courier_kill']
                p_neutral_kill = p_neutral_kill + player['neutral_kill']
                p_ancient_kill = p_ancient_kill + player['ancient_kill']
                p_rs_kill = p_rs_kill + player['rs_kill']
                p_tower_kill = p_tower_kill + player['tower_kill']
                # p_barrack_kill = p_barrack_kill + player['barrack_kill']
                p_buyback_count = p_buyback_count + player['buyback_count']
                p_smoke_of_deceit_count = p_smoke_of_deceit_count + player['smoke_of_deceit_count']

                # p_damage_taken_death_ratio = p_damage_taken_death_ratio + float(player['damage_taken_death_ratio'])
                # p_damage_taken_gold_ratio = p_damage_taken_gold_ratio + float(player['damage_taken_gold_ratio'])
            p_tower_location = []
            p_barrack_location = []
            for t_location in item['tower_location']:
                p_tower_location.append(t_location)
            for b_location in item['barrack_location']:
                p_barrack_location.append(b_location)
            print('#################队伍数据，队伍id:', team_id, '################')
            print(time)
            print('[队伍总经济]:', item['gold'], '[计算得出的结果]:', p_gold)
            print('[队伍经济/分钟]:', item['gold_min'], '[计算得出的结果]:', format(p_gold / time, '.2f'))
            print('[队伍经济差]:', item['gold_diff'], '[计算得出的结果]:')
            print('[队伍总经验]:', item['exp'], '[计算得出的结果]:', p_exp)
            print('[队伍经验/分钟]:', item['exp_min'], '[计算得出的结果]:', format(p_exp / time, '.2f'))
            print('[队伍经验差]:', item['exp_diff'], '[计算得出的结果]:')
            print('[队伍总正补刀]:', item['lh'], '[计算得出的结果]:', p_lh)
            print('[队伍正补刀/分钟]:', item['lh_min'], '[计算得出的结果]:', format(p_lh / time, '.2f'))
            print('[队伍正补刀差]:', item['lh_diff'], '[计算得出的结果]:')
            print('[队伍总反补刀]:', item['deny'], '[计算得出的结果]:', p_deny)
            print('[队伍反补刀/分钟]:', item['deny_min'], '[计算得出的结果]:', format(p_deny / time, '.2f'))
            print('[队伍反补刀差]:', item['deny_diff'])
            print('[队伍英雄总击杀数]:', item['kill'], '[计算得出的结果]:', p_kill)
            print('[队伍英雄总助攻数]:', item['assist'], '[计算得出的结果]:', p_assist)
            print('[队伍英雄总死亡数]:', item['death'], '[计算得出的结果]:', p_death)
            if p_death == 0:
                print('[队伍kda]:', item['kda'], '[计算得出的结果]: ', format((p_kill + p_assist) / 1, '.2f'))
            else:
                print('[队伍kda]:', item['kda'], '[计算得出的结果]: ', format((p_kill + p_assist) / p_death, '.2f'))
            print('[队伍双杀次数]:', item['double'], '[计算得出的结果]:', p_double)
            print('[队伍三杀次数]:', item['triple'], '[计算得出的结果]:', p_triple)
            print('[队伍四杀次数]:', item['ultra'], '[计算得出的结果]:', p_ultra)
            print('[队伍五杀次数]:', item['rampage'], '[计算得出的结果]:', p_rampage)
            print('[队伍最大连续击杀]:', item['kill_streak'], '[计算得出的结果]:', p_kill_streak)
            print('[平均队员参团率]:', item['team_fight'], '[计算得出的结果]:', format(p_team_fight / 5, '.2f'))
            print('[队伍总输出]:', item['damage'], '[计算得出的结果]:', p_damage)
            print('[队伍对英雄造成的总输出]:', item['hero_damage'], '[计算得出的结果]:', p_hero_damage)
            # print('[队伍建筑总输出]:', item['structure_damage'], '[计算得出的结果]:', p_structure_damage)
            print('[队伍输出/分钟]:', item['damage_min'], '[计算得出的结果]:', format(p_damage / time, '.2f'))
            print('[平均队员输出]:', item['avg_player_damage'], '[计算得出的结果]:', format(p_damage / 5, '.2f'))
            if p_death == 0:
                print('[队伍平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format(p_hero_damage / 1, '.2f'))
            else:
                print('[队伍平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format(p_hero_damage / p_kill, '.2f'))
            print('[队伍输出经济比]:', item['damage_gold_ratio'], '[计算得出的结果]:', format(p_hero_damage / p_gold, '.2f'))
            print('[队伍治疗总量]:', item['heal'], '[计算得出的结果]:', p_heal)
            print('[队伍治疗量/分钟]:', item['heal_min'], '[计算得出的结果]:', format(p_heal / time, '.2f'))
            print('[平均队员治疗量]:', item['avg_player_heal'], '[计算得出的结果]:', format(p_heal / 5, '.2f'))
            print('[队伍摧毁塔总数]:', item['tower_kill'])
            print('[队伍摧毁塔位置]:', item['tower_location'], '[计算得出的结果]:', p_tower_location)
            print('[队伍摧毁兵营总数]:', item['barrack_kill'])
            print('[队伍摧毁兵营位置]:', item['barrack_location'], '[计算得出的结果]:', p_barrack_location)
            # print('[队伍总承伤]:', item['damage_taken'], '[计算得出的结果]:', p_damage_taken)
            # print('[队伍承伤/分钟]:', item['damage_taken_min'], '[计算得出的结果]:', format(p_damage_taken / time, '.2f'))
            # print('[平均队员承伤]:', item['avg_player_damage_taken'], '[计算得出的结果]:', format(p_damage_taken / 5, '.2f'))
            # print('[队伍平均死亡承伤]:', item['damage_taken_death_ratio'], '[计算得出的结果]:', format(p_damage_taken_death_ratio / 5, '.2f'))
            # # print('[队伍承伤经济比例]:', item['damage_taken_gold_ratio'], '[计算得出的结果]:', format(p_damage_taken_gold_ratio / 5, '.2f'))
            # print('[队伍暴君击杀数]:', item['pharaoh_kill'])
            # print('[队伍主宰击杀数]:', item['master_kill'])

def player_cal(data, team_id):
    team_data = data['data']
    for item in team_data:
        if item['team_id'] == team_id:
            # 队员计算需要用到的队伍数据
            player_data = item['player']
            team_gold = item['gold']
            team_kill = item['kill']
            team_exp = item['exp']
            team_lh = item['lh']
            team_deny = item['deny']
            team_heal = item['heal']
            team_death = item['death']
            team_damage = item['damage']
            team_hero_damage = item['hero_damage']
    for item in player_data:
        print('###############队员的id: ', item['player_id'], '########################')
        print(time)
        print('[队员等级]:', item['level'])
        print('[队员的装备]:', item['item'])
        # print('[队员的技能信息]:', item['spell'], )
        print('[队员的经济]:', item['gold'])
        print('[队员的平均时间经济]:', item['gold_min'], '[计算得出的结果]:', format((item['gold']) / time, '.2f'))
        print('[队员的对位经济差]:', item['gold_diff'], '[计算得出的结果]:')
        print('[队员经济占队伍总经济比例]:', item['gold_ratio'], '[计算得出的结果]:', format( (item['gold']) / team_gold, '.2f'))
        print('[队员经验]:', item['exp'])
        print('[队员经验/分钟]:', item['exp_min'], '[计算得出的结果]:', format((item['exp']) / time, '.2f'))
        print('[队员对位经验差]:', item['exp_diff'], '[计算得出的结果]:')
        print('[队员经验占队伍总经验比例]:', item['exp_ratio'], '[计算得出的结果]:', format(item['exp'] / team_exp, '.2f'))
        print('[队员总正补刀]:', item['lh'])
        print('[队员正补刀/分钟]:', item['lh_min'], '[计算得出的结果]:', format(item['lh'] / time, '.2f'))
        print('[队员对位正补刀差]:', item['lh_diff'], '[计算得出的结果]:')
        print('[队员正补刀占队伍总补刀比例]:', item['lh_ratio'], '[计算得出的结果]:', format(item['lh'] / team_lh, '.2f'))
        print('[队员总反补刀]:', item['deny'])
        print('[队员反补刀/分钟]:', item['deny_min'], '[计算得出的结果]:', format(item['deny'] / time, '.2f'))
        print('[队员对位反补刀差]:', item['deny_diff'], '[计算得出的结果]:')
        print('[队员反补刀占队伍总反补刀比例]:', item['deny_ratio'], '[计算得出的结果]:', format(item['deny'] / team_deny, '.2f'))

        print('[队员插假眼数]:', item['observer'])
        print('[队员插真眼数]:', item['sentry'])
        print('[队员排假眼数]:', item['observer_kill'])
        print('[队员排真眼数]:', item['sentry_kill'])

        print('[队员英雄击杀数，助攻数，死亡数]:', item['kill'], item['assist'], item['death'])
        # kda 计算方式
        if item['death'] != 0:
            kda = (item['kill'] + item['assist']) / item['death']
            print('[队员的kda]:', item['kda'], "[计算得出的结果]:", format(kda, '.2f'))
        else:
            kda = (item['kill'] + item['assist']) / 1
            print('[队员的kda]:', item['kda'], "[计算得出的结果]:", format(kda, '.2f'))

        print('[队员双杀、三杀、四杀、五杀、连杀次数]:', item['double'], item['triple'], item['ultra'], item['rampage'], item['kill_streak'])
        print('[队员参团率]:', item['team_fight'], '[计算得出的结果]:', format((item['kill'] + item['assist']) / team_kill, '.2f'))
        print('[队员总输出]:', (item['damage']))
        print('[队员对英雄造成的总输出]:', item['hero_damage'])
        print('[队员塔输出]:', item['tower_damage'])

        print('[队员输出/分钟]:', item['damage_min'], '[计算得出的结果]:', format((item['hero_damage']) / time, '.2f'))
        print('[队员输出占比]:', item['damage_ratio'], '[计算得出的结果]:', format((item['hero_damage']) / team_hero_damage, '.2f'))
        if item['kill'] == 0:
            print('[队员平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format((item['hero_damage']) / 1, '.2f'))
        else:
            print('[队员平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format((item['hero_damage']) / item['kill'], '.2f'))
        print('[队员输出经济比例]:', item['damage_gold_ratio'], '[计算得出的结果]:', format((item['hero_damage']) / item['gold'], '.2f'))
        print('[队员承伤]:', item['damage_taken'])
        print('[队员治疗量]:', item['heal'])
        print('[队员治疗量/分钟]:', item['heal_min'], '[计算得出的结果]:', format((item['heal']) / time, '.2f'))
        if team_heal == 0:
            print('[队员治疗量占比]:', item['heal_ratio'], '[计算得出的结果]:', format((item['heal']) / 1, '.2f'))
        else:

            print('[队员治疗量占比]:', item['heal_ratio'], '[计算得出的结果]:', format((item['heal']) / team_heal, '.2f'))

        print('[队员信使击杀数]:', item['courier_kill'])
        print('[队员中立生物总击杀数]:', item['neutral_kill'])
        print('[队员远古击杀数]:', item['ancient_kill'])
        print('[队员肉山击杀数]:', item['rs_kill'])
        print('[队员摧毁塔数]:', item['tower_kill'])
        print('[队员买活次数]:', item['buyback_count'])
        print('[队员使用诡计之雾次数]:', item['smoke_of_deceit_count'])


if __name__ == '__main__':
    data = get_data(match_id, dataBase, collection)
    print('###############主队队伍id:', team_id_z, '########################')
    player_cal(data, team_id_z)
    player_cal(data, team_id_k)
    team_cal(data, team_id_z)
    team_cal(data, team_id_k)

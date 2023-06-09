from common.do_mongoDB import MongoDB

# 计算数据前需要记录
match_id = 7723  # 小局ID
dataBase = 'data-center'
collection = 'lol_result'
team_id_z = 5472  # 主队ID
team_id_k = 5782  # 客队ID
time = round((1576/60), 2)   # 比赛时长


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
            p_cs = 0
            p_ward = 0
            p_ward_kill = 0
            p_kill = 0
            p_exp = 0
            p_lh = 0
            p_deny = 0
            p_assist = 0
            p_death = 0
            p_double = 0
            p_triple = 0
            p_quadra = 0
            p_penta = 0
            p_fight = 0
            p_damage = 0
            p_physical_damage = 0
            p_magical_damage = 0
            p_true_damage = 0
            p_hero_damage = 0
            p_structure_damage = 0
            p_heal = 0
            p_damage_kill_ratio = 0
            p_damage_gold_ratio = 0
            p_damage_taken = 0
            p_physical_damage_taken = 0
            p_true_damage_taken = 0
            p_neutral_kill = 0
            p_self_neutral_kill = 0
            p_enemy_neutral_kill = 0
            p_herald_kill = 0
            p_nashor_kill = 0
            p_elder_drake_kill = 0
            p_drake_kill = 0
            p_infernal_drake_kill = 0
            p_mountain_drake_kill = 0
            p_cloud_drake_kill = 0
            p_ocean_drake_kill = 0
            p_tower_kill = 0
            p_inhibitor_kill = 0
            for player in player_data:
                p_gold = p_gold + player['gold']
                p_cs = p_cs + player['cs']
                p_ward = p_ward + player['ward']
                p_ward_kill = p_ward_kill + player['ward_kill']
                p_kill = p_kill + player['kill']
                p_assist = p_assist + player['assist']
                p_death = p_death + player['death']
                # p_exp = p_exp + player['exp']
                # p_lh = p_lh + player['lh']
                # p_deny = p_deny + player['deny']
                p_double = p_double + player['double']
                p_triple = p_triple + player['triple']
                p_quadra = p_quadra + player['quadra']
                p_penta = p_penta + player['penta']
                p_fight = p_fight + float(player['team_fight'])
                p_damage = p_damage + player['damage']
                p_physical_damage = p_physical_damage + player['physical_damage']
                p_magical_damage = p_magical_damage + player['magical_damage']
                p_true_damage = p_true_damage + player['true_damage']
                p_hero_damage = p_hero_damage + player['hero_damage']
                # p_structure_damage = p_structure_damage + player['structure_damage']
                p_heal = p_heal + player['heal']
                p_damage_kill_ratio = p_damage_kill_ratio + float(player['damage_kill_ratio'])
                p_damage_gold_ratio = p_damage_gold_ratio + float(player['damage_gold_ratio'])
                p_damage_taken = p_damage_taken + player['damage_taken']
                p_physical_damage_taken = p_physical_damage_taken + player['physical_damage_taken']
                p_true_damage_taken = p_true_damage_taken + player['true_damage_taken']
                p_neutral_kill = p_neutral_kill + player['neutral_kill']
                p_self_neutral_kill = p_self_neutral_kill + player['self_neutral_kill']
                p_enemy_neutral_kill = p_enemy_neutral_kill + player['enemy_neural_kill']
                if player['herald_kill'] is None:
                    player['herald_kill'] = 0
                p_herald_kill = p_herald_kill + player['herald_kill']
                if player['nashor_kill'] is None:
                    player['nashor_kill'] = 0
                p_nashor_kill = p_nashor_kill + player['nashor_kill']
                if player['elder_drake_kill'] is None:
                    player['elder_drake_kill'] = 0
                p_elder_drake_kill = p_elder_drake_kill + player['elder_drake_kill']
                if player['drake_kill'] is None:
                    player['drake_kill'] = 0
                p_drake_kill = p_drake_kill + player['drake_kill']
                if player['infernal_drake_kill'] is None:
                    player['infernal_drake_kill'] = 0
                p_infernal_drake_kill = p_infernal_drake_kill + player['infernal_drake_kill']
                if player['mountain_drake_kill'] is None:
                    player['mountain_drake_kill'] = 0
                p_mountain_drake_kill = p_mountain_drake_kill + player['mountain_drake_kill']
                if player['cloud_drake_kill'] is None:
                    player['cloud_drake_kill'] = 0
                p_cloud_drake_kill = p_cloud_drake_kill + player['cloud_drake_kill']
                if player['ocean_drake_kill'] is None:
                    player['ocean_drake_kill'] = 0
                p_ocean_drake_kill = p_ocean_drake_kill + player['ocean_drake_kill']
                if player['tower_kill'] is None:
                    player['tower_kill'] = 0
                p_tower_kill = p_tower_kill + player['tower_kill']
                if player['inhibitor_kill'] is None:
                    player['inhibitor_kill'] = 0
                p_inhibitor_kill = p_inhibitor_kill + player['inhibitor_kill']
            p_tower_location = []
            p_barrack_location = []
            # for t_location in item['tower_location']:
            #     p_tower_location.append(t_location)
            # for b_location in item['barrack_location']:
            #     p_barrack_location.append(b_location)
            print('#################队伍数据，队伍id:', team_id, '################')
            print(time)
            print('[队伍总经济]:', item['gold'], '[计算得出的结果]:', p_gold)
            print('[队伍经济/分钟]:', item['gold_min'], '[计算得出的结果]:', format(p_gold / time, '.2f'))
            print('[队伍经济差]:', item['gold_diff'], '[计算得出的结果]:')
            print('[队伍总补刀]:', item['cs'], '[计算得出的结果]:', p_cs)
            print('[队伍补刀/分钟]:', item['cs_min'], '[计算得出的结果]:', format(p_cs / time, '.2f'))
            print('[队伍插眼总数]:', item['ward'], '[计算得出的结果]:', p_ward)
            print('[队伍排眼总数]:', item['ward_kill'], '[计算得出的结果]:', p_ward_kill)
            print('[队伍插眼数/分钟]:', item['ward_min'], '[计算得出的结果]:', format(p_ward / time, '.2f'))
            print('[队伍拆眼数/分钟]:', item['ward_kill_min'], '[计算得出的结果]:', format(p_ward_kill / time, '.2f'))
            print('[队伍英雄总击杀数]:', item['kill'], '[计算得出的结果]:', p_kill)
            print('[队伍英雄总助攻数]:', item['assist'], '[计算得出的结果]:', p_assist)
            print('[队伍英雄总死亡数]:', item['death'], '[计算得出的结果]:', p_death)
            if p_death == 0:
                print('[队伍kda]:', item['kda'], '[计算得出的结果]: ', format((p_kill + p_assist) / 1, '.2f'))
            else:
                print('[队伍kda]:', item['kda'], '[计算得出的结果]: ', format((p_kill + p_assist) / p_death, '.2f'))
            print('[队伍双杀次数]:', item['double'], '[计算得出的结果]:', p_double)
            print('[队伍三杀次数]:', item['triple'], '[计算得出的结果]:', p_triple)
            print('[队伍四杀次数]:', item['quadra'], '[计算得出的结果]:', p_quadra)
            print('[队伍五杀次数]:', item['penta'], '[计算得出的结果]:', p_penta)
            print('[队伍最大连续击杀]:', item['kill_streak'], '[计算得出的结果]:')
            print('[平均队员参团率]:', item['team_fight'], '[计算得出的结果]:', format(p_fight / 5, '.2f'))
            print('[队伍总输出]:', item['damage'], '[计算得出的结果]:', p_damage)
            print('[队伍对英雄造成的总输出]:', item['hero_damage'], '[计算得出的结果]:', p_hero_damage)
            print('[队伍物理总输出]:', item['physical_damage'], '[计算得出的结果]:', p_physical_damage)
            print('[队伍魔法总输出]:', item['magical_damage'], '[计算得出的结果]:', p_magical_damage)
            print('[队伍真实总输出]:', item['true_damage'], '[计算得出的结果]:', p_true_damage)
            print('[队伍输出/分钟]:', item['damage_min'], '[计算得出的结果]:', format(p_hero_damage / time, '.2f'))
            print('[平均队员输出]:', item['avg_player_damage'], '[计算得出的结果]:', format(p_damage / 5, '.2f'))
            if p_death == 0:
                print('[队伍平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format(p_hero_damage / 1, '.2f'))
            else:
                print('[队伍平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format(p_hero_damage / p_kill, '.2f'))
            print('[队伍输出经济比]:', item['damage_gold_ratio'], '[计算得出的结果]:', format(p_hero_damage / p_gold, '.2f'))
            print('[队伍总承伤]:', item['damage_taken'], '[计算得出的结果]:', p_damage_taken)
            print('[队伍物理总承伤]:', item['physical_damage_taken'], '[计算得出的结果]:', p_physical_damage_taken)
            print('[队伍真实总承伤]:', item['true_damage_taken'], '[计算得出的结果]:', p_true_damage_taken)
            print('[队伍承伤/分钟]:', item['damage_taken_min'], '[计算得出的结果]:', format(p_damage_taken / time, '.2f'))
            print('[平均队员承伤]:', item['avg_player_damage_taken'], '[计算得出的结果]:', format(p_damage_taken / 5, '.2f'))
            print('[队伍平均死亡承伤]:', item['damage_taken_death_ratio'], '[计算得出的结果]:', format(p_damage_taken / p_death, '.2f'))
            print('[队伍承伤经济比例]:', item['damage_taken_gold_ratio'], '[计算得出的结果]:', format(p_damage_taken / p_gold, '.2f'))
            print('[队伍治疗总量]:', item['heal'], '[计算得出的结果]:', p_heal)
            print('[队伍治疗量/分钟]:', item['heal_min'], '[计算得出的结果]:', format(p_heal / time, '.2f'))
            print('[平均队员治疗量]:', item['avg_player_heal'], '[计算得出的结果]:', format(p_heal / 5, '.2f'))
            print('[队伍中立生物总击杀数]:', item['neutral_kill'], '[计算得出的结果]:', p_neutral_kill)
            print('[队伍己方野区中立生物总击杀数]:', item['self_neutral_kill'], '[计算得出的结果]:', p_self_neutral_kill)
            print('[队伍敌方野区中立生物总击杀数]:', item['enemy_neural_kill'], '[计算得出的结果]:', p_enemy_neutral_kill)
            print('[队伍峡谷先锋总击杀数]:', item['herald_kill'], '[计算得出的结果]:', p_herald_kill)
            print('[队伍大龙（纳什男爵）总击杀数]:', item['nashor_kill'], '[计算得出的结果]:', p_nashor_kill)
            print('[队伍远古巨龙总击杀数]:', item['elder_drake_kill'], '[计算得出的结果]:', p_elder_drake_kill)
            print('[队伍小龙总击杀数]:', item['drake_kill'], '[计算得出的结果]:', p_drake_kill)
            print('[队伍炼狱亚龙总击杀数]:', item['infernal_drake_kill'], '[计算得出的结果]:', p_infernal_drake_kill)
            print('[队伍山脉亚龙总击杀数]:', item['mountain_drake_kill'], '[计算得出的结果]:', p_mountain_drake_kill)
            print('[队伍云端亚龙总击杀数]:', item['cloud_drake_kill'], '[计算得出的结果]:', p_cloud_drake_kill)
            print('[队伍海洋亚龙总击杀数]:', item['ocean_drake_kill'], '[计算得出的结果]:', p_ocean_drake_kill)
            print('[队伍摧毁塔总数]:', item['tower_kill'], '[计算得出的结果]:', p_tower_kill)
            print('[队伍摧毁水晶总数]:', item['inhibitor_kill'], '[计算得出的结果]:', p_inhibitor_kill)


def player_cal(data, team_id):
    team_data = data['data']
    for item in team_data:
        if item['team_id'] == team_id:
            # 队员计算需要用到的队伍数据
            player_data = item['player']
            team_gold = item['gold']
            team_kill = item['kill']
            team_cs = item['cs']
            # team_exp = item['exp']
            # team_lh = item['lh']
            # team_deny = item['deny']
            team_heal = item['heal']
            team_death = item['death']
            # team_damage = item['damage']
            team_damage_taken = item['damage_taken']
            team_hero_damage = item['hero_damage']
    for item in player_data:
        print('###############队员的id: ', item['player_id'], '########################')
        print(time)
        print('[队员等级]:', item['level'])
        print('[队员的装备]:', item['item'])
        print('[队员的技能信息]:', item['spell'] )
        print('[队员的经济]:', item['gold'], )
        print('[队员的平均时间经济]:', item['gold_min'], '[计算得出的结果]:', format((item['gold']) / time, '.2f'))
        print('[队员的对位经济差]:', item['gold_diff'], '[计算得出的结果]:')
        print('[队员经济占队伍总经济比例]:', item['gold_ratio'], '[计算得出的结果]:', format((item['gold'] / team_gold), '.2f'))
        print('[队员补刀数]:', item['cs'])
        print('[队员补刀/分钟]:', item['cs_min'], '[计算得出的结果]:', format((item['cs']) / time, '.2f'))
        print('[队员对位补刀差]:', item['cs_diff'], '[计算得出的结果]:')
        print('[队员补刀占队伍总补刀比例]:', item['cs_ratio'], '[计算得出的结果]:', format((item['cs'] / team_cs), '.2f'))
        print('[队员插眼数]:', item['ward'])
        print('[队员排眼数]:', item['ward_kill'])
        print('[队员分均插眼数]:', item['ward_min'], '[计算得出的结果]:', format((item['ward']) / time, '.2f'))
        print('[队员分均排眼数]:', item['ward_kill_min'], '[计算得出的结果]:', format((item['ward_kill']) / time, '.2f'))
        print('[队员英雄击杀数]:', item['kill'])
        print('[队员英雄助攻数]:', item['assist'])
        print('[队员英雄死亡数]:', item['death'])
        if item['death'] != 0:
            kda = (item['kill'] + item['assist']) / item['death']
        else:
            kda = (item['kill'] + item['assist']) / 1
        print('[队员的kda]:', item['kda'], "[计算得出的结果]:", format(kda, '.2f'))
        print('[队员双杀、三杀、四杀、五杀、连杀次数]:', item['double'], item['triple'], item['quadra'], item['penta'], item['kill_streak'])
        print('[队员参团率]:', item['team_fight'], '[计算得出的结果]:', format((item['kill'] + item['assist']) / team_kill, '.2f'))
        print('[队员物理输出]:', item['physical_damage'])
        print('[队员魔法输出]:', item['magical_damage'])
        print('[队员真实输出]:', item['true_damage'])
        print('[队员输出/分钟]:', item['damage_min'], '[计算得出的结果]:', format((item['hero_damage']) / time, '.2f'))
        print('[队员输出占比]:', item['damage_ratio'], '[计算得出的结果]:', format((item['hero_damage']) / team_hero_damage, '.2f'))
        if item['kill'] == 0:
            print('[队员平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:',format((item['hero_damage']) / 1, '.2f'))
        else:
            print('[队员平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format((item['hero_damage']) / item['kill'], '.2f'))
        print('[队员承伤]:', item['damage_taken'])
        print('[队员物理承伤]:', item['physical_damage_taken'])
        print('[队员真实承伤]:', item['true_damage_taken'])
        print('[队员承伤/分钟]:', item['damage_taken_min'], '[计算得出的结果]:', format(item['damage_taken'] / time, '.2f'))
        print('[队员承伤占比]:', item['damage_taken_ratio'], '[计算得出的结果]:', format(item['damage_taken'] / team_damage_taken, '.2f'))
        if item['death'] == 0:
            print('[队员平均死亡承伤]:', item['damage_taken_death_ratio'], '[计算得出的结果]:', format(item['damage_taken'] / 1, '.2f'))
        else:
            print('[队员平均死亡承伤]:', item['damage_taken_death_ratio'], '[计算得出的结果]:', format(item['damage_taken'] / item['death'], '.2f'))
        print('[队员承伤经济比例]:', item['damage_taken_gold_ratio'], '[计算得出的结果]:', format(item['damage_taken'] / item['gold'], '.2f'))
        print('[队员治疗量]:', item['heal'])
        print('[队员治疗量/分钟]:', item['heal_min'], '[计算得出的结果]:', format((item['heal']) / time, '.2f'))
        print('[队员治疗量占比]:', item['heal_ratio'], '[计算得出的结果]:', format((item['heal']) / team_heal, '.2f'))
        print('[队员中立生物击杀数]:', item['neutral_kill'])
        print('[队员己方野区中立生物击杀数]:', item['self_neutral_kill'])
        print('[队员敌方野区中立生物击杀数]:', item['enemy_neural_kill'])
        print('[队员峡谷先锋击杀数]:', item['herald_kill'])
        print('[队员大龙（纳什男爵）击杀数]:', item['nashor_kill'])
        print('[队员远古巨龙击杀数]:', item['elder_drake_kill'])
        print('[队伍小龙击杀数]:', item['drake_kill'])
        print('[队员炼狱亚龙击杀数]:', item['infernal_drake_kill'])
        print('[队员山脉亚龙击杀数]:', item['mountain_drake_kill'])
        print('[队员云端亚龙击杀数]:', item['cloud_drake_kill'])
        print('[队员海洋亚龙击杀数]:', item['ocean_drake_kill'])
        print('[队员摧毁塔数]:', item['tower_kill'])
        print('[队员摧毁水晶数]:', item['inhibitor_kill'])


if __name__ == '__main__':
    data = get_data(match_id, dataBase, collection)
    print('###############主队队伍id:', team_id_z, '########################')
    player_cal(data, team_id_z)
    player_cal(data, team_id_k)
    team_cal(data, team_id_z)
    team_cal(data, team_id_k)

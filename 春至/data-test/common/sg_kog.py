from common.do_mongoDB import MongoDB




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
            p_kill = 0
            p_assist = 0
            p_death = 0
            p_double = 0
            p_triple = 0
            p_quadra = 0
            p_penta = 0
            p_streak = 0
            p_fight = 0
            p_damage = 0
            p_damage_kill_ratio = 0
            p_damage_gold_ratio = 0
            p_damage_taken = 0
            p_damage_taken_death_ratio = 0
            p_damage_taken_gold_ratio = 0
            for player in player_data:
                p_gold = p_gold + player['gold']
                p_kill = p_kill + player['kill']
                p_assist = p_assist + player['assist']
                p_death = p_death + player['death']
                # p_double = p_double + player['double']
                # p_triple = p_triple + player['triple']
                # p_quadra = p_quadra + player['quadra']
                # p_penta = p_penta + player['penta']
                # p_streak = p_streak + player['kill_streak']
                p_fight = p_fight + float(player['team_fight'])
                p_damage = p_damage + player['damage']
                p_damage_kill_ratio = p_damage_kill_ratio + float(player['damage_kill_ratio'])
                p_damage_gold_ratio = p_damage_gold_ratio + float(player['damage_gold_ratio'])
                p_damage_taken = p_damage_taken + player['damage_taken']
                p_damage_taken_death_ratio = p_damage_taken_death_ratio + float(player['damage_taken_death_ratio'])
                p_damage_taken_gold_ratio = p_damage_taken_gold_ratio + float(player['damage_taken_gold_ratio'])
            print('#################队伍数据，队伍id:', team_id, '################')
            print('[队伍总经济]:', item['gold'], '[计算得出的结果]:', p_gold)
            print('[队伍经济/分钟]:', item['gold_min'], '[计算得出的结果]:', format(p_gold / (time / 60), '.2f'))
            print('[队伍经济差]:', item['gold_diff'], '[计算得出的结果]:')
            print('[队伍英雄总击杀数]:', item['kill'], '[计算得出的结果]:', p_kill)
            print('[队伍英雄总助攻数]:', item['assist'], '[计算得出的结果]:', p_assist)
            print('[队伍英雄总死亡数]:', item['death'], '[计算得出的结果]:', p_death)
            print('[队伍kda]:', item['kda'], '[计算得出的结果]: ', format((p_kill + p_assist) / p_death, '.2f'))
            print('[队伍双杀次数]:', item['double'], '[计算得出的结果]:', p_double)
            print('[队伍三杀次数]:', item['triple'], '[计算得出的结果]:', p_triple)
            print('[队伍四杀次数]:', item['quadra'], '[计算得出的结果]:', p_quadra)
            print('[队伍五杀次数]:', item['penta'], '[计算得出的结果]:', p_penta)
            print('[队伍最大连续击杀]:', item['kill_streak'], '[计算得出的结果]:', p_streak)
            print('[平均队员参团率]:', item['team_fight'], '[计算得出的结果]:', format(p_fight / 5, '.2f'))
            print('[队伍总输出]:', item['damage'], '[计算得出的结果]:', p_damage)
            print('[队伍输出/分钟]:', item['damage_min'], '[计算得出的结果]:', format(p_damage / (time / 60), '.2f'))
            print('[平均队员输出]:', item['avg_player_damage'], '[计算得出的结果]:', format(p_damage / 5, '.2f'))
            # print('[队伍平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format(p_damage_kill_ratio / 5, '.2f'))
            print('[队伍平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format(p_damage / p_kill, '.2f'))
            # print('[队伍输出经济比]:', item['damage_gold_ratio'], '[计算得出的结果]:', format(p_damage_gold_ratio / 5, '.2f'))
            print('[队伍输出经济比]:', item['damage_gold_ratio'], '[计算得出的结果]:', format(p_damage / p_gold, '.2f'))
            print('[队伍总承伤]:', item['damage_taken'], '[计算得出的结果]:', p_damage_taken)
            print('[队伍承伤/分钟]:', item['damage_taken_min'], '[计算得出的结果]:', format(p_damage_taken / (time / 60), '.2f'))
            print('[平均队员承伤]:', item['avg_player_damage_taken'], '[计算得出的结果]:', format(p_damage_taken / 5, '.2f'))
            # print('[队伍平均死亡承伤]:', item['damage_taken_death_ratio'], '[计算得出的结果]:', format(p_damage_taken_death_ratio / 5, '.2f'))
            print('[队伍平均死亡承伤]:', item['damage_taken_death_ratio'], '[计算得出的结果]:', format(p_damage_taken / p_death, '.2f'))
            # print('[队伍承伤经济比例]:', item['damage_taken_gold_ratio'], '[计算得出的结果]:', format(p_damage_taken_gold_ratio / 5, '.2f'))
            print('[队伍承伤经济比例]:', item['damage_taken_gold_ratio'], '[计算得出的结果]:', format(p_damage_taken / p_gold, '.2f'))
            print('[队伍暴君击杀数]:', item['pharaoh_kill'])
            print('[队伍主宰击杀数]:', item['master_kill'])
            print('[队伍摧毁塔总数]:', item['tower_kill'])


def player_cal(data, team_id):
    team_data = data['data']
    for item in team_data:
        if item['team_id'] == team_id:
            # 队员计算需要用到的队伍数据
            player_data = item['player']
            team_gold = item['gold']
            team_kill = item['kill']
            team_death = item['death']
            team_damage = item['damage']
            team_damage_taken = item['damage_taken']
    for item in player_data:
        print('###############队员的id: ', item['player_id'], '########################')
        print('[队员的装备]:', item['item'])
        print('[队员的技能信息]:', item['spell'], )
        print('[队员的经济]:', item['gold'], )
        print('[队员的平均时间经济]:', item['gold_min'], '[计算得出的结果]:', format((item['gold']) / (time / 60), '.2f'))
        print('[队员的对位经济差]:', item['gold_diff'], '[计算得出的结果]:')
        print('[队员经济占队伍总经济比例]:', item['gold_ratio'], '[计算得出的结果]:', format((item['gold']) / team_gold, '.2f'))
        print('[队员英雄击杀数，助攻数，死亡数]:', item['kill'], item['assist'], item['death'])
        # kda 计算方式
        if item['death'] != 0:
            kda = (item['kill'] + item['assist']) / item['death']
        else:
            kda = (item['kill'] + item['assist']) / 1
        print('[队员的kda]:', item['kda'], "[计算得出的结果]:", format(kda, '.2f'))
        print('[队员双杀、三杀、四杀、五杀、连杀次数]:', item['double'], item['triple'], item['quadra'], item['penta'],
              item['kill_streak'])
        print('[队员参团率]:', item['team_fight'], '[计算得出的结果]:', format((item['kill'] + item['assist']) / team_kill, '.2f'))
        print('[队员输出]:', item['damage'])
        print('[队员输出/分钟]:', item['damage_min'], '[计算得出的结果]:', format((item['damage']) / (time / 60), '.2f'))
        print('[队员输出占比]:', item['damage_ratio'], '[计算得出的结果]:', format((item['damage']) / team_damage, '.2f'))
        if item['kill'] != 0 :

            kill = item['kill']
        else:
            kill = 1
        if item['death'] != 0:
            death = item['death']
        else:
            death = 1
        print('[队员平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format((item['damage']) / kill, '.2f'))
        damage_ratio = float(item['damage_ratio'])
        gold_ratio = float(item['gold_ratio'])
        print('[队员输出经济比例]:', item['damage_gold_ratio'], '[计算得出的结果]:',
              format(item['damage'] / item['gold'], '.2f'))
        print('[队员承伤]:', item['damage_taken'])
        print('[队员承伤/分钟]:', item['damage_taken_min'], '[计算得出的结果]:', format((item['damage_taken']) / (time / 60), '.2f'))
        print('[队员承伤占比]:', item['damage_taken_ratio'], '[计算得出的结果]:',
              format((item['damage_taken']) / team_damage_taken, '.2f'))
        print('[队员平均死亡承伤]:', item['damage_taken_death_ratio'], '[计算得出的结果]:',
              format((item['damage_taken']) / death, '.2f'))
        damage_taken_ratio = float(item['damage_taken_ratio'])
        print(damage_taken_ratio)
        print('[队员承伤经济比例]:', item['damage_taken_gold_ratio'], '[计算得出的结果]:',
              format(item['damage_taken'] / item['gold'], '.2f'))


# 计算数据前需要记录
match_id = 1177  # 小局ID
dataBase = 'data-center'
collection = 'kog_result'
team_id_z = 890  # 主队ID
team_id_k = 947  # 客队ID
time = 1197  # 比赛时长

if __name__ == '__main__':
    data = get_data(match_id, dataBase, collection)
    print('###############主队队伍id:', team_id_z, '########################')
    player_cal(data, team_id_z)
    print('###############副队队伍id:', team_id_k, '########################')
    player_cal(data, team_id_k)
    team_cal(data, team_id_z)
    team_cal(data, team_id_k)

from common.do_mongoDB import MongoDB

# 计算数据前需要记录
match_id = 17659  # 小局ID
dataBase = 'data-center'
collection = 'csgo_result'
team_id_z = 3827  # 主队ID
team_id_k = 3828  # 客队ID
round_num = 24   # 回合数


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
            p_kpr = 0
            p_kill = 0
            p_headshot = 0
            p_death = 0
            p_assist = 0
            p_flash_assist = 0
            p_entry_kill = 0
            p_entry_death = 0
            # p_inhibitor_kill = 0
            p_one_win_multi = 0
            p_multi_kill = 0
            p_fk_diff = 0
            p_adr = 0
            p_kast = 0
            p_impact = 0
            p_rating = 0
            for player in player_data:
                p_kill = p_kill + player['kill']
                p_headshot = p_headshot + player['headshot']
                p_assist = p_assist + player['assist']
                p_death = p_death + player['death']
                p_one_win_multi = p_one_win_multi + player['one_win_multi']
                p_multi_kill = p_multi_kill + player['multi_kill']
                # p_inhibitor_kill = p_inhibitor_kill + player['inhibitor_kill']
                p_flash_assist = p_flash_assist + player['flash_assist']
                p_entry_kill = p_entry_kill + player['entry_kill']
                p_entry_death = p_entry_death + player['entry_death']
                p_fk_diff = p_fk_diff + float(player['fk_diff'])
                p_adr = p_adr + float(player['adr'])
                p_kast = p_kast + float(player['kast'])
                p_impact = p_impact + float(player['impact'])
                p_rating = p_rating + float(player['rating'])
            print('#################队伍数据，队伍id:', team_id, '################')
            print(round_num)
            print('[KPR，队伍平均回合击杀数]:', item['kpr'], '[计算得出的结果]:', p_kill / round_num)
            print('[队伍小局总击杀数]:', item['kill'], '[计算得出的结果]:', p_kill)
            print('[队伍平均回合爆头数]:', item['avg_headshot'], '[计算得出的结果]:', p_headshot / round_num)
            print('[队伍该小局总爆头数]:', item['headshot'], '[计算得出的结果]:', p_headshot)
            print('[DPR，队伍平均回合死亡数]:', item['dpr'], '[计算得出的结果]:', p_death / round_num)
            print('[队伍该小局总死亡数]:', item['death'], '[计算得出的结果]:', p_death)
            print('[队伍平均回合助攻数]:', item['avg_assist'], '[计算得出的结果]:', p_assist / round_num)
            print('[队伍该小局总助攻数]:', item['assist'], '[计算得出的结果]:', p_assist)
            print('[队伍平均回合闪光助攻数]:', item['avg_flash_assist'], '[计算得出的结果]:', p_flash_assist / round_num)
            print('[队伍该小局总闪光助攻数]:', item['flash_assist'], '[计算得出的结果]:', p_flash_assist)
            print('[队伍平均回合首次击杀次数]:', item['avg_entry_kill'], '[计算得出的结果]:', p_entry_kill / round_num)
            print('[队伍该小局首次击杀次数]:', item['entry_kill'], '[计算得出的结果]:', p_entry_kill)
            print('[队伍平均回合被首次击杀次数]:', item['avg_entry_death'], '[计算得出的结果]:', p_entry_death / round_num)
            print('[队伍该小局被首次击杀次数]:', item['entry_death'], '[计算得出的结果]:', p_entry_death)

            print('队伍该小局一对多人取胜回合数', item['one_win_multi'], '[计算得出的结果]:')
            print('[队伍该小局多杀回合数（队员击杀2个及以上的回合数）]:', item['multi_kill'], '[计算得出的结果]:', p_multi_kill)

            print('[F/K Diff，队伍该小局首次击杀和被首次击杀的差]:', item['fk_diff'], '[计算得出的结果]:', p_entry_death / round_num)
            print('[K/D Diff，队伍该小局击杀数和死亡数的差]:', item['kd_diff'], '[计算得出的结果]:', p_kill - p_death)
            print('K/D Ratio，队伍该小局击杀数和死亡数的比值', item['kd_ratio'], '[计算得出的结果]:', p_kill / p_death)
            print('ADR，队伍平均回合造成伤害', item['adr'], '[计算得出的结果]:', p_adr / 5)
            print('KAST，队伍平均队员KAST数值', item['kast'], '[计算得出的结果]:', p_kast / 5)
            print('Impact，队伍平均队员影响力评分', item['impact'], '[计算得出的结果]:', p_impact / 5)
            print('Rating 2.0，队伍平均队员Rating 2.0数值', item['rating'], '[计算得出的结果]:', p_rating / 5)



def player_cal(data, team_id):
    team_data = data['data']
    for item in team_data:
        if item['team_id'] == team_id:
            # 队员计算需要用到的队伍数据
            player_data = item['player']
    for item in player_data:
        print('###############队员的id: ', item['player_id'], '########################')
        print(round_num)
        print('[KPR，队员平均回合击杀数]:', item['kpr'])
        print('[队员小局总击杀数]:', item['kill'])
        print('[队员平均回合爆头数]:', item['avg_headshot'], '[计算得出的结果]:', item['headshot'] / round_num)
        print('[队员小局总爆头数]:', item['headshot'])
        print('[DPR，队员平均回合死亡数]:', item['dpr'])
        print('[队员小局总死亡数]:', item['death'])
        print('[队员平均回合助攻数]:', item['avg_assist'], '[计算得出的结果]:', item['assist'] / round_num)
        print('[队员小局总助攻数]:', item['assist'])
        print('[队员平均回合闪光助攻数]:', item['avg_flash_assist'], '[计算得出的结果]:', item['flash_assist'] / round_num)
        print('[队员小局总闪光助攻数]:', item['flash_assist'])
        print('[队员平均回合首次击杀次数]:', item['avg_entry_kill'], '[计算得出的结果]:', item['entry_kill'] / round_num)
        print('[队员该小局首次击杀次数]:', item['entry_kill'])
        print('[队员平均回合首次被击杀次数]:', item['avg_entry_death'], '[计算得出的结果]:', item['entry_death'] / round_num)
        print('[队员该小局被首次击杀次数]:', item['entry_death'])
        print('[队员该小局一对多人取胜回合数]:', item['one_win_multi'])
        print('[队员该小局多杀回合数（队员击杀2个及以上的回合数）]:', item['multi_kill'])
        print('[F/K Diff，队员该小局首次击杀和被首次击杀的差]:', item['fk_diff'])
        print('[K/D Diff，队员该小局击杀数和死亡数的差]:', item['kd_diff'])
        print('[K/D Ratio，队员该小局击杀数和死亡数的比例]:', item['kd_ratio'])
        print('[ADR，队员平均回合造成伤害]:', item['adr'])
        print('[KAST，队员该小局KAST数值]:', item['kast'])
        print('[Impact，队员该小局影响力评分]:', item['impact'])
        print('[Rating 2.0，队员该小局Rating 2.0数值]:', item['rating'])


if __name__ == '__main__':
    data = get_data(match_id, dataBase, collection)
    print('###############主队队伍id:', team_id_z, '########################')
    player_cal(data, team_id_z)
    player_cal(data, team_id_k)
    team_cal(data, team_id_z)
    team_cal(data, team_id_k)

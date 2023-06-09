from common.do_mongoDB import MongoDB
# from common.test import data

game_id = 3
match_id = 10214  # 小局id
round_num = 22  # 回合总数


def get_data(match_id, dataBase, collection):
    myDb = MongoDB()
    collect = myDb.connect(dataBase, collection)
    sen = '{"match_id":' + str(match_id) + '}'
    result = myDb.select_data_one(collect, sen)
    return result


# 获取每个队员的数据 state 0为a队数据 1为b队数据
def get_player_data(data, state, p_data):
    team = data['data']
    team_data = team[state]
    single_player = []
    player = team_data['player']
    for item in player:
        data = item[p_data]
        single_player.append(data)
    return single_player


def get_team_data(state, t_data):
    team = data["data"]
    team_data = team[state]
    team_kpr = team_data[t_data]
    return team_kpr


def commom(data, state, isAll, t_data, p_data, mes):
    '''
        data:数据传参
        state:队伍  0为a队  1为b队
        isAll：是否计算总和 0为平均 1为总和
        t_data：队伍数据
        p_data：队员数据
        mes:统计项目名称
    '''
    if state == 0:
        count_a = 0
        team_data = get_team_data(state, t_data)
        hs_p = get_player_data(data, state, p_data)
        if isAll == 0:
            if p_data in ['adr', 'kast', 'impact', 'rating']:
                for i in hs_p:
                    count_a = count_a + float(i)
                num = format(count_a / 5, '.2f')
                if team_data == num:
                    print(mes, 'a队数据对比正确', num, team_data)
                else:
                    print(mes, 'a队数据对比不正确', num, team_data)
            else:
                for i in hs_p:
                    count_a = count_a + float(i)
                num = format(count_a / round_num, '.2f')
                if team_data == num:
                    print(mes, 'a队数据对比正确', num, team_data)
                else:
                    print(mes, 'a队数据对比不正确', num, team_data)
        else:
            for i in hs_p:
                count_a = count_a + float(i)
            if team_data == count_a:
                print(mes, 'a队数据对比正确', count_a, team_data)
            else:
                print(mes, 'a队数据对比不正确', count_a, team_data)
    else:
        count_a = 0
        team_data = get_team_data(state, t_data)
        hs_p = get_player_data(data, state, p_data)
        if isAll == 0:
            if p_data in ['adr', 'kast', 'impact', 'rating']:
                for i in hs_p:
                    count_a = count_a + float(i)
                num = format(count_a / 5, '.2f')
                if team_data == num:
                    print(mes, 'a队数据对比正确', num, team_data)
                else:
                    print(mes, 'a队数据对比不正确', num, team_data)
            else:
                for i in hs_p:
                    count_a = count_a + float(i)
                num = format(count_a / round_num, '.2f')
                if team_data == num:
                    print(mes, 'a队数据对比正确', num, team_data)
                else:
                    print(mes, 'a队数据对比不正确', num, team_data)
        else:
            for i in hs_p:
                count_a = count_a + float(i)
            if team_data == count_a:
                print(mes, 'b队数据对比正确', count_a, team_data)
            else:
                print(mes, 'b队数据对比不正确', count_a, team_data)


def sub(data, state, p1, p2, t_data, com_str):
    player = get_player_data(data, state, p1)
    count_kill = 0
    for i in player:
        count_kill = count_kill + i
    player = get_player_data(data, state, p2)
    count_killed = 0
    for i in player:
        count_killed = count_killed + i
    num = count_kill - count_killed
    if get_team_data(state, t_data) == num:
        print(com_str + '数据结果正确', num, get_team_data(state, t_data))
    else:
        print(com_str + '数据结果不正确', num, get_team_data(state, t_data))


def div(data, state, p1, p2, t_data, com_str):
    player = get_player_data(data, state, p1)
    count_kill = 0
    for i in player:
        count_kill = count_kill + i
    player = get_player_data(data, state, p2)
    count_killed = 0
    for i in player:
        count_killed = count_killed + i
    num = count_kill / count_killed
    if get_team_data(state, t_data) == num:
        print(com_str + '数据结果正确', num, get_team_data(state, t_data))
    else:
        print(com_str + '数据结果不正确', num, get_team_data(state, t_data))


def calculate(team, state, data):
    print(team, '队伍的数据')
    commom(data, state, 0, 'kpr', 'kill', '队伍平均回合击杀数kpr')
    commom(data, state, 1, 'kill', 'kill', '队伍小局总击杀数kill')
    commom(data, state, 0, 'avg_headshot', 'headshot', '队伍小局总爆头数avg_headshot')
    commom(data, state, 1, 'headshot', 'headshot', '队伍小局总爆头数headshot')
    commom(data, state, 0, 'dpr', 'death', '队伍平均回合死亡数dpr')
    commom(data, state, 1, 'death', 'death', '队伍该小局总死亡数death')
    commom(data, state, 0, 'avg_assist', 'assist', '队伍平均回合助攻数avg_assist')
    commom(data, state, 1, 'assist', 'assist', '队伍该小局总助攻数assist')
    commom(data, state, 0, 'avg_flash_assist', 'flash_assist', '队伍平均回合闪光助攻数avg_flash_assist')
    commom(data, state, 1, 'flash_assist', 'flash_assist', '队伍该小局总闪光助攻数flash_assist')
    commom(data, state, 0, 'avg_entry_kill', 'entry_kill', '队伍平均回合首次击杀次数avg_entry_kill')
    commom(data, state, 1, 'entry_kill', 'entry_kill', '队伍该小局首次击杀次数entry_kill')
    commom(data, state, 0, 'avg_entry_death', 'entry_death', '队伍平均回合被首次击杀次数avg_entry_death')
    commom(data, state, 1, 'entry_death', 'entry_death', '队伍该小局被首次击杀次数entry_death')
    commom(data, state, 1, 'one_win_multi', 'one_win_multi', '队伍该小局一对多人取胜回合数one_win_multi')
    commom(data, state, 1, 'multi_kill', 'multi_kill', '队伍该小局一对多人取胜回合数multi_kill')
    sub(data, state, 'entry_kill', 'entry_death', 'fk_diff', '队伍该小局首次击杀和被首次击杀的差fkdiff')
    sub(data, state, 'kill', 'death', 'kd_diff', '队伍该小局首次击杀和被首次击杀的差kddiff')
    div(data, state, 'kill', 'death', 'kd_ratio', '队伍该小局首次击杀和被首次击杀的比值kdratio')
    commom(data, state, 0, 'adr', 'adr', '队伍平均回合造成伤害adr')
    commom(data, state, 0, 'kast', 'kast', '队伍平均队员kast数值kast')
    commom(data, state, 0, 'impact', 'impact', '队伍平均队员影响力评分impact')
    commom(data, state, 0, 'rating', 'rating', '队伍平均队员rating2.0数值rating')


if __name__ == '__main__':
    data = get_data(match_id, 'data-center', 'csgo_result')
    calculate('a队伍', 0, data)
    calculate('b队伍', 1, data)

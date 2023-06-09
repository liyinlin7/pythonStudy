from common.do_mongoDB import MongoDB

# 计算数据前需要记录
match_id = 72069  # 小局ID
dataBase = 'sports-soccer'
collection = 'result'
team_id_z = 206484  # 主队ID
team_id_k = 201193  # 客队ID
time = round((1576/60), 2)   # 比赛时长


# 获取数据
def get_data(match_id, dataBase, collection):
    myDb = MongoDB()
    collect = myDb.sport_connect(dataBase, collection, status=0)  # status=0 是测试环境数据库
    sen = '{"match_id":' + str(match_id) + '}'
    result = myDb.select_data_one(collect, sen)
    print(result)
    return result


def team_cal(data, team_id):
    team_data = data['data']
    for item in team_data:
        if item['id'] == team_id:
            player_data = item['player']
            p_is_starting = 0
            p_score = 0
            p_penalty_kick = 0
            p_penalty_goal = 0
            p_own_goal = 0
            p_assist = 0
            p_shot = 0
            p_target_shot = 0
            p_post_shot = 0
            p_foul = 0
            p_fouled = 0
            p_offside = 0
            p_offsode_create = 0
            p_red = 0
            p_yellow = 0
            p_play_time = 0
            p_pass = 0
            p_square_pass = 0
            p_long_pass = 0
            p_through_pass = 0
            p_key_pass = 0
            p_pass_success = 0
            p_pass_success_rate = 0
            p_break = 0
            p_dispossession = 0
            p_turnover = 0
            p_tackle = 0
            p_slide = 0
            p_block = 0
            p_clear = 0
            for player in player_data:
                p_score = p_score + player['score']
                p_penalty_kick = p_penalty_kick + player['penalty_kick']
                p_penalty_goal = p_penalty_goal + player['penalty_goal']
                p_own_goal = p_own_goal + player['own_goal']
                p_assist = p_assist + player['assist']
                p_shot = p_shot + player['shot']
                p_target_shot = p_target_shot + player['target_shot']
                p_post_shot = p_post_shot + player['post_shot']
                p_foul = p_foul + player['foul']
                p_red = p_red + player['red']
                p_yellow = p_yellow + player['yellow']
                p_offside = p_offside + player['offside']
                p_pass = p_pass + player['pass']
                p_square_pass = p_square_pass + player['square_pass']
                p_long_pass = p_long_pass + player['long_pass']
                p_turnover = p_turnover + player['turnover']
                p_through_pass = p_through_pass + player['through_pass']
                p_key_pass = p_key_pass + player['key_pass']
                p_pass_success = p_pass_success + player['pass_success']
                p_break = p_break + player['break']
                p_dispossession = p_dispossession + player['dispossession']
                p_tackle = p_tackle + player['tackle']
                p_slide = p_slide + player['slide']
                p_block = p_block + player['block']
                p_clear = p_clear + player['clear']

            print(f"**********队伍ID：{team_id}*************")
            print(f"队伍是否为先开球方：{item['is_kick_off']},计算结果：")
            print(f"队伍进球数：{item['score']},计算结果：")
            t_penalty_kick = item['penalty_kick']
            print(f"队伍进球数：{t_penalty_kick},需要计算的计算结果：{p_penalty_kick}")
            t_penalty_goal = item['penalty_goal']
            print(f"队伍点球进球数：{t_penalty_goal},需要计算的计算结果：{p_penalty_goal}")
            t_own_goal = item['own_goal']
            print(f"队伍乌龙球数：{t_own_goal},计算结果：{p_own_goal}")
            t_assist = item['assist']
            print(f"队伍助攻数：{t_assist},计算结果：{p_assist}")
            t_shot = item['shot']
            print(f"队伍射门数：{t_shot},计算结果：{p_shot}")
            t_target_shot = item['target_shot']
            print(f"队伍射正数：{t_target_shot},计算结果：{p_target_shot}")
            t_post_shot = item['post_shot']
            print(f"队伍射中门框数：{t_post_shot},计算结果：{p_post_shot}")
            t_free_kick = item['free_kick']
            print(f"队伍任意球数：{t_free_kick},计算结果：")
            t_throw_in = item['throw_in']
            print(f"队伍界外球数：{t_throw_in},计算结果：")
            t_header = item['header']
            print(f"队伍头球数：{t_header},计算结果：")
            t_corner = item['corner']
            print(f"队伍角球数：{t_corner},计算结果：")
            t_substitute = item['substitute']
            print(f"队伍换人数：{t_substitute},计算结果：")
            t_foul = item['foul']
            print(f"队伍犯规数：{t_foul},计算结果：{p_foul}")
            t_red = item['red']
            print(f"队伍红牌数：{t_red},计算结果：{p_red}")
            t_yellow = item['yellow']
            print(f"队伍黄牌数：{t_yellow},计算结果：{p_yellow}")
            t_offside = item['offside']
            print(f"队伍越位数：{t_offside},计算结果：{p_offside}")
            t_possession = item['possession']
            print(f"队伍控球率：{t_possession},计算结果：")
            t_attack = item['attack']
            print(f"队伍进攻次数：{t_attack},计算结果：")
            t_dangerous_attack = item['dangerous_attack']
            print(f"队伍危险进攻次数：{t_dangerous_attack},计算结果：")
            t_pass = item['pass']
            print(f"队伍传球数：{t_pass},计算结果：{p_pass}")
            t_square_pass = item['square_pass']
            print(f"队伍横传数：{t_square_pass},需要计算的计算结果：{p_square_pass}")
            t_long_pass = item['long_pass']
            print(f"队伍长传数：{t_long_pass},计算结果：{p_long_pass}")
            t_turnover = item['turnover']
            print(f"队伍失误数：{t_turnover},需要计算的计算结果：{p_turnover}")
            t_short_pass = item['short_pass']
            print(f"队伍短传数：{t_short_pass},计算结果：")
            t_through_pass = item['through_pass']
            print(f"队伍直塞数：{t_through_pass},需要计算的计算结果：{p_through_pass}")
            t_key_pass = item['key_pass']
            print(f"队伍关键传球数：{t_key_pass},需要计算的计算结果：{p_key_pass}")
            t_pass_success = item['pass_success']
            print(f"队伍传球成功数：{t_pass_success},需要计算的计算结果：{p_pass_success}")
            t_pass_success_rate = item['pass_success_rate']
            print(f"队伍传球成功率：{t_pass_success_rate},计算结果：")
            t_break = item['break']
            print(f"队伍过人次数：{t_break},计算结果：{p_break}")
            t_dispossession = item['dispossession']
            print(f"队伍失去球权数：{t_dispossession},需要计算的计算结果：{p_dispossession}")
            t_tackle = item['tackle']
            print(f"队伍拦截数：{t_tackle},计算结果：{p_tackle}")
            t_slide = item['slide']
            print(f"队伍铲断数：{t_slide},计算结果：{p_slide}")
            t_block = item['block']
            print(f"队伍封堵数：{t_block},需要计算的计算结果：{p_block}")
            t_clear = item['clear']
            print(f"队伍解围数：{t_clear},需要计算的计算结果：{p_clear}")


def player_cal(data, team_id):
    team_data = data['data']
    for item in team_data:
        if item['id'] == team_id:
            # 队员计算需要用到的队伍数据
            player_data = item['player']
    for item in player_data:
        print('###############队员的id: ', item['id'], '########################')
        print('[是否是首发]:', item['is_starting'])
        print('[队员进球数]:', item['score'])
        print('[队员获得点球]:', item['penalty_kick'])
        print('[队员点球进球数]:', item['penalty_goal'])
        print('[队员乌龙球数]:', item['own_goal'])
        print('[队员助攻数]:', item['assist'])
        print('[队员射门数]:', item['shot'])
        print('[队员射正数]:', item['target_shot'])
        print('[队员射中门框数]:', item['post_shot'])
        print('[队员犯规数]:', item['foul'])
        print('[队员被犯规数]:', item['fouled'])
        print('[队员越位数]:', item['offside'])
        print('[队员造成越位数]:', item['offside_create'])
        print('[队员红牌数]:', item['red'])
        print('[队员黄牌数]:', item['yellow'])
        print('[上场时间]:', item['play_time'])
        print('[队员传球数]:', item['pass'])
        print('[队员横传数]:', item['square_pass'])
        print('[队员长传数]:', item['long_pass'])
        print('[队员直塞数]:', item['through_pass'])
        print('[队员关键传球数]:', item['key_pass'])
        print('[队员传球成功数]:', item['pass_success'])
        print('[队员传球成功率]:', item['pass_success_rate'])
        print('[队员过人数]:', item['break'])
        print('[队员失去球权数]:', item['dispossession'])
        print('[队员失误数]:', item['turnover'])
        print('[队员拦截数]:', item['tackle'])
        print('[队员铲断数]:', item['slide'])
        print('[队员封堵数]:', item['block'])
        print('[队员解围数]:', item['clear'])


if __name__ == '__main__':
    data = get_data(match_id, dataBase, collection)
    # print('###############主队队伍id:', team_id_z, '########################')
    # player_cal(data, team_id_z)
    # player_cal(data, team_id_k)
    # team_cal(data, team_id_z)
    # team_cal(data, team_id_k)

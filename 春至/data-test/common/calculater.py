from common.do_mysql import DoMySql


def do_sql_dict(cursor, state):
    desc = cursor.description
    if state == 1:
        res = cursor.fetchone()  # 返回的数据类型是元组
    else:
        res = cursor.fetchall()  # 返回的数据类型是列表,里面的元素是元组
    data_dic = [dict(zip([col[0] for col in desc], row)) for row in res]
    return data_dic


#
def calculate(num, series_id, team_id_a, team_id_b, state, match_id):
    con = DoMySql().link_testsql()
    cursor = con.cursor()
    sql = 'SELECT * FROM `api-mega`.w_event WHERE round_num <={} and series_id = {} and match_id = {} and stage = 2'.format(num, series_id, match_id)
    cursor.execute(sql)
    data = do_sql_dict(cursor, state)
    Kpr(num, team_id_a, team_id_b, data)  # 队伍平均回合击杀数
    Dpr(num, team_id_a, team_id_b, data)  # 队伍平均回合死亡数
    f_k_diff(num, team_id_a, team_id_b, series_id, con, match_id)  # 队伍该小局首次击杀和被首次击杀的差
    k_d_diff(num, team_id_a, team_id_b, series_id, con, match_id)  # 队伍该小局击杀数和死亡数的差
    k_d_ratio(num, team_id_a, team_id_b, series_id, con, match_id)  # 队伍该小局击杀数和死亡数的比值


# kpr 队伍平均回合击杀数
def Kpr(num, team_id_a, team_id_b, data):
    count_a = 0  # a队计数
    count_b = 0  # b队计数
    for event in data:
        if event['e_type'] == 7:
            if event['kill_team_id'] == team_id_a:
                count_a += 1
            if event['kill_team_id'] == team_id_b:
                count_b += 1
    kpr_a = count_a / num
    kpr_b = count_b / num
    print('a队Kpr:', kpr_a, '   b队Kpr:', kpr_b)


# Dpr 队伍平均回合死亡数
def Dpr(num, team_id_a, team_id_b, data):
    count_a = 0  # a队计数
    count_b = 0  # b队计数
    for event in data:
        if event['e_type'] == 7:
            if event['killed_team_id'] == team_id_a:
                count_a += 1
            if event['killed_team_id'] == team_id_b:
                count_b += 1
    dpr_a = count_a / num
    dpr_b = count_b / num
    print('a队Dpr:', dpr_a, '   b队Dpr:', dpr_b)


# f/k diff 队伍该小局首次击杀和被击杀的差
def f_k_diff(num, team_id_a, team_id_b, series_id, con, match_id):
    count_a = 0  # a队计数
    count_b = 0  # b队计数
    for i in range(1, num + 1):
        flag = 0
        sql = 'SELECT * FROM `api-mega`.w_event WHERE round_num = {} and series_id = {} and match_id={} and stage = 2'.format(i, series_id, match_id)
        cursor = con.cursor()
        cursor.execute(sql)
        data = do_sql_dict(cursor, 0)
        for event in data:
            if event['e_type'] == 7 and flag == 0:
                if event['kill_team_id'] == team_id_a:
                    count_a += 1
                if event['kill_team_id'] == team_id_b:
                    count_b += 1
                flag = 1
    f_k_diff_a = count_a - count_b
    f_k_diff_b = count_b - count_a
    print('a队f/k diff:', f_k_diff_a, '      b队f/k diff:', f_k_diff_b)


# k/d diff 队伍该小局击杀数和死亡数的差
def k_d_diff(num, team_id_a, team_id_b, series_id, con, match_id):
    count_a = 0  # a队计数
    count_b = 0  # b队计数
    sql = 'SELECT * FROM `api-mega`.w_event WHERE round_num  <= {} and series_id = {} and match_id={} and stage = 2'.format(num, series_id, match_id)
    cursor = con.cursor()
    cursor.execute(sql)
    data = do_sql_dict(cursor, 0)
    for event in data:
        if event['e_type'] == 7:
            if event['kill_team_id'] == team_id_a:
                count_a += 1
            if event['kill_team_id'] == team_id_b:
                count_b += 1
    k_d_diff_a = count_a - count_b
    k_d_diff_b = count_b - count_a
    print('a队k/d diff:', k_d_diff_a, '      b队k/d diff:', k_d_diff_b)


# k/d ratio 队伍该小局击杀数和死亡数的比值
def k_d_ratio(num, team_id_a, team_id_b, series_id, con, match_id):
    count_a = 0  # a队计数
    count_b = 0  # b队计数
    sql = 'SELECT * FROM `api-mega`.w_event WHERE round_num  <= {} and series_id = {} and match_id={} and stage = 2'.format(num, series_id, match_id)
    cursor = con.cursor()
    cursor.execute(sql)
    data = do_sql_dict(cursor, 0)
    for event in data:
        if event['e_type'] == 7:
            if event['kill_team_id'] == team_id_a:
                count_a += 1
            if event['kill_team_id'] == team_id_b:
                count_b += 1
    if count_b and count_b:
        k_d_ratio_a = count_a / count_b
        k_d_ratio_b = count_b / count_a
        print('a队k/d ratio:', k_d_ratio_a, '      b队k/d ratio:', k_d_ratio_b)
    else:
        print('a队k/d ratio和b队k/d ratio 数值不对')


# 队员数据计算
def get_player(num, series_id, match_id):
    con = DoMySql().link_testsql()
    cursor = con.cursor()
    # 取出第几回合的数据
    sql = 'SELECT data_json FROM `api-mega`.w_statistics WHERE round_num = {} and match_id={}'.format(num, match_id)
    cursor.execute(sql)
    result = cursor.fetchone()
    result = ''.join(result)
    result = eval(result)
    payload = result['payload']
    payload_data = eval(payload)
    team_data = payload_data['team']
    team_a = team_data[0]
    team_b = team_data[1]
    ap = do_playerData(team_a)        # a player
    bp = do_playerData(team_b)        # b player
    print(ap, bp)
    sql1 = 'SELECT * FROM `api-mega`.w_event WHERE round_num <={} and series_id = {} and match_id = {} and stage = 2'.format(num, series_id, match_id)
    cursor.execute(sql1)
    data = do_sql_dict(cursor, 0)
    for pid in ap:
        p_kpr(pid, data, num)
        p_dpr(pid, data, num)
        p_fk(pid, num, series_id, match_id, cursor)
        p_kd_diff(pid, data)
        p_kd_ratio(pid, data)
    for pid in bp:
        p_kpr(pid, data, num)
        p_dpr(pid, data, num)
        p_fk(pid, num, series_id, match_id, cursor)
        p_kd_diff(pid, data)
        p_kd_ratio(pid, data)


def do_playerData(data):
    players = data['player']
    list = []
    for player in players:
        list.append(player['player_id'])
    return list


# 队员平均回合击杀数
def p_kpr(pid, data, num):
    count = 0
    for i in data:
       if pid == i['kill_player_id']:
           count += 1
    kpr = count / num
    print('队员id：', pid, '该队员kpr值为:', kpr)


# 队员平均回合死亡数
def p_dpr(pid, data, num):
    count = 0
    for i in data:
       if pid == i['killed_player_id']:
           count += 1
    dpr = count / num
    print('队员id：', pid, '该队员dpr值为:', dpr)


# 队员该小局首次击杀和被首次击杀的差
def p_fk(pid, num, series_id, match_id, cursor):
    kill = 0
    killed = 0
    for num in range(1, num+1):
        sql = 'SELECT * FROM `api-mega`.w_event WHERE round_num ={} and series_id = {} and match_id = {} and stage = 2'.format(num, series_id, match_id)
        cursor.execute(sql)
        data = do_sql_dict(cursor, 0)
        flag = 0
        for event in data:
            if event['e_type'] == 7 and flag == 0:
                if event['kill_player_id'] == pid:
                    kill += 1
                if event['killed_player_id'] == pid:
                    killed += 1
                flag = 1
    p_fk_diff = kill - killed
    print('队员id：', pid, '该队员p_fk_diff值为:', p_fk_diff)


# 队员该小局击杀数和死亡数的差
def p_kd_diff(pid, data):
    kill = 0
    killed = 0
    for i in data:
        if i['kill_player_id'] == pid:
            kill += 1
        if i['killed_player_id'] == pid:
            killed += 1
    p_kd_diff = kill - killed
    print('队员id：', pid, '该队员p_kd_diff值为:', p_kd_diff)


# 队员该小局击杀数和死亡数的比例
def p_kd_ratio(pid, data):
    kill = 0
    killed = 0
    for i in data:
        if i['kill_player_id'] == pid:
            kill += 1
        if i['killed_player_id'] == pid:
            killed += 1
    if killed != 0:
        p_kd_ratio = kill / killed
    else:
        p_kd_ratio = 'NAN'
    print('队员id：', pid, '该队员p_kd_ratio值为:', p_kd_ratio)


if __name__ == '__main__':
    # 回合数  系列赛id  team1  team2 state match_id
    calculate(16, 297, 174, 173, 0, 1263)
    # 回合数  系列赛id  match_id
    get_player(16, 297, 1263)
from common.do_mongoDB import MongoDB
from common.do_mysql import DoMySql

game_id = 3
match_id = 1333  # 小局id
round_num = 29  # 回合总数
team_id = 180


def get_seriesId():
    sidList = []
    cnn = DoMySql().link_testsql()
    cursor = cnn.cursor()
    sql = 'SELECT * FROM `data-center`.series WHERE league_id = 149 AND game_id = 3'
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        sidList.append(list(i)[0])
    return sidList


def get_data(dataBase, collection):
    myDb = MongoDB()
    collect = myDb.connect(dataBase, collection)
    sen = '{}'
    result = myDb.select_data_all(collect, sen)
    return result


def filter(data, list):
    result = []
    for item in data:
        if item['series_id'] in list:
            result.append(item)
    return result


# 参与统计的小局总数为
def count_match(data):
    count = 0
    for item in data:
        team_data = item['data']
        for i in team_data:
            if i['team_id'] == team_id:
                count += 1
    print("参与统计的小局总数为:", count)


# 队伍获胜的小局总数
def match_win_count(data):
    count = 0
    for item in data:
        team_data = item['data']
        for item in team_data:
            if item['team_id'] == team_id:
                if item['team_score'][0] == 16:
                    count += 1
    print('队伍获胜的小局总数为:', count)


# 连胜/连败 小局
def match_wl_streak(data):
    count_win = 0
    count_lose = 0
    max_win = 0
    max_lose = 0
    for item in data:
        team_data = item['data']
        for item in team_data:
            if item['team_id'] == team_id:
                if item['team_score'][0] == 16:
                    count_lose = 0
                    count_win += 1
                    if count_win > max_win:
                        max_win = count_win
                else:
                    count_win = 0
                    count_lose += 1
                    if count_lose > max_lose:
                        max_lose = count_lose
    print('小局连胜数量为:', max_win, ' 小局连败数量为:', max_lose)


# 参与统计的系列赛数量
def series_count(data):
    s_list = []
    count = 0
    for item in data:
        team_data = item['data']
        for i in team_data:
            if i['team_id'] == team_id:
                if item['series_id'] not in s_list:
                    s_list.append(item['series_id'])
                    count += 1
    print("参与统计的系列赛总数为:", count)


if __name__ == '__main__':
    data = get_data('data-center', 'csgo_result')
    list = get_seriesId()
    data = filter(data, list)
    count_match(data)
    match_win_count(data)
    match_wl_streak(data)
    series_count(data)
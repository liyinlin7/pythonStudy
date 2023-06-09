from common.do_mongoDB import MongoDB

mogonDB_dataBase = 'data-center'
mogonDB_collection_csgo = 'csgo_event'


class CSGOWinType(object):

    def csgo_win(self,match_id, env_flag):
        coll = MongoDB().connect(dataBase=mogonDB_dataBase,  collection=mogonDB_collection_csgo, status=env_flag)
        sen = '{"match_id":' + str(match_id) + '}'
        datas = MongoDB().select_data_all(collection=coll, sen=sen)
        team_A = 0
        team_B = 0
        for i in datas:
            win_value = ''
            if i.get('type') == 6:
                event = i.get('event')
                round_num = event['round_num']
                win_type = event['win_type']
                win_team_id = event['win_team_id']
                if round_num <= 15:
                    if win_type == 1:
                        win_value = 'CT获胜-全歼'
                        team_A += 1
                    elif win_type == 2:
                        win_value = 'T获胜-全歼'
                        team_B += 1
                    elif win_type == 3:
                        win_value = 'T获胜-炸弹爆炸'
                        team_B += 1
                    elif win_type == 4:
                        win_value = 'CT获胜-炸弹拆除'
                        team_A += 1
                    elif win_type == 5:
                        win_value = 'CT获胜-时间耗尽'
                        team_A += 1
                    elif win_type == 6:
                        win_value = '平局'
                elif round_num > 15 and round_num <= 30:
                    if win_type == 1:
                        win_value = 'CT获胜-全歼'
                        team_B += 1
                    elif win_type == 2:
                        win_value = 'T获胜-全歼'
                        team_A += 1
                    elif win_type == 3:
                        win_value = 'T获胜-炸弹爆炸'
                        team_A += 1
                    elif win_type == 4:
                        win_value = 'CT获胜-炸弹拆除'
                        team_B += 1
                    elif win_type == 5:
                        win_value = 'CT获胜-时间耗尽'
                        team_B += 1
                    elif win_type == 6:
                        win_value = '平局'
                elif round_num > 30:
                    print("加时赛")
                print("round_num:", round_num)
                print("win_team_id:", win_team_id)
                print("胜利方式为:", win_value)
                print(f'CT的比分   {str(team_A)}:{str(team_B)}   T的比分')
                print("--------------------------------------------------------")


if __name__ == '__main__':
    cs_event = CSGOWinType()
    cs_event.csgo_win(match_id=34263, env_flag=1)

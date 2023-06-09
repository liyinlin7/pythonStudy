import json


class Live_csgo(object):

    def __init__(self):
        self.data = '''
           {"match_id":29642,"series_id":1606932826,"round_num":3,"round_time":69,"team":[{"team_id":1087,"round_kill":2,"kill":6,"round_headshot":2,"headshot":4,"round_death":1,"death":11,"round_assist":0,"assist":1,"round_flash_assist":0,"flash_assist":0,"entry_kill":2,"entry_death":1,"one_win_multi":0,"multi_kill":1,"player":[{"player_id":569,"gold":450,"hp":71,"item":[116,114,95],"round_kill":1,"kill":2,"round_headshot":1,"headshot":1,"round_death":0,"death":2,"round_assist":0,"assist":0,"round_flash_assist":0,"flash_assist":0,"entry_kill":1,"entry_death":0,"one_win_multi":0,"multi_kill":0},{"player_id":566,"gold":400,"hp":39,"item":[116,114,95],"round_kill":0,"kill":2,"round_headshot":0,"headshot":1,"round_death":0,"death":2,"round_assist":0,"assist":0,"round_flash_assist":0,"flash_assist":0,"entry_kill":0,"entry_death":1,"one_win_multi":0,"multi_kill":1},{"player_id":567,"gold":200,"hp":0,"item":[],"round_kill":0,"kill":1,"round_headshot":0,"headshot":1,"round_death":1,"death":3,"round_assist":0,"assist":1,"round_flash_assist":0,"flash_assist":0,"entry_kill":1,"entry_death":0,"one_win_multi":0,"multi_kill":0},{"player_id":570,"gold":350,"hp":34,"item":[116,114,95],"round_kill":1,"kill":1,"round_headshot":1,"headshot":1,"round_death":0,"death":2,"round_assist":0,"assist":0,"round_flash_assist":0,"flash_assist":0,"entry_kill":0,"entry_death":0,"one_win_multi":0,"multi_kill":0},{"player_id":571,"gold":300,"hp":100,"item":[116,114,92],"round_kill":0,"kill":0,"round_headshot":0,"headshot":0,"round_death":0,"death":2,"round_assist":0,"assist":0,"round_flash_assist":0,"flash_assist":0,"entry_kill":0,"entry_death":0,"one_win_multi":0,"multi_kill":0}]},{"team_id":1104,"round_kill":1,"kill":11,"round_headshot":1,"headshot":9,"round_death":2,"death":6,"round_assist":0,"assist":2,"round_flash_assist":0,"flash_assist":2,"entry_kill":1,"entry_death":2,"one_win_multi":0,"multi_kill":3,"player":[{"player_id":5362,"gold":3000,"hp":0,"item":[],"round_kill":1,"kill":3,"round_headshot":1,"headshot":3,"round_death":1,"death":1,"round_assist":0,"assist":0,"round_flash_assist":0,"flash_assist":0,"entry_kill":0,"entry_death":0,"one_win_multi":0,"multi_kill":0},{"player_id":850,"gold":1300,"hp":41,"item":[116,114,97],"round_kill":0,"kill":3,"round_headshot":0,"headshot":2,"round_death":0,"death":2,"round_assist":0,"assist":0,"round_flash_assist":0,"flash_assist":0,"entry_kill":0,"entry_death":0,"one_win_multi":0,"multi_kill":1},{"player_id":852,"gold":100,"hp":0,"item":[],"round_kill":0,"kill":2,"round_headshot":0,"headshot":1,"round_death":1,"death":2,"round_assist":0,"assist":1,"round_flash_assist":0,"flash_assist":0,"entry_kill":1,"entry_death":2,"one_win_multi":0,"multi_kill":1},{"player_id":853,"gold":1150,"hp":100,"item":[116,114,112,94],"round_kill":0,"kill":2,"round_headshot":0,"headshot":2,"round_death":0,"death":1,"round_assist":0,"assist":0,"round_flash_assist":0,"flash_assist":0,"entry_kill":0,"entry_death":0,"one_win_multi":0,"multi_kill":1},{"player_id":3989,"gold":2400,"hp":98,"item":[116,114,112,105],"round_kill":0,"kill":1,"round_headshot":0,"headshot":1,"round_death":0,"death":0,"round_assist":0,"assist":1,"round_flash_assist":0,"flash_assist":2,"entry_kill":0,"entry_death":0,"one_win_multi":0,"multi_kill":0}]}]}
        '''
        self.data_tj = '''
            {"match_id":29642,"series_id":1606932826,"round_num":3,"team":[{"team_id":1104,"team_score":[2,2,0,0],"kpr":"3.67","dpr":"2.00","fk_diff":"-1.00","kd_diff":"5.00","kd_ratio":"1.83","adr":"83.73","kast":"2.60","player":[{"player_id":850,"kpr":"1.00","dpr":"0.67","fk_diff":"0.00","kd_diff":"1.00","kd_ratio":"1.50","adr":"125.67","kast":"3"},{"player_id":853,"kpr":"0.67","dpr":"0.33","fk_diff":"0.00","kd_diff":"1.00","kd_ratio":"2.00","adr":"67.33","kast":"3"},{"player_id":3989,"kpr":"0.33","dpr":"0.00","fk_diff":"0.00","kd_diff":"1.00","kd_ratio":"","adr":"76.33","kast":"3"},{"player_id":5362,"kpr":"1.00","dpr":"0.33","fk_diff":"0.00","kd_diff":"2.00","kd_ratio":"3.00","adr":"69","kast":"3"},{"player_id":852,"kpr":"0.67","dpr":"0.67","fk_diff":"-1.00","kd_diff":"0.00","kd_ratio":"1.00","adr":"80.33","kast":"1"}]},{"team_id":1087,"team_score":[1,1,0,0],"kpr":"2.00","dpr":"3.67","fk_diff":"1.00","kd_diff":"-5.00","kd_ratio":"0.55","adr":"45.27","kast":"2.00","player":[{"player_id":566,"kpr":"0.67","dpr":"0.67","fk_diff":"-1.00","kd_diff":"0.00","kd_ratio":"1.00","adr":"64","kast":"2"},{"player_id":571,"kpr":"0.00","dpr":"0.67","fk_diff":"0.00","kd_diff":"-2.00","kd_ratio":"","adr":"0","kast":"1"},{"player_id":569,"kpr":"0.67","dpr":"0.67","fk_diff":"1.00","kd_diff":"0.00","kd_ratio":"1.00","adr":"49.33","kast":"2"},{"player_id":567,"kpr":"0.33","dpr":"1.00","fk_diff":"1.00","kd_diff":"-2.00","kd_ratio":"0.33","adr":"54","kast":"3"},{"player_id":570,"kpr":"0.33","dpr":"0.67","fk_diff":"0.00","kd_diff":"-1.00","kd_ratio":"0.50","adr":"59","kast":"2"}]}]}
        '''

    def live_data(self):
        data = self.data
        json_data = json.loads(data)
        teams_data = json_data.get('team')
        print(teams_data)
        for i in teams_data:
            players_data = i.get('player')
            team_round_kill = i['round_kill']
            team_kill = i['kill']
            team_round_headshot = i['round_headshot']
            team_headshot = i['headshot']
            team_round_death = i['round_death']
            team_death = i['death']
            team_round_assist = i['round_assist']
            team_assist = i['assist']
            team_round_flash_assist = i['round_flash_assist']
            team_flash_assist = i['flash_assist']
            team_entry_kill = i['entry_kill']
            team_entry_death = i['entry_death']
            team_one_win_multi = i['one_win_multi']
            team_multi_kill = i['multi_kill']
            # ---------------------------------
            player_round_kill = 0
            player_kill = 0
            player_round_headshot = 0
            player_headshot = 0
            player_round_death = 0
            player_death = 0
            player_round_assist = 0
            player_assist = 0
            player_round_flash_assist = 0
            player_flash_assist = 0
            player_entry_kill = 0
            player_entry_death = 0
            player_one_win_multi = 0
            player_multi_kill = 0
            for b in players_data:
                player_round_kill += b['round_kill']
                player_kill += b['kill']
                player_round_headshot += b['round_headshot']
                player_headshot += b['headshot']
                player_round_death += b['round_death']
                player_death += b['death']
                player_round_assist += b['round_assist']
                player_assist += b['assist']
                player_round_flash_assist += b['round_flash_assist']
                player_flash_assist += b['flash_assist']
                player_entry_kill += b['entry_kill']
                player_entry_death += b['entry_death']
                player_one_win_multi += b['one_win_multi']
                player_multi_kill += b['multi_kill']
            print(f"队伍 round_kill 推送数据：{team_round_kill}，计算{player_round_kill}")
            print(f"队伍 kill 推送数据：{team_kill}，计算{player_kill}")
            print(f"队伍 round_headshot 推送数据：{team_round_headshot}，计算{player_round_headshot}")
            print(f"队伍 headshot 推送数据：{team_headshot}，计算{player_headshot}")
            print(f"队伍 round_death 推送数据：{team_round_death}，计算{player_round_death}")
            print(f"队伍 death 推送数据：{team_death}，计算{player_death}")
            print(f"队伍 round_assist 推送数据：{team_round_assist}，计算{player_round_assist}")
            print(f"队伍 assist 推送数据：{team_assist}，计算{player_assist}")
            print(f"队伍 round_flash_assist 推送数据：{team_round_flash_assist}，计算{player_round_flash_assist}")
            print(f"队伍 flash_assist 推送数据：{team_flash_assist}，计算{player_flash_assist}")
            print(f"队伍 entry_kill 推送数据：{team_entry_kill}，计算{player_entry_kill}")
            print(f"队伍 entry_death 推送数据：{team_entry_death}，计算{player_entry_death}")
            print(f"队伍 one_win_multi 推送数据：{team_one_win_multi}，计算{player_one_win_multi}")
            print(f"队伍 multi_kill 推送数据：{team_multi_kill}，计算{player_multi_kill}")
            print(f"----------------------------{i['team_id']}--------------------------------------")

    def live_data_tj(self):
        '''
            统计数据和实时数据 计算对比
        :return:
        '''
        data_tj = self.data_tj
        data = self.data
        json_data_tj = json.loads(data_tj)
        teams_data_tj = json_data_tj.get('team')
        json_data = json.loads(data)
        teams_data = json_data.get('team')
        for i in teams_data:
            print("--------team_id------------", i['team_id'])
            players_data = i.get('player')
            round_num = json_data['round_num']
            for y in teams_data_tj:
                y_players = y['player']
                if i['team_id'] == y['team_id']:
                    player_entry_kill = 0
                    player_entry_death = 0
                    player_kill = 0
                    player_death = 0
                    player_kast = 0
                    player_adr = 0
                else:
                    continue
                for b in players_data:
                        b_player_id = b['player_id']
                        player_kill += b['kill']
                        player_death += b['death']
                        player_entry_kill += b['entry_kill']
                        player_entry_death += b['entry_death']
                        for c in y_players:
                            if b_player_id == c['player_id']:
                                print("--------player_id------------", c['player_id'])
                                player_adr += float(c['adr'])
                                player_kast += float(c['kast'])
                                print(f"队员 kpr 推送数据：{c['kpr']}，计算{b['kill'] / round_num}")
                                print(f"队员 dpr 推送数据：{c['dpr']}，计算{b['death'] / round_num}")
                                print(f"队员 fk_diff 推送数据：{c['fk_diff']}，计算{b['entry_kill']-b['entry_death']}")
                                print(f"队员 kd_diff 推送数据：{c['kd_diff']}，计算{b['kill'] - b['death']}")
                                if b['death'] == 0:
                                    print(f"队员 kd_ratio 推送数据：{c['kd_ratio']}，计算{b['kill'] / 1}")
                                else:
                                    print(f"队员 kd_ratio 推送数据：{c['kd_ratio']}，计算{b['kill'] / b['death']}")
                                print(f"队员 adr 推送数据：{c['adr']}，计算{None}")
                                print(f"队员 kast 推送数据：{c['kast']}，计算{None}")
                print("--------------------------------------")
                print(f"队伍 kpr 推送数据：{y['kpr']}，计算{player_kill / round_num}")
                print(f"队伍 dpr 推送数据：{y['dpr']}，计算{player_death / round_num}")
                print(f"队伍 fk_diff 推送数据：{y['fk_diff']}，计算{player_entry_kill - player_entry_death}")
                print(f"队伍 kd_diff 推送数据：{y['kd_diff']}，计算{player_kill - player_death}")
                print(f"队伍 kd_ratio 推送数据：{y['kd_ratio']}，计算{player_kill / player_death}")
                print(f"队伍 adr 推送数据：{y['adr']}，计算{player_adr /5}")
                print(f"队伍 kast 推送数据：{y['kast']}，计算{player_kast /5}")


if __name__ == '__main__':
    li = Live_csgo()
    # li.live_data()
    li.live_data_tj()

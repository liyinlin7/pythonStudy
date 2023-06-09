import time
import json
from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
import datetime
from common import my_logger
from common.read_config import ReadConfig
from common import read_path


class BasketBallResult(object):

    def __init__(self, env_flag):
        self.env_flag = env_flag
        self.do_mysql = DoMySql()
        self.cnn_basketball = self.do_mysql.connect_mysql(env_flag=env_flag)  # 0是测试，1是线上
        self.team = self.football_team()
        self.player = self.football_player()
        self.request_dataBase = ReadConfig().read_config(read_path.conf_path, 'sports_soccer', 'dataBase')
        self.request_dataBase_result = ReadConfig().read_config(read_path.conf_path, 'sports_soccer',
                                                                'mogonDB_collection_result')

    def football_team(self):
        sql = '''
            SELECT * FROM `sports-soccer`.team ;
        '''
        basket_team_datas = self.do_mysql.select(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        team_list = []
        for i in basket_team_datas:
            team_map = {}
            team_map[i['id']] = i['name_zh']
            team_list.append(team_map)
        return team_list

    def football_player(self):
        sql = '''
            SELECT * FROM `sports-soccer`.player ;
        '''
        basket_player_datas = self.do_mysql.select(cnn=self.cnn_basketball, sql=sql, env_flag=self.env_flag)
        player_list = []
        for i in basket_player_datas:
            player_map = {}
            player_map[i['id']] = i['name_zh']
            player_list.append(player_map)
        return player_list

    def requestdata_team_player_id_null(self, match_id, team_id_):
        '''
            1.赛果数据-有team_id=0
            2.赛果数据-有player_id=0
        :return:
        '''
        print(self.request_dataBase_result)
        print(self.request_dataBase)
        dcnn = MongoDB(self.env_flag).sport_connect(dataBase=self.request_dataBase, collection=self.request_dataBase_result)
        result_datas = MongoDB(self.env_flag).get_data_list(dcnn=dcnn, list=match_id)
        for i in result_datas:
            data_list = i['data']
        for i in data_list:
            playere_lists = i['player']
            team_id = i['teamId']
            team_goal = i['goal']
            team_assist = i['assist']
            team_yellow2RedCards = i['yellow2RedCards']
            team_dribble = i['dribble']
            team_dribbleSuccess = i['dribbleSuccess']
            team_dribbleSuccessRate = i['dribbleSuccessRate']
            team_block = i['block']
            team_clearance = i['clearance']
            team_tackle = i['tackle']
            team_interception = i['interception']
            team_pass = i['pass']
            team_passSuccess = i['passSuccess']
            team_passSuccessRate = i['passSuccessRate']
            team_longPass = i['longPass']
            team_longPassSuccess = i['longPassSuccess']
            team_longPassSuccessRate = i['longPassSuccessRate']
            team_crossPass = i['crossPass']
            team_crossPassSuccess = i['crossPassSuccess']
            team_crossPassSuccessRate = i['crossPassSuccessRate']
            team_keyPass = i['keyPass']
            team_lossPossession = i['lossPossession']
            team_challenge = i['challenge']
            team_challengeSuccess = i['challengeSuccess']
            team_challengeSuccessRate = i['challengeSuccessRate']
            team_foul = i['foul']
            team_fouled = i['fouled']
            team_offside = i['offside']
            team_save = i['save']
            team_fistBall = i['fistBall']
            team_runOut = i['runOut']
            team_runOutSuccess = i['runOutSuccess']
            team_runOutSuccessRate = i['runOutSuccessRate']
            team_highClaim = i['highClaim']
            player_goal = 0
            player_assist = 0
            player_yellow2RedCards = 0
            player_dribble = 0
            player_dribbleSuccess = 0
            player_block = 0
            player_clearance = 0
            player_tackle = 0
            player_interception = 0
            player_pass = 0
            player_passSuccess = 0
            player_longPass = 0
            player_longPassSuccess = 0
            player_crossPass = 0
            player_crossPassSuccess = 0
            player_keyPass = 0
            player_lossPossession = 0
            player_challenge = 0
            player_challengeSuccess = 0
            player_foul = 0
            player_fouled = 0
            player_offside = 0
            player_save = 0
            player_fistBall = 0
            player_runOut = 0
            player_runOutSuccess = 0
            player_highClaim = 0
            for player in playere_lists:
                player_goal += player['goal']
                player_assist += player['assist']
                player_yellow2RedCards += player['yellow2RedCards']
                player_dribble += player['dribble']
                player_dribbleSuccess += player['dribbleSuccess']
                player_block += player['block']
                player_clearance += player['clearance']
                player_tackle += player['tackle']
                player_interception += player['interception']
                player_pass += player['pass']
                player_passSuccess += player['passSuccess']
                player_longPass += player['longPass']
                player_longPassSuccess += player['longPassSuccess']
                player_crossPass += player['crossPass']
                player_crossPassSuccess += player['crossPassSuccess']
                player_keyPass += player['keyPass']
                player_lossPossession += player['lossPossession']
                player_challenge += player['challenge']
                player_challengeSuccess += player['challengeSuccess']
                player_foul += player['foul']
                player_fouled += player['fouled']
                player_offside += player['offside']
                player_save += player['save']
                player_fistBall += player['fistBall']
                player_runOut += player['runOut']
                player_runOutSuccess += player['runOutSuccess']
                player_highClaim += player['highClaim']
            print("队伍的 goal：", team_goal, "队员之和：", player_goal)
            print("队伍的 assist：", team_assist, "队员之和：", player_assist)
            print("队伍的 yellow2RedCards：", team_yellow2RedCards, "队员之和：", player_yellow2RedCards)
            print("队伍的 dribble：", team_dribble, "队员之和：", player_dribble)
            print("队伍的 dribble_success：", team_dribbleSuccess, "队员之和：", player_dribbleSuccess)
            if team_dribbleSuccess == 0 or team_dribble == 0:
                team_dribbleSuccessRate_ = 0
            else:
                team_dribbleSuccessRate_ = team_dribbleSuccess / team_dribble
            print("队伍的 dribble_success_rate：", team_dribbleSuccessRate, "队员之和：", team_dribbleSuccessRate_)
            print("队伍的 block：", team_block, "队员之和：", player_block)
            print("队伍的 clearance：", team_clearance, "队员之和：", player_clearance)
            print("队伍的 tackle：", team_tackle, "队员之和：", player_tackle)
            print("队伍的 interception：", team_interception, "队员之和：", player_interception)
            print("队伍的 pass：", team_pass, "队员之和：", player_pass)
            print("队伍的 pass_success：", team_passSuccess, "队员之和：", player_passSuccess)
            if team_passSuccess == 0 or team_pass == 0:
                team_passSuccessRate_ = 0
            else:
                team_passSuccessRate_ = team_passSuccess / team_pass
            print("队伍的 pass_success_rate：", team_passSuccessRate, "计算：", team_passSuccessRate_)
            print("队伍的 long_pass：", team_longPass, "队员之和：", player_longPass)
            print("队伍的 long_pass_success：", team_longPassSuccess, "队员之和：", player_longPassSuccess)
            if team_longPassSuccess == 0 or team_longPass == 0:
                team_longPassSuccessRate_ = 0
            else:
                team_longPassSuccessRate_ = team_longPassSuccess / team_longPass
            print("队伍的 long_pass_success_rate：", team_longPassSuccessRate, "计算：", team_longPassSuccessRate_)
            print("队伍的 cross_pass：", team_crossPass, "队员之和：", player_crossPass)
            print("队伍的 cross_pass_success：", team_crossPassSuccess, "队员之和：", player_crossPassSuccess)
            if team_crossPassSuccess == 0 or team_crossPass == 0:
                team_crossPassSuccessRate_ = 0
            else:
                team_crossPassSuccessRate_ = team_crossPassSuccess / team_crossPass
            print("队伍的 cross_pass_success_tate：", team_crossPassSuccessRate, "计算：", team_crossPassSuccessRate_)
            print("队伍的 key_pass：", team_keyPass, "队员之和：", player_keyPass)
            print("队伍的 loss_possession：", team_lossPossession, "队员之和：", player_lossPossession)
            print("队伍的 challenge：", team_challenge, "队员之和：", player_challenge)
            print("队伍的 challenge_success：", team_challengeSuccess, "队员之和：", player_challengeSuccess)
            if team_challengeSuccess == 0 or team_challenge == 0:
                team_challengeSuccessRate_ = 0
            else:
                team_challengeSuccessRate_ = team_challengeSuccess / team_challenge
            print("队伍的 challenge_success_rate：", team_challengeSuccessRate, "队员之和：", team_challengeSuccessRate_)
            print("队伍的 foul：", team_foul, "队员之和：", player_foul)
            print("队伍的 fouled：", team_fouled, "队员之和：", player_fouled)
            print("队伍的 offside：", team_offside, "队员之和：", player_offside)
            print("队伍的 save：", team_save, "队员之和：", player_save)
            print("队伍的 fist_ball：", team_fistBall, "队员之和：", player_fistBall)
            print("队伍的 run_out：", team_runOut, "队员之和：", player_runOut)
            print("队伍的 run_out_success：", team_runOutSuccess, "队员之和：", player_runOutSuccess)
            if team_runOutSuccess == 0 or team_runOut == 0:
                team_runOutSuccessRate_ = 0
            else:
                team_runOutSuccessRate_ = team_runOutSuccess / team_runOut
            print("队伍的 run_out_success_rate：", team_runOutSuccessRate, "计算：", team_runOutSuccessRate_)
            print("队伍的 high_claim：", team_highClaim, "队员之和：", player_highClaim)
            print('-------------------------------------------------------------------------')


if __name__ == '__main__':
    b = BasketBallResult(env_flag=0)
    b.requestdata_team_player_id_null([75912], [1491, 1476])
    # con = DoMySql().link_testsql()
    # storage_data(data, con)
    # storage_statistics(data, con)
    # storage_special_event(data, con)






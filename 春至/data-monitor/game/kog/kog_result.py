from common.do_mysql import DoMySql
from common.do_mongoDB import MongoDB
import datetime
import json




class Kog_Result(object):
    '''
        赛果数据的计算
    '''
    def __init__(self, env_flag, cnn_centon, cnn_basic, mysql_cnn, monGon_cnn):
        self.env_flag = env_flag
        self.cnn_centon = cnn_centon
        self.cnn_basic = cnn_basic
        self.mogonDB_dataBase = 'data-result'
        self.mogonDB_collection_kog_result = 'kog_result'
        self.monGon = monGon_cnn
        self.doMysql = mysql_cnn

    def get_data_one(self, match_id, dataBase, collection):
        myDb = self.monGon
        collect1 = myDb.connect(dataBase, collection)
        sen = '{"match_id":' + str(match_id) + '}'
        result = myDb.select_data_one(collect1, sen)
        return result

    def kog_result_data(self, match_id):
        result_datas = self.get_data_one(match_id=match_id, dataBase=self.mogonDB_dataBase, collection=self.mogonDB_collection_kog_result)
        data = result_datas['data']
        print(data)
        self.team_data(team_id_z, data)
        self.team_data(team_id_k, data)
        print('###############主队队伍id:', team_id_z, '########################')
        self.player_data(team_id_z, data)
        print('###############副队队伍id:', team_id_k, '########################')
        self.player_data(team_id_k, data)


    def team_data(self, team_id, data):
        '''
        :param team_id:  队伍ID
        :param data: 赛果数据
        :return:
        '''
        for team in data:
            if team_id == team['team_id']:
                player_data = team['player']
                p_gold, p_kill, p_assist, p_death, p_fight, p_damage, p_damage_taken = 0, 0, 0, 0, 0, 0, 0
                p_streak = []
                for player in player_data:
                    p_gold = p_gold + player['gold']
                    p_kill = p_kill + player['kill']
                    p_assist = p_assist + player['assist']
                    p_death = p_death + player['death']
                    p_fight = p_fight + float(player['team_fight'])
                    if player['damage'] is not None:
                        p_damage = p_damage + player['damage']
                    if player['damage_taken'] is not None:
                        p_damage_taken = p_damage_taken + player['damage_taken']
                    p_streak.append(player['kill_streak'])
                print('#################队伍数据，队伍id:', team_id, '################')
                print('[队伍总经济]:', team['gold'], '[计算得出的结果]:', p_gold)
                print('[队伍经济/分钟]:', team['gold_min'], '[计算得出的结果]:', format(team['gold'] / (time / 60), '.2f'))
                print('[队伍经济差]:', team['gold_diff'], '[计算得出的结果]:')
                print('[队伍英雄总击杀数]:', team['kill'], '[计算得出的结果]:', p_kill)
                print('[队伍英雄总助攻数]:', team['assist'], '[计算得出的结果]:', p_assist)
                print('[队伍英雄总死亡数]:', team['death'], '[计算得出的结果]:', p_death)
                print('[队伍kda]:', team['kda'], '[计算得出的结果]: ', format((team['kill'] + p_assist) / p_death, '.2f'))
                print('[队伍最大连续击杀]:', team['kill_streak'], '[计算得出的结果]:', p_streak)
                print('[平均队员参团率]:', team['team_fight'], '[计算得出的结果]:', format(p_fight / 5, '.2f'))
                print('[队伍总输出]:', team['damage'], '[计算得出的结果]:', p_damage)
                print('[队伍输出/分钟]:', team['damage_min'], '[计算得出的结果]:', format(p_damage / (time / 60), '.2f'))
                print('[平均队员输出]:', team['avg_player_damage'], '[计算得出的结果]:', format(p_damage / 5, '.2f'))
                print('[队伍平均击杀输出]:', team['damage_kill_ratio'], '[计算得出的结果]:', format(p_damage / p_kill, '.2f'))
                print('[队伍输出经济比]:', team['damage_gold_ratio'], '[计算得出的结果]:', format(p_damage / p_gold, '.2f'))
                print('[队伍总承伤]:', team['damage_taken'], '[计算得出的结果]:', p_damage_taken)
                print('[队伍承伤/分钟]:', team['damage_taken_min'], '[计算得出的结果]:', format(p_damage_taken / (time / 60), '.2f'))
                print('[平均队员承伤]:', team['avg_player_damage_taken'], '[计算得出的结果]:', format(p_damage_taken / 5, '.2f'))
                print('[队伍平均死亡承伤]:', team['damage_taken_death_ratio'], '[计算得出的结果]:',
                      format(p_damage_taken / p_death, '.2f'))
                print('[队伍承伤经济比例]:', team['damage_taken_gold_ratio'], '[计算得出的结果]:',
                      format(p_damage_taken / p_gold, '.2f'))
                print('[队伍中立生物总击杀数]:', team['neutral_kill'])
                print('[队伍暴君击杀数]:', team['tyrant_kill'])
                print('[队伍黑暗暴君击杀数]:', team['dark_tyrant_kill'])
                print('[队伍先知主宰击杀数]:', team['prophet_overlord_kill'])
                print('[队伍主宰击杀数]:', team['overlord_kill'])
                print('[队伍风暴龙王击杀数]:', team['storm_dragon_kill'])
                print('[队伍摧毁防御塔总数]:', team['tower_kill'])

    def player_data(self, team_id, data):
        player_data = None
        for item in data:
            if item['team_id'] == team_id:
                # 队员计算需要用到的队伍数据
                player_data = item['player']
                team_gold = item['gold']
                team_kill = item['kill']
                team_death = item['death']
                team_damage = item['damage']
                team_damage_taken = item['damage_taken']
        # print(player_data)
        for item in player_data:
            print('###############队员的id: ', item['player_id'], '########################')
            print('[队员的等级]:', item['level'])
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
            print('[队员多杀次数]:', item['multi_kill'])
            print('[队员最大连续击杀]:', item['kill_streak'])
            print('[队员参团率]:', item['team_fight'], '[计算得出的结果]:',
                  format((item['kill'] + item['assist']) / team_kill, '.2f'))
            print('[队员输出]:', item['damage'])
            if item['kill'] != 0:
                kill = item['kill']
            else:
                kill = 1
            if item['death'] != 0:
                death = item['death']
            else:
                death = 1
            if item['damage'] is None:
                print('[队员输出/分钟]:', item['damage_min'], '[计算得出的结果]:', )
                print('[队员输出/分钟]:', item['damage_ratio'], '[计算得出的结果]:', )
                print('[队员平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', )
                print('[队员输出经济比例]:', item['damage_gold_ratio'], '[计算得出的结果]:',)
            else:
                print('[队员输出/分钟]:', item['damage_min'], '[计算得出的结果]:', format((item['damage']) / (time / 60), '.2f'))
                print('[队员输出占比]:', item['damage_ratio'], '[计算得出的结果]:', format((item['damage']) / team_damage, '.2f'))
                print('[队员平均击杀输出]:', item['damage_kill_ratio'], '[计算得出的结果]:', format((item['damage']) / kill, '.2f'))
                print('[队员输出经济比例]:', item['damage_gold_ratio'], '[计算得出的结果]:',format(item['damage'] / item['gold'], '.2f'))
            # damage_ratio = float(item['damage_ratio'])
            # gold_ratio = float(item['gold_ratio'])

            print('[队员承伤]:', item['damage_taken'])
            if item['damage_taken'] is None:
                print('[队员承伤/分钟]:', item['damage_taken_min'], '[计算得出的结果]:',)
                print('[队员承伤占比]:', item['damage_taken_ratio'], '[计算得出的结果]:',)
                print('[队员平均死亡承伤]:', item['damage_taken_death_ratio'], '[计算得出的结果]:',)
                print('[队员承伤经济比例]:', item['damage_taken_gold_ratio'], '[计算得出的结果]:',)
            else:
                print('[队员承伤/分钟]:', item['damage_taken_min'], '[计算得出的结果]:', format((item['damage_taken']) / (time / 60), '.2f'))
                print('[队员承伤占比]:', item['damage_taken_ratio'], '[计算得出的结果]:', format((item['damage_taken']) / team_damage_taken, '.2f'))
                print('[队员平均死亡承伤]:', item['damage_taken_death_ratio'], '[计算得出的结果]:', format((item['damage_taken']) / death, '.2f'))
                print('[队员承伤经济比例]:', item['damage_taken_gold_ratio'], '[计算得出的结果]:',format(item['damage_taken'] / item['gold'], '.2f'))
            # damage_taken_ratio = float(item['damage_taken_ratio'])
            # print(damage_taken_ratio)
            print('[队员中立生物总击杀数]:', item['neutral_kill'])
            print('[队员暴君击杀数]:', item['tyrant_kill'])
            print('[队员黑暗暴君击杀数]:', item['dark_tyrant_kill'])
            print('[队员先知主宰击杀数]:', item['prophet_overlord_kill'])
            print('[队员主宰击杀数]:', item['overlord_kill'])
            print('[队员风暴龙王击杀数]:', item['storm_dragon_kill'])

# 计算数据前需要记录
team_id_z = 890  # 主队ID
team_id_k = 184  # 客队ID
time = 1095  # 比赛时长
if __name__ == '__main__':
    mysql_cnn = DoMySql()
    monGon_cnn = MongoDB()
    cnn_centon = mysql_cnn.cnn_centon_def()
    cnn_basic = mysql_cnn.cnn_basic_def()
    a = Kog_Result('develop', cnn_centon, cnn_basic, mysql_cnn, monGon_cnn)
    a.kog_result_data(4232)


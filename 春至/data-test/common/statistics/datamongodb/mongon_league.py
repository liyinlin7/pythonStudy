from common.do_mongoDB import MongoDB




dataBase = 'data-center'
collection = 'kog_result'

def mongoDB_league(dataBase, collection):
    match_id = [29,26,27,28,57,60,58,56,59,134,131,133,132,197,198,199,200,196]
    myDb = MongoDB()
    collect = myDb.connect(dataBase, collection, status=0)  # status=0 是测试环境数据库
    sen = '{"match_id":' + '{$in:'+str(match_id) + '}}'
    # print(match_id)
    # aa = eval(aa)
    # print(aa)
    result = myDb.select_data_all(collect, sen)
    print(result)
    return result

'''
    {
    "player_id": "",  # 队员Id
    "level": int(),  # 等级
    "item": [],  # 装备
    "spell": [],  # 技能信息

    "gold": None,  # 队员总经济
    "gold_min": None,  # 队员经济/分钟
    "gold_diff": None,  # 经济差
    "gold_ratio": None,  # 队员经济占队员总经济比例

    "cs": int(),  # 补刀
    "cs_min": "",  # 队员补刀/分钟
    "cs_diff": int(),  # 队员补刀差
    "cs_ratio": "",  # 队员补刀占队员总补刀比例

    "ward": None,  # 队员总插眼数  wards_placed
    "ward_kill": None,  # 队员排眼总数
    "ward_min": None,  # 队员插眼/分钟
    "ward_kill_min": None,  # 队员排眼/分钟

    "kill": int(),  # 英雄总击杀数
    "assist": int(),  # 总助攻
    "death": int(),  # 队员总死亡
    "kda": "",  # KDA

    "double": None,  # 队员双杀次数
    "triple": None,  # 队员三杀次数
    "quadra": None,  # 队员四杀次数
    "penta": None,  # 队员五杀次数
    "kill_streak": None,  # 队员最大连续击杀次数

    "team_fight": "",  # 平均队员参团率
    "damage": None,  # 队员输出
    "hero_damage": None,  # 队员英雄总输出

    "physical_damage": None,  # 队员物理总输出
    "magical_damage": None,  # 队员魔法总输出

    "damage_min": None,  # 队员输出/分钟
    "damage_ratio": None,  # 队员输出占比
    "damage_kill_ratio": None,  # 队员平均击杀输出
    "damage_gold_ratio": None,  # 队员输出经济比例
    "damage_taken": None,  # 队员总承伤

    "physical_damage_taken": None,  # 队员物理总承伤
    "true_damage_taken": None,  # 队员真实承伤
    "true_damage": None,    # 队员真实输出

    "damage_taken_min": None,  # 队员承伤/分钟
    "damage_taken_ratio": None,  # 队员承伤占比
    "damage_taken_death_ratio": None,  # 队员平均死亡承伤
    "damage_taken_gold_ratio": None,  # 队员承伤经济比例

    "heal": None,  # 队员治疗总量
    "heal_min": None,  # 队员治疗量/分钟
    "heal_ratio": None,  # 队员治疗量占比

    "neutral_kill": None,  # 队员中立生物总击杀数
    "self_neutral_kill": None,  # 队员己方野区中立生物总击杀数
    "enemy_neural_kill": None,  # 队员敌方野区中立生物中击杀数
    "herald_kill": int(),  # 队员峡谷先锋总击杀数
    "nashor_kill": int(),  # 队员大龙总击杀数
    "elder_drake_kill": int(),  # 队员远古巨龙总击杀数
    "drake_kill": int(),  # 队员小龙总击杀数
    "infernal_drake_kill": int(),  # 队员炼狱亚龙总击杀数
    "mountain_drake_kill": int(),  # 队员山脉亚龙总击杀数
    "cloud_drake_kill": int(),  # 队员云端亚龙总击杀数
    "ocean_drake_kill": int(),  # 队员海洋亚龙总击杀数
    "tower_kill": None,  # 队员摧毁塔总数
    "inhibitor_kill": None,  # 队员摧毁水晶总数
}
'''

if __name__ == '__main__':
    mongoDB_league(dataBase, collection)
import os
import json
import time
import datetime

# a = 1609825330 - 3600*24*20
#
#
# print(a)
#
f = """
   '2-45703696-358085357-111.5-u-111.5', '2-45703695-358085456-111.5-u-111.5', '2-45703695-358085462-113.5-o-113.5', '2-45703696-358085357-111.5-o-111.5', '2-45703696-358085598--3-a-3', '2-45703696-358085362-114.5-o-114.5', '2-45703695-358085669--2.5-h--2.5', '2-45703695-358085636-224.5-h-224.5', '2-45703696-358085598--3-h--3', '2-45703695-358085462-113.5-u-113.5', '2-45703695-358085669--2.5-a-2.5', '2-45703696-358085557-226.5-a-226.5', '2-45703696-358085557-226.5-h-226.5', '2-45703696-358085362-114.5-u-114.5', '2-45703695-358085636-224.5-a-224.5', '2-45703695-358085456-111.5-o-111.5'
   """
h = f.replace("'", '')
z = h.replace(" ", '')
print(z)
#
#
# time_ = datetime.timedelta(seconds=178000)

# time_1 = datetime.datetime.fromtimestamp(178000/1000)
# str1 = time_1.strftime("%H:%M:%S.%f")
# print(time_)
# print(str1)
#
#
# now_time = time.time()
# print(int(now_time))


# timestamp = 1629365597
# print(datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=timestamp))
# timeArray = time.localtime(1629365597)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(otherStyleTime)

# a = int(1625727942 / 60) * 60
# print(a)
# a = [1,2]
# b = [1,2]
# if a == b:
#     print(111)
#
import json
a = '{"ex_id":"3610031","source":4,"action_type":1,"league_id":"22","season_id":"0","type":0,"match_start_time":1629804600,"status":10,"has_odds":1,"has_inplay":1,"has_stream":1,"arena_en":"","arena_zh":"","create_time":1629812514,"team":[{"ex_id":"10581","is_home":3,"is_winner":2,"score":"56,9,16,18,13,0","player":[{"ex_id":"10655","position":0,"number":"0"},{"ex_id":"64293","position":0,"number":"6"},{"ex_id":"64294","position":0,"number":"13"},{"ex_id":"64295","position":0,"number":"15"},{"ex_id":"64296","position":0,"number":"11"},{"ex_id":"64297","position":0,"number":"41"},{"ex_id":"64298","position":0,"number":"16"},{"ex_id":"64299","position":0,"number":"7"},{"ex_id":"64301","position":0,"number":"12"},{"ex_id":"64302","position":0,"number":"27"},{"ex_id":"64303","position":0,"number":"5"}]},{"ex_id":"10592","is_home":2,"is_winner":4,"score":"72,13,20,17,22,0","player":[{"ex_id":"64304","position":0,"number":"55"},{"ex_id":"64305","position":0,"number":"42"},{"ex_id":"64306","position":0,"number":"5"},{"ex_id":"64307","position":0,"number":"12"},{"ex_id":"64308","position":0,"number":"10"},{"ex_id":"64309","position":0,"number":"4"},{"ex_id":"64310","position":0,"number":"14"},{"ex_id":"64311","position":0,"number":"0"},{"ex_id":"64312","position":0,"number":"22"},{"ex_id":"64313","position":0,"number":"8"},{"ex_id":"64314","position":0,"number":"44"},{"ex_id":"64315","position":0,"number":"13"}]}]}'
b = json.loads(a)
ex_a = []
teams = b['team']
for i in teams:
    # print(i)
    players = i['player']
    for y in players:
        # print(y)
        ex_a.append(y['ex_id'])
print(len(ex_a))
print(ex_a)

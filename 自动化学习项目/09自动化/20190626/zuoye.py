# import  random
#
# booll = True
# while booll:
#     num = random.random()
#     new_num = num * 100
#     if 28 <= new_num < 60:
#         print(new_num)
#         booll = False
#     else:
#         booll = True

# str_str = "hello_new_world"
# new_str = str_str.split("_")
# print(new_str)

# num = 1
# # print("000"+str(num))

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# set_a = set(a)
# set_b = set(b)
# set_new = set_a | set_b
# new_list = list(set_new)
# print(new_list)

# d = {"k": 1, "v": 2}
# for key ,value in d.items():
#     print(key)
#     print(value)

# my_list = [{"k": 1, "v": 2}, {"k": 12, "v": 22}, {"k": 13, "v": 32}]
# my_list.sort(key=lambda x: x["k"], reverse=True)
# print(my_list)

# s = set([1, 2, 3, 4])
# d = set([2, 4, 9, 0, 3])
# set_j = s & d
# set_b = s | d
# set_c = s ^ d
# print(set_j)
# print(set_b)
# print(set_c)

# a = ["a", "b"]
# b = ",".join(a)
# print(b)

#
# num = sum([x for x in range(0, 101)])
# print(num)

# a = [1, 2, 4, 3, 2, 2, 4]
# set_a = set(a)
# print(list(set_a))

import datetime

today = datetime.date.today()
oneday = datetime.timedelta(days=5)
tomorrow = (today + oneday).strftime("%d")
today = today.strftime("%d")
print(today, tomorrow)
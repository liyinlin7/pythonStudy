

# student_list = []
# for i in range(1, 6):
#     student_name = input("请输入同学的名字：")
#     student_list.append(student_name)
#
# print(student_list)
#
# for student_name in student_list:
#     print(student_name[1])

# list1 = [1, 3, 4, 5, 7]
# list2 = [0, 66, 8, 9]
# my_set1 = set(list1)
# my_set2 = set(list2)
# new_set1 = my_set1 | my_set2
# print(new_set1)
# new_list1 = list(new_set1)
# new_list1.sort()
# print(new_list1)


# dict1 = {"school": "lebo", "date": 2018, "address": "beijing"}
# for key, vy in dict1.items():
#     if vy == "lebo":
#         print(key)

# import random
# nums_list = []
# for i in range(1, 6):
#     num = random.randint(0, 100)
#     nums_list.append(num)
# print(nums_list)
# for num in nums_list:
#     new_num = 100 - num
#     print(new_num)


# people = {}
# name_value = input("请输入您的姓名：")
# age_value = input("请输入您的年龄：")
# num_value = input("请输入您的学号：")
# people["name"] = name_value
# people["age"] = int(age_value)
# people["num"] = num_value
# print(people)


#倒叙的冒泡算法
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for j in range(len(num_list)-1, 0, -1):
#     count = 0
#     for i in range(0, j):
#         if num_list[i] < num_list[i + 1]:
#             num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
#             count += 1
#     if count == 0:
#         break
# print(num_list)


# new_num_list = list(reversed(num_list))
# numadd = 0
# print(new_num_list)
# for num in new_num_list:
#     index = new_num_list.index(num)
#     if index % 2 == 0:
#         numadd += num
# print(numadd)

# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止
#     打印每个设计后，都将其移到列表completed
#     _
#     models中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#     # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# def sum_nums_3(a, *args, b=22, c=33, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     d = list(args)
#     print(d)
#     print(args)
#     print(kwargs)
#
# sum_nums_3(100, 200, 300, 400, 500, 600, 700, b=1, c=2, mm=800, nn=900)

my_list = [2, 1, 3, 4]
print(my_list)
my_list = [2, 1, 3, 4]
my_list.sort()
print(my_list)
my_list = [2, 1, 3, 4]
my_list.sort(reverse=True)
print(my_list)
my_list = [2, 1, 3, 4]
my_list.reverse()
print(my_list)

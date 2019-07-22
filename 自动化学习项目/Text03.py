li = [1, 2, 3, 4]
arry = []
for i in range(1, 11):
    arry.append(li.copy())
print(arry)
arry[0][1] = 100
print(arry)
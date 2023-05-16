import csv

# 1.读取csv文件,方法1
csvFile = open("csvData1.csv", "r")
reader = csv.reader(csvFile)
data1 = []
for item in reader:
    print(item)
    data1.append(item)
print(data1)
csvFile.close()


# 2.读取csv文件方法2
data2 = []
with open("csvData1.csv", "r") as csvFile2:
    reader2 = csv.reader(csvFile2)
    for item in reader2:
        print(item)
        data2.append(item)
    print(data2)

# 3.从列表写入CSV文件
csvFile1 = open("csvData2.csv", "w", newline='')
writer1 = csv.writer(csvFile1)
m = len(data2)
for i in range(m):
    writer1.writerow(data2[i])
csvFile1.close()

# 4.从字典写入Csv文件
dic = {'张三': 123, '李四': 321, '王五': 654}
csvFile3 = open('csvData3.csv', 'w', newline='')
writer2 = csv.writer(csvFile3)
for key in dic:
    writer2.writerow([key, dic[key]])
csvFile3.close()

f = lambda a, b: a+b

print(f(5, 6))

z = lambda : 90

print(z())

#列表推导式
my_list = [i for i in range(1, 11)]
print(my_list)

my_list1 = [(x, y) for x in range(0, 3) for y in range (0, 3)]
print(my_list1)

#读写文件
# w 为写入文件，但是文件不存在时候，会创建文件；重复写入的时候，会覆盖之前的文件内容
f = open("text.txt", "w", encoding="utf-8")
f.write("哈哈")
f.close()

# r 为读取文件，文件不存在会报错。
f = open("text.txt", "r", encoding="utf-8")
fel = f.read()
print(fel)
f.close()

# a 为写入文件，会在文件末尾继续写入，不会覆盖文件之前的内容
f = open("text.txt", "a", encoding="utf-8")
f.write("\n\t中国")
f.close()
f = open("text.txt", "r", encoding="utf-8")
fel = f.read()
print(fel)
f.close()


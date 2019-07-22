#私有的属性
class Cc(object):
    def __init__(self):
        self.name="李"
        self.__classs="python"#私有属性，__变量名

    def Show(self):
        print("班级是私有的。姓名:%s，班级：%s" % (self.name, self.__classs))

    def __Hhow(self):#私有的方法，__方法名
        print("私有方法")

    def Classname(self):
        return "私有的值："+self.__classs

    def Hhow(self):
        return Cc.__Hhow(self)

class Xx(Cc):
    pass

zz = Xx()
print(zz.name)
zz.name = "龙"
zz.Show()
print("--------私有的属性和私有的方法-------")
#强行使用私有方法
zz.Hhow()
print(zz.Classname())
print("--------调用私有的属性和私有的方法-------")


#Python的自己的new方法
class Person(object):
    def __new__(cls, *args, **kwargs):
        print("new")
        return object.__new__(cls)

    def __init__(self):
        print("init")
        self.num = 20

p = Person()
print(p.num)
print("-----new模块在init模块之前执行------")

#异常
try:
    print(num)
except NameError as err:
    print("没有找到该变量名",err)

print("-----------")

try:
    open("text.text1", "r")
except  FileNotFoundError  as err:
    print("没有找到读取的文件", err)

print("-----------")

try:
    print(num)
except (NameError, FileNotFoundError):
    print("多异常")

print("-----------")

try:
    open("text.text", "w")
except  FileNotFoundError  as err:
    print("没有找到读取的文件", err)
else:
    print("try里的else的运用")
finally:
    print("不管如何都会执行finally")

print("-----------")
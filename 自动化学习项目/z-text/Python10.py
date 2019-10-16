class Text(object):
    def __init__(self, name, age, classs):
        self.name = name
        self.age = age
        self.classs = classs

    def ShowStudents(self):
        print("学生姓名:%s,年龄:%s,班级:%s" % (self.name, self.age, self.classs))

    def __str__(self):
        return "学生姓名:%s,年龄:%s,班级:%s" % (self.name, self.age, self.classs)




students = Text(name = "李", age = 30, classs = "1班")
students.ShowStudents()
print(students)
print("------------------")


#继承,多继承有同名方法时，以第一个继承的方法为准
class Master(object):
    def __init__(self):
        self.ma="父级master"
    def fast(self):
        print("Master的fast方法")

    def last(self):
        print("Master的last方法")

class Son(object):
    def __init__(self):
        self.ma="父级son"
    def fast(self):
        print("Son的fast方法")

    def de(self):
        print("Son的de方法")

class Grandson(Master, Son):
    pass


grandson_text = Grandson()
grandson_text.fast()
grandson_text.last()
grandson_text.de()
print("--------继承,多继承----------")

#重写
class ChongXue(Master, Son):
    def __init__(self):
        self.ma = "ChongXue"
    def fast(self):
        print("重写的方法")

cx = ChongXue()
print(cx.ma)
cx.fast()
print("--------重写----------")


#子类调用父类重名方法
class ChongXue01(Master, Son):
    def __init__(self):
        self.ma = "ChongXue01"
        Master. __init__(self)

    def fast(self):
        print("重写的方法")

    def Mastrt_fast(self):
        Master.fast(self)

    def Son_fast(self):
        Son.fast(self)

    def Super(self):
        print("super继承方法,调用父类的方法")
        super(ChongXue01, self).fast()


cx01 = ChongXue01()
print(cx01.ma)
cx01.fast()
cx01.Mastrt_fast()
cx01.Son_fast()
cx01.Super()
print("--------子类调用父类重名方法----------")

#多层继承
class DuoCeng(ChongXue01):
    pass

duo = DuoCeng()
print(duo.ma)
duo.Mastrt_fast()
duo.Son_fast()
duo.de()
duo.last()
duo.Super()
print("-------多层继承-----------")






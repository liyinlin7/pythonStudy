from Text01 import Text01

class Text02(object):
    def __init__(self, Text01):
        self.name = Text01.name
        self.age = Text01.age
        self.classs = Text01.classs

    def ShowStudents(self):
        print("学生姓名:%s,年龄:%s,班级:%s" % (self.name, self.age, self.classs))


students = Text01(name = "", age = 0, classs = "")
students1 = Text02(students)
students1.ShowStudents()
students.name = "张"
students.age = 18
students.classs = "2班"
students1 = Text02(students)
students1.ShowStudents()

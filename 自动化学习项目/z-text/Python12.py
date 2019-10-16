

class Person(object):
    __country = ""
    #魔法方法
    def __init__(self):
        self.__name = ""

    #实例方法
    def set_Name(self, new_Name):
        self.__name = new_Name

    def get_Name(self):
        return  self.__name

    #类方法
    @classmethod
    def set_Country(cls, new_Country):
        cls.__country = new_Country

    @classmethod
    def get_Country(cls):
        return  cls.__country

    #静态方法
    @staticmethod
    def hello_Python():
        print("静态方法")

person = Person()
person.set_Name("小明")
print(person.get_Name())
person.set_Country("English ")
print(person.get_Country())
person.hello_Python()

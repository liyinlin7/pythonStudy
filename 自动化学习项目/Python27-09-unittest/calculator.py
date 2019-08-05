# 被测试类，构造一个类Math包含整数加法运算
class Math:
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

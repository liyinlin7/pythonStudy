

class Text(object):
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def add(self):
        return  self.a+self.b

    def chengyi(self): return  self.a*self.b


text = Text(2, 5)
a=text.add()
print(a)
print(text.chengyi())

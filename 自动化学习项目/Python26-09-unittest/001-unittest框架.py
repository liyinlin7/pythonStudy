import unittest

#被测试类
class myclass(object):
    """classmethod修饰符对应的函数不需要实例化，
    不需要self参数，但第一个参数需要是表示自身类的cls参数，
    可以来调用类的属性，类的方法，实例化对象等。"""
    @classmethod
    def sum(cls,a,b):
        return a+b

    @classmethod
    def sub(cls,a,b):
        return a-b


# 测试用例编写
class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("------setUpClass------")

    @classmethod
    def tearDownClass(cls):
        print("------tearDownClass-----")

    # 初始化工作
    def setUp(self):
        self.a=3
        self.b=1
        print("-----setUp-------")

    # 退出清理工作
    def tearDown(self):
        print("------tearDown------")

    # 具体的测试用例，一定要以test开头
    def test_sum(self):
        self.assertEqual(myclass.sum(self.a, self.b), 4, 'test sum fail')

    def test_sub(self):
        self.assertEqual(myclass.sub(self.a, self.b), 2, 'test sub fail')


if __name__=='__main__':
    # 启动单元测试
    unittest.main()

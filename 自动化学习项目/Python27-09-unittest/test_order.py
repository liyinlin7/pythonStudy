# 用例的执行顺序
# 执行顺序规则---测试类或测试方法的数字与字母顺序 0~9，a~z,A~Z
import unittest


class Test1(unittest.TestCase):
    def setUp(self):
        print("test1 start")

    def test_c(self):
        print("test_c")

    def test_b(self):
        print("test_b")

    def tearDown(self):
        print("test1 end")


class Test2(unittest.TestCase):
    def setUp(self):
        print("test2 start")

    def test_d(self):
        print("test_d")

    def test_a(self):
        print("test_a")

    def tearDown(self):
        print("test2 end")


if __name__=='__main__':

    # 默认unittext的执行顺序
    unittest.main()

    # 用例集，手动改变用例执行顺序
    suite = unittest.TestSuite()
    suite.addTest(Test2("test_d"))
    suite.addTest(Test1("test_b"))
    suite.addTest(Test2("test_a"))
    suite.addTest(Test1("test_c"))

    runner = unittest.TextTestRunner()
    runner.run(suite)

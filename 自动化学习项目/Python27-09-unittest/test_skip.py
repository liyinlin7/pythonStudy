# 跳过测试和预期失败
# 一般作为脚本调试用
import unittest


class Test1(unittest.TestCase):
    def setUp(self):
        print("test1 start")

    # 条件为真的时候跳过用例
    @unittest.skipIf(4 > 3, "skip Test_c")
    def test_c(self):
        print("test_c")

    # 条件为假的时候跳过用例
    @unittest.skipUnless(1 < 0, "skip Test_b")
    def test_b(self):
        print("test_b")

    def tearDown(self):
        print("test1 end")


# 跳过
@unittest.skip("skip Test_2")
class Test2(unittest.TestCase):
    def setUp(self):
        print("test2 start")

    def test_d(self):
        print("test_d")

    def test_a(self):
        print("test_a")

    def tearDown(self):
        print("test2 end")


if __name__ == '__main__':
    unittest.main()


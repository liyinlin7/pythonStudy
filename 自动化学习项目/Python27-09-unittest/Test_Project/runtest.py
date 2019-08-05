import unittest


# 在当前目录
test_dir = './'
# 找到测试用例 text_dir是需要在哪个“目录”去找，pattern是找什么“文件”
discovery = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discovery)

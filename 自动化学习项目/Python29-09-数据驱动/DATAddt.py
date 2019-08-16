from selenium import webdriver
import unittest,time
# traceback模块的意义是异常的获取与处理
import logging,traceback
import ddt
from selenium.common.exceptions import NoSuchElementException

# 初始化日志对象
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=r"d:\test-ddt.log"
)


# 数据驱动装饰器
@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # 数据驱动时指定的三个数据，每一个数据是一个list
    @ddt.data(["郎平", "排球"],
              ["李宁", "程序猿"])

    @ddt.unpack
    def test_dataDrivernDDT(self, testdata, expectdata):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:  # 页面元素不存在的异常
            # format_exc()代表是把异常栈以字符串的形式返回
            logging.error("查找的页面元素不存在，异常信息："+str(traceback.format_exc()))
        except AssertionError as e:  # 断言异常
            logging.info('搜索-"%s",期望-"%s",-失败' % (testdata, expectdata))
        except Exception as e:
            logging.error("未知错误，错误信息："+str(traceback.format_exc()))
        else:
            logging.info('搜索-"%s",期望-"%s",-通过' % (testdata, expectdata))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()













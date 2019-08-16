from selenium import webdriver
import unittest,time
# traceback模块的意义是异常的获取与处理
import logging,traceback
import ddt
from selenium.common.exceptions import NoSuchElementException
from ExcelUtil import ParseExcel


# 初始化日志对象
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=r"d:\test-excel.log"
)
excelPath = r'D:\Python项目\自动化学习项目\Python29-09-数据驱动\excel-data\测试数据.xlsx'
sheetName = "搜索数据表"
excel = ParseExcel(excelPath, sheetName)


# 数据驱动装饰器
@ddt.ddt
class TestDemoExcel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(*excel.getDatasFromSheet())
    def test_dataDrivernExcel(self, data):
        # 将我们得到的data数据转换成元组
        print('tuple(data):', tuple(data))
        # 将data元组中的数据拆分为两个变量
        testData,expectData = tuple(data)
        print("testData:", testData)
        print("expectData:", expectData)
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("kw").send_keys(testData)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectData in self.driver.page_source)
        except NoSuchElementException as e:
            # format_exc()代表是把异常栈以字符串的形式返回
            logging.error("查找的页面元素不存在，异常信息："+str(traceback.format_exc()))
        except AssertionError as e:
            logging.info('搜索-"%s",期望-"%s",-失败' % (testData, expectData))
        except Exception as e:
            logging.error("未知错误，错误信息："+str(traceback.format_exc()))
        else:
            logging.info('搜索-"%s",期望-"%s",-通过' % (testData, expectData))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

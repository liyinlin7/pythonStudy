import requests
import unittest
import ddt
from common import read_path
from time import sleep
from common.common_fun import Common


def data_value():
    xlsx_path = read_path.test_data_path
    print(xlsx_path)
    data_list = Common().getExcelTestData_sheetName(xlsx_path, '杭州')
    print(data_list)
    return data_list

# 构造测试用例类，继承 unittest.TestCase
@ddt.ddt
class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url = "https://restapi.amap.com/v3/weather/weatherInfo?key=a8027e654468652b74bb2cca354d8e2b&output=JSON&extensions=base"

    @ddt.data(*data_value())
    # 数据驱动时指定的几个数据，每一个数据是一个list
    # @ddt.data(["330102", '上城区'],
    #           ["330105", "拱墅区"])
    @ddt.unpack
    def test_weather_baijing(self, city_name, city_code, city_s):
        # payload = {"name": "jack", "age": 22, "height": 177}
        print(city_code)
        print(city_name)
        r = requests.get(self.url + '&city=' + city_code)
        result = r.json()
        # print(result['lives'][0]['city'])
        self.assertEqual(result['lives'][0]['city'], city_name, '城市不一样')
        print(result)

    # def test_weather_baijing_1(self):
    #     payload = {"name": "jack", "age": 22, "height": 177}
    #     r = requests.post("http://127.0.0.1:5000/add_user", json=payload)
    #     result = r.json()
    #     print(result)

    def tearDown(self):
        print("test end!")


if __name__ == "__main__":
    unittest.main()

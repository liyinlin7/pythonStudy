import requests
import unittest
from time import sleep

# 构造测试用例类，继承 unittest.TestCase
class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url="http://t.weather.sojson.com/api/weather/city"

    def test_weather_baijing(self):
        data={'city_code':'101010100'}
        r= requests.get(self.url+'/'+data['city_code'])
        result=r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success感谢又拍云(upyun.com)提供CDN赞助')
        self.assertEqual(result['cityInfo']['city'],'北京市')
        self.assertEqual(result['cityInfo']['citykey'],'101010100')
        sleep(5)

    def test_weather_param_error(self):
        data = {'city_code': '666abc'}
        r = requests.get(self.url + '/' + data['city_code'])
        result = r.json()
        self.assertEqual(result['status'],404)
        self.assertEqual(result['message'],'Request resource not found.')
        sleep(5)

    def test_weather_no_param(self):
        data = {'city_code': ''}
        r = requests.get(self.url + '/' + data['city_code'])
        result = r.json()
        self.assertEqual(result['status'], 404)
        self.assertEqual(result['message'], 'Request resource not found.')
        sleep(5)

    def test_weather_non_existent(self):
        data = {'city_code': '123456789'}
        r = requests.get(self.url + '/' + data['city_code'])
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], '获取失败')
        sleep(5)

    def tearDown(self):
        print("test end!")

if __name__=="__main__":
    unittest.main()
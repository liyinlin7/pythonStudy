import requests
import unittest
from time import sleep


# 构造测试用例类，继承 unittest.TestCase
class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://t.weather.sojson.com/api/weather/city"

    def test_weather_baijing(self):
        payload = {"name": "jack", "age": 22, "height": 177}
        r = requests.post(self.url + '/' + 'add_user', json=payload)
        # r = requests.post("http://127.0.0.1:5000/add_user", json=payload)
        result = r.json()
        print(result)

    def test_weather_baijing_1(self):
        payload = {"name": "jack", "age": 22, "height": 177}
        r = requests.post("http://127.0.0.1:5000/add_user", json=payload)
        result = r.json()
        print(result)


    def tearDown(self):
        print("test end!")


if __name__ == "__main__":
    unittest.main()

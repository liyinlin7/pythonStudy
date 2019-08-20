'''
注意事项目：
1.每个IP日调用额度2000次，超过过多，会直接封掉IP段
2.每次请求间隔必须3秒以上
'''

import requests

# 构造接口测试数据
base_url='http://t.weather.sojson.com/api/weather/city'
data={'city_code':'101010100'}
# 发送请求
r = requests.get(base_url+'/'+data['city_code'])
print(r.url)
print("状态码：",r.status_code)

# 将返回结果转换为json类型
response_data=r.json()

# 从返回结果中获取（日期、信息、状态、城市）
print(response_data['date'])  #请求的当天日期
print(response_data['message'])
print(response_data['status'])
print(response_data['cityInfo']['city'])

# 获取当天的天气
print(response_data['data']['forecast'][0]['date'])
print(response_data['data']['forecast'][0]['type'])
print(response_data['data']['forecast'][0]['high'])
print(response_data['data']['forecast'][0]['low'])
# json.loads():将json数据类型转为python数据类型
import json

json_str = '{"id": 1, "name": "wang", "password": 666}'
data = json.loads(json_str)
print(type(json_str))
print(type(data))
print(data["name"])
# json数据类型是字符串，没有键和值之分，所以以下代码是错误的
# print(json_str["name"])

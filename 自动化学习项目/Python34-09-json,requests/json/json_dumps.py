# json.dumps():将python数据类型转化为json数据类型
import json

data = {"id": 1, "name": "wang", "password": 666}
print(type(data))

json_str = json.dumps(data)
print(type(json_str))
print(json_str)


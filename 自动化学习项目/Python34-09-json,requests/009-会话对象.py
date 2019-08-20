# 【1】以下代码有两个请求，一个是设置cookie，另一个是获取cookie，在没有session
# 保存机制的情况下，第二个接口无法获取第一个接口设置的cookie值
import requests

base_url = 'http://httpbin.org'

# 设置cookie
r = requests.get(base_url+'/cookies/set/user/wang')
print(r.text)

print("++++++++++++++++++++++++++++++++++++++++++++")

# 获取cookie
r = requests.get(base_url+'/cookies')
print(r.text)


# 【2】使用session保存机机制
import requests

base_url = 'http://httpbin.org'

print("以下代码中使用了 session保存机制")
# 生成会话对象
s = requests.Session()

# 设置cookie
r = s.get(base_url+'/cookies/set/user/wang')
print(r.text)

print("++++++++++++++++++++++++++++++++++++++++++++")

# 获取cookie
r = s.get(base_url+'/cookies')
print(r.text)

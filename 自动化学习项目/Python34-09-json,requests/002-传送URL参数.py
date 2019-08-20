import requests

base_url = "https://httpbin.org"

# 发送带参数的GET请求
param_data = {'user': 'wang', 'password': 666, 'id': 1}
r = requests.get(base_url+'/get', params=param_data)
# 查看请求后的域名
print(r.url)
# 查看状态码
print(r.status_code)
# 查看返回文本信息
print(r.text)

print("++++++++++++++++++++++++++++++++++")
form_data = {'user': 'wang', 'password': 6666}
r = requests.post(base_url+'/post', data=form_data)
# 查看请求后的域名
print(r.url)
# 查看状态码
print(r.status_code)
# 查看返回文本信息
print(r.text)

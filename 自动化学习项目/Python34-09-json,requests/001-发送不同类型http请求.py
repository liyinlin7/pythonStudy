import requests

base_url = "https://httpbin.org"

r = requests.get(base_url+'/get')
print("GET请求的状态码：", r.status_code)

r = requests.post(base_url+'/post')
print("POST请求的状态码：", r.status_code)

r = requests.delete(base_url+'/delete')
print("DELETE请求的状态码：", r.status_code)

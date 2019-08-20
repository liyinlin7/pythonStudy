import requests

base_url = "https://httpbin.org"

# 有些网站在发送接口数据时，要求必须设置请求头，如知乎
form_data = {'user': 'wang', 'password': 6666}
header = {'User-Agent': 'Mozilla/5.0'}
r = requests.post(base_url+'/post', data=form_data, headers=header)
print(r.status_code)
print(r.text)
print(r.json())

# # 针对知乎网站的测试，必须加请求头
# header={'User-Agent':'Mozilla/5.0'}
# r=requests.get('https://www.zhihu.com/',headers=header)
# print(r.status_code)
# print(r.text)
# print(r.headers)

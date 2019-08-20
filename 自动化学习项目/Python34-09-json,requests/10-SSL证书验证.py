import requests

# r=requests.get('http://www.12306.cn')

# 关闭验证SSL
r = requests.get('http://www.12306.cn', verify=False)

print(r.status_code)
print(r.text)

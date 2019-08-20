import requests

r = requests.get('https://www.baidu.com')
print(type(r.cookies))
print(r.cookies)

# 使用items()方法将其转化为元组组成的列表，遍历输出每一个Cookie的名和值，实现Cookies的遍历解析
for key, value in r.cookies.items():
    print(key+':'+value)



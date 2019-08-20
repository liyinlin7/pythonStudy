import requests

base_url = "https://httpbin.org"
cookie = {"user": "wang"}
r = requests.get(base_url+'/cookies', cookies=cookie)
print(r.text)

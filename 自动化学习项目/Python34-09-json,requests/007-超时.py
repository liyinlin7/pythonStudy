import requests

base_url = "https://httpbin.org"
r = requests.get(base_url+'/cookies', timeout=5)
print(r.text)

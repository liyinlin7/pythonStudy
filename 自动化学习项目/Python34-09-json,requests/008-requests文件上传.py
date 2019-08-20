import requests

base_url = "http://httpbin.org"

file = {'file': open('httpbin.png', 'rb')}
r = requests.post(base_url+'/post', files=file)
print(r.status_code)
print(r.text)

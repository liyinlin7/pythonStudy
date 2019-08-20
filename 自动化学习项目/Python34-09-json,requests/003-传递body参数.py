import requests

base_url = "https://httpbin.org"

form_data = {'user': 'wang', 'password': 6666}
r = requests.post(base_url+'/post', data=form_data)
print(r.text)

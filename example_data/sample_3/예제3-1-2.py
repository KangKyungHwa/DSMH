import requests
import json

url="http://api.open-notify.org/iss-now.json"
r=requests.get(url)
dt_dict =r.json()
print(dt_dict['iss_position'])

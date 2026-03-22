import requests
import json
import time

url="http://api.open-notify.org/iss-now.json"

for i in range(10):
    r=requests.get(url)
    dt_dict =r.json()
    print(dt_dict['iss_position'])
    time.sleep(5)
    
2
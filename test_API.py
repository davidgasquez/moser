import requests
import json

# TODO: Use py.test and automate with Travis

base_url = 'http://localhost:5000'

print(requests.get(base_url).text)

data = {
        'sl': 5.5,
        'sw': 2.8,
        'pl': 4.1,
        'pw': 1.2
    }

r = requests.post(base_url + '/predict', data)

print(r.json())

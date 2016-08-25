import requests
import json

# TODO: Use py.test and automate with Travis

base_url = 'http://localhost:5000'

data = {
        'sl': 5.5,
        'sw': 2.8,
        'pl': 4.1,
        'pw': 1.2
    }

r = requests.post(base_url + '/api/models/test/predict', json=data)

print(r.json())

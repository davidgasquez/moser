import requests

# TODO: Use py.test and automate with Travis

base_url = 'http://localhost:5000'

filename = 'sample_model/model.pkl'

# Set the model
with open(filename, 'rb') as f:
    model = f.read()
    r = requests.put(base_url + '/api/models/test', data=model)

# Make a single prediction
data = {
        'sl': 5.5,
        'sw': 2.8,
        'pl': 4.1,
        'pw': 1.2
    }

r = requests.post(base_url + '/api/models/test/predict', json=data)
print(r.json())

# Make several predictions
with open('sample_model/unknown.csv', 'rb') as f:
    unknown_data = f.read()
    r = requests.put(base_url + '/api/models/test/predict', data=unknown_data)
    print(r.json())

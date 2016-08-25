import requests

# TODO: Use py.test and automate with Travis

base_url = 'http://localhost:5000'

filename = 'sample_model/model.pkl'

# Set the model
with open(filename, 'rb') as f:
    model = f.read()
    r = requests.put(base_url + '/api/models/test', data=model)

# Make predictions from JSON
data = {
    "column_names": ["a", "b", "c", "d"],
    "values": [
        [1, 4, 1, 1],
        [2, 0, 6, 1],
        [1, 4, 8, 1]
    ]
}
r = requests.post(base_url + '/api/models/test/predict', json=data)
print(r, r.json())

# Make predictions from CSV
with open('sample_model/unknown.csv', 'rb') as f:
    unknown_data = f.read()
    r = requests.put(base_url + '/api/models/test/predict', data=unknown_data)
    print(r, r.json())

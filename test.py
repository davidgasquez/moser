import requests
import cloudpickle

# TODO: Use py.test and automate with Travis

base_url = 'http://localhost:5000'

filename = 'sample_model/model.pkl'

# Set the model
with open(filename, 'rb') as f:
    model = f.read()
    r = requests.put(base_url + '/api/models/test', data=model)
    print(r)

# Make predictions from JSON
data = {
    "features": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
    "values": [
        [1, 4, 1, 1],
        [2, 0, 6, 1],
        [1, 4, 8, 1]
    ]
}
r = requests.post(base_url + '/api/models/test/predict', json=data)
print(r, r.json())


def f(x, y):
    return x + y

pkl = cloudpickle.dumps(f)
r = requests.put(base_url + '/api/functions/my_function', data=pkl)
print(r)

json = {'a': 3, 'b': 5}
r = requests.post(base_url + '/api/functions/my_function/run', json=json)
print(r, r.json())

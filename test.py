import requests
import cloudpickle
from textblob import TextBlob

# TODO: Use py.test and automate with Travis

base_url = 'http://localhost:5000'

filename = 'sample_model/model.pkl'

# Set the model
with open(filename, 'rb') as f:
    model = f.read()
    r = requests.put(base_url + '/api/models/iris', data=model)
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
r = requests.post(base_url + '/api/models/iris/predict', json=data)
print(r, r.json())


def correct(text):
    return str(TextBlob(text).correct())

pkl = cloudpickle.dumps(correct)
r = requests.put(base_url + '/api/functions/correct', data=pkl)
print(r)

json = {'text': 'Some mmen just wamt to watch the world burn'}
r = requests.post(base_url + '/api/functions/correct/run', json=json)
print(r, r.text)

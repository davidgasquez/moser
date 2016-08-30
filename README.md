# Moser: A Model Server Prototype

Moser is a simple way to serve your Machine Learning models. The goal of Moser
is making super easy to setup any kind of predictive model in a production
server and being able to interact with them through RESTful API calls.

## Features

- Set Models
- Set Functions

## Get Started

You can test it running the container (`make`) and heading
to [http://localhost:5000](http://localhost:5000)

1. Generate the model `pkl`
2. Build the container `make build`
3. Run the API with `make`
4. Make some requests to [http://localhost:5000](http://localhost:5000):
    - Add a model to the API with a `PUT` call to `/api/models/your_model_name`
    - Use the previous model calling `/api/models/your_model_name/predict` with
      a `POST` request providing a single JSON with the feature names and
      values.

## Example

```python
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

iris = load_iris()
data = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                    columns=iris['feature_names'] + ['target'])

clf = RandomForestClassifier()
clf.fit(data.drop('target', axis=1), data['target'])

joblib.dump(clf, 'model.pkl', compress=9)
```

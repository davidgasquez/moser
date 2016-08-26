# Scikit Learn Flask API

Basic Machine Learning API to make predictions in real time from a
picked Scikit Learn model. This will make super easy setup a
trained model and use it making RESTful API calls.

You can test it running the container (`make`) and heading
to [http://localhost:5000](http://localhost:5000)

## Features

- Models
- Functions

## Get Started

1. Generate the model `pkl` file - `cd sample_model && python train_model.py`
2. Build the container `make build`
3. Run the API `make`
4. Make some requests (I've been using Postman)
    - Add a model to the API with a `PUT` call to `/api/models/your_model_name`
    - Use the previous model calling `/api/models/your_model_name/predict`
        - `PUT`: Add a CSV file like `sample_model/unknown.csv`
        - `POST`: Single JSON with the feature names and values

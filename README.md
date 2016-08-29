# Scikit Learn Flask API

A simple way to productionize your Machine Learning models. The goal of _NAME_
is making super easy to setup any kind of predictive model in a server and
interact with it through RESTful API calls.

## Features

- Set Models
- Set Functions

## Get Started

You can test it running the container (`make`) and heading
to [http://localhost:5000](http://localhost:5000)

1. Generate the model `pkl` file - `cd sample_model && python train_model.py`
2. Build the container `make build`
3. Run the API `make`
4. Make some requests (I've been using Postman)
    - Add a model to the API with a `PUT` call to `/api/models/your_model_name`
    - Use the previous model calling `/api/models/your_model_name/predict`
        - `PUT`: Add a CSV file like `sample_model/unknown.csv`
        - `POST`: Single JSON with the feature names and values

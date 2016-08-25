from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from sklearn.externals import joblib
import pandas as pd

# Load trained model
clf = joblib.load('model/model.pkl')

# Generate Flask application
app = Flask(__name__)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)
        X = pd.DataFrame(json_data)
        prediction = clf.predict(X)
        return jsonify(result=prediction.tolist())
    else:
        prediction = clf.predict([4, 2, 1, 3])
        return jsonify(result=prediction.tolist())


# TODO
@app.route('/train')
def train():
    return 'Trainig'


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

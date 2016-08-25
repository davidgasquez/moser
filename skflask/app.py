from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import os
import cloudpickle
# from io import StringIO
from sklearn.externals import joblib
import pandas as pd

# Available Models
clfs = {}

# Generate Flask application
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


@app.route('/api/models/<name>/predict', methods=['POST', 'PUT'])
def predict_api(name):
    """Make a prediction with a model and return the result.

    sample_json = {
        "features": ["a", "b", "c"],
        "values": [
            [1, 4, 9],
            [2, 0, 6],
            [1, 4, 8]
        ]
    }
    """
    js = request.get_json()

    if clfs[name]['features'] != js['features']:
        return 'Not the sames features or order.'

    X = pd.DataFrame(js['values'], columns=js['features'])

    # Preprocessing function
    if clfs.get(name).get('preprocessing'):
        f = cloudpickle.loads(clfs[name]['preprocessing'])
        X = f(X)

    prediction = clfs.get(name)['model'].predict(X)

    return jsonify(result=prediction.tolist())

    # elif request.method == 'PUT':
    #     data = request.data.decode("utf-8")
    #     X = pd.read_csv(StringIO(data))
    #     prediction = clfs[name].predict(X)
    #     return jsonify(result=prediction.tolist())


@app.route('/api/models/<name>', methods=['PUT'])
def model(name):
    """Load a model into memory."""
    tmp_path = '/tmp/{}.plk'.format(name)

    # Write Model to disk
    with open(tmp_path, 'wb') as f:
        f.write(request.data)

    # This approach will keep all the models in memory
    clfs[name] = joblib.load(tmp_path)

    # Remove from disk
    os.remove(tmp_path)

    return jsonify(success=True)


@app.route('/models', methods=['GET'])
def list_models():
        """List loaded models."""
        return jsonify(list(clfs.keys()))


@app.route('/models/<name>', methods=['GET'])
def print_model(name):
        return jsonify(list(clfs[name]))


@app.route('/models/<name>/predict', methods=['GET'])
def predict(name):
        return 'Dynamic Template Here'


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

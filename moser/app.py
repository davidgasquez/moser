import os
import cloudpickle
import pandas as pd
from sklearn.externals import joblib

from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

# Available models and functions
models = {}
functions = {}

# Generate Flask application
app = Flask('moser')


@app.errorhandler(404)
def not_found(error):
    return jsonify(error=error.description), 404


@app.route('/api/models/<name>/predict', methods=['POST'])
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

    if models[name]['features'] != js['features']:
        return jsonify(error='Not the sames features or order.')

    X = pd.DataFrame(js['values'], columns=js['features'])

    # Preprocessing function (move to own API call)
    if models.get(name).get('preprocessing'):
        f = cloudpickle.loads(models[name]['preprocessing'])
        X = f(X)

    prediction = models.get(name)['model'].predict(X)

    return jsonify(result=prediction.tolist())


@app.route('/api/functions/<name>/run', methods=['GET'])
def run_function(name):
    """Executed a loaded function."""
    js = request.get_json()

    variable_names = functions[name].__code__.co_varnames
    if set(js.keys()) != set(variable_names):
        return 'Different arguments provided.'

    # Order parameters
    parameters = [js[var] for var in variable_names]

    # TODO: Handle optional parameters

    # Load function
    result = functions[name](*parameters)

    return jsonify(result)


@app.route('/api/functions/<name>', methods=['PUT'])
def load_function(name):
    """Load a function into memory."""
    functions[name] = cloudpickle.loads(request.data)
    return jsonify(success=True)


@app.route('/api/models/<name>', methods=['PUT'])
def load_model(name):
    """Load a model into memory."""
    tmp_path = '/tmp/{}.plk'.format(name)

    # Write Model to disk
    with open(tmp_path, 'wb') as f:
        f.write(request.data)

    # This approach will keep all the models in memory
    models[name] = joblib.load(tmp_path)

    # Remove from disk
    os.remove(tmp_path)

    return jsonify(success=True)


@app.route('/functions/<name>', methods=['GET'])
def print_function(name):
    return jsonify(name=functions[name].__name__)


@app.route('/functions', methods=['GET'])
def list_functions():
        """List loaded functions."""
        return jsonify(list(functions.keys()))


@app.route('/models', methods=['GET'])
def list_models():
        """List loaded models."""
        return jsonify(list(models.keys()))


@app.route('/models/<name>', methods=['GET'])
def print_model(name):
        # TODO: More Verbosity
        return jsonify(list(models[name]))


@app.route('/models/<name>/predict', methods=['GET'])
def predict(name):
        return 'Dynamic Template Here'


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

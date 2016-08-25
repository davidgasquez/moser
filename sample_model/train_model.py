import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib
import cloudpickle


def preprocessing(X):
    return X + 20


def dump_model(model, features=None,
               target_names=None, preprocessing=None):
    model = {}
    model['model'] = clf
    if features:
        model['features'] = features
    if target_names:
        model['target_names'] = target_names
    if preprocessing:
        model['preprocessing'] = preprocessing

    return model

# Read Data
iris = pd.read_csv('iris.csv', header=None,
                   names=['sepal_length', 'sepal_width',
                          'petal_length', 'petal_width', 'class'])


# Encode Class
le = LabelEncoder()
y = le.fit_transform(iris['class'])

# Prepare X
X = iris.drop('class', axis=1)

# Train classifier
clf = RandomForestClassifier()
clf.fit(X, y)

# Picke classifier
final_model = dump_model(clf,
                         features=list(X.columns),
                         target_names=list(le.classes_),
                         preprocessing=cloudpickle.dumps(preprocessing))

joblib.dump(final_model, 'model.pkl', compress=9)

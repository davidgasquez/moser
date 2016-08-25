import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib

# Read Data
iris = pd.read_csv('data/iris.csv', header=None,
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
joblib.dump(clf, 'model/model.pkl', compress=9)
